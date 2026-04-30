# Blue Rock Radio Observatory — Research Plan

**Observer:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory, Blue Rock Court, San Jose, California, USA  
**Repository:** https://github.com/Steve-Hawker/blue-rock-radio-observatory  
**Plan version:** 1.2  
**Date:** 2026-04-30  
**Academic context:** BSc Honours Astronomy (Distance Learning), University of Lancashire  
**Anticipated supervisor:** Dr Megan Argo, University of Lancashire  

---

## 1. Overview

This document describes the planned observing programme at Blue Rock Radio Observatory
for the period 2026–2031, in support of a BSc Honours thesis in Astronomy and potential
subsequent MRes research. The programme focuses on systematic hydrogen line (HI, 1420.405 MHz)
observations using a 70cm parabolic dish with AZ/EL tracking capability.

The BSc Honours degree (University of Lancashire, distance learning) requires 360 credit
points across 18 courses, with thesis submission anticipated in 2030/31. This gives
approximately four years of systematic observations before write-up, strengthening the
dataset considerably compared with an earlier projected completion date.

The author's background in engineering informs both the instrumentation design and signal
processing pipeline development aspects of this programme. The central motivation is to
develop and validate techniques for low-cost, small-aperture HI spectroscopy from an urban
site, and to apply those techniques to produce scientifically meaningful results comparable
with professional survey data.

---

## 2. Scientific Objectives

### Primary objectives

**O1 — HI spectral mapping of M31 (Andromeda Galaxy)**  
Detect and characterise the integrated HI spectral profile of M31. Use the AZ/EL
tracking capability to accumulate long integrations at fixed pointings and, where
sensitivity permits, attempt to discriminate velocity structure across the major axis
by systematic offset pointing. Compare results quantitatively with the HI4PI survey
and published rotation curve data.

**O2 — High-velocity cloud monitoring (Complex C)**  
Conduct systematic, long-baseline monitoring of HVC Complex C at anomalous LSR
velocities (-90 to -170 km/s). Build a high-sensitivity integrated spectrum through
co-addition of sessions across the three-year programme. Search for any brightness
variability. Map velocity gradient across the cloud extent by varying pointing position.

**O3 — RFI environment characterisation**  
Systematically characterise the radio frequency interference environment at 1420 MHz
from an urban site in San Jose, California. Document temporal patterns (time of day,
day of week, seasonal), identify persistent and intermittent sources, and develop
flagging strategies. This is both a scientific contribution and a necessary foundation
for all other objectives.

### Secondary objectives

**O4 — HI detection of M33 (Triangulum Galaxy)**  
Attempt detection of M33 HI emission. M33 is fainter than M31 but well-placed from
San Jose. A confirmed detection with characterised spectral profile would complement
the M31 dataset and demonstrate the programme's sensitivity limits.

**O5 — Cas A secular flux decrease**  
Monitor Cassiopeia A flux density over the three-year programme with sufficient
consistency and calibration rigour to detect or constrain the known secular decrease
of ~0.77% per year. This requires ~2.3% total change to be measurable over the
programme lifetime — challenging but potentially achievable with careful methodology.

**O6 — HI absorption toward Cas A**  
Use Cas A as a bright background continuum source to detect foreground HI absorption
features at known LSR velocities corresponding to Perseus arm, Local arm, and Outer
arm sightline components. Confirms velocity calibration pipeline and spectral resolution.

---

## 3. Instrument Description

### Antenna
- 70cm parabolic dish
- AZ/EL tracking mount with motorised drives
- Beamwidth at 1420 MHz: ~17°
- Effective collecting area: ~0.30 m² (assuming ~80% efficiency)

### Signal chain
Antenna → LNA1 (QPL9547, NF ~0.6 dB) → SAW Filter 1 → LNA2 → SAW Filter 2 → SDR

### System performance estimates
- System temperature (Tsys): ~150 K (estimated, to be measured)
- SEFD: ~138,000 Jy (estimated, to be refined from Cas A observations)
- Beamwidth: ~17° at 1420 MHz

Full equipment details maintained in versioned equipment log files (equipment/E00X).

### Site
- Location: San Jose, California, USA (37.3382°N, 121.8863°W, ~25m ASL)
- Urban environment with significant RFI
- Declination coverage: approximately -40° to +85° (practical limits)
- Notable constraint: LMC/SMC not visible from this latitude

---

## 4. Target List and Prioritisation

| Priority | Target | Type | RA (J2000) | Dec (J2000) | Season | Rationale |
|---|---|---|---|---|---|---|
| 1 | Cas A | SNR / calibrator | 23h 23m 28s | +58° 48' 42" | Year-round | Primary flux calibrator, HI absorption science |
| 1 | M31 | Spiral galaxy | 00h 42m 44s | +41° 16' 09" | Sep–Jan | Primary extragalactic science target |
| 1 | Complex C | HVC | ~15h 30m | ~+55° | Year-round | Primary HVC monitoring target |
| 2 | M33 | Spiral galaxy | 01h 33m 51s | +30° 39' 37" | Sep–Jan | Secondary extragalactic target |
| 2 | M1 | Pulsar wind nebula | 05h 34m 32s | +22° 00' 52" | Oct–Feb | Secondary calibrator, personal science target |
| 2 | Galactic plane | ISM | Various | Various | Year-round | Spiral arm structure, pipeline validation |
| 3 | M81 | Spiral galaxy | 09h 55m 34s | +69° 03' 55" | Year-round | Stretch goal, circumpolar from San Jose |

---

## 5. Observing Strategy

### Scheduling philosophy

Radio astronomy at 1420 MHz does not require darkness. The observer has
full schedule flexibility through part-time working arrangements and distance
learning, with complete control over working hours. This is a significant
operational advantage over observers constrained to fixed night-time windows.

Observations are conducted whenever the following conditions are simultaneously met:
- Target is above useful elevation (>30°, ideally >45°)
- Cas A is accessible for calibration
- RFI environment is acceptable (determined by brief pre-session survey)
- No adverse weather (high wind primarily)

This opportunistic scheduling approach maximises total integration time
accumulated over the three-year programme. Two sessions per week is a
**minimum floor** not a target ceiling. During prime M31 season (Sep–Jan)
with good conditions, significantly more sessions per week are anticipated.

### Daytime observing

Daytime observations are explicitly part of the programme. At 1420 MHz
the Sun does not affect observations provided the beam is not pointed
within ~20–30° of the solar position. Stellarium is used to verify
solar separation before each session.

The practical daytime constraint is wind (affects pointing stability)
rather than solar illumination. San Jose afternoons can be windy —
morning sessions on calm days are often preferable to afternoon sessions.

### Session cadence
- Minimum: two sessions per week during active periods
- Expected average: three to five sessions per week in prime season
- Cas A: observed at start and end of every science session for calibration
- M31: concentrated observing September–January
- Complex C: year-round, lower priority during M31 season

### Standard session structure
Each session follows this sequence:

1. Check equipment state — confirm equipment log version current (5 min)
2. Brief RFI survey — confirm band is usable (5 min)
3. Point to Cas A — opening calibration spectrum (15 min)
4. Slew to primary target — integrate (1–4 hours, set and monitor remotely)
5. Return to Cas A — closing calibration check (15 min)
6. Data backup to secondary storage
7. Session log completion and Git commit (15 min)

**Total active time per session: ~50 minutes regardless of integration length.**
The integration itself runs unattended. This ratio makes frequent sessions
practical even on working days.

### Integration strategy
Long-baseline co-addition is the primary sensitivity strategy. Individual sessions
will be reduced and then co-added in software, with careful alignment in LSR velocity
space. This requires consistent Doppler correction across all sessions — see Section 7.

### Seasonal planning
| Season | Primary focus |
|---|---|
| Sep — Jan | M31 (high elevation, best sensitivity) — maximum session frequency |
| Feb — Apr | Complex C, Galactic plane, pipeline development |
| May — Aug | Complex C, M81, calibration, software work |

---

## 6. Software and Pipeline Plan

### Phase 1 — Year 1 (2026–2027): EZRa primary
Use EZRa for all data acquisition. EZRa handles frequency switching, baseline
subtraction, and Doppler correction automatically. Focus is on establishing
reliable observing routine, characterising system performance, and beginning
data accumulation on all primary targets.

### Phase 2 — Year 2 (2027–2028): GNU Radio development
Develop a custom signal processing pipeline in GNU Radio and Python running
in parallel with EZRa. Key components to implement:

- Frequency switching (on/off line)
- Dicke switching (if hardware permits)
- Doppler correction to LSR using Astropy
- RFI flagging and excision
- Spectral baseline subtraction
- Session co-addition with LSR alignment

### Phase 3 — Year 3 (2028–2029): Custom pipeline primary
Custom pipeline becomes primary data reduction tool. EZRa retained for
cross-validation. Final dataset produced from custom pipeline with full
provenance documentation.

### Software stack
- GNU Radio — signal processing and data acquisition
- Python 3 / NumPy / SciPy — data reduction
- Astropy — Doppler corrections, coordinate transforms, FITS I/O
- Matplotlib / Healpy — visualisation
- Git / GitHub — version control and archiving

### Comparison datasets
- **HI4PI survey** (Ben Bekhti et al. 2016, A&A 594 A116) — primary professional benchmark
- **WSRT M31 HI data** — M31 rotation curve comparison
- **Chemin et al. 2009** — M31 HI kinematics reference
- **Wakker et al. 2007, 2008** — Complex C reference

---

## 7. Doppler Correction Policy

All velocities will be expressed in the **LSR (Local Standard of Rest)** frame.
Corrections applied using `astropy.coordinates.SkyCoord.radial_velocity_correction()`.

Components corrected:
- Earth's diurnal rotation (~0.5 km/s)
- Earth's orbital velocity (~30 km/s, seasonal variation)
- Solar motion relative to LSR (~20 km/s)

All raw data files will retain original topocentric frequencies. Doppler correction
applied at reduction stage and documented in session logs. This policy ensures raw
data is never altered and corrections can be reapplied if methodology improves.

---

## 8. Calibration Policy

### Flux calibration
Cassiopeia A is the primary flux calibration standard.  
Reference flux: 2723 Jy at 1420 MHz (epoch J2000, Baars et al. 1977 scale).  
Secular decrease: 0.77% per year.  
All Cas A observations recorded in `calibration/CasA_timeseries.csv`.

### System temperature
Tsys derived from each Cas A observation using the Y-factor method.
Time series of Tsys maintained to detect any system degradation.

### Velocity calibration
Verified against known HI absorption features toward Cas A (Perseus arm ~-47 km/s,
Local arm ~-5 km/s). Any systematic velocity offset to be documented and corrected.

### Equipment change policy
Any change to the signal chain (component replacement, cable change, repointing,
software version change) requires:
1. A new equipment log version (E00X) before the next observation
2. A Cas A calibration observation at the first opportunity after the change
3. A note in the session log referencing the new equipment version

---

## 9. Known Limitations

The following limitations are recognised at the outset of this programme. They are
documented here to demonstrate that results are interpreted within understood constraints,
not to minimise the scientific value of the work.

**Aperture** — A 70cm dish has an SEFD of ~138,000 Jy, severely limiting sensitivity
compared with professional instruments. Long integration times partially compensate
but fundamental sensitivity limits apply. Virgo cluster galaxies and most objects
beyond the Local Group are not achievable targets.

**Beam size** — The ~17° beamwidth at 1420 MHz means all targets are unresolved.
No spatial mapping is possible within a single pointing. Crude spatial discrimination
across extended sources (M31, Complex C) requires careful offset pointing strategy.

**Urban RFI** — San Jose is a challenging RFI environment. The 1420 MHz band has
some statutory protection but interference is inevitable. Robust flagging is essential
and some data loss is expected.

**Single polarisation** — The feed captures a single polarisation. This precludes
Zeeman splitting measurements and introduces sensitivity loss relative to dual
polarisation systems.

**Pointing accuracy** — Absolute pointing accuracy of the AZ/EL mount is to be
determined. Systematic pointing errors would affect flux measurements of compact sources.

**Atmospheric effects** — Minor at 1420 MHz but not negligible for precision
flux measurements. Not corrected in Phase 1; may be addressed in Phase 2 pipeline.

---

## 10. Academic Schedule and Observing Timeline

### Degree Credit Structure

| Academic Year | Courses | Credits | Cumulative | Notes |
|---|---|---|---|---|
| 2025/26 | 2 | 40 | 40 | Current year |
| 2026 | 2 | 40 | 80 | Accredited from BEng |
| 2026/27 | 3 | 60 | 140 | Approved to proceed |
| 2027/28 | 3 | 60 | 200 | |
| 2028/29 | 3 | 60 | 260 | |
| 2029/30 | 3 | 60 | 320 | |
| 2030/31 | 2 + thesis | 40 | 360 | Thesis from this project |

Total: 360 credits (18 courses) for BSc Honours.
Two courses accredited from BEng — formal recognition of engineering background.
Thesis submission anticipated: 2030/31.

### Observing Milestones

### Year 1 — 2025/26 — Commissioning
- [ ] Complete observatory construction and first light
- [ ] E001 equipment log completed — full system documented
- [ ] Cas A first detection — system temperature measured (E002 created)
- [ ] EZRa pipeline operational
- [ ] First RFI survey completed
- [ ] RFI characterisation programme begun
- [ ] M31 first detection attempt
- [ ] Complex C first detection attempt
- [ ] Formal site assessment completed — horizon profile measured
- [ ] Begin BSc background reading and literature review
- [ ] Raspberry Pi 3 configured and operational

### Year 2 — 2026/27 — Establishment
- [ ] M31 integrated spectrum with SNR > 5
- [ ] Complex C integrated spectrum confirmed
- [ ] HI absorption toward Cas A detected — velocity calibration confirmed
- [ ] Cas A secular decrease monitoring — first full year data
- [ ] RFI environment fully characterised — flagging algorithm operational
- [ ] GNU Radio custom pipeline begun
- [ ] M33 detection attempted
- [ ] DDOEE installed — Pi and SDR moved to mast (autumn 2026)

### Year 3 — 2027/28 — Development
- [ ] M31 integrated spectrum with SNR > 10
- [ ] GNU Radio custom pipeline validated against EZRa
- [ ] Custom pipeline becomes primary data acquisition tool
- [ ] M31 velocity structure — offset pointing programme begun
- [ ] Cas A secular decrease — two year baseline
- [ ] INV001 noise budget analysis complete
- [ ] INV002 digital filter investigation complete
- [ ] Upgrade path decision made — implement if warranted

### Year 4 — 2028/29 — Maturity
- [ ] Full science programme running on custom pipeline
- [ ] M31 four-year dataset accumulating
- [ ] Complex C four-year monitoring dataset
- [ ] Cas A secular decrease — three year baseline
- [ ] INV003 RFI flagging investigation complete
- [ ] Begin thesis outline discussions with supervisor
- [ ] SARA proceedings paper drafted

### Year 5 — 2029/30 — Final Observations
- [ ] Final observations season — maximum integration on primary targets
- [ ] All datasets complete and archived
- [ ] Full quantitative comparison with HI4PI and reference literature
- [ ] Thesis outline agreed with supervisor
- [ ] Begin thesis writing

### Year 6 — 2030/31 — Write Up
- [ ] BSc thesis written and submitted
- [ ] Four years of observations behind the thesis
- [ ] MRes application considered — dataset available as supporting evidence
- [ ] SARA proceedings paper submitted

---

## 11. Success Criteria

### BSc thesis level
- Detection of M31 HI emission with SNR > 5 in integrated spectrum
- Spectral profile consistent with published double-horn morphology
- Quantitative comparison with HI4PI demonstrating pipeline validity
- Detection of Complex C at anomalous velocity
- Documented RFI characterisation of site
- Validated custom reduction pipeline (if Phase 2 complete)

### MRes level (if pursued)
All BSc criteria plus:
- M31 velocity structure discriminated across major axis by offset pointing
- Multi-year Complex C monitoring dataset with flux density measurements
- Custom GNU Radio pipeline fully documented and independently reproducible
- Cas A secular decrease measured or meaningfully constrained
- Results presented in SARA proceedings or equivalent

---

## 12. Acknowledgements

This observing programme was conceived with the assistance of discussions arising
from BSc Introduction to Astronomy coursework at the University of Lancashire.
The author thanks Dr Megan Argo (University of Lancashire) for encouragement and guidance.

The observatory name Blue Rock Radio Observatory derives from its location on
Blue Rock Court, San Jose, California.

---

## Plan Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-28 | Initial plan |
| 1.1 | 2026-04-30 | Section 5 — expanded observing strategy, daytime observing, flexible scheduling |
| 1.2 | 2026-04-30 | Revised timeline to reflect actual degree structure 2025–2031, four years observations, thesis 2030/31 |

---

*This plan is a living document. Amendments will be committed to the repository
with clear version notes explaining the reason for any change.*
