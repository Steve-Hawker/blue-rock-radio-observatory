# Interferometer Upgrade — Design Study

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-04-30  
**Version:** 0.1 — conceptual design, Phase 4 programme item  

---

## Overview

This document analyses the upgrade path from a single Discovery Dish
to a 5-element interferometric array using the KrakenSDR 5-channel
phase-coherent receiver. This upgrade is a Phase 4 programme item —
planned for after the single-dish programme is well established —
but documented now to inform long-term planning.

The KrakenSDR was designed by Carl Laufer (KrakenRF) with exactly
this use case in mind. The Discovery Dish, Feed, Drive, and KrakenSDR
form a coherent product ecosystem specifically targeting amateur
interferometry.

---

## Background — Why Interferometry

A single 70cm dish provides:
- Beamwidth: ~17° — M31 (3° × 1°) completely unresolved
- SEFD: ~138,000 Jy
- Science: integrated flux and spectral profiles only

An interferometric array provides:
- Resolution proportional to maximum baseline — not dish size
- Sensitivity proportional to total collecting area
- Spatial mapping capability — imaging, not just flux integration

The transition from single-dish to interferometer is the transition
from measuring *what* is there to understanding *where* it is and
*how* it is structured. For M31 this is the difference between
detecting the galaxy and mapping its rotation.

---

## The KrakenSDR

| Parameter | Value |
|---|---|
| Channels | 5 phase-coherent receivers |
| Frequency range | 24 MHz — 1766 MHz |
| Clock sharing | Single shared reference clock — all channels coherent |
| Sample rate | Up to 2.56 Msps per channel |
| ADC bits | 8 (RTL2832U based) |
| Interface | USB |
| Price | ~$400 |
| Software | KrakenSDR open source software |
| Designed for | Direction finding, passive radar, interferometry |

**Critical property:** All five channels share a single clock. The
phase relationship between channels is precisely known and stable.
This is the fundamental requirement for interferometry — independent
SDRs cannot do this as their clocks drift independently.

**Note on ADC:** The KrakenSDR uses 8-bit ADCs (RTL2832U). For
interferometry the phase coherence matters more than dynamic range —
the coherent combination of signals from multiple baselines provides
the imaging capability. ADC resolution is a secondary concern compared
with clock coherence.

---

## Array Configuration

### Number of elements and baselines

For N antenna elements, the number of unique baselines is:

$$N_{baselines} = \frac{N(N-1)}{2}$$

| Elements | Unique baselines |
|---|---|
| 2 | 1 |
| 3 | 3 |
| 4 | 6 |
| 5 | 10 |

A 5-element array provides 10 independent baseline measurements —
10 independent samples of the visibility function of the source.
This is modest by professional standards but sufficient for basic
spatial structure measurement of extended sources like M31.

### Resolution vs baseline length

At 1420 MHz (λ = 21.106 cm):

$$\theta_{resolution} \approx \frac{\lambda}{B_{max}} \text{ radians} = \frac{12.2°}{B_{max}[\text{m}]}$$

| Maximum baseline | Resolution | M31 resolution |
|---|---|---|
| 1 m | ~12° | Unresolved |
| 5 m | ~2.4° | Marginally resolved |
| 10 m | ~1.2° | Starting to resolve M31 major axis |
| 20 m | ~0.6° | Resolving M31 disk |
| 50 m | ~0.24° | Good M31 spatial resolution |
| 100 m | ~0.12° | Excellent M31 resolution |
| 1 km | ~0.012° | Professional quality |

**Science threshold for M31:** ~10m baseline begins resolving the
3° × 1° HI extent. 50m gives genuinely interesting spatial resolution.

---

## Topology Options

### Option A — Linear east-west array (simplest)

All 5 dishes in a line running east-west. Maximum resolution in
right ascension (east-west on sky) but no resolution in declination
(north-south). For M31 whose major axis runs NE-SW at position
angle ~37°, a pure E-W baseline gives only partial resolution
along the major axis.

```
D1 ——— D2 ——— D3 ——— D4 ——— D5
        East-West baseline
```

**Advantage:** Simple cable routing, uniform baseline coverage in RA.  
**Disadvantage:** No N-S resolution — cannot fully map M31 disk.

### Option B — L-shaped array (recommended for small site)

Three dishes along one baseline, two along a perpendicular arm.
Provides 2D resolution with modest footprint. Suited to the
Blue Rock patio and immediate surroundings.

```
D1 — D2 — D3
           |
           D4
           |
           D5
```

Example spacings within ~6m patio + garden:

| Pair | Baseline (m) | Direction |
|---|---|---|
| D1-D2 | 1.5 | E-W |
| D1-D3 | 4.0 | E-W |
| D3-D4 | 2.0 | N-S |
| D3-D5 | 4.0 | N-S |
| D1-D5 | ~5.7 | diagonal |
| ... | ... | ... |

10 unique baselines ranging from 1.5m to ~6m in multiple orientations.

**Advantage:** 2D resolution, fits small site, cable runs manageable.  
**Disadvantage:** Modest maximum baseline limits resolution.

### Option C — Distributed array (maximum baseline)

Dishes distributed across a larger area — neighbouring properties,
street, park — with longer cable or fibre runs between elements.
Maximum baselines of 50–100m become achievable.

This requires:
- Permission from neighbours / authorities
- Longer cable runs with associated phase calibration challenges
- More complex installation

**Advantage:** Substantially better resolution — M31 properly resolved.  
**Disadvantage:** Significant logistical and engineering complexity.

### Option D — Y-configuration (professional analogy)

Three arms at 120° separation, inspired by the VLA configuration.
Provides good 2D coverage of the UV plane. Requires more space than
Option B but less than Option C.

---

## Effect on Sensitivity

### Collecting area

Total physical aperture scales linearly with number of dishes:

$$A_{total} = N \times A_{single} = 5 \times 0.29 \approx 1.44 \text{ m}^2$$

Single dish to 5-dish array: **5× increase in collecting area.**

### SEFD improvement

For a connected-element interferometer, the effective SEFD for
imaging improves as:

$$SEFD_{array} = \frac{SEFD_{single}}{\sqrt{N_{baselines}}} = \frac{138,000}{\sqrt{10}} \approx 43,600 \text{ Jy}$$

**~3× improvement in effective SEFD for imaging.**

However this applies to the *imaging* sensitivity — detecting and
mapping spatial structure. For total flux measurement the single-dish
remains relevant.

### SNR improvement

$$\Delta SNR = \sqrt{N} = \sqrt{5} \approx 2.2 \times \approx +3.5 \text{ dB}$$

A useful but modest sensitivity improvement. The resolution gain
is the transformative benefit, not sensitivity.

### Virgo cluster implications

Current single-dish SEFD: ~138,000 Jy — Virgo galaxies (~1 Jy) impractical.  
5-dish array SEFD: ~43,600 Jy — Virgo galaxies remain very challenging
but not completely out of reach with very long integrations.

---

## Phase Calibration — The Critical Engineering Challenge

An interferometer's resolution is only achievable if the phase
relationship between all antenna pairs is precisely known.

### The cable length problem

At 1420 MHz (λ = 21.106 cm), a cable length difference of:

$$\Delta L = 1 \text{ cm} \rightarrow \Delta\phi = \frac{2\pi \times 0.01}{0.211} = 0.30 \text{ rad} = 17°$$

**A 1cm cable length difference introduces 17° of phase error.**

For coherent combination, phase errors must be <10° — requiring cable
length matching to better than **6mm** between all element pairs.

This is achievable but requires careful measurement and matched cable
cutting. Alternatively, phase offsets can be measured and corrected
in software using a known calibration source.

### Calibration procedure

**Cas A as phase calibrator:**
1. Point all dishes at Cas A
2. Cross-correlate each baseline pair
3. The phase of each baseline cross-correlation gives the phase offset
   between that pair of elements
4. Apply correction to subsequent observations
5. Repeat calibration at start of each session — thermal expansion
   of cables changes phase slightly

This is standard interferometric calibration procedure and directly
analogous to what professional arrays do — they also use bright point
sources as phase calibrators before every observation.

### Cable velocity factor

The electrical length of a cable depends on its velocity factor (VF).
For LMR200-equivalent coax, VF ≈ 0.83. Physical length must be
adjusted for VF when matching electrical lengths:

$$L_{physical} = L_{electrical} \times VF$$

All array cables must be the same electrical length, not necessarily
the same physical length. Cut and measure carefully.

---

## Correlator Software

Processing interferometer data requires a correlator — software that
cross-multiplies the signals from each baseline pair and accumulates
the visibility function.

### Options

**KrakenSDR software** — KrakenRF provide open source software for
direction finding using the KrakenSDR. Some of this infrastructure
is applicable to interferometry. Check current KrakenRF GitHub for
interferometry-specific tools.

**CASA (Common Astronomy Software Applications)** — the professional
standard for radio interferometry data reduction. Steep learning curve
but comprehensive. Available free from NRAO. Running CASA on a dataset
from 5 × 70cm dishes would be a remarkable amateur achievement.

**Custom GNU Radio pipeline** — extending the Phase 2 custom pipeline
(INV002) to handle multi-baseline correlation. A significant but
tractable software development project. Would constitute original
methodology contribution at MRes level.

**OpenVINO / KFR** — open source signal processing libraries with
FFT correlation capability. Lower-level than CASA but more flexible.

---

## Hardware Requirements

| Item | Quantity | Unit cost | Total |
|---|---|---|---|
| KrakenSDR | 1 | ~$400 | $400 |
| Discovery Dish (additional) | 4 | ~$137 | $548 |
| HI Feed (additional) | 4 | ~$117 | $468 |
| Discovery Drive (additional) | 4 | ~$700 | $2,800 |
| Matched LMR200 cable sets | 5 | ~$30 | $150 |
| Mounts / poles | 4 | ~$50 | $200 |
| **Total additional** | | | **~$4,566** |
| **Total programme** | | | **~$5,750** |

**Note:** The Discovery Drive cost dominates. A simpler fixed-mount
or manual pointing solution for secondary dishes would reduce cost
significantly — tracking is less critical for short integrations
if phase calibration is done frequently.

**Reduced cost option — fixed mounts for secondary dishes:**

| Item | Quantity | Unit cost | Total |
|---|---|---|---|
| KrakenSDR | 1 | ~$400 | $400 |
| Discovery Dish (additional) | 4 | ~$137 | $548 |
| HI Feed (additional) | 4 | ~$117 | $468 |
| Fixed AZ/EL mount (simple) | 4 | ~$100 | $400 |
| Matched LMR200 cable sets | 5 | ~$30 | $150 |
| **Total additional (reduced)** | | | **~$1,966** |

---

## Phased Implementation

### Phase 4a — Two-element prototype (recommended first step)

Add a single second dish — one additional baseline. This:
- Tests the KrakenSDR phase coherence in practice
- Develops the calibration procedure on a manageable system
- Produces first interferometric fringes — a milestone in its own right
- Validates the cable matching methodology
- Costs ~$700 additional (dish + feed + simple mount + KrakenSDR)

A two-element interferometer detecting fringes on Cas A is a
publishable result in SARA proceedings.

### Phase 4b — Five-element array

Add three more dishes to complete the array. Implement chosen topology.
Develop correlator pipeline. Begin M31 spatial mapping programme.

---

## Science Programme — Interferometer Phase

### Primary goal — M31 HI velocity mapping

With 50m baseline array, resolve M31's disk into multiple spatial
elements. Build a crude velocity map — the HI equivalent of an optical
velocity field map. Compare with professional data from WSRT and VLA.

This would be a genuinely unprecedented amateur result — spatially
resolved HI kinematics of M31 from a sub-$6,000 backyard array.

### Secondary goals

- Complex C spatial structure — map the density and velocity
  field across the HVC
- Cas A morphology — resolve the 5 arcmin SNR shell at sufficient
  baseline
- M81/M82 spatial separation — distinguish the two galaxies in
  the same beam

---

## Relationship to Thesis and MRes

A two-element interferometer achieving first fringes on Cas A during
the BSc programme would be a strong thesis result. The full 5-element
array with M31 velocity mapping would be MRes-level science by any
reasonable assessment.

The progression is natural:
- BSc: single-dish integrated flux and spectral profiles
- MRes: interferometric spatial mapping

The single-dish programme described in this repository is not just
science in its own right — it is the commissioning and characterisation
phase for the eventual interferometer.

---

## Open Questions

- What is the maximum practical baseline achievable at the Blue Rock
  site or nearby accessible locations?
- Does KrakenRF provide interferometry-specific software beyond
  direction finding?
- What is the minimum baseline for which fringes are detectable
  on Cas A with 70cm dishes?
- Can CASA process KrakenSDR output directly or is a conversion
  step required?
- What phase stability does the KrakenSDR clock achieve in practice
  over a typical 4-hour integration?

---

## Action Items

- [ ] Watch Carl Laufer's KrakenSDR interferometry demonstrations
- [ ] Check KrakenRF GitHub for interferometry software tools
- [ ] Determine maximum practical baseline at Blue Rock site
- [ ] Research CASA compatibility with KrakenSDR data format
- [ ] Add INV004_interferometer_calibration to investigations plan
- [ ] Plan Phase 4a two-element prototype when single-dish programme
      is established (estimated Year 3–4)

---

## References

- Thompson, Moran & Swenson — *Interferometry and Synthesis in Radio
  Astronomy* (3rd ed.) — the standard reference
- KrakenRF GitHub — KrakenSDR software and documentation
- NRAO Essential Radio Astronomy — interferometry chapters
- Taylor, Carilli & Perley (eds.) — *Synthesis Imaging in Radio
  Astronomy II* — NRAO summer school lectures, freely available
- WSRT M31 HI data — professional comparison for eventual results

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1 | 2026-04-30 | Initial conceptual design — KrakenSDR, topology options, calibration framework, phased implementation |
