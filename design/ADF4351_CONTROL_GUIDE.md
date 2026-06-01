# ADF4351 Control Script — User Guide

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-06-01  
**Version:** 1.0  
**Script:** `scripts/adf4351_control.py`  

---

## Overview

`adf4351_control.py` controls the ADF4351 wideband signal source via
the Raspberry Pi 3 SPI interface. It is used for all ADF4351-based
calibration procedures (CAL-000 through CAL-005) defined in
`design/ADF4351_CALIBRATION.md`.

The script runs on Pi 3 — the same machine that hosts the RTL-SDR V4c.
You operate it over SSH from your MacBook while GQRX runs on the MacBook
receiving from the V4c.

---

## Hardware Setup

### What you need

- Raspberry Pi 3 (powered, on network)
- ADF4351 board
- 7 male-to-female jumper wires
- 30 dB SMA attenuator
- Short SMA cable (ADF4351 output to attenuator)
- Short SMA cable (attenuator to V4c input)
- MacBook running GQRX

### Wiring — ADF4351 to Pi 3

Connect the ADF4351 header to the Pi 3 GPIO header as follows.

**Physical Pi 3 GPIO header layout (top of board, looking down):**

```
  3V3 [ 1] [ 2] 5V
GPIO2 [ 3] [ 4] 5V
GPIO3 [ 5] [ 6] GND
      ...
GPIO10[19] [20] GND     ← MOSI (DAT)
GPIO11[23] [22] GPIO25  ← SCLK (CLK)
 GPIO8[24] [25] GND     ← CE0  (LE)
      ...
GPIO24[18] [17] 3V3     ← Lock detect input
```

**Connections:**

| ADF4351 pin | Connect to | Pi physical pin | Notes |
|---|---|---|---|
| 3V3 | 3.3V | Pin 17 | Powers ADF4351 logic |
| GND (top row) | GND | Pin 25 | |
| DAT | GPIO 10 (MOSI) | Pin 19 | SPI data |
| CLK | GPIO 11 (SCLK) | Pin 23 | SPI clock |
| LE | GPIO 8 (CE0) | Pin 24 | Latch enable — loads registers |
| CE | 3.3V | Pin 17 | Tie high — keeps chip enabled |
| GND (bottom row) | GND | Pin 20 | Any GND pin |
| LD | GPIO 24 | Pin 18 | Lock detect — confirms PLL locked |
| MUX | — | — | Leave unconnected |
| POR/PDR | — | — | Leave unconnected |

**Double-check before powering on:**
- 3V3 to 3V3 (NOT 5V — will damage the Pi GPIO pins)
- LE goes to CE0 (Pin 24) — this is the latch, not CE
- CE is tied to 3V3, not connected to a GPIO

### RF connections

```
ADF4351 RF output
    → SMA cable
        → 30 dB attenuator
            → SMA cable
                → RTL-SDR V4c SMA input
```

**Always connect the 30 dB attenuator before powering the ADF4351.**
Without attenuation the ADF4351 output (~+5 dBm) will saturate
the V4c ADC immediately.

---

## One-Time Setup on Pi 3

These steps only need to be done once.

### 1. Enable SPI interface

```bash
sudo raspi-config
```

Navigate to: **Interface Options → SPI → Yes → OK → Finish**

Reboot when prompted:
```bash
sudo reboot
```

### 2. Verify SPI is enabled

After reboot, SSH back in and check:

```bash
ls /dev/spi*
```

You should see `/dev/spidev0.0` and `/dev/spidev0.1`. If not, repeat step 1.

### 3. Install Python dependencies

```bash
pip3 install RPi.GPIO spidev
```

If pip3 is not installed:
```bash
sudo apt update
sudo apt install python3-pip
pip3 install RPi.GPIO spidev
```

### 4. Create the calibration data directory

```bash
mkdir -p ~/brro/calibration
```

### 5. Copy the script to the Pi

From your MacBook, copy the script over SSH:

```bash
scp scripts/adf4351_control.py pi@<pi3-ip-address>:~/brro/scripts/
```

Or clone/pull the full repository on the Pi:

```bash
cd ~
git clone https://github.com/Steve-Hawker/blue-rock-radio-observatory brro
```

### 6. Make the script executable

```bash
chmod +x ~/brro/scripts/adf4351_control.py
```

---

## Running the Script

All commands below assume you are SSH'd into Pi 3 from your MacBook:

```bash
ssh pi@<pi3-ip-address>
cd ~/brro
```

### CAL-000 — SDR Baseline (interactive)

The main calibration procedure. Walks through all four steps with
prompts for GQRX readings. Results saved automatically.

**Before running:**
1. Open GQRX on MacBook — connect to V4c
2. Set GQRX centre frequency to **1422.000 MHz**
3. Set GQRX sample rate to **2.4 Msps**
4. Set GQRX gain to a moderate level (~30 dB) to start
5. Confirm ADF4351 is wired and attenuator is connected

**Run:**
```bash
python3 scripts/adf4351_control.py --cal000
```

The script will guide you through:
- **Step 1:** LO frequency accuracy — tone at -1 MHz in GQRX
- **Step 2:** Wideband sweep 1360–1480 MHz — note power at each step
- **Step 3:** IQ imbalance — tone at +500 kHz, image at -500 kHz
- **Step 4:** Dynamic range — find maximum useful gain before saturation

Results are appended to `~/brro/calibration/ADF4351_timeseries.csv`.
Copy back to MacBook after the session:

```bash
# From MacBook:
scp pi@<pi3-ip-address>:~/brro/calibration/ADF4351_timeseries.csv \
    calibration/ADF4351_timeseries.csv
```

---

### Set a single frequency

Set the ADF4351 to one frequency and hold it. Useful for manual
GQRX inspection or any step where you want to control the pace.

```bash
python3 scripts/adf4351_control.py --freq 1421.0
```

```bash
python3 scripts/adf4351_control.py --freq 1422.5
```

```bash
python3 scripts/adf4351_control.py --freq 1420.0
```

The script prints the actual frequency, the frequency error in Hz,
the velocity equivalent in km/s, and whether the PLL locked.
Press **Enter** to exit — the script turns off the RF output cleanly.

---

### Interactive mode

Type frequencies on demand. Useful for exploration during commissioning.

```bash
python3 scripts/adf4351_control.py --interactive
```

Type a frequency in MHz at the prompt. Type `q` to quit.

```
Frequency (MHz): 1421
  Set:    1421.000000 MHz
  Actual: 1420.999756 MHz
  Error:  -244.1 Hz (-0.0515 km/s)
  PLL:    LOCKED

Frequency (MHz): 1090
  Set:    1090.000000 MHz
  ...

Frequency (MHz): q
ADF4351 output off. GPIO cleaned up.
```

---

### Frequency sweep

Automated sweep through a frequency range. The script steps through
each frequency, dwells for the specified time, and logs to a CSV file.
Run this alongside `rtl_power` for automated passband measurement (CAL-002).

**Basic sweep (2 MHz steps, 2 second dwell):**
```bash
python3 scripts/adf4351_control.py --sweep 1360 1480 2
```

**Fine sweep for CAL-002 (1 MHz steps, 2 second dwell):**
```bash
python3 scripts/adf4351_control.py --sweep 1360 1480 1
```

**Fine sweep with longer dwell (5 seconds per step):**
```bash
python3 scripts/adf4351_control.py --sweep 1360 1480 1 --dwell 5
```

Sweep log saved to:
`~/brro/calibration/sweep_1360_1480_YYYYMMDD_HHMMSS.csv`

---

## Reading the Output

### Frequency error and velocity equivalent

Every time the script sets a frequency it reports:

```
Set:    1421.000000 MHz       ← what you asked for
Actual: 1420.999756 MHz       ← what the ADF4351 can achieve (register quantisation)
Error:  -244.1 Hz             ← difference
        (-0.0515 km/s)        ← velocity equivalent at 1420 MHz
PLL:    LOCKED                ← PLL lock status
```

The register quantisation error (typically a few hundred Hz) is separate
from the ADF4351 crystal frequency error (~10 ppm = ~14 kHz at 1420 MHz).
The crystal error will shift all frequencies systematically — this is what
CAL-000 Step 1 measures.

**Acceptance criterion (CAL-000 Step 1):**
Total LO error < 1 kHz → velocity error < 0.21 km/s → PASS

### PLL lock

`LOCKED` means the PLL has stabilised at the requested frequency.
`NO LOCK` means something is wrong — check wiring, power, and SPI
connections before trusting any measurements.

---

## CAL-000 Frequency Reference

| Step | ADF4351 frequency | Purpose |
|---|---|---|
| 1 — LO accuracy | 1421.000 MHz | Tone at -1.000 MHz in GQRX (LO at 1422 MHz) |
| 2 — Wideband | 1360 → 1480 MHz | SDR passband shape, 2 MHz steps |
| 3 — IQ imbalance | 1422.500 MHz | +500 kHz tone; image at -500 kHz |
| 4 — Dynamic range | 1420.000 MHz | In-band tone for gain/saturation test |

---

## Output Files

| File | Contents | Location |
|---|---|---|
| `ADF4351_timeseries.csv` | CAL-000 scalar results (LO error, IRR, max gain) | `~/brro/calibration/` on Pi 3 |
| `cal000_sweep_YYYY-MM-DD.csv` | Step 2 wideband sweep power readings | `~/brro/calibration/` on Pi 3 |
| `sweep_START_STOP_TIMESTAMP.csv` | Automated frequency sweep log | `~/brro/calibration/` on Pi 3 |

Copy all files back to MacBook after each session and commit to repo.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `No module named 'spidev'` | spidev not installed | `pip3 install spidev` |
| `No module named 'RPi'` | RPi.GPIO not installed | `pip3 install RPi.GPIO` |
| `cannot open /dev/spidev0.0` | SPI not enabled | Run `sudo raspi-config` → Interface Options → SPI |
| `NO LOCK` on every frequency | Wiring error | Check DAT, CLK, LE connections; check 3V3 power |
| No tone visible in GQRX | RF not reaching V4c | Check SMA connections; check attenuator; check GQRX centre frequency |
| Tone at wrong offset in GQRX | GQRX not centred at 1422 MHz | Set GQRX centre frequency to exactly 1422.000 MHz |
| Permission denied on GPIO | Script not run with correct permissions | Try `sudo python3 ...` or add user to gpio group: `sudo adduser pi gpio` |

---

## Safety Reminders

- **Always connect the 30 dB attenuator** before connecting ADF4351
  to V4c. Without it, the ~+5 dBm output will saturate the SDR.
- **Never connect ADF4351 to the HI feed output** — the feed contains
  ~40 dB of LNA gain. ADF4351 + attenuator + LNA gain would severely
  overdrive the SDR.
- **3V3 only on the GPIO header** — the Pi GPIO pins are not 5V tolerant.
  The ADF4351 board uses 3.3V logic. Confirm before connecting.

---

## Related Documents

- `design/ADF4351_CALIBRATION.md` — calibration procedure definitions
- `calibration/ADF4351_timeseries.csv` — results time series
- `OPEN_ITEMS.md` — ADF4351 SPI library status

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-06-01 | Initial guide — hardware setup, wiring, one-time Pi configuration, all script modes, output files, troubleshooting |
