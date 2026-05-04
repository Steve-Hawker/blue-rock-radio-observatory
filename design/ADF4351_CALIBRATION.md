# ADF4351 Signal Source — Calibration Design

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-02  
**Version:** 1.0  

---

## Overview

This document describes the use of an ADF4351 wideband PLL synthesiser
module as a calibration signal source for the Blue Rock Radio Observatory
signal chain. The ADF4351 covers 35 MHz to 4.4 GHz, comfortably spanning
the 1380–1460 MHz HI feed passband and the 1422 MHz LO operating frequency.

The ADF4351 provides:
- Frequency calibration — LO offset verification
- Passband shape measurement — empirical SAW filter characterisation
- Gain chain verification — Friis cascade validation
- IQ imbalance quantification — pipeline correction coefficients
- Annual comparative calibration — five-year system performance record

The ADF4351 complements Cas A flux calibration — it does not replace it.
Cas A provides absolute flux calibration and sensitivity measurement.
The ADF4351 provides frequency, gain, and linearity characterisation.
Both are required for a complete calibration programme.

---

## Hardware

### ADF4351 module

| Parameter | Value |
|---|---|
| Frequency range | 35 MHz — 4.4 GHz |
| Output power | Approximately 0 to -4 dBm (register adjustable) |
| Reference oscillator | 25 MHz TCXO (onboard) |
| Reference accuracy | ~10 ppm (onboard crystal) |
| Interface | SPI (controllable via USB dongle or Arduino) |
| Supply voltage | 5V USB |
| Cost | ~$25 |

### Required accessories

| Item | Purpose | Cost |
|---|---|---|
| SMA attenuator kit | Protect LNA from overdrive | ~$15 |
| SMA cables (15–30cm) | Bench connections | ~$10 |
| USB SPI controller or Arduino | ADF4351 frequency control | ~$10 |
| **Total** | | **~$60** |

### Optional upgrade — GPSDO reference

The onboard 25 MHz crystal reference provides ~10 ppm accuracy. At
1422 MHz, 10 ppm = 14.2 kHz frequency uncertainty = 3.0 km/s velocity
uncertainty. This is marginal for LO frequency verification.

A GPS-disciplined oscillator (GPSDO) reference improves accuracy to
~10 ppb — frequency uncertainty of 14 Hz at 1422 MHz = 0.003 km/s.
Recommended after Phase 1 commissioning if LO frequency verification
proves important.

| Option | Accuracy at 1422 MHz | Velocity equiv. | Cost |
|---|---|---|---|
| Onboard crystal | ~14.2 kHz | ~3.0 km/s | Included |
| GPSDO reference | ~14 Hz | ~0.003 km/s | ~$50–100 |
| Rubidium standard | ~1.4 Hz | ~0.0003 km/s | ~$200+ |

**Decision point:** After first LO frequency check with onboard crystal,
assess whether accuracy is sufficient for programme requirements.

---

## Safety — LNA Protection

**Critical:** The ADF4351 output of 0 dBm will damage or saturate the
HI feed LNA (QPL9547) if injected directly. Always use attenuation.

The QPL9547 P1dB compression point is approximately +17 dBm input.
Operating at least 20 dB below P1dB is required for linear operation.
Maximum safe input for calibration: approximately -3 dBm.

**Minimum attenuation: 30 dB** between ADF4351 output and feed input.
This gives -30 dBm at the LNA input — 47 dB below P1dB. Safe.

Standard calibration configuration:
```
ADF4351 (0 dBm) → 30 dB attenuator → Feed input → LNA1 → ...
```

Always verify attenuator is connected before applying ADF4351 output
to any feed or LNA input. Note in session log.

---

## Injection Points

Two injection points in the signal chain serve different purposes:

**Point A — Feed input (before LNA1):**
Tests the complete signal chain: LNA1 → SAW1 → LNA2 → SAW2 → SDR.
Use for: gain chain measurement, passband sweep, IQ imbalance check.
Requires: 30 dB minimum attenuation.

**Point B — Between SAW2 and SDR (after feed output):**
Tests SDR and downstream only, bypassing the feed.
Use for: SDR-only characterisation, isolating feed vs SDR problems.
Requires: 20 dB minimum attenuation.

A labelled SMA connector on the feed input for Point A injection
should be installed during commissioning and noted in E002.

---

## Calibration Procedures

### CAL-001 — LO Frequency Verification

**Purpose:** Verify SDR LO frequency accuracy. Frequency error converts
directly to velocity error in HI spectroscopy.

**Frequency error to velocity error:**
$$\Delta v = \frac{\Delta f}{f_{HI}} \times c = \frac{\Delta f}{1420.405 \times 10^6} \times 299{,}792 \text{ km/s}$$

At 1420 MHz: 1 kHz LO error = **0.21 km/s velocity error**

**Procedure:**
1. Set ADF4351 to 1421.000 MHz (1.000 MHz below LO at 1422.000 MHz)
2. Connect ADF4351 → 30 dB attenuator → feed input
3. Open GQRX or GNU Radio, LO set to 1422.000 MHz
4. Observe tone in baseband spectrum — should appear at -1.000 MHz
5. Measure actual tone frequency to nearest 100 Hz
6. Calculate LO error: error = (measured offset + 1.000 MHz)
7. Calculate velocity equivalent
8. Record in ADF4351_timeseries.csv

**Acceptance criterion:** LO error < 1 kHz (< 0.21 km/s velocity error)
**Frequency:** Every observing season start, and after any SDR replacement

---

### CAL-002 — Passband Shape Measurement

**Purpose:** Empirical characterisation of SAW filter cascade passband.
Fills in SAW_FILTER_DESIGN.md commissioning measurements. Reveals
insertion loss profile, passband ripple, and roll-off characteristics.

**Procedure:**
1. Connect ADF4351 → 30 dB attenuator → feed input (Point A)
2. Set SDR to record power spectrum with 1 MHz resolution bandwidth
3. Step ADF4351 from 1360 MHz to 1480 MHz in 1 MHz steps
4. At each frequency: record SDR centre power, wait 2 seconds, step
5. Normalise to flat — subtract mean power across flat passband region
6. Plot passband shape: frequency vs normalised power (dB)
7. Identify: 3 dB bandwidth, passband ripple, roll-off rate at edges
8. Save plot and raw data to calibration/ directory
9. Compare with SAW filter datasheets (when received from KrakenRF)

**Expected result:**
- Flat passband: 1380–1460 MHz (within ±1 dB)
- Sharp roll-off outside passband
- Ripple < 1 dB across flat region

**Frequency:** Once during commissioning, then annually

---

### CAL-003 — Gain Chain Verification

**Purpose:** Measure total signal chain gain and compare with Friis
prediction from INV001. Validates noise budget model.

**Procedure:**
1. Set ADF4351 output power to known value (register setting)
2. Record exact ADF4351 output power with power meter if available,
   otherwise use nominal datasheet value
3. Connect ADF4351 → 30 dB attenuator → feed input
4. Set ADF4351 to 1420.000 MHz (within passband, away from DC)
5. Record SDR signal level (dBFS) at the tone frequency
6. Calculate total chain gain:
   G_total = SDR_level(dBFS) - ADF4351_power(dBm) + 30 dB(att)
7. Compare with Friis prediction from INV001
8. Record discrepancy and note any explanation

**Frequency:** During commissioning, then annually

---

### CAL-004 — IQ Imbalance Measurement

**Purpose:** Quantify IQ amplitude and phase imbalance to derive
correction coefficients for GNU Radio pipeline (see
DOWNCONVERSION_ARCHITECTURE.md, mitigation S2).

**Procedure:**
1. Connect ADF4351 → 30 dB attenuator → feed input
2. Set ADF4351 to LO + 500 kHz = 1422.500 MHz
3. In a perfect IQ system: single tone at +500 kHz in baseband
4. Measure true tone amplitude: A_true (dBFS)
5. Measure image tone amplitude at -500 kHz: A_image (dBFS)
6. IQ image rejection ratio (IRR) = A_true - A_image (dB)
7. Apply IQ correction in GNU Radio and repeat — verify improvement
8. Record IRR before and after correction

**Typical values:**
- Uncorrected V4c: IRR ~30–35 dB
- Uncorrected Airspy R2: IRR ~35–40 dB
- After software correction: IRR ~55–65 dB

**Acceptance criterion:** IRR > 50 dB after correction
**Frequency:** During commissioning, then after any SDR firmware update

---

### CAL-005 — Annual Comparative Calibration

**Purpose:** Track system performance over the five-year programme.
Detect gradual degradation before it affects science data.

**Procedure:** Run CAL-001 through CAL-004 in sequence. Record all
results in ADF4351_timeseries.csv with date and equipment version.

**Timing:** Start of each M31 observing season (September each year)

**What to look for:**
- LO frequency drift between seasons
- Passband shape changes (connector degradation, LNA aging)
- Gain chain changes (LNA gain drift, cable loss changes)
- IQ imbalance changes (SDR chip aging)

Any parameter changing by more than 1 dB between seasons warrants
investigation before the season's science observations begin.

---

## Python Automation Script

A Python script to automate the ADF4351 frequency stepping for CAL-002
passband sweep — controlling the ADF4351 via SPI and logging SDR power
at each step:

```python
# adf4351_calibration.py — to be developed in Phase 2
# Requires: pyserial, numpy, rtlsdr or airspy Python bindings
# Controls ADF4351 via USB-SPI adapter
# Logs power at each frequency step to CSV
# See INV002_digital_filters for GNU Radio pipeline integration
```

Full script development deferred to Phase 2 alongside GNU Radio
pipeline development (INV002).

---

## Relationship to Other Calibration Methods

| Method | What it measures | Frequency |
|---|---|---|
| Cas A Y-factor | Tsys, SEFD, absolute flux scale | Every session |
| ADF4351 CAL-001 | LO frequency accuracy | Annual |
| ADF4351 CAL-002 | Passband shape, SAW filter response | Commissioning + annual |
| ADF4351 CAL-003 | Total chain gain | Commissioning + annual |
| ADF4351 CAL-004 | IQ imbalance | Commissioning + after updates |
| HI4PI comparison | Integrated flux scale validation | Per target, per season |

---

## References

- Analog Devices ADF4351 datasheet — frequency synthesiser specifications
- SAW_FILTER_DESIGN.md — passband measurement context (this repository)
- DOWNCONVERSION_ARCHITECTURE.md — IQ imbalance mitigation (this repository)
- INV001_noise_budget — Friis gain chain (this repository)
- INV002_digital_filters — automation script development (this repository)
- Laufer — *The Hobbyist's Guide to the RTL-SDR* — filter measurement
  with low cost equipment

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-02 | Initial document — four calibration procedures, hardware specification, LNA protection requirements, annual programme |
