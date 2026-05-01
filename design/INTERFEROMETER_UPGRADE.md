# Interferometer Upgrade — Design Study

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-04-30  
**Version:** 0.2 — calibration methodology expanded, site strategy added  

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

## Phase Calibration — Methodology

An interferometer's resolution is only achievable if the phase
relationship between all antenna pairs is precisely known and stable.
This section documents the complete calibration strategy for the
Blue Rock array.

### The cable length problem — quantified

At 1420 MHz (λ = 21.106 cm), a cable length difference of:

$$\Delta L = 1 \text{ cm} \rightarrow \Delta\phi = \frac{2\pi \times 0.01}{0.211} = 0.30 \text{ rad} = 17°$$

**A 1cm cable length difference introduces 17° of phase error.**

For coherent combination, phase errors must be kept small — ideally
<10° total across the array. However physical cable matching to 6mm
precision is NOT required if astronomical phase calibration is used
(see below). What matters is that cable phase is **stable** rather
than **identical**.

### Three-stage calibration strategy

#### Stage 1 — Physical cable construction (author's domain)

The author's professional background in cable construction applies
directly. Build all array feed cables to approximately equal physical
length — within a few centimetres is sufficient. Consistent connector
type and termination technique throughout.

**Recommended cable: LMR400** (not LMR200) for array feed cables.

| Property | LMR200 | LMR400 | Reason for upgrade |
|---|---|---|---|
| Loss at 1420 MHz | ~0.7 dB/m | ~0.3 dB/m | Lower insertion loss |
| Temperature coefficient | Higher | Lower | Better phase stability |
| Mechanical stability | Good | Better | Less phase change with flexing |
| Minimum bend radius | 13mm | 25mm | More rigid — less accidental flex |
| Cost | Lower | Higher | Justified for array application |

For array use, phase stability with temperature and mechanical
movement matters more than in the single-dish setup. LMR400's
better temperature coefficient reduces session-to-session phase
drift and simplifies calibration.

**Construction procedure:**
1. Cut all cables to the same physical length (±1cm adequate)
2. Strip and terminate consistently — same connector type throughout,
   same torque on all fittings
3. Label each cable clearly — D1, D2, D3, D4, D5
4. Store coiled with consistent bend radius — do not kink

#### Stage 2 — TDR fault verification

**What TDR can and cannot do at 1420 MHz:**

The time difference corresponding to a 6mm cable length mismatch:

$$\Delta t = \frac{\Delta L}{c \times VF} = \frac{0.006}{3 \times 10^8 \times 0.83} = 24 \text{ picoseconds}$$

A standard 100 MHz oscilloscope has rise time ~3.5 ns — approximately
150× too slow to resolve 24 ps time differences directly. TDR with
a standard oscilloscope **cannot** measure sub-mm cable length
differences at 1420 MHz.

**What TDR is useful for:**

TDR with a 1 GHz bandwidth oscilloscope (~$300 used) resolves
reflections to ~15cm — adequate to locate:
- Physical cable faults (cuts, kinks)
- Bad connector terminations
- Significant impedance discontinuities

**TDR procedure:**
1. Apply a fast rise-time pulse to each cable in turn
2. Observe the reflected waveform
3. A clean cable shows only the far-end reflection
4. Any intermediate reflection indicates a fault
5. Time to reflection gives distance to fault

This validates physical cable integrity before deployment. Do not
rely on TDR for phase matching — use astronomical calibration instead.

#### Stage 3 — Astronomical phase calibration (primary method)

This is the definitive calibration step and the most elegant. No
test equipment is needed beyond the array itself. Cas A provides
a bright, compact, stable calibration source at exactly the
operating frequency, through the complete signal chain including
all connectors, at operating temperature.

**Procedure:**
1. Point all dishes at Cas A simultaneously
2. Record cross-correlations on all 10 baseline pairs via KrakenSDR
3. For each baseline pair (i,j), measure the phase of the
   cross-correlation: φ_ij = arg(V_ij)
4. These phases are the cable + electronics phase offsets for each baseline
5. Store as correction factors: Δφ_ij
6. Apply corrections to all subsequent observations:
   V_ij_corrected = V_ij × exp(-i × Δφ_ij)
7. Verify correction by checking that Cas A appears as a point source
   at the correct position in the reconstructed image

**Why this is superior to physical matching:**
- Measures phase at exactly 1420 MHz — not at some test frequency
- Includes all phase contributions: cable, connectors, LNA, feed
- Self-consistent — the sky provides the truth
- Absorbs all systematic errors automatically
- Standard practice at all professional arrays worldwide

**Cas A phase calibration — expected precision:**
Cas A SNR with 5 × 70cm dishes in ~15 minutes integration is high
(Cas A is ~2567 Jy). Phase measurement uncertainty:

$$\sigma_\phi \approx \frac{1}{SNR} \text{ radians}$$

At SNR = 100 (easily achievable on Cas A): σ_φ ≈ 0.01 rad ≈ 0.6°

Phase calibration accurate to better than 1° — well within the
coherent combination requirement.

### Thermal drift management

Cable phase changes with temperature due to thermal expansion and
changes in dielectric constant. For LMR400 the temperature
coefficient of phase is approximately 0.5°C per 10m per degree C.

For 6m cables over a typical San Jose temperature swing of 10°C
during a session:

$$\Delta\phi_{thermal} \approx 0.5 \times \frac{6}{10} \times 10 = 3°$$

A 3° drift over a session is acceptable. However for long integrations
(4+ hours) spanning larger temperature swings, recalibration on Cas A
mid-session is prudent.

**Recalibration schedule:**
- Start of every session — mandatory
- Every 2 hours during long integrations
- After any significant temperature change (>5°C)
- After any cable disturbance

### Connector discipline

Each SMA or N-type connector introduces a small but reproducible
phase shift. The author's cable construction experience is directly
relevant here. Key requirements:

- **Consistent connector type** throughout — do not mix SMA-male
  from different manufacturers
- **Consistent torque** on all fittings — use a torque wrench
  if available; finger-tight plus 1/4 turn as minimum standard
- **Clean mating surfaces** — contamination causes phase
  irreproducibility
- **Weatherproof** all outdoor connections — moisture ingress
  changes phase and causes slow drift

A systematic connector log noting connector type, batch, and
torque applied for each cable is worth maintaining — exactly
analogous to the equipment log approach already established for
the single-dish system.

### Annual verification

The author proposed annual cable re-verification. Recommended procedure:

1. Repeat TDR fault check — look for any degradation in cable integrity
2. Repeat astronomical phase calibration on Cas A
3. Compare correction factors with previous year
4. Document any systematic drift in the equipment log
5. Replace any cable showing significant change in phase correction factor

Phase correction factors that remain stable year-to-year confirm
the array is mechanically and electrically stable. Significant
changes flag a cable or connector issue requiring investigation.

---

## Site Strategy — Land Constraints and Partnership Options

### Blue Rock patio — immediate capability

Within the 8×20ft patio, maximum baseline ~6m giving ~2° resolution.
An L-shaped 5-element array is feasible within this footprint.
Modest science capability but sufficient to develop calibration
methodology and achieve first fringes.

### Foothill College partnership — recommended long-term strategy

Foothill College (Los Altos Hills, ~8 miles from San Jose) has open
campus land and a Physical Sciences, Mathematics and Engineering
division. A partnership could provide:

- 50–100m baselines — transformative resolution improvement
- Teaching resource value to the college
- Student involvement in a real research programme
- Institutional connection complementing the UCLan affiliation

**Value proposition to Foothill College:**
A working interferometer array on campus producing publishable HI
maps of M31 is a compelling teaching and outreach resource. The
observer brings hardware, expertise, and a University of Lancashire
research affiliation. The college provides land and potentially
student participation.

**Approach strategy:**
- Establish single-dish programme and achieve published results first
- Approach Physical Sciences faculty with documented programme
  (GitHub repository provides immediate credibility)
- FRAS fellowship and UCLan affiliation provide academic standing
- Propose initially as a visiting researcher / community partnership
- Timing: Year 3–4 of current programme

### Other site options

- **SJAA dark site** — San Jose Astronomical Association may have
  land access. Already a member — natural conversation to have.
- **NASA Ames Research Center** (Mountain View, ~10 miles) —
  long shot but worth awareness
- **Local parks / open space** — requires permits but some Santa
  Clara County open space preserves have flat accessible land

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
| 0.2 | 2026-04-30 | Expanded calibration methodology — three-stage strategy, TDR limitations, astronomical calibration, LMR400 recommendation, Foothill College partnership, thermal drift management |
