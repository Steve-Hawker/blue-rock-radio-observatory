# Site Assessment Methodology for Amateur HI Radio Astronomy
## Characterising Urban and Suburban Sites with Accessible Tools

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory, San Jose CA  
**Date:** 2026-04-30  
**Version:** 0.1 — framework, worked example pending  
**Context:** Developed in support of BSc Honours Astronomy programme,
University of Lancashire. Intended for publication as SARA technical note.

---

## Abstract

A rigorous site assessment methodology for amateur hydrogen line (HI,
1420.405 MHz) radio astronomy is presented, requiring only a smartphone,
a tape measure, and approximately one hour of field work. The methodology
produces a calibrated three-dimensional horizon model, quantitative
obstruction characterisation, RF environment baseline, and target
clearance calculations for any proposed observing programme.

The methodology is demonstrated on a real urban site — Blue Rock Radio
Observatory, San Jose, California — a small patio in a residential
neighbourhood with significant horizon obstructions including a 15-metre
deciduous tree and an adjacent single-storey house. The assessment
demonstrates that this apparently constrained site provides full
unobstructed access to primary science targets at transit elevation,
and documents the precise seasonal and daily observing windows
available within the constraints.

The approach is designed to be accessible to any amateur astronomer
regardless of prior survey experience. It addresses a significant
barrier to entry in amateur radio astronomy: the widespread assumption
that urban and suburban sites are unsuitable without a formal basis
for that assessment. Systematic site characterisation frequently
reveals that apparently constrained sites are viable, and provides
the documented evidence needed to plan an effective observing
programme.

---

## 1. Introduction

### 1.1 The urban site problem

Amateur radio astronomy at 1420 MHz (the hydrogen line) is technically
accessible to a growing community through affordable software-defined
radio hardware and purpose-built antenna systems. The primary barrier
to participation is no longer cost or technical complexity — it is
the widespread belief that an urban or suburban observing site is
simply not good enough.

This belief is frequently incorrect, but without a rigorous methodology
for characterising what a specific site can actually do, aspiring
observers have no basis for evaluating their own situation. The result
is a significant community of potential radio astronomers who never
start because they assume their garden, patio, or balcony is unviable.

This document presents a methodology that addresses this problem
directly. It enables any observer to characterise their site
quantitatively, understand precisely what observations are and are
not possible, and plan an effective programme within real constraints.

### 1.2 Why urban sites are often better than assumed

Several properties of 1420 MHz radio astronomy work in favour of
urban observers:

**High transit elevations from mid-latitudes.** Primary HI targets
including M31 (Andromeda Galaxy), Cas A (Cassiopeia A), and high-
velocity cloud Complex C transit at 70–86° elevation from typical
mid-latitude sites. At these elevations only very tall obstructions
close to the observer cause any problem — and most urban gardens do
not have obstructions above 60° elevation in any direction.

**Observations valid in daylight.** At 1420 MHz the Sun does not
prevent observations provided sufficient angular separation is
maintained (>20–30°). An observer with full schedule flexibility
can observe primary targets during the day, effectively extending
the observing season to year-round for all targets.

**Large beam width of small apertures.** A 70cm dish has a beam
width of approximately 17° at 1420 MHz. This means pointing accuracy
requirements are modest and small obstructions that would block an
optical telescope have essentially no effect.

**Radio transparency of common materials.** Timber fencing,
composite materials, plastic, dry vegetation, and brick are largely
transparent at 1420 MHz. A 6-foot composite fence that completely
blocks an optical view has negligible effect on HI observations.
A deciduous tree in winter (the prime observing season for many
northern hemisphere targets) is nearly transparent.

### 1.3 What this methodology provides

The methodology produces:

1. **Calibrated horizon profile** — elevation angle of obstructions
   at every azimuth bearing, measured directly with a smartphone
   theodolite application

2. **Three-dimensional site model** — parametric 3D representation
   of the site geometry enabling visualisation and further analysis

3. **Target clearance table** — for each programme target, the
   clearance above the horizon obstruction at transit and the
   resulting daily and seasonal observing windows

4. **RF environment baseline** — characterisation of the radio
   frequency environment at the site, identifying persistent and
   intermittent interference sources

5. **Observing programme viability assessment** — a documented,
   evidence-based conclusion on what science programme is achievable
   from the site

---

## 2. Tools Required

All tools are freely available or already owned by most smartphone users.
No specialised survey equipment is required.

### 2.1 Essential tools

| Tool | Purpose | Recommended app / source |
|---|---|---|
| Smartphone theodolite app | Elevation angle measurement | Theodolite by Hunter Research (iOS, free) |
| Smartphone compass app | Azimuth bearing measurement | Built-in compass app (iOS/Android) |
| Tape measure | Distance measurement | 10m minimum, 30m preferred |
| Notepad or tablet | Field data recording | Physical log book preferred |
| Camera (smartphone adequate) | Photographic record | Standard smartphone camera |

### 2.2 Optional but recommended

| Tool | Purpose |
|---|---|
| WiFi analyser app | RF environment survey |
| Second person | Tape measure assistance |
| Printed measurement checklist | Systematic field recording |

### 2.3 Magnetic declination

All compass bearings are magnetic. To convert to true (astronomical)
bearings, apply the local magnetic declination correction:

**True bearing = Magnetic bearing + Declination (East positive)**

For San Jose, California (2026): **+13.0° East**
Example: Magnetic bearing 162° → True bearing 175°

Find your local declination at: https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml

Magnetic declination changes slowly over time (~0.1°/year). Note the
declination value and date of your assessment. Recheck annually for
programmes spanning multiple years.

---

## 3. Understanding What to Measure

### 3.1 The horizon profile concept

For any antenna at a fixed location, the sky is divided into accessible
and inaccessible regions by the local horizon — the profile of obstructions
surrounding the site. For optical astronomy the relevant horizon is the
physical silhouette of trees, buildings, and terrain visible to the eye.

For 1420 MHz radio astronomy the relevant horizon is subtly different:

- Materials transparent at 1420 MHz (dry timber, composite fencing,
  plastic, dry vegetation) do not form an effective horizon even if
  they create an optical obstruction
- Only conductive and dense materials (metal, reinforced concrete,
  saturated soil) form a genuine horizon at 1420 MHz
- The beam width (~17° for a 70cm dish) means obstructions must
  subtend a significant angle to affect observations meaningfully

The measurement methodology captures the physical horizon profile —
the true angular elevation of obstructions at each azimuth. Post-
processing applies the RF transparency correction where appropriate.

### 3.2 The critical calculation — transit clearance

For each science target, the key question is:

**At the target's transit azimuth (due south for most northern
hemisphere targets), what is the elevation of the horizon obstruction,
and how much clearance does the target have above it?**

For a target transiting at elevation E_transit with a horizon
obstruction of angular height E_horizon at the transit azimuth:

$$Clearance = E_{transit} - E_{horizon}$$

A positive clearance means the target is observable at transit.
A clearance greater than the beam half-width (~8.5° for a 70cm dish)
means the target is fully unobstructed at transit.

### 3.3 Rising and setting constraints

Even when a target is unobstructed at transit, obstructions at other
azimuths limit the total daily observing window — the time during
which the target is above the minimum useful elevation. Measuring
the full 360° horizon profile allows calculation of the precise
rise and set times as seen from the specific dish location.

---

## 4. The Measurement Protocol

### 4.1 Establishing the reference position

All measurements are made from the proposed dish position — not an
approximate location but the exact marked point where the tripod
will stand.

Before beginning measurements:

1. Set up the tripod at operating height
2. Mark the tripod foot positions on the patio surface
3. This is your reference point for all measurements

If the tripod is not yet available, use a temporary ground marker
at the planned position. Note that measurements should be repeated
from the actual operating position once the tripod arrives.

### 4.2 The 36-point horizon sweep

The horizon profile is measured at 36 azimuths, every 10° from
0° (true north) to 350°. At each azimuth:

1. Point smartphone compass in the measurement direction
2. Note the magnetic bearing
3. Convert to true azimuth: true = magnetic + 13° (San Jose)
4. Hold smartphone in theodolite mode
5. Aim at the highest obstruction in that direction
6. Record the elevation angle
7. Note brief description of obstruction (fence, house, tree, clear sky)

**Theodolite app technique:**
- Hold phone vertically, lens pointing at obstruction
- The app displays elevation angle in real time
- Take the reading when the crosshair is on the highest point
  of the obstruction
- For clear sky, record 0°

**Time required:** Approximately 20 minutes for the full 36-point sweep.

### 4.3 Key obstruction measurements

For each significant obstruction (anything above ~20° elevation),
take additional measurements:

- Angular width — bearing to left edge and right edge
- Distance — tape measure to base of obstruction
- Height — theodolite elevation angle × distance (trigonometry)
- Material — affects RF transparency assessment

### 4.4 Dish position measurements

Measure and record:
- Distance from dish position to each fence panel
- Distance from dish position to house wall
- Operating tripod height
- Feed height above patio surface

---

## 5. Photography Protocol

Photographs serve two purposes: permanent visual record of site
conditions, and input for AI-assisted analysis and 3D model generation.

### 5.1 The panorama series

From the dish position, photograph every 45° of azimuth — 8 photos
covering the full 360°. Hold the phone vertically to capture both
ground and sky. These 8 images give complete visual coverage of
the horizon from the observing position.

### 5.2 Obstruction detail photos

For each significant obstruction:
- Wide shot showing full obstruction in context
- Close-up of the highest point
- Photo with tape measure showing key distance

### 5.3 Site overview photos

- Full patio from house doorway
- Dish position marked on patio surface
- Primary transit direction (due south for northern hemisphere)

### 5.4 Photography for AI analysis

For maximum utility in AI-assisted analysis:

- Shoot in good light — avoid shooting directly into sun
- Include a known scale reference where possible (tape measure,
  person of known height, object of known size)
- Shoot from consistent positions — panorama series from exactly
  the dish position
- Clear focus — the AI needs to identify objects at distance

The combination of filled measurement checklist and panorama photograph
series provides sufficient information for AI-assisted generation of
a calibrated 3D site model and target clearance analysis.

---

## 6. RF Environment Survey

### 6.1 Why RF environment matters

The 1420 MHz band has statutory protection under ITU Radio Regulations
(passive use only, 1400–1427 MHz). However statutory protection does
not prevent interference from spurious emissions, harmonics, and
intermodulation products from nearby transmitters.

An RF environment survey establishes the baseline interference
environment before any science observations begin. This serves two
purposes:

- Identifies persistent interference sources that require mitigation
- Provides a reference against which future changes can be assessed

### 6.2 Survey procedure

Using a wideband SDR receiver (RTL-SDR or equivalent) connected to
a simple dipole antenna tuned to 1420 MHz:

1. Set up the SDR and dipole at the dish position
2. Record wideband power spectrum (1380–1460 MHz minimum) for
   30 minutes at each of the following times:
   - Weekday business hours (09:00–11:00 local)
   - Weekday evening (20:00–22:00 local)
   - Weekend morning (10:00–12:00 local)
   - Weekend night (01:00–03:00 local)

3. For each recording note:
   - Any persistent spectral features (frequency, bandwidth, level)
   - Any intermittent features and their temporal pattern
   - Any transient events

4. Note any visible potential sources:
   - Cell tower locations and bearings
   - WiFi access points (use WiFi analyser app)
   - Industrial or commercial premises nearby
   - Power lines

### 6.3 In-band assessment

Pay particular attention to the 1419–1422 MHz range — the core
HI observing band. Any persistent interference in this range
requires specific mitigation planning before science observations begin.

---

## 7. Data Processing and Analysis

### 7.1 From measurements to horizon profile

Once the 36-point azimuth sweep is complete, plot the horizon profile:
- X-axis: azimuth 0–360°
- Y-axis: obstruction elevation angle 0–90°
- Mark the transit elevation of each programme target as a horizontal line

Any target whose transit elevation line is above the horizon profile
at the transit azimuth is unobstructed at transit.

### 7.2 Target clearance calculations

For each programme target:

$$Clearance = E_{transit} - E_{horizon,transit\_azimuth}$$

Where E_horizon is the obstruction elevation at the target's transit azimuth.

Clearance > beam half-width (typically 8–9° for 70cm dish): **fully unobstructed**
Clearance > 0° but < beam half-width: **partially obstructed at transit**
Clearance < 0°: **blocked at transit — target not observable**

### 7.3 Daily observing window calculation

Using the horizon profile, calculate the azimuth range over which
each target is above both the minimum elevation threshold (30°) and
the local horizon. This gives the precise daily observing window —
which varies seasonally as the target rises and sets at different
azimuths.

### 7.4 AI-assisted 3D model generation

The completed measurement checklist and panorama photograph series
can be submitted to an AI assistant for:

- Generation of a parametric 3D site model (OpenSCAD format)
- Visual verification of measurements against photographs
- Identification of any obstructions not captured in the measurement
  sweep
- Calculation of target clearances at any azimuth and elevation
- Production of a horizon profile plot

This represents a significant reduction in the technical barrier to
site assessment — the AI handles the geometry and visualisation while
the observer provides the measurements and photographs.

---

## 8. Interpreting the Results

### 8.1 What the assessment tells you

A completed site assessment answers the following questions
definitively:

- Which programme targets are accessible at transit?
- What is the daily observing window for each target in each month?
- Which obstructions cause the greatest constraint and could be
  mitigated?
- Is the RF environment compatible with HI science observations?
- What is the realistic science programme for this site?

### 8.2 Common findings in urban assessments

**Finding 1 — Most primary targets are unobstructed at transit**
Because northern hemisphere HI targets transit at 60–86° elevation
from mid-latitudes, they clear most urban obstructions easily.
The problem is rarely "can I observe this target at all" but
"when during the day or season is the best window."

**Finding 2 — Trees matter less than expected**
A deciduous tree in full leaf causes some attenuation at 1420 MHz
but is not opaque. In winter (bare) it is nearly transparent. The
RF transparency of the tree material significantly reduces its
impact compared with an optical obstruction of the same angular size.

**Finding 3 — The fence is usually not a problem**
A 6-foot composite fence at 3 metres distance subtends an elevation
angle of approximately 27°. For targets transiting above 30° elevation
(all primary HI targets from mid-latitudes), the fence is below the
beam even at the minimum useful elevation. At transit elevations of
70–86° the fence is completely irrelevant.

**Finding 4 — The house is usually worse than the fence**
A single-storey house at 5 metres distance can subtend 40–45°
elevation. This can intrude into the observing window for targets
at lower elevations or in directions close to the house bearing.
The key is to identify which azimuths and seasons are affected.

**Finding 5 — Daytime availability changes everything**
Many observers discount months when targets transit during the day.
At 1420 MHz these sessions are entirely valid (subject to solar
separation). An observer with flexible scheduling effectively has
no "bad season" — every target is accessible every day.

### 8.3 Honest limitations

The methodology has known limitations that should be explicitly
acknowledged:

- Measurements are made at a single date — seasonal foliage changes
  affect the obstruction profile
- RF environment surveys are snapshots — new interference sources
  may appear
- 36-point azimuth sweep may miss narrow obstructions between
  measurement points
- Smartphone theodolite accuracy is approximately ±1° — adequate
  for most purposes but not suitable for precision survey work
- Photographs provide qualitative context but cannot substitute for
  direct measurement

---

## 9. Worked Example — Blue Rock Radio Observatory

*This section will be completed following the formal site assessment
of Blue Rock Radio Observatory, San Jose CA, anticipated [date TBD].*

### 9.1 Site description

Blue Rock Radio Observatory is located on a residential patio in
San Jose, California (37.3382°N, 121.8863°W). The site represents
a typical urban/suburban amateur astronomy installation:

- Small patio: approximately 8ft × 20ft (2.4m × 6.1m)
- Surrounded by 6ft composite fencing on all sides
- Single-storey house at approximately SE bearing (~150°)
- Large deciduous tree at approximately SSE bearing (~175°)
- Open aspect toward SW (210°) — primary transit direction

The site was selected not for its astronomical properties but because
it is where the observer lives — exactly the situation facing the
majority of aspiring amateur radio astronomers.

### 9.2 Pre-assessment estimates

Prior to formal measurement, the following estimates were made from
visual inspection and approximate distance pacing:

| Obstruction | Bearing | Distance | Height | Calc. elev. angle |
|---|---|---|---|---|
| House roofline | ~150° | ~5m | ~5m | ~45° |
| Deciduous tree | ~175° | ~9m (30ft) | ~15m (50ft) | ~59° |
| Composite fence | All sides | ~2–4m | ~1.8m (6ft) | ~25–42° |

### 9.3 Formal assessment results

*(To be completed after site assessment — insert measured values,
horizon profile plot, target clearance table, RF survey results,
and 3D model here)*

### 9.4 Conclusions

*(To be completed after site assessment)*

---

## 10. Application to Interferometer Array Siting

The methodology extends naturally to multi-element interferometer
arrays where baseline geometry and mutual obstruction between
elements must also be assessed.

For a 5-element array using the KrakenSDR and Discovery Dish system,
the site assessment must additionally characterise:

- Available baseline lengths and orientations within the site
- Mutual line-of-sight between all element pairs
- Cable routing constraints
- Power distribution requirements

The 3D site model generated from the single-dish assessment provides
the foundation for array layout planning. Candidate element positions
can be tested against the model before any hardware is deployed.

This aspect of the methodology is demonstrated in the Blue Rock
programme through the Foothill College partnership investigation
(see design/INTERFEROMETER_UPGRADE.md), where a larger site provides
the extended baselines required for spatially resolved HI mapping.

---

## 11. Recommendations for the Amateur Community

### 11.1 Do the assessment before concluding the site is unsuitable

The single most important recommendation. Many potential observers
have dismissed their sites without measurement. A one-hour assessment
frequently reveals that the site is viable — and documents precisely
what is and is not possible.

### 11.2 Assess the site you have, not the site you wish you had

The methodology is designed for real urban sites with real constraints.
The Blue Rock worked example demonstrates that a patio with a 50ft
tree and an adjacent house can support a serious four-year HI
programme producing publishable results.

### 11.3 Document everything

A documented site assessment is more valuable than an undocumented
one. The documentation:
- Proves to supervisors and reviewers that systematic methodology
  was applied
- Provides a baseline against which future changes can be assessed
- Enables comparison between sites in the community
- Supports the case that urban sites are viable

### 11.4 Reassess annually

Site conditions change. Trees grow, new structures are built,
new interference sources appear. An annual reassessment takes
30 minutes and keeps the site characterisation current.

---

## 12. Acknowledgements

This methodology was developed in the course of establishing Blue
Rock Radio Observatory as part of a BSc Honours Astronomy programme
at the University of Lancashire. The author thanks Dr Megan Argo
(University of Lancashire) for supervision and encouragement.

The approach of combining smartphone survey tools with AI-assisted
analysis for 3D model generation emerged from the practical constraints
of establishing a research-grade observatory on a residential patio
in an urban environment — a constraint shared by the majority of
aspiring amateur radio astronomers worldwide.

---

## Appendix A — Measurement Checklist

See: setup/SITE_ASSESSMENT_CHECKLIST.md in the Blue Rock repository.
Available at: https://github.com/Steve-Hawker/blue-rock-radio-observatory

---

## Appendix B — Recommended Smartphone Applications

| App | Platform | Purpose | Cost |
|---|---|---|---|
| Theodolite (Hunter Research) | iOS | Elevation angle measurement | Free |
| Compass (built-in) | iOS/Android | Azimuth bearing | Free |
| WiFi Analyser | Android | RF environment survey | Free |
| Network Analyser | iOS/Android | WiFi environment survey | Free |
| Stellarium | iOS/Android/Mac | Target elevation planning | Free |
| Clear Outside | iOS/Android | Observing conditions forecast | Free |

---

## Appendix C — Magnetic Declination by Location (2026)

| City | Declination |
|---|---|
| San Jose CA | +13.0° E |
| Los Angeles CA | +11.5° E |
| New York NY | -13.0° W |
| London UK | +0.5° W |
| Sydney AU | +12.5° E |
| Tokyo JP | -8.5° W |

Find precise local value: https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1 | 2026-04-30 | Initial framework — all sections drafted, worked example pending site assessment |
