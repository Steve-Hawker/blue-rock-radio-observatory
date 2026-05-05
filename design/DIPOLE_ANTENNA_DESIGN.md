# Dipole Antenna Design — Chain A RFI Monitoring

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-04-30  
**Version:** 2.0  

---

## Purpose

This document records the engineering rationale for the dipole antenna
configuration used in Chain A (RTL-SDR V4c RFI monitoring). The RTL-SDR
Blog dipole kit includes two pairs of telescopic arms of different maximum
lengths. This document explains why the short arms at a specific length
are used rather than longer configurations, and documents the discovery
that the stock arms cannot reach the correct resonant length for 1420 MHz —
and the solution.

---

## The RTL-SDR Blog Dipole Kit

| Parameter | Short Arms | Long Arms |
|---|---|---|
| Minimum length per arm (collapsed) | 5 cm visible + 2 cm internal = **7 cm total** | ~23 cm |
| Maximum length per arm (extended) | 13 cm visible + 2 cm internal = **15 cm total** | 100 cm + 2 cm |
| Best frequency range | ~575 MHz and above | ~75 MHz and above |
| Role at Blue Rock | HI monitoring (1420 MHz) — see problem below | Not used — VHF/UHF work only |

**Critical note from dipole kit guide:** Each arm has approximately **2 cm of
metal inside the base** that counts toward the electrical length. The visible
extension plus this internal length equals the total arm length for resonance
calculations.

---

## Target Frequency

**1420.405 MHz** — the hydrogen line rest frequency.

At 1420 MHz:
- Wavelength λ = c/f = 299,792,458 / 1,420,405,752 = **21.106 cm**
- Quarter wavelength (λ/4) = **5.265 cm total per arm**
- Required visible extension = 5.265 - 2.0 = **3.265 cm visible per arm**
- Half wavelength total dipole = **10.53 cm**

---

## The Problem — Minimum Arm Length

The short telescopic arms have a **minimum collapsed length of 5 cm visible**
(7 cm total including 2 cm internal). This is already longer than the
5.265 cm total needed for resonance at 1420 MHz.

**The stock short arms cannot reach the correct resonant length for 1420 MHz.**

At minimum extension (7 cm total per arm):

$$f_{resonant} = \frac{c}{4 \times L_{arm}} = \frac{29,979}{4 \times 7} \approx 1071 \text{ MHz}$$

The collapsed arms are resonant at ~1030–1070 MHz — not 1420 MHz.

### Mismatch loss at minimum extension

At minimum extension (7 cm total, resonant ~1070 MHz) used at 1420 MHz:

- Arm length as fraction of λ at 1420 MHz: 7/21.1 = 0.332λ per arm
- Total dipole: 0.664λ — between λ/2 resonance and λ anti-resonance
- Estimated impedance: complex, ~150–250Ω resistive + reactive component
- Estimated mismatch loss: **~2–3 dB**

This is tolerable for RFI monitoring (where absolute sensitivity is not
critical) but is a known systematic that must be documented.

### Mismatch loss comparison

| Configuration | Total arm length | Resonant freq | Mismatch loss | Status |
|---|---|---|---|---|
| Custom brass element (solution) | 5.265 cm | 1420 MHz | ~0.15 dB | ✓ Correct |
| Stock arm minimum collapsed | 7 cm | ~1070 MHz | ~2–3 dB | Interim only |
| Stock arm at 5.25 cm visible (impossible) | — | — | — | Cannot achieve |
| Stock arm maximum extended | 15 cm | ~500 MHz | ~4–6 dB | Incorrect |

---

## Solution — Custom Brass Elements

The correct engineering solution is to fabricate custom replacement elements
cut to the exact resonant length for 1420 MHz.

### Specification

| Parameter | Value |
|---|---|
| Target total arm length | 5.265 cm |
| Less internal base metal | 2.0 cm |
| **Required element length** | **3.265 cm** (cut to 3.3 cm) |
| Thread | M5 — matches dipole base (verify physically on receipt) |
| Material | Brass rod, 5mm diameter |
| Quantity | 2 elements (one per arm) |
| Tip finish | File smooth, no sharp edges |

### Materials required

- 5mm brass rod stock — available at hardware stores, ~$5 for 300mm
- M5 tap and tap wrench
- Junior hacksaw or pipe cutter
- Small file for tip finishing
- Vernier calipers for accurate length measurement

### Fabrication procedure

1. Verify M5 thread on existing elements by measurement before ordering
   brass rod (M5 = 5mm diameter, 0.8mm pitch — confirm this is correct)
2. Cut two lengths of 5mm brass rod, each approximately 40mm
   (leaves room for threading and adjustment)
3. Tap M5 thread on one end of each rod — approximately 10mm of thread
4. Cut to final length: **3.3 cm from tip to start of threaded section**
5. File tip smooth
6. Screw into dipole base and verify fit
7. Measure total arm length (visible + base internal) = ~5.3 cm
8. Label elements: "1420 MHz" to distinguish from stock elements

### Cost

Approximately **$5–10** total. Negligible.

### Storage

Keep stock arms for use at other frequencies (137 MHz weather satellites,
433 MHz ISM, 1090 MHz ADS-B). Use custom brass elements for all HI
programme observations.

---

## Interim Configuration (until brass elements fabricated)

Until custom elements are made, use stock arms at **minimum extension
(fully collapsed)**. This gives:

- Total arm length: ~7 cm
- Resonant frequency: ~1070 MHz
- Mismatch loss at 1420 MHz: ~2–3 dB
- Usable for RFI survey work — sensitivity degraded but functional

**Document in session logs:** All RFI survey sessions prior to custom
element fabrication should note "stock dipole arms, fully collapsed,
~2–3 dB mismatch loss at 1420 MHz."

**Calibration:** Use CAL-000 with the ADF4351 to measure the actual
mismatch loss empirically once the V4c arrives. This gives a real number
to replace the ~2–3 dB estimate.

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

**At 4λ per arm (100cm arms at 1420 MHz = 4.74λ per arm):**
- Severe impedance mismatch — multiple anti-resonances
- Highly complex multi-lobe radiation pattern
- Deep nulls in multiple directions
- Completely unsuitable for this application

---

## Physical Configuration

**Arms:** Custom brass elements, 3.3 cm visible + M5 threaded section  
**Total arm length:** ~5.3 cm (including 2 cm internal base metal)  
**Orientation:** Vertical — arms pointing up and down  
**Mounting:** On Amazon Basics tripod at ~52" height  
**Connection:** SMA to RTL-SDR V4c input, bias tee OFF (passive antenna)  
**Polarisation:** Vertical linear  

**Note on polarisation:** Most man-made RFI sources (cellular, WiFi,
broadcast) use vertical polarisation. A vertically oriented dipole
is therefore well matched to the dominant polarisation of urban RFI
at 1420 MHz.

---

## Frequency Agility

For future RFI investigations at other frequencies, use stock telescopic
arms with length calculated as:

$$L_{visible} = \frac{7500}{f_{MHz}} - 2.0 \text{ cm (internal metal)}$$

| Frequency | Total arm length | Visible extension | Arms |
|---|---|---|---|
| 1420 MHz (HI line) | 5.265 cm | 3.265 cm — **use custom brass** | Custom |
| 1575 MHz (GPS L1) | 4.76 cm | 2.76 cm — **use custom brass** | Custom |
| 1090 MHz (ADS-B) | 6.88 cm | 4.88 cm — stock collapsed | Short |
| 433 MHz (ISM band) | 17.3 cm | 15.3 cm — stock at max | Short |
| 137 MHz (weather sats) | 54.7 cm | 52.7 cm | Long |
| 88–108 MHz (FM radio) | 69–85 cm | 67–83 cm | Long |

Note that GPS L1 (1575 MHz) also requires custom elements shorter than
the stock minimum — worth making a second pair when fabricating the
1420 MHz elements.

---

## Action Items

- [ ] Verify M5 thread on stock elements when dipole kit arrives
- [ ] Purchase 5mm brass rod stock
- [ ] Fabricate 1420 MHz custom elements (3.3 cm visible)
- [ ] Optionally fabricate 1575 MHz custom elements simultaneously
- [ ] Label all elements clearly
- [ ] Run CAL-000 with ADF4351 to measure actual mismatch loss of
      stock arms at 1420 MHz (interim characterisation)
- [ ] Update session logs to note which elements are in use

---

## Connection to INV002 and INV003

The dipole antenna design directly affects the quality of RFI data
feeding into the flagging algorithm (INV003). A properly matched
resonant dipole provides:

- Consistent, well-characterised sensitivity across the band
- Predictable radiation pattern for spatial RFI analysis
- No impedance mismatch artefacts in the baseband spectrum

An off-resonance dipole introduces frequency-dependent sensitivity
variations. The interim stock arm configuration must be documented
in all RFI survey sessions until custom elements are installed.

---

## References

- Balanis, C.A. — *Antenna Theory: Analysis and Design* — dipole impedance
  and radiation patterns (standard reference)
- RTL-SDR Blog dipole kit guide — equipment/datasheets/ (this repository)
- RTL-SDR Blog V4 users guide — equipment/datasheets/ (this repository)
- DUAL_SDR_ARCHITECTURE.md — Chain A system context (this repository)
- SDR_SELECTION.md — V4 selection rationale (this repository)
- ADF4351_CALIBRATION.md — CAL-000 mismatch loss measurement (this repository)
- INV003_rfi_flagging — RFI flagging algorithm (this repository)

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-30 | Initial document — λ/4 rationale, mismatch loss analysis, configuration |
| 2.0 | 2026-05-04 | Major revision — discovered stock arms cannot reach 1420 MHz resonant length; custom brass element solution documented; interim configuration defined; CAL-000 measurement added |


---
