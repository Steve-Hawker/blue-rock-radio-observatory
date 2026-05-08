# Dish Position Calibration — IMU and Environmental Sensor Package

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-07  
**Version:** 1.0  

---

## Overview

This document describes a sensor package mounted to the Discovery Drive
tray that provides:

1. **Continuous dish position verification** — LSM6DSOX 6-axis IMU
   (accelerometer + gyroscope) confirms actual dish position matches
   commanded position from rotctl
2. **Ambient environmental monitoring** — BME280 measures true outside
   temperature, humidity, and pressure for observation metadata

Both sensors share a single I2C bus, connected to Raspberry Pi 2 via
a thin cable running from the DDOEE to the Drive tray.

---

## Motivation

### Dish position verification

The Discovery Drive is a lightweight rotator on a tripod in a garden
environment. Several factors can cause the actual dish position to
differ from the commanded position:

- **Wind loading** — the 70cm dish presents significant wind area;
  gusts can cause transient dish movement during integration
- **Mechanical backlash** — rotator gearing has finite backlash;
  the commanded position may differ from actual by a few tenths of
  a degree
- **Tripod settling** — ground movement, thermal expansion of the
  tripod, and vibration can cause slow drift over a session
- **Slew settling time** — after a slew command, the dish takes time
  to mechanically settle; premature integration captures blurred data

Professional radio telescopes use position encoders and accelerometers
to verify actual pointing. The LSM6DSOX provides this capability for
Blue Rock at low cost.

### Environmental monitoring

Temperature, humidity and pressure affect:
- **Signal chain performance** — QPL9547 noise figure has temperature
  dependence; SAW filter centre frequency drifts at -80 ppm/K
- **Atmospheric path** — pressure and humidity affect propagation
  at 1420 MHz (small but measurable for precise flux calibration)
- **Observation metadata** — professional observatories log weather
  conditions with every observation; this is standard practice

The sensor package is mounted on the Discovery Drive tray — outside
the DDOEE stainless enclosure — giving true ambient readings rather
than enclosure-affected measurements.

---

## Hardware

### Sensor package

| Component | Function | Interface | Cost |
|---|---|---|---|
| LSM6DSOX | 6-axis IMU — accelerometer + gyroscope | I2C | ~$5-10 |
| BME280 | Temperature, humidity, pressure | I2C | ~$8-10 |
| ABS project box (small) | Weather protection housing | — | ~$3-5 |

Both sensors share the I2C bus — different I2C addresses, no conflict.

### Enclosure

Small ABS project box mounted to the **underside of the Discovery Drive
tray** (the plate that faces downward when the dish points at the sky).

**Weather protection strategy:**
- ABS box faces downward — rain cannot pool inside
- Small holes drilled in the bottom of the ABS box for ventilation
  and sensor access to ambient air
- No rain ingress — holes face down, protected by the tray above
- No active heating or sealing required

**Mounting:**
- Rigid epoxy or M3 screws directly to the Drive tray
- LSM6DSOX must be rigidly mounted — any flex invalidates tilt
  measurements. No foam tape or compliant mounts.
- BME280 can be less rigidly mounted as position is irrelevant

---

## Sensor Specifications

### LSM6DSOX — Dish Position

| Parameter | Value |
|---|---|
| Accelerometer range | ±2g to ±16g (selectable) |
| Accelerometer resolution | 16-bit |
| Gyroscope range | ±125 to ±2000 dps (selectable) |
| Gyroscope resolution | 16-bit |
| Interface | I2C / SPI |
| Supply voltage | 1.71V to 3.6V |
| I2C address | 0x6A or 0x6B (selectable) |

**At ±2g range:** tilt resolution from gravity vector ~0.06° — adequate
for dish pointing verification at the ~0.5° level.

### BME280 — Environmental

| Parameter | Value |
|---|---|
| Temperature range | -40°C to +85°C |
| Temperature accuracy | ±1°C |
| Humidity range | 0–100% RH |
| Humidity accuracy | ±3% RH |
| Pressure range | 300–1100 hPa |
| Pressure accuracy | ±1 hPa |
| Interface | I2C / SPI |
| I2C address | 0x76 or 0x77 (selectable) |

---

## I2C Bus Architecture

```
Pi 2 GPIO (I2C bus 1 — pins 3 and 5)
        |
        | I2C cable (4-wire: VCC, GND, SDA, SCL)
        | runs from DDOEE through gland to Drive tray
        |
    ----+----
    |       |
LSM6DSOX  BME280
(0x6A)    (0x76)
```

**Cable:** 4-wire, thin gauge (24-26 AWG adequate for I2C at this
distance). Maximum recommended I2C cable length ~1m without repeater —
distance from DDOEE to Drive tray on mast is approximately 0.5-1m,
within spec.

**Cable routing:** Alongside the 12V DC cable to the Discovery Drive
in Gland 2, or via a small dedicated 4th penetration in the bottom
panel.

---

## Software Architecture

### Pi 2 sensor logging script

```python
# dish_sensors.py — to be developed
# Runs continuously on Pi 2
# Logs to CSV with UTC timestamp
# Accessible over ethernet to Pi 3, Pi 5, and MacBook

# Libraries required:
# pip install smbus2 RPi.GPIO
# BME280: bme280 library or adafruit-circuitpython-bme280
# LSM6DSOX: adafruit-circuitpython-lsm6ds

import time
import board
import busio
import adafruit_bme280
import adafruit_lsm6ds.lsm6dsox as adafruit_lsm6dsox

# Logging fields:
# timestamp_utc, temp_c, humidity_pct, pressure_hpa,
# accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z,
# tilt_elevation_deg, tilt_azimuth_deg
```

### Tilt to elevation angle calculation

From accelerometer gravity vector with dish pointing at elevation θ:

```
elevation = arctan2(accel_z, sqrt(accel_x² + accel_y²))
```

With the sensor rigidly mounted to the tray, elevation angle is
derived directly from the gravity vector — no calibration required
beyond initial orientation measurement.

**Accuracy:** ±0.1° with 16-bit accelerometer at ±2g range and
appropriate averaging (10-100 sample average).

**Comparison with rotctl:** Log both commanded elevation (from rotctl)
and measured elevation (from IMU). Discrepancy > 0.5° triggers a
flag in the observation log.

---

## Calibration Procedure

### IMU orientation calibration

1. Level the tripod carefully using a spirit level
2. Point dish to known elevation (e.g. park position — horizon)
3. Record accelerometer readings as reference orientation
4. Derive rotation matrix from sensor frame to dish frame
5. Apply rotation matrix to all subsequent measurements

This calibration should be repeated:
- After any tripod repositioning
- At the start of each observing season
- If the sensor housing is disturbed

### BME280 cross-check

At the start of each session compare BME280 reading with a reference
thermometer / barometer. Log any offset. San Jose NWS station data
provides a reference for pressure calibration.

---

## Integration with Observation Pipeline

Environmental and position data are logged to CSV files on Pi 2 and
synced to the MacBook at session end. The observation pipeline
(EZRa / custom GNU Radio) should record:

- Start/end temperature, humidity, pressure for each observation
- Mean dish elevation during integration (from IMU)
- RMS dish position scatter during integration (wind effect metric)
- Any position excursion events > 0.5° during integration

These metadata fields become standard columns in the calibration
timeseries and observation log.

---

## Relationship to Existing Documents

- POWER_ARCHITECTURE.md — Pi 2 weather station, I2C cable through gland
- design/ADF4351_CALIBRATION.md — temperature as calibration covariate
- design/SAW_FILTER_DESIGN.md — SAW filter temperature coefficient -80 ppm/K
- setup/SITE_ASSESSMENT_CHECKLIST.md — tripod levelling procedure
- calibration/CasA_timeseries.csv — add temperature column

---

## Action Items

- [ ] Purchase LSM6DSOX breakout board (~$5-10)
- [ ] Purchase BME280 breakout board × 2 (one here, one internal DDOEE)
- [ ] Purchase small ABS project box
- [ ] Develop dish_sensors.py logging script (Pi 2)
- [ ] Determine I2C cable routing — Gland 2 bundle or 4th penetration
- [ ] Initial orientation calibration after tripod setup
- [ ] Add temperature/humidity/pressure columns to CasA_timeseries.csv
- [ ] Add IMU position verification to observation pipeline

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-07 | Initial document — LSM6DSOX + BME280 package on Drive tray; ABS housing design; I2C architecture; software outline; calibration procedure |
