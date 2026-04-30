# M1 Crab Nebula — Expansion Vector Analysis

**Author:** Steve Hawker BEng MBA FRAS  
**Date:** 2026-04-30  
**Context:** Alston Observatory weekend session, University of Lancashire  
**Participants:** Mark Norris, Jason Kirk, Derek Ward-Thompson, Steve Hawker  
**Version:** 0.1 — initial write-up  

---

## 1. Background

The Crab Nebula (M1, NGC 1952) is the remnant of a supernova explosion
recorded by Chinese astronomers in 1054 AD. At its heart lies the Crab
Pulsar (PSR B0531+21), a neutron star rotating at ~30 Hz, continuously
injecting energy into the surrounding nebula via a pulsar wind.

The primary exercise set during the Alston Observatory weekend session was
to calculate the age of M1 from proper motion data of expansion nodes —
essentially working backwards from the current expansion rate to derive
the explosion date.

The author completed the set exercise using 10 nodes, deriving an explosion
date of **1093 AD** — 39 years from the accepted 1054 AD date. Dr Mark Norris
noted that a more rigorous methodology would approach **1300 AD**, suggesting
a systematic component to the error (see Section 4).

In addition to the set exercise, the author independently plotted the velocity
vectors of each measured node and extended them across the nebula. This
unsolicited analysis produced two findings of independent scientific interest,
documented in Sections 5 and 6.

---

## 2. Data and Methodology

### 2.1 Data source

*(Document the data source used — proper motion measurements, epoch,
instrument, catalogue reference)*

| Parameter | Value |
|---|---|
| Data source | |
| Epochs used | |
| Number of nodes measured | 10 |
| Node selection method | |
| Software / tools used | |

### 2.2 Age calculation methodology

The age of the remnant was derived by:

1. Measuring the current angular position of each expansion node
2. Measuring the proper motion (angular velocity) of each node
3. Assuming an expansion model (specify: free expansion / deceleration corrected)
4. Extrapolating each node backward to zero displacement — the derived explosion date
5. Taking the mean of node-derived dates as the age estimate

**Derived explosion date:** 1093 AD  
**Accepted explosion date:** 1054 AD (SN recorded July 4, 1054 by Chinese astronomers)  
**Residual:** +39 years  
**Number of nodes used:** 10  

### 2.3 Node table

| Node | RA (J2000) | Dec (J2000) | Proper motion (arcsec/yr) | Direction (°) | Derived date (AD) | Notes |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| **Mean** | | | | | | |
| **Std dev** | | | | | | |

---

## 3. Age Calculation Results

**Derived age:** 1093 AD  
**Uncertainty (1σ from node scatter):** ± (TBD) years  
**Accepted value:** 1054 AD  
**Residual:** +39 years (+3.7%)  

### 3.1 Discussion of residual

The 39-year overestimate (younger than true age) is consistent with the
node sample having preferentially sampled faster-expanding filaments —
regions moving more rapidly than the mean expansion velocity. Faster
nodes project back to a more recent origin.

Possible contributing factors:
- Node selection bias toward prominent, fast-moving filaments
- Projection effects — nodes moving partly toward/away from observer
  show reduced apparent proper motion
- Deceleration model — free expansion assumption underestimates true age
- Distance uncertainty — adopted distance ± uncertainty propagates into
  physical expansion rate

Dr Norris's suggestion that rigorous methodology would give ~1300 AD
implies a systematic correction (likely deceleration model) dominates
over the statistical scatter. This is discussed in Section 4.

---

## 4. Systematic Error Analysis — Why 1300 AD?

*(To be developed in discussion with Dr Norris)*

Dr Norris suggested that correct methodology would yield ~1300 AD —
older than both the derived 1093 AD and the true 1054 AD. This is
counterintuitive at first: if the true date is 1054 AD, why would
a more rigorous method give a *worse* answer of 1300 AD?

The resolution likely lies in the **deceleration correction**:

**Free expansion assumption** (used in this analysis):
The shell is assumed to have been expanding at its current velocity
since the explosion. This gives the youngest age estimate — if the
shell is moving at V km/s now, it took D/V years to reach size D.

**Deceleration corrected** (more physically realistic):
The shell was moving faster in the past and has been decelerating as
it sweeps up interstellar medium. If the shell was faster early on,
it reached its current size in *less* time than the free expansion
calculation suggests — giving an *older* derived age.

This is the Sedov-Taylor blast wave solution:
- Early phase: free expansion at initial velocity
- Later phase: Sedov-Taylor — R ∝ t^(2/5) — decelerating expansion

Applying the deceleration correction moves the derived age older —
potentially to ~1300 AD depending on the assumed ISM density and
explosion energy. The fact that this overcorrects past the true date
of 1054 AD suggests the deceleration model parameters need careful
calibration.

**The implication:** the true age sits between the free expansion
estimate (1093 AD, too young) and the deceleration-corrected estimate
(~1300 AD, too old). A correctly parameterised intermediate model
would approach 1054 AD.

*(Add quantitative analysis here when deceleration model is implemented)*

---

## 5. Finding A — No Common Vector Intersection

### 5.1 Method

In addition to the age calculation, the velocity vectors of all 10 nodes
were plotted as directed lines on the plane of the sky, extended both
forward (future position) and backward (historical origin). If M1 were
expanding perfectly symmetrically from a point source, all vectors
extended backward would intersect at a single point — the explosion origin.

### 5.2 Result

**The vectors do not converge on a common intersection point.**

The backward-extended vectors show a scattered distribution of apparent
origins, with no single convergence point within the nebula or nearby.

### 5.3 Interpretation

This non-convergence directly reflects the physical nature of the
Crab Nebula's expansion:

**Asymmetric explosion** — the progenitor star did not explode
symmetrically. The explosion energy was not distributed uniformly,
producing an asymmetric initial velocity field that persists in the
current expansion pattern.

**Pulsar wind distortion** — the Crab Pulsar has been injecting
directed energy into the nebula for ~970 years, distorting the
expansion from simple radial symmetry. The pulsar wind nebula
component (inner torus and jets visible in X-ray) drives non-radial
motions in the outer filaments.

**ISM inhomogeneity** — the expanding shell encounters non-uniform
interstellar medium, producing different deceleration in different
directions.

**Turbulence and instabilities** — Rayleigh-Taylor instabilities at
the shell boundary produce the characteristic filamentary structure
and introduce non-radial velocity components.

The vector plot visualises this complexity directly — it shows not
just the age but the *nature* of the expansion. This is more
information than the age calculation alone provides.

*(Insert vector plot here when available)*

---

## 6. Finding B — The Crab Pulsar is Not Central

### 6.1 Observation

When the pulsar position (PSR B0531+21, RA 05h 34m 31.97s,
Dec +22° 00' 52.1") is overlaid on the vector plot and the geometric
centre of the optical nebula is identified, the pulsar is **offset
from the geometric centre** of the gas cloud.

### 6.2 Measurement

*(Add measured offset here)*

| Parameter | Value |
|---|---|
| Pulsar position | RA 05h 34m 31.97s, Dec +22° 00' 52.1" |
| Geometric centre of nebula | (measure from data) |
| Offset (arcsec) | (to be measured) |
| Offset direction | (to be measured) |
| Offset (physical, at 2.0 kpc) | (to be calculated) |

### 6.3 Interpretation — Pulsar Natal Kick

The offset of the pulsar from the geometric centre of the remnant
is a direct observational consequence of the **pulsar natal kick** —
the velocity imparted to the neutron star at birth by an asymmetric
supernova explosion.

When a massive star explodes asymmetrically, conservation of momentum
means the compact remnant (neutron star) recoils in the opposite
direction to the asymmetric ejecta. The neutron star is born with
a significant space velocity — the natal kick velocity.

For the Crab Pulsar:
- The pulsar has been moving away from the explosion centre for ~970 years
- The offset represents ~970 years of travel at the kick velocity
- From the measured offset and the age, the transverse kick velocity
  can be estimated

**Natal kick velocity estimate:**
*(Calculate from measured offset and age)*

V_kick = (offset in parsecs) / (age in years) km/s

Pulsar natal kicks are a significant area of current research. Observed
kick velocities range from tens to over 1000 km/s, with a distribution
peaking around 200-500 km/s. The mechanism is not fully understood —
proposed explanations include asymmetric neutrino emission during the
core collapse, asymmetric mass ejection, and electromagnetic rocket
effects from an off-centre magnetic dipole.

### 6.4 Significance

This finding — derived independently from the vector plot without being
set as an exercise — demonstrates:

1. The asymmetric nature of the Crab supernova explosion
2. Direct observational evidence for pulsar natal kicks
3. That the pulsar wind nebula structure is centred on the pulsar's
   *current* position, not the explosion origin

The offset between the pulsar (centre of the wind nebula) and the
geometric centre of the outer filamentary shell is a visible record
of the neutron star's journey since birth.

*(Insert annotated image showing pulsar position, nebula centre,
and offset vector here)*

---

## 7. Connections to Blue Rock Programme

This analysis connects to the Blue Rock observing programme in
several ways:

**M1 as a radio target** — the Crab Nebula is a planned secondary
calibration target at Blue Rock (see targets/M1_CrabNebula.md).
Radio flux measurements will complement the optical/proper motion
analysis done here.

**Methodology parallels** — the systematic error analysis in Section 4
directly mirrors the methodology challenges in the M31 HI rotation
curve analysis. Both involve:
- Deriving physical quantities from measured velocities
- Model assumptions affecting the derived result
- Systematic vs statistical error distinction
- The importance of understanding *why* the answer differs from truth

**Sparse data robustness** — getting a defensible result (1093 AD,
3.7% error) from 10 nodes demonstrates that well-chosen sparse data
can give meaningful answers. This principle applies directly to
Blue Rock's long-baseline approach — fewer but better-calibrated
sessions outperform many poorly-calibrated ones.

**Pulsar natal kicks and radio astronomy** — pulsar timing and
proper motion are active areas of radio astronomy. The Crab Pulsar
itself is a strong radio source and has been extensively studied
with radio telescopes. This analysis provides physical context for
future reading in this area.

---

## 8. Further Work

- [ ] Obtain and document the data source properly
- [ ] Complete the node table with measured values
- [ ] Measure pulsar offset from geometric centre quantitatively
- [ ] Calculate natal kick velocity estimate
- [ ] Implement deceleration model and compare with free expansion result
- [ ] Discuss systematic error analysis with Dr Norris
- [ ] Add vector plot as figure
- [ ] Add annotated nebula image showing pulsar offset
- [ ] Add to Zotero — key references on pulsar natal kicks
- [ ] Consider whether this warrants a SARA note

---

## 9. References

- Hester 2008 — *ARA&A* 46, 127 "The Crab Nebula: An Astrophysical Chimera"
- Kaplan et al. 2008 — Crab Pulsar proper motion
- Hobbs et al. 2005 — *MNRAS* 360, 974 "A statistical study of 233 pulsar proper motions" — natal kick velocity distribution
- Sedov 1959 — blast wave solution (deceleration model)
- All available via NASA ADS: `ui.adsabs.harvard.edu`

---

## 10. Acknowledgements

Analysis conducted during Alston Observatory weekend session,
University of Lancashire. Thanks to Dr Mark Norris, Dr Jason Kirk,
and Professor Derek Ward-Thompson for the observing session and
discussion. The vector analysis and pulsar offset finding were
conducted independently by the author as an extension of the
set exercise.

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1 | 2026-04-30 | Initial write-up — methodology and findings documented, quantitative measurements pending |
