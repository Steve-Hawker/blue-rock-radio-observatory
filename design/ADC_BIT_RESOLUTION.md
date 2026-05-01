# ADC Bit Resolution — Design Analysis and SDR Selection Rationale

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-04-30  
**Version:** 1.0  

---

## Overview

This document analyses the relationship between ADC bit resolution and
radio astronomy performance, establishing the mathematical basis for
SDR selection and identifying the point of diminishing returns beyond
which additional bit depth provides no meaningful science benefit.

The analysis informs the Phase 1 (RTL-SDR V4, 8-bit) and Phase 2
(Airspy R2, 12-bit) SDR selection documented in SDR_SELECTION.md.

---

## Fundamental Relationship — Quantisation Noise

When an ADC samples an analogue signal it rounds each sample to the
nearest discrete level. This rounding error is quantisation noise.

For an n-bit ADC with full-scale range V_fs:

**Quantisation step size:**
$$\Delta = \frac{V_{fs}}{2^n}$$

**Quantisation noise power:**
$$\sigma_q^2 = \frac{\Delta^2}{12} = \frac{V_{fs}^2}{12 \cdot 2^{2n}}$$

**Signal to Quantisation Noise Ratio (SQNR) for a full-scale sinusoid:**
$$SQNR = 6.02n + 1.76 \text{ dB}$$

**Critical result: every additional bit adds exactly 6.02 dB of dynamic range.**

---

## Theoretical Dynamic Range by Bit Depth

| Bits | Theoretical SQNR | Voltage levels | Notes |
|---|---|---|---|
| 8 | 49.9 dB | 256 | RTL-SDR V4 nominal |
| 10 | 62.0 dB | 1,024 | |
| 12 | 74.0 dB | 4,096 | Airspy R2 nominal |
| 14 | 86.1 dB | 16,384 | SDRplay RSPdx nominal |
| 16 | 98.1 dB | 65,536 | |
| 18 | 110.2 dB | 262,144 | Airspy HF+ nominal |
| 24 | 146.2 dB | 16,777,216 | Audio ADC standard |

---

## The Diminishing Returns — Three Physical Limits

The theoretical SQNR assumes a perfect ADC. Three physical effects
impose a ceiling well below the theoretical limit, defining where
additional bits stop providing benefit.

### Limit 1 — Effective Number of Bits (ENOB)

Real ADCs never achieve their theoretical bit depth due to non-linearity,
integral non-linearity (INL), differential non-linearity (DNL), and
clock jitter. Actual performance is characterised by ENOB:

$$ENOB = \frac{SINAD - 1.76}{6.02}$$

Where SINAD is the measured Signal to Noise And Distortion ratio.

**Real-world ENOB for relevant devices:**

| Device | Nominal bits | Typical ENOB | Effective SQNR | Loss |
|---|---|---|---|---|
| RTL-SDR V4 (RTL2832U) | 8 | ~7.0 | ~44 dB | ~1 bit |
| Airspy R2 | 12 | ~11.0–11.5 | ~68 dB | ~0.5–1 bit |
| SDRplay RSPdx | 14 | ~13.0 | ~80 dB | ~1 bit |
| Airspy HF+ | 18 | ~15–16 | ~92 dB | ~2–3 bits |
| Professional ADC | 16 | ~14–15 | ~86 dB | ~1–2 bits |

The real-world gap between V4 and Airspy R2 is approximately **24 dB**
of dynamic range — meaningful and worth the upgrade.

### Limit 2 — Thermal Noise Floor

Every resistor and amplifier adds Johnson-Nyquist thermal noise
regardless of ADC resolution:

$$V_{noise} = \sqrt{4 k_B T R \Delta f}$$

At room temperature (T = 290K), with ~100Ω source impedance and
2 MHz bandwidth:

$$V_{noise} = \sqrt{4 \times 1.38 \times 10^{-23} \times 290 \times 100 \times 2 \times 10^6}$$
$$V_{noise} \approx 57 \text{ nV} \approx -135 \text{ dBm}$$

Once quantisation noise falls below the thermal noise floor, additional
bits quantise thermal noise more finely — yielding no science benefit.

**For the Blue Rock HI feed with Tsys ~150K:**

System noise power in 2 MHz bandwidth:
$$P_{noise} = k_B T_{sys} \Delta f = 1.38 \times 10^{-23} \times 150 \times 2 \times 10^6 \approx -134 \text{ dBm}$$

The Airspy R2 at ~68 dB effective SQNR has quantisation noise well
below this thermal floor. Going to 14 or 16-bit provides no additional
sensitivity — thermal noise utterly dominates.

### Limit 3 — Spurious Free Dynamic Range (SFDR)

Non-linearities create harmonic distortion and intermodulation between
signals. A strong RFI signal at f_RFI produces spurious products at
2f_RFI, 3f_RFI, and intermodulation products that can fall in the
HI passband and masquerade as spectral features.

$$SFDR \approx 6.02n + C \text{ dB}$$

Better bit depth and linearity pushes spurious products lower relative
to the signal. However once SFDR exceeds the thermal noise floor by a
comfortable margin, further improvement is irrelevant — spurious products
are buried in noise regardless.

---

## Why Bit Depth Matters for Radio Astronomy — RFI Headroom

In radio astronomy the HI signal is typically 6–8 orders of magnitude
weaker than the receiver noise. The ADC digitises:

$$V_{ADC} = V_{receiver\_noise} + V_{RFI} + V_{HI}$$

The HI signal emerges through spectral averaging across many integrations,
not through the ADC directly resolving small voltages.

**Bit depth matters primarily for RFI headroom — not inherent sensitivity.**

With a strong RFI spike and an 8-bit ADC (256 levels):
- RFI spike occupies most of the 256 available levels
- Receiver noise and HI signal are compressed into the remaining levels
- Effective bit depth for science signal is drastically reduced
- In extreme cases ADC saturates — all information irretrievably lost

With a 12-bit ADC (4096 levels), the same RFI spike occupies
proportionally fewer levels, preserving headroom for the science signal.

**This is the primary justification for 12-bit in the San Jose urban
RFI environment — not improved intrinsic sensitivity, but ADC saturation
resistance.**

---

## Gain Staging and ADC Headroom

Whatever ADC is used, the signal arriving at the ADC must be correctly
scaled. Two failure modes:

**Insufficient gain:**
Signal occupies only the bottom few bits — effectively reducing usable
bit depth. Quantisation noise dominates over thermal noise.
Result: degraded sensitivity.

**Excessive gain:**
Strong RFI saturates the ADC — clipping occurs and all information
in that time sample is irretrievably lost. Cannot be corrected in
post-processing.
Result: corrupted data.

**Correct setting:**
Noise floor occupies roughly the bottom 30–40% of ADC range.
Sufficient headroom above for RFI peaks without saturation.
Science signal remains above quantisation noise floor.

The LNA chain in the Discovery Dish HI feed provides substantial fixed
gain. The SDR's variable gain control adjusts the final level into the
ADC. Optimal gain setting must be determined empirically during
commissioning and documented in the equipment log.

**Commissioning procedure:**
1. Point dish at cold sky (away from Galactic plane)
2. Adjust SDR gain until noise floor is clearly visible but not clipping
3. Note gain setting and time-average power level
4. Check that known RFI sources do not cause saturation at this gain
5. Document final gain setting in equipment log — do not change without
   re-documenting

---

## The Point of Diminishing Returns — Quantified

| Upgrade | Dynamic range gain | Science benefit | Recommendation |
|---|---|---|---|
| 8-bit → 12-bit | ~24 dB real-world | Significant — RFI headroom for urban site | Do it — Airspy R2 |
| 12-bit → 14-bit | ~12 dB real-world | Marginal — thermal noise dominates | Probably not worth it |
| 14-bit → 16-bit | ~12 dB real-world | Negligible — well below thermal floor | No benefit |
| 16-bit → 18-bit | ~12 dB real-world | None — thermal noise dominates completely | No benefit |

**The 8→12 bit upgrade is the only one with clear science justification
for HI radio astronomy from an urban site.**

Beyond 12-bit, money is better spent on:
- LNA1 noise figure improvement (INV001 — direct Tsys reduction)
- Feed positioning optimisation (aperture efficiency)
- RFI flagging algorithm (INV003 — recover data rather than prevent loss)
- Cryogenic LNA (exotic — Tsys from ~150K to ~25K, transformative)

---

## SDR Candidates at 12-bit and Above

| SDR | Nominal bits | ENOB | SFDR | Max Msps | Bias tee | Price | Notes |
|---|---|---|---|---|---|---|---|
| Airspy R2 | 12 | ~11.5 | ~80 dB | 10 | Yes | ~$169 | Recommended Phase 2 |
| Airspy Mini | 12 | ~11.0 | ~75 dB | 6 | Yes | ~$99 | Less bandwidth than R2 |
| SDRplay RSP1B | 14 | ~12–13 | ~85 dB | 10 | No* | ~$120 | *External bias tee needed |
| SDRplay RSPdx | 14 | ~13 | ~98 dB | 10 | No* | ~$200 | *External bias tee needed |
| Airspy HF+ Discovery | 18 | ~15 | ~105 dB | 0.66† | Yes | ~$169 | †Optimised for HF — poor at 1420 MHz |
| ADALM-Pluto | 12 | ~11 | ~70 dB | 61 | No | ~$150 | Overkill bandwidth, no bias tee |

**Notes on candidates:**

**Airspy HF+ Discovery** — despite 18-bit nominal resolution and
impressive ENOB at HF, this device is optimised for frequencies below
~30 MHz and VHF. Performance at 1420 MHz is significantly degraded.
Not recommended for HI work despite the impressive specifications.

**SDRplay devices** — no built-in bias tee. Requires external bias tee
injector to power the HI feed LNA chain. Adds complexity, cost, and
connector loss. Confirmed compatible hardware preferred — see
SDR_SELECTION.md.

**Airspy R2 remains the recommended Phase 2 SDR** — 12-bit ENOB at
the thermal noise knee for this application, built-in bias tee,
explicitly compatible with Discovery Dish feed, well supported in
GNU Radio via SoapySDR.

---

## Relationship to INV001 Noise Budget

The ADC contributes to the system noise budget via quantisation noise.
In the Friis cascade the ADC is the final stage — its noise contribution
is divided by the cumulative gain of all preceding stages:

$$F_{total} = F_{LNA1} + \frac{F_{F1}-1}{G_{LNA1}} + \cdots + \frac{F_{ADC}-1}{G_{LNA1} \cdot G_{F1} \cdot G_{LNA2} \cdot G_{F2}}$$

With typical preceding gain of ~40–50 dB (factors of 10,000–100,000),
the ADC noise contribution is suppressed by this factor before reaching
the total. Even an 8-bit ADC with relatively high quantisation noise
contributes negligibly to Tsys via the Friis formula.

**The ADC's impact on Tsys is negligible. Its impact on dynamic range
and RFI headroom is significant. These are separate effects.**

This explains why improving the LNA1 noise figure (INV001) has far more
impact on Tsys and SEFD than upgrading ADC bit depth. But upgrading
ADC bit depth improves RFI tolerance which LNA improvement does not.
The two upgrades address different problems and are complementary.

---

## Summary for Blue Rock Programme

| Phase | SDR | ADC bits | ENOB | Primary limitation |
|---|---|---|---|---|
| 1 | RTL-SDR V4 | 8 | ~7 | RFI headroom in urban environment |
| 2 | Airspy R2 | 12 | ~11.5 | Thermal noise (appropriate) |
| Beyond 2 | Not ADC | — | — | Focus on LNA, feed, flagging |

The upgrade from 8-bit to 12-bit is scientifically justified and planned.
Beyond 12-bit, diminishing returns are severe and budget is better
directed elsewhere in the signal chain.

---

## References

- Walden 1999 — "Analog-to-digital converter survey and analysis"
  *IEEE Journal on Selected Areas in Communications* 17(4)
- SDR_SELECTION.md — SDR hardware selection (this repository)
- INV001_noise_budget — Friis noise analysis (this repository)
- Airspy R2 specifications — airspy.com
- RTL-SDR Blog V4 specifications — rtl-sdr.com

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-30 | Initial document — SQNR derivation, diminishing returns analysis, SDR comparison, gain staging |
