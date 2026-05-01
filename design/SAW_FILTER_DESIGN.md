# SAW Filter Design — Analysis and Characterisation

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-04-30  
**Version:** 0.1 — framework only, awaiting KrakenRF component data  

---

## Status

**PENDING — awaiting response from KrakenRF.**

A component specification request was submitted to KrakenRF via their
contact form on 2026-04-30, requesting:

- SAW Filter 1 and SAW Filter 2 part numbers and datasheets
- Insertion loss (dB)
- Passband (MHz)
- Stopband rejection (dB)
- Passband ripple (dB)
- LNA2 chip identification and specifications

This document will be completed once that information is received.
The analytical framework is documented here in advance so that
commissioning measurements can be planned and executed systematically.

---

## Overview

The Discovery Dish HI feed contains two SAW (Surface Acoustic Wave)
filter stages in its signal chain:

```
Antenna → LNA1 (QPL9547) → SAW Filter 1 → LNA2 → SAW Filter 2 → Output
```

The SAW filters serve two critical roles:

1. **Anti-alias protection** — reject out-of-band signals before they
   reach the SDR ADC. Signals outside the passband that are not
   attenuated will alias into the HI band after downconversion.
   Once ADC saturation or aliasing occurs, information is
   irretrievably lost — no digital processing can recover it.

2. **RFI rejection** — reduce the amplitude of interfering signals
   before they reach LNA2 and the SDR mixer, reducing even-order
   intermodulation distortion (see DOWNCONVERSION_ARCHITECTURE.md).

The SAW filter analogy from the author's telephony background:
the SAW filters perform exactly the role of the anti-alias filter
before a codec ADC. The constraint is identical — the analogue
domain must do its job before sampling occurs. No digital processing
compensates for inadequate pre-ADC filtering.

---

## Known Specifications (from KrakenRF documentation)

| Parameter | Value | Source |
|---|---|---|
| Overall feed passband | 1380–1460 MHz | KrakenRF wiki |
| Target frequency | 1420.405 MHz | HI rest frequency |
| Number of SAW stages | 2 | KrakenRF wiki |
| SAW filter type | SAW (Surface Acoustic Wave) | KrakenRF wiki |
| Filter 1 part number | **TBD — awaiting KrakenRF** | |
| Filter 2 part number | **TBD — awaiting KrakenRF** | |
| Manufacturer | **TBD** | |

---

## Component Data — Pending KrakenRF Response

### SAW Filter 1

| Parameter | Value | Notes |
|---|---|---|
| Part number | TBD | |
| Manufacturer | TBD | |
| Centre frequency (MHz) | TBD | |
| Passband -3dB (MHz) | TBD | Lower edge |
| Passband +3dB (MHz) | TBD | Upper edge |
| Insertion loss (dB) | TBD | Feeds directly into Friis — critical |
| Passband ripple (dB) | TBD | Affects spectral baseline flatness |
| Stopband rejection (dB) | TBD | At what offset? |
| Shape factor | TBD | Ratio of 60dB to 3dB bandwidth |
| Roll-off rate (dB/MHz) | TBD | At band edges |
| Impedance (Ω) | TBD | Match to LNA1 output |
| Package | TBD | |
| Datasheet URL | TBD | |

### SAW Filter 2

| Parameter | Value | Notes |
|---|---|---|
| Part number | TBD | |
| Manufacturer | TBD | |
| Centre frequency (MHz) | TBD | |
| Passband -3dB (MHz) | TBD | |
| Passband +3dB (MHz) | TBD | |
| Insertion loss (dB) | TBD | |
| Passband ripple (dB) | TBD | |
| Stopband rejection (dB) | TBD | |
| Shape factor | TBD | |
| Roll-off rate (dB/MHz) | TBD | |
| Datasheet URL | TBD | |

### LNA2

| Parameter | Value | Notes |
|---|---|---|
| Chip / module | TBD | |
| Nominal gain (dB) | TBD | |
| Noise figure (dB) | TBD | |
| Datasheet URL | TBD | |

---

## Analytical Framework

### Role in Friis Noise Budget (INV001)

SAW filter insertion loss directly adds to system noise temperature.
For a passive lossy component at physical temperature T_phys:

$$F_{filter} = 10^{L_{dB}/10}$$

Where L_dB is the insertion loss in dB. Noise temperature contribution:

$$T_{filter} = T_{phys}(F_{filter} - 1)$$

At room temperature (T_phys = 290K) with 2 dB insertion loss:
$$F = 10^{0.2} = 1.585$$
$$T_{filter} = 290 \times 0.585 = 170 \text{ K}$$

But in the Friis cascade Filter 1 appears after LNA1 — its contribution
is divided by G_LNA1:

$$T_{F1,contribution} = \frac{T_{F1}}{G_{LNA1}}$$

With G_LNA1 = 20 dB (factor of 100):
$$T_{F1,contribution} = \frac{170}{100} = 1.7 \text{ K}$$

This is the critical calculation awaiting the actual insertion loss
values. See INV001_noise_budget for the full Friis analysis.

### Cascaded Filter Rejection

Two SAW stages in series multiply their rejection:

$$L_{total,dB} = L_{filter1,dB} + L_{filter2,dB}$$

If each filter provides 40 dB stopband rejection, the cascade provides
80 dB. This combined rejection determines how well out-of-band signals
are suppressed before the SDR ADC.

### Alias Vulnerability Frequencies

With SDR sample rate f_s, signals at f_LO ± f_s/2 alias directly into
the centre of the baseband. For LO = 1422 MHz at f_s = 2.4 Msps:

- Lower alias vulnerability: 1422 - 1.2 = **1420.8 MHz**
- Upper alias vulnerability: 1422 + 1.2 = **1423.2 MHz**

The SAW filters must provide adequate attenuation at these frequencies.
Once the passband edges are known from datasheets, check the filter
attenuation at these specific frequencies.

At f_s = 10 Msps (Airspy R2 maximum):
- Lower: 1422 - 5 = **1417 MHz**
- Upper: 1422 + 5 = **1427 MHz**

Both within the filter passband at maximum sample rate — the filter
cannot protect against aliasing at full Airspy bandwidth. Appropriate
sample rate selection is therefore important: use the minimum sample
rate that captures the required velocity range.

**Required bandwidth for M31 full velocity range:**
M31 HI spans approximately -570 to -30 km/s LSR. At 1420 MHz:

$$\Delta f = \frac{f_{HI} \times \Delta v}{c} = \frac{1420.405 \times 540}{299792} \approx 2.56 \text{ MHz}$$

Minimum sample rate to capture full M31 profile: ~3 Msps.
Recommended sample rate: **4–5 Msps** (some margin for filter roll-off).

### Passband Edge Effects on HI Observations

The SAW filter passband is not perfectly flat — it rolls off toward
the band edges. This roll-off affects observations of:

**Galactic HI emission at high velocities:** The Milky Way HI emission
spans a wide velocity range. At high positive velocities (receding gas),
the HI line is redshifted toward lower frequencies — toward the lower
passband edge at 1380 MHz. At -300 km/s (M31 systemic velocity), the
HI line is blueshifted to approximately 1422 MHz — well within the
passband. No concern for M31 observations.

**Passband ripple and spectral baseline:** Ripple across the passband
introduces a frequency-dependent gain variation that appears as a
structured baseline in the spectrum. This must be removed by baseline
subtraction (polynomial fitting to line-free channels). The amplitude
of the ripple determines how aggressively the baseline must be modelled.

---

## Empirical Characterisation Plan

Regardless of what datasheets KrakenRF provides, empirical
characterisation of the installed filter chain is essential.
Datasheets give component specifications — installed performance
may differ due to impedance mismatch at interconnects, temperature,
and manufacturing variation.

### Measurement 1 — Passband Shape

**Method:** Sky survey scan  
**Procedure:**
1. Point dish at cold sky (high elevation, away from Galactic plane)
2. Set SDR to maximum bandwidth
3. Record wideband power spectrum
4. Normalise to flat receiver response
5. The resulting curve is the effective passband of the full system

**Expected result:** Approximately flat from 1380–1460 MHz with
roll-off outside this range. Any passband ripple visible at this
scale affects spectral baselines.

**When:** During Phase 1 commissioning, before first science observations.

### Measurement 2 — Insertion Loss (via Tsys comparison)

**Method:** Y-factor comparison with Friis prediction  
**Procedure:**
1. Measure Tsys from Cas A Y-factor method
2. Calculate expected Tsys from Friis using datasheet insertion loss
3. Compare measured vs predicted
4. Discrepancy indicates actual vs datasheet insertion loss difference

**Expected result:** Measured Tsys within 10–20K of Friis prediction
if datasheets are accurate.

### Measurement 3 — Stopband Rejection (empirical)

**Method:** Known signal strength comparison  
**Procedure:**
1. Identify known out-of-band signal sources (GPS at 1575 MHz,
   cellular at 1700–1800 MHz) with known approximate EIRP
2. Measure their apparent level in the SDR output
3. Compare with expected level without filtering
4. Difference gives empirical stopband rejection estimate

**Limitation:** Requires knowledge of the transmitter EIRP — estimated
values only. Gives order-of-magnitude rejection figure.

### Measurement 4 — Passband Ripple

**Method:** Calibrated noise source scan  
**Procedure:**
1. Using a stable wideband noise source (or the sky at known
   brightness temperature), scan the SDR across the passband
   in narrow steps
2. Fit a smooth polynomial to the passband shape
3. Residuals from the polynomial fit reveal ripple amplitude

**Expected result:** Ripple < 1 dB across the 1380–1460 MHz passband
for a good SAW filter. Larger ripple requires more aggressive baseline
subtraction.

---

## Implications for Pipeline Design

Once insertion loss and passband shape are characterised, the following
pipeline elements can be properly specified:

**Baseline subtraction polynomial order** (INV002):
Higher passband ripple requires higher order polynomial to fit the
baseline. The polynomial order must be low enough not to absorb
the broad HI line but high enough to fit the ripple structure.
This is the key tradeoff that the passband ripple measurement informs.

**Usable velocity range:**
The passband roll-off at 1380 and 1460 MHz sets the maximum velocity
range over which the sensitivity is uniform. Observations near the
band edges have reduced sensitivity and increased baseline uncertainty.

**Frequency switching offset:**
The on/off line frequency switching offset must keep both frequencies
within the flat portion of the passband. If the off-line frequency
is too close to the band edge, the switched spectra have different
effective bandwidths and the subtraction is imperfect.

---

## Action Items

- [ ] Await KrakenRF response to contact form submitted 2026-04-30
- [ ] On response: pull datasheets for both SAW filters
- [ ] Complete component data tables above
- [ ] Complete Friis calculation in INV001 with actual insertion loss
- [ ] Calculate alias vulnerability frequencies for planned sample rates
- [ ] Plan commissioning measurement sequence (measurements 1–4 above)
- [ ] Update DOWNCONVERSION_ARCHITECTURE.md with specific filter rejection data
- [ ] Update E002 equipment log with confirmed component specifications

---

## References

- Morgan & Morgan — *Surface Acoustic Wave Filters* (2nd ed.) —
  SAW filter theory and design
- KrakenRF contact form response (pending)
- INV001_noise_budget — Friis noise analysis (this repository)
- DOWNCONVERSION_ARCHITECTURE.md — downconversion design (this repository)
- ADC_BIT_RESOLUTION.md — ADC analysis (this repository)

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1 | 2026-04-30 | Initial framework — awaiting KrakenRF component data |
