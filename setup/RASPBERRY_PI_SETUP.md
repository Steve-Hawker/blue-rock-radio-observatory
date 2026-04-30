# Raspberry Pi Setup Guide — Blue Rock Radio Observatory

**Observer:** Steve Hawker BEng MBA FRAS  
**Version:** 1.0  
**Date:** 2026-04-30  
**Platform:** Raspberry Pi 3  
**Role:** Observatory control computer — dish pointing, SDR data capture, logging

---

## Overview

The Raspberry Pi 3 serves as the observatory control computer, mounted at or
near the dish in the Discovery Dish Outdoor Electronics Enclosure (DDOEE) or
indoors depending on cable routing. It handles:

- Dish pointing via rotctl protocol to Discovery Drive (WiFi)
- SDR data capture (Airspy R2 via USB)
- EZRa data acquisition (Phase 1)
- Data transfer to MacBook Pro for processing and logging
- Remote access from MacBook Pro via SSH over WiFi

GNU Radio pipeline development (Phase 2) will be done on the MacBook Pro
initially, with the Pi 3 used for data capture only. A Pi 4 may be considered
for Phase 2 if the Pi 3 proves insufficient for real-time processing.

---

## Hardware Required

| Item | Specification | Notes |
|---|---|---|
| Raspberry Pi 3 | Model 3B or 3B+ | Already owned |
| microSD card | 32GB, Class 10 or better | Replace old card — 8yr old cards unreliable |
| Power supply | 5V 2.5A USB micro | Ensure adequate current for Pi 3 + USB SDR |
| Case (optional) | — | DDOEE provides weatherproofing if mounted outside |

**Recommended microSD:** SanDisk Endurance or Samsung PRO Endurance —
these are rated for continuous write operations, important for a logging
application that writes data continuously during observations.

---

## Step 1 — Install Raspberry Pi Imager on MacBook

Download from: `https://raspberrypi.com/software`

Install and open. You will use this to write the OS to the microSD card.

---

## Step 2 — Write OS to microSD Card

1. Insert microSD card into MacBook (use USB adapter if needed)
2. Open Raspberry Pi Imager
3. Click **Choose Device** → select Raspberry Pi 3
4. Click **Choose OS** → Raspberry Pi OS (other) → **Raspberry Pi OS Lite (64-bit)**
   - Lite = no desktop, command line only — correct for headless observatory use
5. Click **Choose Storage** → select your microSD card
6. Click **Next** → **Edit Settings** — configure:

**General tab:**
- Hostname: `bluerock`
- Username: `steve` (or your preference)
- Password: (choose a strong password)
- Configure WiFi: enter your home WiFi SSID and password
- Locale: America/Los_Angeles, keyboard US

**Services tab:**
- Enable SSH: ✓
- Use password authentication: ✓

7. Click **Save** → **Yes** → confirm write
8. Wait for write and verification to complete (~5 minutes)

---

## Step 3 — First Boot

1. Insert microSD card into Pi 3
2. Connect power
3. Wait ~90 seconds for first boot (longer than subsequent boots)
4. From MacBook Terminal, connect via SSH:

```bash
ssh steve@bluerock.local
```

If `bluerock.local` doesn't resolve, find the Pi's IP address from your
router's device list and connect directly:

```bash
ssh steve@192.168.x.x
```

You should see the Raspberry Pi OS command prompt. First boot complete.

---

## Step 4 — System Update

**Run these commands immediately after first boot.** An 8-year gap means
the base OS needs all security and software updates before anything else.

```bash
sudo apt update
sudo apt full-upgrade -y
sudo reboot
```

Reconnect after reboot:

```bash
ssh steve@bluerock.local
```

---

## Step 5 — Install Core Dependencies

```bash
# Essential tools
sudo apt install -y git vim curl wget htop

# Hamlib — provides rotctl for dish control
sudo apt install -y hamlib-utils

# Python scientific stack
sudo apt install -y python3-pip python3-numpy python3-scipy python3-matplotlib

# Astropy — Doppler corrections, coordinates, FITS
pip3 install astropy --break-system-packages

# Check versions
python3 -c "import astropy; print('Astropy:', astropy.__version__)"
rotctl --version
```

---

## Step 6 — Install Airspy Driver

```bash
# Install build dependencies
sudo apt install -y cmake libusb-1.0-0-dev build-essential

# Clone and build airspy host library
cd ~
git clone https://github.com/airspy/airspyone_host.git
cd airspyone_host
mkdir build && cd build
cmake ../ -DINSTALL_UDEV_RULES=ON
make
sudo make install
sudo ldconfig

# Add udev rule so Pi can access Airspy without root
sudo sh -c 'echo "ATTR{idVendor}==\"1d50\", ATTR{idProduct}==\"60a1\", MODE=\"0666\"" > /etc/udev/rules.d/52-airspy.rules'
sudo udevadm control --reload-rules

# Test — connect Airspy R2 via USB and run:
airspy_info
```

Expected output shows device found with sample rate options.

---

## Step 7 — Install EZRa

*(Instructions to be added when EZRa installation procedure confirmed)*

EZRa repository: check current installation instructions at source.
Note EZRa version installed in equipment log software section.

---

## Step 8 — Configure rotctl for Discovery Drive

The Discovery Drive uses the rotctl protocol over WiFi.
Default port is 4533.

Test connection (Discovery Drive must be powered and on same WiFi network):

```bash
# Test rotctl connection to Discovery Drive
rotctl -m 204 -r bluerock-drive.local:4533

# In rotctl interactive mode, test pointing:
p          # get current position
P 180 45   # point to azimuth 180°, elevation 45°
```

*(Discovery Drive hostname — check web UI for actual hostname or IP)*

---

## Step 9 — Configure Stellarium Remote Control

Stellarium on the MacBook connects to the Discovery Drive directly.
The Pi is not involved in this pathway.

On MacBook:
1. Open Stellarium
2. Plugins → Telescope Control → enable
3. Add telescope → select rotctl protocol
4. Enter Discovery Drive IP address and port 4533

Test by clicking a target in Stellarium and pressing the slew button.

---

## Step 10 — Set Up Data Directory Structure

```bash
# Create observation data directory
mkdir -p ~/bluerock-data/raw
mkdir -p ~/bluerock-data/reduced
mkdir -p ~/bluerock-data/logs

# This mirrors the repository structure for data files
# Raw data stays on Pi temporarily, transferred to MacBook after each session
# MacBook holds the permanent archive
```

---

## Step 11 — Configure Automatic Data Transfer to MacBook

Set up rsync from Pi to MacBook for post-session data transfer:

```bash
# On MacBook — test rsync from Pi (run this on MacBook Terminal):
rsync -avz steve@bluerock.local:~/bluerock-data/raw/ ~/bluerock-data/raw/
```

Consider adding this to your post-session checklist — after each session,
run rsync to pull all new data files to the MacBook before backing up.

---

## Step 12 — Enable Pi on Boot

Configure the Pi to start required services automatically on power-up:

```bash
# Enable SSH on boot (should already be enabled from Imager setup)
sudo systemctl enable ssh

# Confirm WiFi connects automatically on boot
# (configured during Imager setup — test by rebooting and reconnecting)
sudo reboot
```

After reboot, confirm you can SSH in without any manual intervention on the Pi.

---

## Connecting from MacBook — Daily Use

```bash
# Connect to Pi
ssh steve@bluerock.local

# Check disk space
df -h

# Check data files from last session
ls -lh ~/bluerock-data/raw/

# Transfer data to MacBook (run on MacBook)
rsync -avz steve@bluerock.local:~/bluerock-data/ ~/Documents/bluerock-data/

# Shutdown Pi after session
sudo shutdown -h now
```

---

## Troubleshooting

**Can't find bluerock.local:**
- Check Pi is powered and booted (~90 seconds)
- Check Pi and MacBook are on same WiFi network
- Find Pi IP from router device list and use IP directly

**Airspy not detected:**
- Check USB connection
- Run `lsusb` — should show Airspy device
- Check udev rules installed correctly
- Try unplugging and replugging

**rotctl can't connect to Discovery Drive:**
- Confirm Discovery Drive is powered
- Check Drive and Pi are on same WiFi network
- Check Drive IP/hostname in Discovery Drive web UI
- Try connecting from MacBook browser to Drive web UI first

**EZRa errors:**
- Check Airspy is detected first
- Check bias tee voltage — feed requires 3.3–5V

---

## Software Version Log

*Record versions here when installed. Update when software is upgraded.*

| Software | Version | Date installed | Notes |
|---|---|---|---|
| Raspberry Pi OS Lite 64-bit | | | |
| Python | | | |
| Astropy | | | |
| Hamlib / rotctl | | | |
| Airspy host library | | | |
| EZRa | | | |

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-30 | Initial setup guide |
