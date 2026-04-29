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

## Site Characteristics

*Complete this section from a formal site assessment. Use a theodolite app on
the smartphone to measure elevation angles to obstructions accurately.
A compass app gives azimuth bearings. Record date of assessment — site
characteristics may change over time (tree growth, new structures).*

**Site assessment date:** YYYY-MM-DD  
**Assessment method:** (e.g. smartphone theodolite app, visual estimate)

### Location

| Parameter | Value |
|---|---|
| Address | Blue Rock Court, San Jose, California |
| Latitude | 37.3382° N |
| Longitude | 121.8863° W |
| Elevation ASL | ~25m |
| Patio dimensions | ~8ft × 20ft (2.4m × 6.1m) |
| Patio orientation | 210° SW open aspect |
| Patio surface | |
| Patio enclosure | 6ft composite fence all around |

### Magnetic Declination

| Parameter | Value |
|---|---|
| Magnetic declination | 13.0° E (2026) |
| Annual change | ~0.1° per year |
| Last updated | 2026-04-28 |
| Source | (e.g. NOAA magnetic declination calculator) |

*Note: Confirm mount software applies this correction automatically.
Recheck declination value annually and update equipment log if significant.*

### Dish Position on Patio

| Parameter | Value |
|---|---|
| Position description | (e.g. centre of patio, 1m from south fence) |
| Position marked on patio | Yes / No |
| Marking method | (e.g. adhesive dots, chalk marks) |
| Distance from house wall | m |
| Distance from south fence | m |

### Horizon Profile

*Measured azimuth and elevation of obstructions around the full 360°.
Update with accurate measurements from formal site assessment.*

| Azimuth (°) | Direction | Obstruction | Angular height (°) | Distance (m) | Notes |
|---|---|---|---|---|---|
| 0 | N | | | | |
| 30 | NNE | | | | |
| 60 | ENE | | | | |
| 90 | E | | | | |
| 120 | ESE | | | | |
| 150 | SE | House roofline | ~40 (estimated) | ~5 | Single storey |
| 175 | SSE | Deciduous tree | 59 (calculated) | 9 (30ft) | 15m (50ft) tall, deciduous — largely bare Sep–Jan |
| 180 | S | Open | 0 | — | Clear |
| 210 | SSW | Open | 0 | — | Primary observing direction |
| 240 | WSW | Fence | ~10 (estimated) | ~3 | 6ft composite — transparent at 1420 MHz |
| 270 | W | | | | |
| 300 | WNW | | | | |
| 330 | NNW | | | | |

**Horizon notes:**  
- Primary targets (M31, Cas A, Complex C) transit at 74–78° elevation — well above all obstructions
- Tree at 175° clears by ~17° at transit elevation
- SE horizon limited by house — affects rising time for easterly targets
- Composite fence transparent at 1420 MHz — negligible impact at high elevations
- Deciduous tree largely transparent at 1420 MHz when bare (Oct–Feb)

### Target Visibility Summary

*Derived from horizon profile. Update after formal site assessment.*

| Target | Transit Az | Transit El | Obstruction risk | Estimated obs window |
|---|---|---|---|---|
| M31 | 180° | 76° | None at transit | ~6–8 hrs/night (autumn) |
| Cas A | 180° | 74° | None at transit | ~8 hrs/night |
| Complex C | 180° | 78° | None at transit | Year-round |
| M33 | 180° | 69° | None at transit | ~6 hrs/night (autumn) |
| Galactic centre | 180° | 28° | Low elevation — monitor | Limited |

### RFI Environment — Initial Assessment

*To be updated from systematic RFI surveys (see rfi/ directory).*

| Parameter | Value |
|---|---|
| Urban environment | Yes — San Jose CA |
| Nearest known WiFi sources | (note after survey) |
| Known local interference | (note after survey) |
| In-band RFI assessment | (pending first survey) |

---

## Notes

(Any additional notes on this configuration, quirks, planned upgrades, known issues)

---

*Create a new equipment version file whenever any component, cable, software version, or configuration changes. Increment E001 to E002 etc.*
