# Dipole Antenna Design — Chain A RFI Monitoring

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-04-30  
**Version:** 1.0  

---

## Purpose

This document records the engineering rationale for the dipole antenna
configuration used in Chain A (RTL-SDR V4 RFI monitoring). The RTL-SDR
Blog dipole kit includes two pairs of telescopic arms of different maximum
lengths. This document explains why the short arms at a specific length
are used rather than longer configurations.

---

## The RTL-SDR Blog Dipole Kit

| Parameter | Short Arms | Long Arms |
|---|---|---|
| Maximum length per arm | 13 cm | 100 cm |
| Best frequency range | ~575 MHz and above | ~75 MHz and above |
| Role at Blue Rock | HI monitoring (1420 MHz) | Not used — VHF/UHF work only |

---

## Target Frequency

**1420.405 MHz** — the hydrogen line rest frequency.

At 1420 MHz:
- Wavelength λ = c/f = 299,792,458 / 1,420,405,752 = **21.106 cm**
- Quarter wavelength (λ/4) = **5.265 cm per arm**
- Half wavelength total dipole = **10.53 cm**

**Setting: 5.25 cm per arm** (rounded to nearest mm — adequate precision
given mechanical tolerance of telescopic arms)

---

## Why λ/4 Per Arm — Not Longer

This question deserves careful engineering analysis because the intuition
that "longer antenna = more signal collected" is wrong for dipoles.

### Resonance and impedance

A dipole antenna has specific resonant lengths where its impedance is
well-defined and suitable for connection to 50Ω coaxial cable and the
SDR input. Away from resonance the impedance becomes complex (resistive
and reactive) and causes significant mismatch loss.

**At λ/2 total (λ/4 per arm) — first resonance:**
- Impedance: ~73Ω — close to 50Ω coax
- Reflection coefficient Γ = (73-50)/(73+50) = 0.187
- Mismatch loss = -10log₁₀(1 - 0.187²) = **0.15 dB** — negligible
- Pattern: clean figure-of-eight, broad coverage
- This is the correct operating point

**At λ total (λ/2 per arm) — first anti-resonance:**
- Impedance rises to several thousand ohms
- At 2000Ω into 50Ω: Γ = (2000-50)/(2000+50) = 0.951
- Mismatch loss = -10log₁₀(1 - 0.951²) = **13 dB lost**
- The antenna is physically twice as large but receives far less signal
- The 13cm arms at 1420 MHz give 0.617λ per arm — approaching this
  anti-resonance region

**At 3λ/2 total (3λ/4 per arm) — second resonance:**
- Impedance returns to ~100Ω — acceptable but not ideal
- However the radiation pattern now has multiple lobes with nulls
- Blind spots appear — unsuitable for omnidirectional RFI monitoring

**At 4λ per arm (100cm arms at 1420 MHz = 4.74λ per arm):**
- Severe impedance mismatch — multiple anti-resonances
- Highly complex multi-lobe radiation pattern
- Deep nulls in multiple directions
- Receives less signal than a properly matched λ/2 dipole
- Completely unsuitable for this application

### Mismatch loss at each arm length setting

| Arm length | λ per arm | Regime | Est. impedance | Mismatch loss |
|---|---|---|---|---|
| 5.25 cm | 0.249λ | Resonant | ~73Ω | ~0.15 dB |
| 13 cm | 0.617λ | Off-resonance | ~300Ω+ | ~4–6 dB |
| 100 cm | 4.74λ | Far off-resonance | Complex | >10 dB |

The 13cm arms at 1420 MHz would lose 4–6 dB compared with the 5.25cm
setting. That is a factor of 2.5–4× less effective — a significant
degradation for no benefit.

### Gain — does a longer dipole collect more energy?

A longer dipole does have marginally higher gain in its main lobe:

| Dipole length | Gain |
|---|---|
| λ/2 (half-wave) | 2.15 dBi |
| λ (full-wave) | ~2.4 dBi |
| 3λ/2 | ~3.5 dBi (but narrow lobes) |

The gain increase from λ/2 to λ is only **0.25 dB** — entirely negligible,
and cancelled many times over by the mismatch loss at off-resonant lengths.
Furthermore any gain increase in a longer dipole comes at the cost of a
narrowing radiation pattern with nulls between lobes.

For an RFI monitoring antenna — which must detect interference coming from
any direction — a multi-lobe pattern with nulls is actively harmful. A
clean broad figure-of-eight pattern from a resonant λ/2 dipole is the
correct choice.

---

## Radiation Pattern Comparison

**λ/2 dipole (correct — 5.25cm arms):**
- Clean figure-of-eight in the plane of the arms
- Broad coverage in the perpendicular plane
- No nulls except along the axis of the arms
- Omnidirectional in the horizontal plane when arms are vertical

**4λ per arm (100cm at 1420 MHz — incorrect):**
- Multiple narrow lobes
- Deep nulls between lobes
- RFI sources in null directions would be invisible
- Completely unsuitable for monitoring role

---

## Physical Configuration

**Arms:** Short telescopic arms, extended to exactly 5.25 cm each  
**Orientation:** Vertical — arms pointing up and down  
**Mounting:** On Amazon Basics tripod at ~52" height  
**Connection:** SMA to RTL-SDR V4 input, bias tee OFF (passive antenna)  
**Polarisation:** Vertical linear  

**Note on polarisation:** Most man-made RFI sources (cellular, WiFi,
broadcast) use vertical polarisation. A vertically oriented dipole
is therefore well matched to the dominant polarisation of urban RFI
at 1420 MHz. This is an advantage for RFI monitoring — the antenna
preferentially picks up the interference we want to characterise.

HI emission from astronomical sources is unpolarised — both polarisations
equally. The dipole captures one polarisation component (3 dB sensitivity
reduction vs a dual-polarisation system) but this is acceptable for RFI
monitoring where signal strength is not the limiting factor.

---

## Setting the Arm Length

The telescopic arms have no calibration markings. Measure to 5.25 cm
from the base of each arm using a ruler. A small piece of tape at the
correct extension position provides a repeatable reference mark for
future setup.

Verify the setting is consistent each session — note any mechanical
drift in the session log.

---

## Frequency Agility

If future RFI investigations require monitoring at other frequencies,
the arm length should be recalculated:

$$L_{arm} = \frac{c}{4f} = \frac{7500}{f_{MHz}} \text{ cm}$$

| Frequency | Arm length |
|---|---|
| 1420 MHz (HI line) | 5.25 cm |
| 1575 MHz (GPS L1) | 4.76 cm |
| 1090 MHz (ADS-B aircraft) | 6.88 cm |
| 433 MHz (ISM band) | 17.3 cm |
| 137 MHz (weather satellites) | 54.7 cm — use long arms |
| 88–108 MHz (FM radio) | 69–85 cm — use long arms |

For all HI programme work: **5.25 cm per arm, short telescopic arms.**

---

## Connection to INV002 and INV003

The dipole antenna design directly affects the quality of RFI data
feeding into the flagging algorithm (INV003). A properly matched
resonant dipole provides:

- Consistent, well-characterised sensitivity across the band
- Predictable radiation pattern for spatial RFI analysis
- No impedance mismatch artefacts in the baseband spectrum

An off-resonance dipole would introduce frequency-dependent sensitivity
variations across the passband, complicating the interpretation of
RFI survey data and potentially masking or mimicking spectral features.

---

## References

- Balanis, C.A. — *Antenna Theory: Analysis and Design* — dipole impedance
  and radiation patterns (standard reference)
- RTL-SDR Blog dipole kit documentation
- DUAL_SDR_ARCHITECTURE.md — Chain A system context (this repository)
- SDR_SELECTION.md — V4 selection rationale (this repository)
- INV003_rfi_flagging — RFI flagging algorithm (this repository)

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-30 | Initial document — λ/4 rationale, mismatch loss analysis, configuration |
