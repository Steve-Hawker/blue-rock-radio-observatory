#!/usr/bin/env python3
"""
adf4351_control.py — ADF4351 Signal Source Control
Blue Rock Radio Observatory

Controls an ADF4351 wideband PLL synthesiser via Raspberry Pi SPI
for observatory calibration procedures CAL-000 through CAL-005.

Wiring (Pi 3 GPIO BCM numbering):
    ADF4351 3V3  → Pi Pin 17 (3.3V)
    ADF4351 GND  → Pi Pin 25 (GND)
    ADF4351 DAT  → Pi GPIO 10 / Pin 19 (MOSI)
    ADF4351 CLK  → Pi GPIO 11 / Pin 23 (SCLK)
    ADF4351 LE   → Pi GPIO 8  / Pin 24 (CE0)
    ADF4351 CE   → Pi Pin 17 (3.3V) — tied high, always enabled
    ADF4351 LD   → Pi GPIO 24 / Pin 18 (lock detect input, optional)
    ADF4351 MUX  → unconnected
    ADF4351 POR  → unconnected

Dependencies:
    pip3 install RPi.GPIO spidev

Usage:
    python3 adf4351_control.py --freq 1421.0
    python3 adf4351_control.py --sweep 1360 1480 2
    python3 adf4351_control.py --cal000
    python3 adf4351_control.py --interactive

Author: Blue Rock Radio Observatory
"""

import spidev
import RPi.GPIO as GPIO
import time
import argparse
import csv
import os
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REFERENCE_FREQ_MHZ = 25.0      # ADF4351 onboard TCXO reference frequency
LD_PIN = 24                     # GPIO BCM pin for lock detect (optional)
LOCK_TIMEOUT_S = 0.1            # Seconds to wait for PLL lock
SWEEP_DWELL_S = 2.0             # Default dwell time per step during sweeps

# Output power register setting (Register 4, bits 4:3)
# 0 = -4 dBm, 1 = -1 dBm, 2 = +2 dBm, 3 = +5 dBm
OUTPUT_POWER = 3                # +5 dBm — use with 30dB attenuator

# CSV log file location
LOG_DIR = os.path.expanduser("~/brro/calibration")
LOG_FILE = os.path.join(LOG_DIR, "adf4351_sweep_log.csv")

# ---------------------------------------------------------------------------
# ADF4351 Register Calculation
# ---------------------------------------------------------------------------
#
# The ADF4351 is programmed by writing six 32-bit registers (R0–R5).
# Each register's lower 3 bits are the register address (0–5).
# Registers must be written in order R5, R4, R3, R2, R1, R0.
#
# To set an output frequency F_out:
#
#   F_out = F_ref × (INT + FRAC/MOD) / RF_DIV
#
# Where:
#   F_ref = reference frequency (25 MHz)
#   INT   = integer part of the N divider (23 ≤ INT ≤ 65535)
#   FRAC  = fractional numerator (0 ≤ FRAC ≤ MOD-1)
#   MOD   = modulus (2 ≤ MOD ≤ 4095)
#   RF_DIV = output divider (1, 2, 4, 8, 16, 32, or 64)
#
# The VCO operates between 2200 MHz and 4400 MHz.
# RF_DIV divides the VCO output down to the desired frequency.
# For 1420 MHz: VCO = 1420 × 2 = 2840 MHz → RF_DIV = 2

def calculate_registers(freq_mhz, ref_mhz=REFERENCE_FREQ_MHZ, mod=4095):
    """
    Calculate ADF4351 register values for a given output frequency.

    Args:
        freq_mhz: Desired output frequency in MHz
        ref_mhz:  Reference oscillator frequency in MHz (default 25.0)
        mod:      Modulus value (default 4095 — fine frequency resolution)

    Returns:
        List of 6 32-bit integers [R0, R1, R2, R3, R4, R5]
    """

    # Step 1: Choose RF output divider
    # VCO range is 2200–4400 MHz. Find smallest divider that puts
    # freq × divider within VCO range.
    rf_div = 1
    rf_div_sel = 0  # Register encoding: 0=÷1, 1=÷2, 2=÷4, 3=÷8, 4=÷16, 5=÷32, 6=÷64
    vco_freq = freq_mhz
    while vco_freq < 2200.0 and rf_div < 64:
        rf_div *= 2
        rf_div_sel += 1
        vco_freq = freq_mhz * rf_div

    if vco_freq < 2200.0 or vco_freq > 4400.0:
        raise ValueError(
            f"Frequency {freq_mhz} MHz: VCO frequency {vco_freq:.1f} MHz "
            f"out of range (2200–4400 MHz)"
        )

    # Step 2: Calculate N divider (INT and FRAC)
    # N = F_vco / F_ref = INT + FRAC/MOD
    n_total = vco_freq / ref_mhz
    int_val = int(n_total)
    frac_val = round((n_total - int_val) * mod)

    # Clamp INT to valid range
    if int_val < 23:
        int_val = 23
        frac_val = 0
    if int_val > 65535:
        raise ValueError(f"INT value {int_val} out of range")

    # Recalculate actual output frequency for verification
    actual_vco = ref_mhz * (int_val + frac_val / mod)
    actual_freq = actual_vco / rf_div
    freq_error_hz = (actual_freq - freq_mhz) * 1e6

    # Step 3: Build registers
    # Register 0: INT (bits 30:15), FRAC (bits 14:3), addr 000
    r0 = ((int_val & 0xFFFF) << 15) | ((frac_val & 0xFFF) << 3) | 0

    # Register 1: Phase (bits 26:15) = 1, MOD (bits 14:3), prescaler (bit 27) = 1
    # Prescaler = 1 (8/9) for frequencies above 3 GHz; 0 (4/5) below
    prescaler = 1 if vco_freq >= 3000 else 0
    phase_val = 1  # Required by datasheet when using fractional mode
    r1 = (prescaler << 27) | (phase_val << 15) | ((mod & 0xFFF) << 3) | 1

    # Register 2: Noise mode (bits 30:29) = 00 (low noise),
    # MUX out (bits 28:26) = 000, ref doubler (bit 25) = 0,
    # RDIV2 (bit 24) = 0, R counter (bits 23:14) = 1,
    # double buffered (bit 13) = 0, charge pump (bits 12:9) = 0111,
    # LDF (bit 8) = 0, LDP (bit 7) = 0, PD polarity (bit 6) = 1,
    # power down (bit 5) = 0, CP tri-state (bit 4) = 0,
    # counter reset (bit 3) = 0, addr 010
    r_counter = 1  # No reference division
    charge_pump = 7  # ~2.5 mA — typical setting
    r2 = (0 << 29) | (0 << 26) | (0 << 25) | (0 << 24) | \
         (r_counter << 14) | (0 << 13) | (charge_pump << 9) | \
         (0 << 8) | (0 << 7) | (1 << 6) | (0 << 5) | (0 << 4) | \
         (0 << 3) | 2

    # Register 3: Band select clock mode (bit 23) = 0,
    # ABP (bit 22) = 0, charge cancel (bit 21) = 0,
    # CSR (bit 18) = 0, clock divider mode (bits 16:15) = 00,
    # clock divider (bits 14:3) = 150, addr 011
    clock_div = 150
    r3 = (0 << 23) | (0 << 22) | (0 << 21) | (0 << 18) | \
         (0 << 15) | (clock_div << 3) | 3

    # Register 4: Feedback select (bit 23) = 1 (fundamental),
    # RF div select (bits 22:20), band select clock divider (bits 19:12) = 200,
    # VCO power down (bit 11) = 0, MTLD (bit 10) = 0,
    # AUX output select (bit 9) = 0, AUX output enable (bit 8) = 0,
    # AUX output power (bits 7:6) = 00, RF output enable (bit 5) = 1,
    # output power (bits 4:3), addr 100
    band_sel_div = 200
    r4 = (1 << 23) | (rf_div_sel << 20) | (band_sel_div << 12) | \
         (0 << 11) | (0 << 10) | (0 << 9) | (0 << 8) | (0 << 6) | \
         (1 << 5) | (OUTPUT_POWER << 3) | 4

    # Register 5: Reserved bits, LD pin mode (bits 23:22) = 01 (digital lock detect)
    r5 = (1 << 22) | 5

    return [r0, r1, r2, r3, r4, r5], actual_freq, freq_error_hz


# ---------------------------------------------------------------------------
# SPI Communication
# ---------------------------------------------------------------------------

def init_spi():
    """Initialise SPI bus and GPIO."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Set up lock detect pin as input (optional but useful)
    GPIO.setup(LD_PIN, GPIO.IN)

    # Open SPI bus 0, device 0 (CE0 = LE pin)
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 1000000   # 1 MHz — conservative, ADF4351 handles up to 20 MHz
    spi.mode = 0b00              # CPOL=0, CPHA=0
    spi.bits_per_word = 8

    return spi


def write_register(spi, register_value):
    """
    Write a single 32-bit register to the ADF4351.
    SPI sends MSB first in 4 bytes.
    """
    bytes_to_send = [
        (register_value >> 24) & 0xFF,
        (register_value >> 16) & 0xFF,
        (register_value >> 8)  & 0xFF,
        (register_value)       & 0xFF,
    ]
    spi.xfer2(bytes_to_send)


def program_adf4351(spi, registers):
    """
    Program all 6 registers to the ADF4351.
    Must be written in reverse order: R5 first, R0 last.
    """
    for reg in reversed(registers):
        write_register(spi, reg)
        time.sleep(0.001)  # Brief pause between registers


def wait_for_lock(timeout=LOCK_TIMEOUT_S):
    """
    Wait for PLL lock detect pin to go high.
    Returns True if locked, False if timeout.
    """
    deadline = time.time() + timeout
    while time.time() < deadline:
        if GPIO.input(LD_PIN):
            return True
        time.sleep(0.001)
    return False


def set_frequency(spi, freq_mhz, verbose=True):
    """
    Set ADF4351 output frequency.

    Args:
        spi:       SpiDev instance
        freq_mhz:  Desired frequency in MHz
        verbose:   Print status to console

    Returns:
        actual_freq_mhz, freq_error_hz
    """
    registers, actual_freq, freq_error_hz = calculate_registers(freq_mhz)
    program_adf4351(spi, registers)

    locked = wait_for_lock()
    lock_str = "LOCKED" if locked else "NO LOCK — check connections"

    if verbose:
        velocity_error = (freq_error_hz / 1420.405e6) * 299792.458
        print(f"  Set:    {freq_mhz:.6f} MHz")
        print(f"  Actual: {actual_freq:.6f} MHz")
        print(f"  Error:  {freq_error_hz:+.1f} Hz ({velocity_error:+.4f} km/s)")
        print(f"  PLL:    {lock_str}")

    return actual_freq, freq_error_hz


# ---------------------------------------------------------------------------
# Calibration Procedures
# ---------------------------------------------------------------------------

def cal_000_interactive(spi):
    """
    CAL-000 — SDR Baseline (interactive mode)
    Walks through all four steps with prompts for GQRX readings.
    Records results to ADF4351_timeseries.csv format.
    """
    print("\n" + "="*60)
    print("CAL-000 — SDR Baseline Characterisation")
    print("="*60)
    print("Configuration: ADF4351 → 30dB attenuator → V4c SMA input")
    print("GQRX: centre frequency 1422.000 MHz, sample rate 2.4 Msps")
    print()
    input("Press Enter when GQRX is open and configured...")

    results = []
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # --- Step 1: LO frequency accuracy ---
    print("\n--- Step 1: LO Frequency Accuracy ---")
    print("Setting ADF4351 to 1421.000 MHz...")
    print("Tone should appear at -1.000 MHz offset in GQRX baseband.")
    set_frequency(spi, 1421.0)

    raw = input("\nMeasured tone position in GQRX (MHz from centre, e.g. -1.0002): ")
    try:
        measured_offset_mhz = float(raw)
        lo_error_hz = (measured_offset_mhz + 1.0) * 1e6
        velocity_error = (lo_error_hz / 1420.405e6) * 299792.458
        print(f"LO error: {lo_error_hz:+.0f} Hz ({velocity_error:+.4f} km/s)")
        if abs(lo_error_hz) < 1000:
            print("✓ PASS — error < 1 kHz (< 0.21 km/s)")
        else:
            print("✗ FAIL — error > 1 kHz — consider GPSDO upgrade")

        results.append({
            "date": date_str,
            "equipment_version": "E001",
            "cal_procedure": "CAL-000-V4c",
            "parameter": "lo_frequency_error_hz",
            "value": f"{lo_error_hz:.1f}",
            "unit": "Hz",
            "notes": f"Measured offset {measured_offset_mhz} MHz from -1.000 MHz expected"
        })
        results.append({
            "date": date_str,
            "equipment_version": "E001",
            "cal_procedure": "CAL-000-V4c",
            "parameter": "lo_velocity_error_kms",
            "value": f"{velocity_error:.4f}",
            "unit": "km/s",
            "notes": ""
        })
    except ValueError:
        print("Skipping — invalid input")

    # --- Step 2: Wideband response ---
    print("\n--- Step 2: Wideband Response Sweep ---")
    print("Stepping 1360–1480 MHz in 2 MHz steps.")
    print("Note the GQRX power reading (dBFS) at each frequency.")
    print("You can record manually or just observe the shape visually.")
    print()
    do_sweep = input("Run sweep? (y/n): ").lower().strip()
    if do_sweep == 'y':
        sweep_log = []
        freqs = [f for f in range(1360, 1482, 2)]
        print(f"\nSweeping {len(freqs)} frequencies. Press Ctrl+C to abort.\n")
        print(f"{'Freq (MHz)':>12}  {'Power (dBFS)':>14}  Notes")
        print("-" * 45)
        for freq in freqs:
            set_frequency(spi, float(freq), verbose=False)
            time.sleep(0.3)  # Settle time
            power_str = input(f"  {freq:>8} MHz   power: ").strip()
            sweep_log.append((freq, power_str))

        # Save sweep to separate CSV
        sweep_file = os.path.join(LOG_DIR, f"cal000_sweep_{date_str}.csv")
        os.makedirs(LOG_DIR, exist_ok=True)
        with open(sweep_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["freq_mhz", "power_dbfs"])
            writer.writerows(sweep_log)
        print(f"\nSweep saved to {sweep_file}")

    # --- Step 3: IQ imbalance ---
    print("\n--- Step 3: IQ Imbalance ---")
    print("Setting ADF4351 to 1422.500 MHz (LO + 500 kHz).")
    print("True tone at +500 kHz. Image at -500 kHz.")
    set_frequency(spi, 1422.5)

    raw_true = input("\nTrue tone amplitude at +500 kHz (dBFS): ").strip()
    raw_image = input("Image amplitude at -500 kHz (dBFS): ").strip()
    try:
        true_db = float(raw_true)
        image_db = float(raw_image)
        irr = true_db - image_db
        print(f"IQ IRR: {irr:.1f} dB")
        if irr >= 30:
            print("✓ Baseline acceptable (≥30 dB uncorrected)")
        else:
            print("✗ Poor IQ balance — investigate")

        results.append({
            "date": date_str,
            "equipment_version": "E001",
            "cal_procedure": "CAL-000-V4c",
            "parameter": "iq_irr_db",
            "value": f"{irr:.1f}",
            "unit": "dB",
            "notes": f"true={raw_true} dBFS, image={raw_image} dBFS"
        })
    except ValueError:
        print("Skipping — invalid input")

    # --- Step 4: Dynamic range ---
    print("\n--- Step 4: Dynamic Range ---")
    print("Setting ADF4351 to 1420.000 MHz.")
    print("Increase GQRX gain until tone just saturates ADC.")
    set_frequency(spi, 1420.0)

    raw_gain = input("\nMaximum useful gain before saturation (dB): ").strip()
    try:
        max_gain = float(raw_gain)
        results.append({
            "date": date_str,
            "equipment_version": "E001",
            "cal_procedure": "CAL-000-V4c",
            "parameter": "max_useful_gain_db",
            "value": f"{max_gain:.1f}",
            "unit": "dB",
            "notes": "Gain at which ADC just saturates with 1420 MHz tone"
        })
        print(f"Recommended HI observation gain: ≤ {max_gain - 10:.0f} dB (10 dB headroom)")
    except ValueError:
        print("Skipping — invalid input")

    # --- Save results ---
    if results:
        os.makedirs(LOG_DIR, exist_ok=True)
        write_mode = 'a' if os.path.exists(LOG_FILE) else 'w'
        with open(LOG_FILE, write_mode, newline='') as f:
            writer = csv.DictWriter(f,
                fieldnames=["date","equipment_version","cal_procedure",
                            "parameter","value","unit","notes"])
            if write_mode == 'w':
                writer.writeheader()
            writer.writerows(results)
        print(f"\nResults appended to {LOG_FILE}")

    print("\nCAL-000 complete.")


def sweep(spi, start_mhz, stop_mhz, step_mhz, dwell_s=SWEEP_DWELL_S):
    """
    Automated frequency sweep — for CAL-002 passband measurement.
    Prints each frequency and dwells for dwell_s seconds.
    No GQRX interaction — run alongside rtl_power for automated logging.
    """
    freqs = []
    f = start_mhz
    while f <= stop_mhz:
        freqs.append(f)
        f = round(f + step_mhz, 6)

    print(f"\nSweep: {start_mhz}–{stop_mhz} MHz, step {step_mhz} MHz, "
          f"dwell {dwell_s}s, {len(freqs)} steps")
    print(f"Total time: ~{len(freqs) * dwell_s / 60:.1f} minutes\n")
    input("Press Enter to start sweep (Ctrl+C to abort)...")

    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    sweep_log = []

    try:
        for i, freq in enumerate(freqs):
            actual, error_hz = set_frequency(spi, freq, verbose=False)
            locked = GPIO.input(LD_PIN)
            ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
            print(f"  [{i+1:3d}/{len(freqs)}] {freq:8.3f} MHz  "
                  f"error {error_hz:+6.0f} Hz  "
                  f"{'LOCK' if locked else 'NO LOCK'}  {ts}")
            sweep_log.append({
                "timestamp": ts,
                "freq_mhz": freq,
                "actual_mhz": f"{actual:.6f}",
                "error_hz": f"{error_hz:.1f}",
                "locked": locked
            })
            time.sleep(dwell_s)

    except KeyboardInterrupt:
        print("\nSweep aborted by user.")

    # Save sweep log
    if sweep_log:
        os.makedirs(LOG_DIR, exist_ok=True)
        log_file = os.path.join(LOG_DIR,
            f"sweep_{start_mhz:.0f}_{stop_mhz:.0f}_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
        with open(log_file, 'w', newline='') as f:
            writer = csv.DictWriter(f,
                fieldnames=["timestamp","freq_mhz","actual_mhz","error_hz","locked"])
            writer.writeheader()
            writer.writerows(sweep_log)
        print(f"\nSweep log saved to {log_file}")


def set_single(spi, freq_mhz):
    """Set a single frequency and hold — interactive use."""
    print(f"\nSetting {freq_mhz} MHz...")
    set_frequency(spi, freq_mhz)
    print("\nHolding frequency. Press Enter to exit and turn off output...")
    input()


def interactive(spi):
    """Simple interactive mode — type frequencies on demand."""
    print("\nInteractive mode. Type a frequency in MHz, or 'q' to quit.")
    print("Examples: 1421, 1422.5, 1420\n")
    while True:
        raw = input("Frequency (MHz): ").strip()
        if raw.lower() in ('q', 'quit', 'exit'):
            break
        try:
            freq = float(raw)
            set_frequency(spi, freq)
        except ValueError:
            print("Invalid frequency — enter a number in MHz")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="ADF4351 control for Blue Rock Radio Observatory calibration"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--freq", type=float, metavar="MHz",
                       help="Set a single frequency in MHz and hold")
    group.add_argument("--sweep", nargs=3, type=float,
                       metavar=("START", "STOP", "STEP"),
                       help="Frequency sweep: start stop step (all MHz)")
    group.add_argument("--cal000", action="store_true",
                       help="Run CAL-000 SDR baseline procedure interactively")
    group.add_argument("--interactive", action="store_true",
                       help="Interactive mode — type frequencies on demand")

    parser.add_argument("--dwell", type=float, default=SWEEP_DWELL_S,
                        help=f"Dwell time per step in seconds (default {SWEEP_DWELL_S})")

    args = parser.parse_args()

    # Initialise hardware
    spi = init_spi()
    print("ADF4351 SPI initialised.")

    try:
        if args.freq:
            set_single(spi, args.freq)

        elif args.sweep:
            start, stop, step = args.sweep
            sweep(spi, start, stop, step, dwell_s=args.dwell)

        elif args.cal000:
            cal_000_interactive(spi)

        elif args.interactive:
            interactive(spi)

    except KeyboardInterrupt:
        print("\nInterrupted.")

    finally:
        # Turn off ADF4351 output on exit by power-down
        # Write register 4 with RF output enable bit cleared
        powerdown_r4 = (1 << 23) | (0 << 20) | (200 << 12) | (0 << 5) | 4
        write_register(spi, powerdown_r4)
        spi.close()
        GPIO.cleanup()
        print("ADF4351 output off. GPIO cleaned up.")


if __name__ == "__main__":
    main()
