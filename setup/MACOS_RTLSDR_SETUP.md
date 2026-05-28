# macOS RTL-SDR V4c Setup Guide

**Observer:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Document:** Chain A — RFI Monitoring Setup (macOS)  
**Version:** 1.0  
**Date:** 2026-05-19  
**Filepath:** `setup/MACOS_RTLSDR_SETUP.md`

---

## Purpose

This document covers installation and verification of the RTL-SDR V4c
on macOS (MacBook Pro), for use as Chain A (RFI monitoring) during
Phase 3 commissioning. The goal is a working dipole → RTL-SDR V4c →
MacBook Pro signal chain, with SDR++ for visual survey and
rtl_power_fftw for systematic data logging.

This setup is **temporary for Phase 3**. In Phase 4, Chain A migrates
to Raspberry Pi 3 for autonomous monitoring. The macOS setup documented
here is for the initial RFI characterisation programme.

---

## Prerequisites

- macOS 13 Ventura or later (tested procedure)
- MacBook Pro with USB-A or USB-C port (V4c connects via USB)
- Homebrew package manager
- RTL-SDR Blog V4c dongle
- Dipole antenna with SMA connector

> **Note on the V4c specifically:** The RTL-SDR Blog V4c uses the
> R828D tuner and includes a built-in HF upconverter, making it
> different from earlier V3 hardware. The driver requirement is
> `librtlsdr` ≥ 0.6.0, which introduced V4 support. The Homebrew
> formula installs a sufficient version — do not use older system
> packages if any exist.

---

## Step 1 — Install Homebrew

If Homebrew is not already installed:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the on-screen instructions. On Apple Silicon Macs, Homebrew
installs to `/opt/homebrew/`; on Intel Macs, `/usr/local/`. The
commands below work for both.

Verify:

```bash
brew --version
```

---

## Step 2 — Install RTL-SDR drivers

```bash
brew install librtlsdr
```

This installs:
- `librtlsdr` — the core driver library
- `rtl_test`, `rtl_sdr`, `rtl_power` — command-line utilities
- `rtl-tcp` — network server (useful later for Pi migration)

Verify the install:

```bash
rtl_test --help
```

You should see a help message listing options. If you get
`command not found`, Homebrew's bin directory is not in your PATH.
Fix with:

```bash
echo 'export PATH="$(brew --prefix)/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

## Step 3 — Plug in the V4c and test

Connect the RTL-SDR V4c to a USB port (use a USB-A to USB-C adapter
if needed — do not use a hub for initial testing, direct connection only).

Run the hardware test:

```bash
rtl_test -t
```

Expected output (approximately):

```
Found 1 device(s):
  0:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: Generic RTL2832U OEM
Found Rafael Micro R820T tuner
Supported gain values (29): 0.0 1.0 2.0 ... 49.6
Sampling at 2048000 S/s.
No E4000 tuner found, aborting.
```

> The "No E4000 tuner found" message is **normal** — it just means
> it's not an E4000-based dongle. The R820T/R828D message confirms
> correct detection.

If you see `usb_claim_interface error -6` or similar, a kernel
extension conflict exists — see Troubleshooting below.

---

## Step 4 — Remove the macOS default USB serial driver (if needed)

macOS sometimes loads a built-in USB serial driver that conflicts with
librtlsdr. This is more common on older macOS versions but worth
checking if Step 3 failed.

Check if the conflicting driver is loaded:

```bash
kextstat | grep -i usb
```

If you see `com.apple.driver.usb.cdc` or similar claiming the device,
you may need to unload it temporarily:

```bash
sudo kextunload -b com.apple.driver.usb.cdc.acm
```

This resets on reboot. In practice, recent macOS versions (13+) rarely
have this issue with RTL-SDR dongles.

---

## Step 5 — Install SDR++

SDR++ is the recommended visual survey tool for macOS. It is a
native, well-maintained application with excellent waterfall display.

Download the latest macOS release from:
https://github.com/AlexandreRouma/SDRPlusPlus/releases

Download the `.dmg` file, open it, and drag SDR++ to Applications.

**First launch — Gatekeeper warning:** macOS will refuse to open
SDR++ the first time because it is not notarised. To bypass:

```
System Settings → Privacy & Security → scroll down → "Open Anyway"
```

Or from Terminal:

```bash
xattr -cr /Applications/sdrpp.app
```

**Configure SDR++ for the V4c:**

1. Launch SDR++
2. In the top-left Source dropdown, select **RTL-SDR**
3. Set sample rate to **2.048 MSPS** (good balance of bandwidth and
   stability for initial surveys)
4. Set gain to **Auto** or start with **30 dB** manual gain
5. Tune to **1420.405 MHz** — your target frequency
6. Press the **Play** button (▶)

You should see a live waterfall and spectrum display. The horizontal
axis is frequency, vertical axis is time (newest at top), and colour
is power level.

**Recommended initial settings for RFI survey:**

- FFT size: 32768 (more frequency resolution)
- Waterfall speed: medium
- Colour map: any — viridis or plasma are good for RFI identification
- Span: zoom to ±10 MHz around 1420 MHz first, then widen

---

## Step 6 — Install rtl_power_fftw

`rtl_power_fftw` is a significantly improved replacement for the
stock `rtl_power` tool. It produces more accurate power measurements
and better handles the V4c's extended frequency range.

```bash
brew install rtl-power-fftw
```

Verify:

```bash
rtl_power_fftw --help
```

---

## Step 7 — Verification sweep

Run a quick 60-second power sweep across the HI band region to
confirm the full chain is working:

```bash
rtl_power_fftw \
  -f 1400M:1440M \
  -b 512 \
  -t 60 \
  -o /tmp/brro_test_sweep.csv
```

Parameters:
- `-f 1400M:1440M` — sweep 1400–1440 MHz (40 MHz span)
- `-b 512` — 512 FFT bins
- `-t 60` — run for 60 seconds
- `-o` — output file

Open the CSV to confirm data is being recorded. Each row is a
frequency bin with a power value in dBFS. If the file is empty
or the command errors, revisit Steps 2–4.

---

## Step 8 — Known V4c birdies on macOS

The RTL-SDR V4c generates internal spurious signals (birdies) that
appear as real signals but are artefacts of the dongle hardware.
These must not be entered into `rfi/persistent_sources.md` as
environmental RFI.

Known V4c birdies to be aware of (verify against your unit):

| Frequency | Notes |
|---|---|
| ~28.8 MHz harmonics | Crystal reference harmonics — HF only |
| ~1.000 GHz region | Internal LO leakage — check empirically |

**Method for birdie identification:** Disconnect the antenna (replace
with a 50Ω terminator or just cap the SMA port) and repeat the sweep.
Any signal that persists without an antenna is a birdie. Document
your unit's birdies before beginning environmental surveys.

---

## Workflow for Phase 3 RFI Surveys

Once setup is complete, the Phase 3 RFI characterisation workflow is:

### Visual survey (SDR++)
1. Connect dipole, launch SDR++, tune to 1420 MHz
2. Scan ±20 MHz either side of 1420.405 MHz
3. Note any signals in the waterfall — frequency, character
   (continuous/pulsed/intermittent), approximate bandwidth
4. Log findings in `rfi/RFI_OVERVIEW.md`

### Systematic logging (rtl_power_fftw)
Run unattended overnight or across multiple time periods to
capture temporal patterns:

```bash
rtl_power_fftw \
  -f 1380M:1460M \
  -b 1024 \
  -t 3600 \
  -o rfi/surveys/$(date -u +%Y%m%dT%H%M%S)_survey.csv
```

The filename timestamp (UTC) allows later correlation with
time-of-day patterns. Run at different times — morning, afternoon,
evening, overnight — to characterise the temporal structure of
the RFI environment.

### Building persistent_sources.md
Any signal observed in ≥3 independent survey sessions at the same
frequency should be entered into `rfi/persistent_sources.md` as a
candidate persistent source. This file is the direct input to the
INV003 known-frequency mask (Step 1 of the flagging pipeline).

---

## Migration to Raspberry Pi 3 (Phase 4)

The macOS setup uses the same underlying tools (`librtlsdr`,
`rtl_power_fftw`) that will run on Raspberry Pi OS. The Pi 3
setup guide will follow the same structure with minor differences
(apt instead of brew, systemd service for unattended operation).

`rtl_tcp` (installed alongside librtlsdr in Step 2) allows the
V4c to be accessed over the network once migrated to the Pi,
enabling monitoring from the MacBook without physically connecting
the dongle.

---

## Troubleshooting

**`usb_claim_interface error -6`**  
Another process has claimed the USB device. Try: unplug and replug
the dongle, then immediately run rtl_test. If persistent, check
for other SDR applications running in the background.

**`No devices found`**  
Try a different USB port (direct, not hub). Confirm the dongle's
LED is lit when connected. On Apple Silicon, confirm you installed
the arm64 Homebrew, not a Rosetta x86_64 version.

**SDR++ shows no signal / flat waterfall**  
Confirm gain is not set to 0. Check the antenna is physically
connected to the SMA port. Confirm the V4c LED is lit (blue).

**Very high noise floor across entire band**  
Normal for an urban San Jose environment — this is what you are
characterising. Compare with antenna disconnected to establish
the noise floor baseline.

**rtl_power_fftw: `error opening device`**  
SDR++ (or another application) may have the device open. Close
all other SDR applications before running command-line tools.
Only one application can access the device at a time.

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-19 | Initial document — macOS Chain A setup |
