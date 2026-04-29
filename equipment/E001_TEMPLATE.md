# Equipment Log — Version E001

**Date of configuration:** YYYY-MM-DD  
**Supersedes:** (none — first entry)  
**Superseded by:** (leave blank until next change)  
**Reason for this version:** Initial system documentation

---

## Antenna

| Parameter | Value |
|---|---|
| Type | Parabolic dish |
| Diameter | 70 cm |
| Surface material | |
| Feed type | |
| Feed position / focal length | |
| Polarisation | |
| Pointing mechanism | AZ/EL driven mount |
| AZ drive | |
| EL drive | |
| Controller | |
| Tracking software | |

**Notes on antenna condition:**  
(Note any surface damage, feed alignment issues, obstructions in beam path)

---

## Signal Chain

Configured as: **Antenna → LNA1 → Filter1 → LNA2 → Filter2 → SDR**

### LNA1

| Parameter | Value |
|---|---|
| Chip | QPL9547 |
| Board/module | |
| Serial / batch (if known) | |
| Nominal gain (dB) | |
| Noise figure (dB) | ~0.6 (datasheet) |
| Supply voltage | |
| Supply current | |
| Measured gain (if known) | |

### Filter 1

| Parameter | Value |
|---|---|
| Type | SAW |
| Model / part number | |
| Centre frequency | 1420.405 MHz |
| Passband (MHz) | |
| Insertion loss (dB) | |
| Stopband rejection (dB) | |

### LNA2

| Parameter | Value |
|---|---|
| Chip / module | |
| Nominal gain (dB) | |
| Noise figure (dB) | |

### Filter 2

| Parameter | Value |
|---|---|
| Type | SAW |
| Model / part number | |
| Centre frequency | 1420.405 MHz |
| Passband (MHz) | |
| Insertion loss (dB) | |

### Interconnects

| Section | Cable type | Length (m) | Est. loss (dB) |
|---|---|---|---|
| Antenna → LNA1 | | | |
| LNA1 → Filter1 | | | |
| Filter1 → LNA2 | | | |
| LNA2 → Filter2 | | | |
| Filter2 → SDR | | | |

---

## SDR Receiver

| Parameter | Value |
|---|---|
| Model | |
| Firmware version | |
| Driver version | |
| ADC bits | |
| Max sample rate | |
| Frequency range | |

---

## Computing

| Parameter | Value |
|---|---|
| OS | Linux |
| Distribution / version | |
| Kernel version | |
| CPU | |
| RAM | |

---

## Software

| Software | Version | Notes |
|---|---|---|
| EZRa | | |
| GNU Radio | | |
| Python | | |
| Astropy | | |

---

## System Temperature Estimate

| Parameter | Value | Method |
|---|---|---|
| Estimated Tsys (K) | | |
| Estimated SEFD (Jy) | | |
| Date of estimate | | |
| Derived from | | (e.g. Cas A observation, Y-factor, noise figure calculation) |

---

## Calibration State

| Parameter | Value |
|---|---|
| Last Cas A session | (none yet) |
| Derived system temperature | (pending) |
| Known issues | |

---

## Notes

(Any additional notes on this configuration, quirks, planned upgrades, known issues)

---

*Create a new equipment version file whenever any component, cable, software version, or configuration changes. Increment E001 to E002 etc.*
