# INV006 — Pointing Model and Mount Calibration

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-06-01  
**Version:** 0.1 — Concept capture  
**Status:** Pre-implementation — data collection begins Phase 3/4  

---

## Motivation

The Discovery Drive rotator has a manufacturer-stated pointing accuracy
of ±1.5°. The 70cm Discovery Dish has a beamwidth of 20–22°, so ±1.5°
pointing error is acceptable for on-target acquisition. However:

1. The actual pointing error behaviour is unknown — is it systematic,
   random, or a combination?
2. Systematic errors can be corrected; random errors can be logged.
3. The LSM6DSOX IMU on the Drive bracket measures actual elevation
   independently of the commanded position.
4. A pointing model built from multiple radio source observations could
   significantly improve effective pointing accuracy.
5. The smartphone compass on the Discovery Drive compass shelf is
   accurate to only ±5–10° in urban conditions — a weak link for
   azimuth calibration.

This investigation characterises the Drive's actual pointing behaviour
and develops a pointing model to correct systematic errors and log
random errors alongside science data.

---

## Background

### Discovery Drive Pointing Specification

| Parameter | Value | Source |
|---|---|---|
| Pointing accuracy | ±1.5° | Manufacturer specification |
| Azimuth range | -360° to +360° | Manufacturer specification |
| Elevation range | 0° to 90° | Manufacturer specification |
| Control protocol | rotctl (WiFi) / EasyComm II | Manufacturer specification |

### Error Budget

| Source | Axis | Error | Notes |
|---|---|---|---|
| Discovery Drive | Az + El | ±1.5° | Manufacturer stated — dominant |
| Tripod levelling | El | ~0.03° | 3ft builder's level — negligible |
| IMU calibration | El | ~0.2–0.6° | Mounting alignment dependent |
| Smartphone compass | Az | ±5–10° | Urban environment — weakest link |
| **Dominant error** | **Both** | **±1.5°** | Drive spec; compass worse in Az |

### Error Classification

**Systematic error:** The Drive consistently points to a predictably
wrong position. Example: always 0.8° low in elevation at 45° commanded.
These are correctable with a pointing model.

**Random error:** The Drive lands somewhere different within ±1.5° each
time with no predictable pattern. These cannot be corrected but can be
logged — science data is tagged with measured pointing rather than
commanded pointing.

**Real behaviour:** Almost certainly a combination of both. This
investigation separates the two components.

### IMU Role in Pointing

The LSM6DSOX IMU measures actual dish elevation via accelerometry
(gravity reference). It provides:

- **Elevation verification:** Did the Drive reach the commanded elevation?
- **Elevation correction:** Apply systematic offset from pointing model
- **Elevation logging:** Tag science data with measured elevation

**Azimuth limitation:** The IMU cannot directly measure azimuth —
accelerometry has no azimuth reference. A magnetometer could in
principle provide azimuth, but magnetometers are unreliable near
metal structures and urban electrical interference.

**Azimuth calibration therefore relies on radio source transits.**

### Smartphone Compass Assessment

The Discovery Drive includes a compass shelf for smartphone azimuth
reference. Typical accuracy:

| Condition | Accuracy |
|---|---|
| Ideal (open field, no interference) | ±2–5° |
| Urban environment | ±5–10° |
| Near metal structures / electronics | ±10°+ |

**Conclusion:** Smartphone compass is useful for rough initial
orientation only. Not suitable for calibrated pointing. Radio source
transits are the correct azimuth calibration method.

### Magnetic Declination

San Jose, CA: **13.0°E** (2026), changing ~0.1°/year.
Must be applied when converting between magnetic and true north.
rotctl uses true north — verify software applies correction.

---

## Azimuth Calibration Methods

In order of accuracy:

| Method | Accuracy | When available |
|---|---|---|
| Smartphone compass | ±5–10° | Always — rough orientation only |
| GPS bearing to known landmark | ~±1° | Initial setup |
| Polaris alignment | ~±0.5° | Clear night, northern sky visible |
| Solar transit | ~±0.1° | Daytime — calculated sun position |
| **Radio source transit** | **~±0.1°** | **Primary method — best accuracy** |

### Radio Source Transit Method

Point dish at meridian (due south, azimuth 180°). As a known strong
radio source (Cas A, Cygnus A, or the Sun) transits the meridian, it
passes through the beam. The time of peak signal defines the true
meridian crossing. Compare with calculated transit time from ephemeris
to derive azimuth pointing error.

**Sources suitable for transit calibration at Blue Rock (37.3°N):**

| Source | Transit elevation | Flux at 1420 MHz | Notes |
|---|---|---|---|
| Cas A | ~74° | ~2567 Jy (2026) | Primary — brightest calibrator |
| Cygnus A | ~67° | ~1580 Jy | Secondary calibrator |
| Sun | Varies seasonally | Very bright | Use with heavy attenuation |
| Virgo A (M87) | ~56° | ~270 Jy | Fainter — Phase 4+ |

---

## Pointing Model Architecture

A pointing model maps commanded position to actual position (or vice
versa) using a set of calibration observations.

### Minimum viable model (Phase 4)

Three-parameter model per axis:

**Elevation:**
```
El_actual = El_commanded + ΔEl_offset + ΔEl_flex × cos(El_commanded)
```
- ΔEl_offset: constant elevation offset (e.g. mechanical zero point error)
- ΔEl_flex: flexure term (structure bends under gravity at different elevations)

**Azimuth:**
```
Az_actual = Az_commanded + ΔAz_offset + ΔAz_collimation × tan(El_commanded)
```
- ΔAz_offset: constant azimuth offset (compass/north alignment error)
- ΔAz_collimation: elevation-azimuth coupling (mount not perfectly vertical)

### Full model (Phase 5+)

Extended pointing model with additional terms for:
- Atmospheric refraction (small at 1420 MHz, increases at low elevation)
- Tube flexure (dish structure deformation under gravity)
- Seasonal thermal expansion effects

### Calibration observations required

Minimum 6 observations at different (Az, El) positions to fit the
three-parameter model. Ideally 20+ for robust fit. Sources: Cas A
at multiple hour angles, Cygnus A, Sun (with attenuation).

---

## Implementation Plan

### Phase 3 — Baseline characterisation

Before pointing model — establish raw Drive behaviour:

1. Command Drive to a grid of positions (Az, El)
2. Log commanded position vs IMU-measured elevation at each point
3. Repeat 3× per position to assess repeatability
4. Characterise systematic vs random components in elevation

**Result:** Elevation error map — commanded vs actual across the sky.

### Phase 4 — Radio source transit calibration

With dish and feed operational:

1. Observe Cas A transit — record time of peak signal
2. Compare with calculated Cas A transit time from ephemeris
3. Derive azimuth pointing offset
4. Repeat at multiple hour angles (different elevations) to fit
   collimation term
5. Observe Cygnus A for independent check
6. Fit minimum pointing model — ΔEl_offset, ΔEl_flex, ΔAz_offset,
   ΔAz_collimation

**Result:** Pointing model coefficients → apply corrections to rotctl
commanded positions.

### Phase 4 — IMU-assisted real-time correction

With pointing model established:

1. Command Drive to target position
2. Apply pointing model correction to commanded position
3. After slew, read IMU elevation
4. If |IMU elevation − model-corrected elevation| > 0.5° → flag
5. Log actual IMU elevation with every science spectrum

**Result:** Science data tagged with best-estimate actual pointing.

### Phase 5 — Full pointing model refinement

With 1+ year of observations:

1. Accumulate pointing residuals from all source transits
2. Fit extended pointing model with additional terms
3. Assess seasonal and thermal variations
4. Publish pointing model characterisation in SARA proceedings

---

## Relationship to Other Investigations

| Investigation | Relationship |
|---|---|
| INV001 — Noise Budget | Pointing error affects beam efficiency — mispointing reduces effective collecting area |
| INV005 — Reference Channel | Accurate pointing needed for spatial RFI correlation |
| INV004 — ML RFI | Science spectra tagged with actual pointing — improves ML training labels |

---

## Relationship to Thesis

| Thesis chapter | INV006 contribution |
|---|---|
| Instrumentation | Drive specification, IMU integration, pointing architecture |
| Methodology | Pointing model derivation, transit calibration method |
| Results | Pointing model coefficients, residual errors, improvement vs uncorrected |
| Conclusions | Achievable pointing accuracy for 70cm dish in urban portable installation |

---

## Levelling Platform

A wooden levelling platform is planned to ensure the tripod is
consistently vertical session to session, eliminating tilt as a
source of systematic pointing error.

### Specification

| Parameter | Value |
|---|---|
| Material | White oak (flooring grade) — dense, stable, weather resistant |
| Finish | Exterior paint — primer + 2 topcoats all surfaces including end grain |
| Adjustable feet | Corner levelling feet — M8/M10 threaded rod, rubber pads, lock nuts |
| Tripod foot retainers | Three-point cradle — small oak blocks or stainless angle brackets |
| Levelling reference | Bull's-eye spirit level fixed to platform surface |
| Levelling tool | 3ft builder's level — accurate to ~0.03°, well within IMU uncertainty |
| Tripod foot spread | Measure on arrival — determines minimum platform size |

### Levelling procedure (per session)

1. Place platform in marked patio position
2. Place tripod in retainers
3. Adjust corner feet until bull's-eye level shows centre
4. Confirm with builder's level across both axes
5. Lock all corner feet
6. IMU confirms vertical after system startup

### Why levelling matters for pointing

An unlevel tripod introduces a systematic elevation error that varies
with azimuth — the classic "cone error" in mount alignment. A 1°
tilt in the mount introduces azimuth-dependent elevation errors of
up to 1° × sin(El). At El = 74° (Cas A transit), this is ~0.96° —
comparable to the Drive spec itself. Levelling to ~0.03° reduces
this to ~0.03° × sin(74°) = ~0.03° — negligible.

---

## Open Questions

- [ ] Measure tripod foot spread — determines platform dimensions
- [ ] Determine optimal tripod foot retainer design — routed recesses
      vs wooden blocks vs stainless brackets
- [ ] Select bull's-eye level for permanent platform mounting
- [ ] Assess whether rotctl applies magnetic declination correction
      automatically or requires manual input
- [ ] Determine minimum number of calibration observations for robust
      pointing model fit
- [ ] Assess feasibility of solar transit calibration — attenuation
      required; safety considerations
- [ ] Consider adding magnetometer to IMU package for azimuth — assess
      urban interference rejection requirements first

---

## Key References

| Reference | Relevance |
|---|---|
| Wallace & Capitaine (2006) — pointing models | Standard pointing model formulation |
| Mangum (2001) — NRAO pointing | Practical pointing model implementation |
| Marr, Snell & Kurtz Vol. 1 | Telescope pointing and calibration |
| design/DISH_POSITION_CALIBRATION.md | IMU hardware specification |
| design/ENCLOSURE_DESIGN.md | Drive bracket and IMU mounting |
| BRRO_references.bib | Full bibliography |

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1 | 2026-06-01 | Initial concept — Drive error budget, azimuth calibration methods, pointing model architecture, IMU role, levelling platform specification, phased implementation plan |
