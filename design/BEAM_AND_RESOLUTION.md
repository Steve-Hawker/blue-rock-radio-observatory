# Beam Width and Spatial Resolution — Design Constraints

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-04-30  
**Version:** 1.1  

---

## Overview

This document records the angular resolution constraints of the Blue Rock
Observatory 70cm dish at 1420 MHz, the implications for each science target,
the practical mitigation strategies available within the current instrument,
and the upgrade path if improved resolution is required.

Understanding beam width is fundamental to interpreting all HI observations
from this instrument. Every result must be understood as the true sky
brightness distribution convolved with the 17° beam.

---

## Beam Width Derivation

The half-power beam width (HPBW) of a circular aperture antenna:

$$\theta_{HPBW} \approx 58 \frac{\lambda}{D} \text{ degrees}$$

At 1420 MHz (λ = 21.106 cm) with a 70cm dish:

$$\theta_{HPBW} \approx 58 \times \frac{21.106}{70} = 58 \times 0.301 = \textbf{17.5°}$$

The first null beamwidth (wider than HPBW):

$$\theta_{null} \approx 70 \frac{\lambda}{D} \approx 21°$$

**Theoretical value: ~17.5° HPBW**

**KrakenRF simulation value: 20–22° HPBW** — from the Discovery Dish
CrowdSupply product page gain/return loss simulation plots at 1.42 GHz:
- Phi=0 plane: angular width (3dB) = 22.6°
- Phi=90 plane: angular width (3dB) = 20.3°
- Main lobe gain: 17.7 dBi
- Sidelobe level: -19.0 dB (Phi=0), -15.1 dB (Phi=90)

The simulation accounts for the actual feed illumination pattern and
aperture efficiency of the Discovery Dish design, which the theoretical
formula does not. The simulation value is therefore more reliable than
the theoretical estimate as a prior for the commissioning measurement.

**Adopted prior: ~21° HPBW** (mean of simulation values) pending
commissioning measurement from Cas A beam scan.

**Note on dish gain:** The simulation gives 17.7 dBi main lobe gain
at 1.42 GHz. This feeds directly into the SEFD calculation in INV001
and improves the sensitivity estimate compared with earlier approximations.

This beamwidth must be measured directly from Cas A observations during
commissioning. The simulation value is a prior, not a measurement.
Measured value supersedes all estimates — see Section 4.

---

## Beam Width in Context

| Object | Angular size | Beam / object ratio | Status |
|---|---|---|---|
| Sun | 0.5° | 34× larger than Sun | Beam >> object |
| Moon | 0.5° | 34× larger than Moon | Beam >> object |
| Cas A | ~5 arcmin (0.08°) | 212× larger than Cas A | Point source |
| M1 | ~7 arcmin (0.12°) | 142× larger than M1 | Point source |
| M31 HI extent | ~3° × 1° | ~6× larger than M31 | Unresolved |
| Complex C | ~30° × 15° | Beam << Complex C | Beam is inside source |
| M33 HI extent | ~1° × 0.7° | ~17× larger than M33 | Unresolved |
| M81 HI extent | ~0.5° × 0.3° | ~34× larger than M81 | Unresolved |

**Key insight:** Every point source target (Cas A, M1) is completely
unresolved — ideal for flux calibration. Every extended target (M31,
Complex C, M33) is also unresolved — integrated flux is measured, not
spatial structure. Complex C is actually *smaller* than the beam —
an advantage for monitoring.

---

## Implications Per Target

### Cas A and M1 — point sources

Unresolved point sources are ideal for beam characterisation and flux
calibration. The measured flux depends on pointing accuracy (keeping
the source within the main beam) and aperture efficiency, not on
angular resolution. Beam width is irrelevant to the science.

### M31 — primary science target

M31's HI emission spans approximately 3° × 1°. The 17° beam captures
the entire galaxy simultaneously in a single pointing. This means:

**Advantages:**
- Complete integrated HI profile in every observation — no mapping required
- Total HI flux measurement is straightforward
- Double-horn spectral profile contains all velocity information

**Limitations:**
- No direct spatial resolution — cannot distinguish emission from
  different parts of the disk in a single pointing
- Spatial information must be extracted indirectly via offset pointing
  and spectral analysis (see Section 5)

### Complex C — HVC monitoring target

Complex C spans ~30° × 15° — much larger than the beam. The 17° beam
samples a specific patch of the cloud at each pointing. This is actually
advantageous:

- No signal dilution — beam is fully filled with HVC emission
- Peak brightness temperature is measured directly, not beam-averaged
  over a small source
- Different pointings sample different parts of the cloud — natural
  mapping capability

### M33 and M81 — secondary extragalactic targets

Both unresolved. Integrated flux profiles only, same situation as M31
but less scientifically interesting given the smaller angular size and
lower flux density. The beam width is not the limiting factor for these
targets — sensitivity is.

---

## Factors Affecting Actual Beam Width

The theoretical 17° assumes perfect conditions. Several factors affect
the real beam:

### Feed positioning

The Discovery Dish has f/D = 0.35, giving a focal length of:

$$f = F/D \times D = 0.35 \times 0.70 = \textbf{24.5 cm from dish vertex}$$

The feed must be positioned accurately at this focal point. Displacement
of the feed from the true focal point reduces effective aperture and
broadens the beam. Even a few mm of axial displacement is significant.

**Action:** Verify feed position carefully during assembly. Measure
the focal length from the dish vertex to the feed phase centre.
Note measured position in E002 equipment log.

### Surface accuracy

Surface errors across the dish scatter radiation away from the focal
point, reducing effective aperture and broadening the beam. The Ruze
formula gives the efficiency loss from surface errors:

$$\eta_{surface} = e^{-(4\pi\sigma/\lambda)^2}$$

Where σ is the RMS surface error. For σ = 1mm at 1420 MHz (λ = 210mm):

$$\eta_{surface} = e^{-(4\pi \times 1/210)^2} = e^{-0.0036} \approx 0.996$$

At 1420 MHz, 1mm surface errors cause only 0.4% efficiency loss —
essentially negligible. Surface accuracy is not a concern at this
frequency for a stamped aluminium dish.

### Aperture blockage

The feed and support arm block part of the aperture. This reduces
effective collecting area (small effect) and introduces diffraction
that slightly raises sidelobe levels (modest effect). Not correctable
without redesigning the feed support. Note in equipment log as a
known systematic.

### Aperture illumination taper

The feed's radiation pattern determines how uniformly the dish is
illuminated. Uniform illumination gives the narrowest beam but highest
sidelobes. Tapered illumination (less intensity at dish edges) gives
slightly broader beam but lower sidelobes. The Discovery Dish feed
illumination pattern is optimised by KrakenRF for this f/D ratio —
accept as designed.

---

## Beam Measurement from Cas A

During commissioning, measure the actual beam width by scanning Cas A
across the beam in both azimuth and elevation:

1. Point dish at Cas A — confirm peak signal
2. Offset pointing in azimuth in steps of 2° from -20° to +20°
3. Record signal strength at each offset
4. Repeat in elevation
5. Fit a Gaussian to the measured profile
6. HPBW = 2√(2ln2) × σ of fitted Gaussian

Record measured HPBW in E002 equipment log. Compare with theoretical
17°. Discrepancy > 2° warrants investigation of feed positioning.

This beam map should be repeated after any mechanical change to the
feed or dish assembly.

---

## Practical Spatial Discrimination Strategies

Despite the 17° beam, useful spatial information can be extracted from
M31 by the following methods:

### 1. Offset pointing programme

M31's major axis runs at position angle ~37° (NE-SW). Systematic
offset pointings along the major axis sample different weighted averages
of the velocity field:

| Pointing | RA offset | Dec offset | Dominant region |
|---|---|---|---|
| Centre | 0° | 0° | Full disk, equal weight |
| NE +1° | +0.75° | +0.66° | Approaching side weighted |
| NE +2° | +1.5° | +1.32° | Approaching arm |
| SW -1° | -0.75° | -0.66° | Receding side weighted |
| SW -2° | -1.5° | -1.32° | Receding arm |

At each pointing the spectral profile changes. The approaching horn
(more negative velocity) strengthens at NE pointings. The receding
horn strengthens at SW pointings. This crude spatial discrimination
is real science — it provides velocity gradient information along
the major axis, which is the foundation of a rotation curve.

**Caution:** This is not conventional mapping. The signal at each
pointing is a 17°-beam-weighted average of the entire disk. The
spatial information is indirect and requires careful modelling to
interpret. Do not overstate the spatial resolution.

### 2. Beam convolution modelling

Mathematically, the measured spectrum at each pointing T_measured is:

$$T_{measured}(\alpha, \delta) = T_{true} \ast B$$

Where B is the beam pattern and ∗ denotes convolution. If B is well
characterised (from Cas A beam mapping) and multiple pointings are
available on a grid, deconvolution in principle recovers T_true.

In practice, deconvolution of a 17° beam on a 3° source with realistic
noise is ill-conditioned. This is an ambitious Phase 3 programme item,
not a Phase 1 or 2 goal. Requires:
- Accurate beam characterisation from Cas A
- High SNR at multiple pointings (years of integration)
- Careful regularisation of the deconvolution

### 3. Velocity field analysis

The double-horn profile encodes spatial information as spectral structure.
The two horns correspond to emission from the approaching and receding
sides of the disk. The separation between horns, the relative horn
heights, and the profile wings all contain information about the
velocity field and disk inclination.

Fitting kinematic models to the integrated profile — even from a
single pointing — extracts velocity dispersion, inclination, and
maximum rotation velocity without requiring spatial resolution.
This is a legitimate and well-established technique for unresolved
galaxies.

---

## Beam Width vs Dish Size

The only fundamental solution to insufficient angular resolution is
a larger dish:

$$\theta_{HPBW} \approx 58 \frac{\lambda}{D}$$

| Dish diameter | HPBW at 1420 MHz | M31 resolution | Practical |
|---|---|---|---|
| 70 cm (current) | ~17° | Fully unresolved | Yes |
| 100 cm | ~12° | Fully unresolved | Yes — modest upgrade |
| 150 cm | ~8° | Marginally resolved | Possible — larger mount needed |
| 200 cm | ~6° | Partly resolved | Significant upgrade |
| 300 cm | ~4° | Resolved major axis | Major installation |
| 600 cm | ~2° | Well resolved | Professional facility |

A 150cm dish would start to resolve M31's major axis (3° extent).
A 300cm dish would give genuinely interesting spatial resolution.
Both require substantially more robust mounts, larger patio footprint,
and significantly higher wind loading.

**Upgrade path:** If spatial resolution of M31 becomes a programme
goal, a 120–150cm dish on the Discovery Drive mount is the practical
next step. The Discovery Drive supports antennas up to 5kg — a 120cm
aluminium dish is feasible within this limit. This would require a
new feed optimised for the different f/D ratio.

This is a post-Phase 2 consideration. Current programme goals are
achievable with the 70cm dish.

---

## Summary — What the 17° Beam Means for Each Programme Goal

| Programme goal | Beam width impact | Mitigation |
|---|---|---|
| M31 integrated HI flux | None — beam captures full source | None needed |
| M31 double-horn profile | None — spectral, not spatial | None needed |
| M31 velocity gradient | Indirect — crude discrimination only | Offset pointing programme |
| M31 rotation curve | Severe — cannot resolve disk directly | Kinematic model fitting |
| Complex C monitoring | Advantageous — beam fills source | None needed |
| Cas A flux calibration | None — point source | None needed |
| M1 flux measurement | None — point source | None needed |
| M33 HI detection | None — unresolved, flux only | None needed |

---

## References

- Kraus — *Radio Astronomy* Ch. 3 (antenna beam patterns)
- Wilson, Rohlfs & Hüttemeister — *Tools of Radio Astronomy* Ch. 7
- Ruze 1966 — surface error efficiency formula
- Chemin, Carignan & Foster 2009 — M31 HI kinematics reference
  (professional comparison — resolved observations)
- E001/E002 equipment log — measured beam width from Cas A scan

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-30 | Initial document — beam derivation, target implications, spatial discrimination strategies, upgrade path |
| 1.1 | 2026-05-04 | Updated beamwidth — KrakenRF simulation gives 20–22° HPBW and 17.7 dBi gain at 1.42 GHz; cable corrected to LMR240-equivalent |
