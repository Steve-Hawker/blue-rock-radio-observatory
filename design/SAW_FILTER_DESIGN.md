# SAW Filter Design — Analysis and Characterisation

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-04-30  
**Version:** 1.0 — component identities confirmed from PCB inspection and datasheet matching  

---

## Status

**RESOLVED — component identities confirmed 2026-05-06.**

SAW filter part numbers identified by:
1. Close-up photograph of the HI feed PCB (Kraken_L-band_ACARS_feed.jpeg)
2. Cross-referencing with Tai-Saw Technology datasheets TA2494A and TA1077A
3. Both filters confirmed as Tai-Saw Technology 1420 MHz 3.0×3.0mm SMD devices

KrakenRF contact form response not required — component identification
achieved directly from PCB inspection.

**Note on feed access:** The HI feed PCB is a sealed assembly. Direct
component measurement (S-parameter measurement of individual filters)
is not possible without disassembly. All characterisation must be
performed at the feed assembly level using the ADF4351 CAL-002 passband
sweep procedure.

---

## Overview

The Discovery Dish HI feed contains two SAW filter stages:

```
Antenna → LNA1 (QPL9547) → SAW1 (TA1077A) → LNA2 → SAW2 (TA2494A) → Output
```

Both filters are manufactured by Tai-Saw Technology Co., Ltd., Taiwan,
and are centre-frequency matched to 1420 MHz. They differ significantly
in impedance topology and out-of-band rejection — the placement order
reflects this.

---

## Known Specifications (confirmed from datasheets)

| Parameter | Value | Source |
|---|---|---|
| Overall feed passband | 1380–1460 MHz | KrakenRF wiki |
| Target frequency | 1420.405 MHz | HI rest frequency |
| Number of SAW stages | 2 | PCB inspection |
| SAW filter 1 (F1) | **TA1077A** | Tai-Saw Technology |
| SAW filter 2 (F2) | **TA2494A** | Tai-Saw Technology |
| Manufacturer | Tai-Saw Technology Co., Ltd., Taiwan | Both filters |
| LNA1 | QPL9547 (Qorvo) | KrakenRF documentation + PCB |
| LNA2 | Unknown — not yet identified | PCB inspection |

---

## Component Data — SAW Filter 1 (TA1077A)

**Position:** After LNA1 (QPL9547), before LNA2

| Parameter | Min | Typ | Max | Units | Notes |
|---|---|---|---|---|---|
| Part number | — | TA1077A | — | — | Tai-Saw Technology |
| Centre frequency | — | 1420 | — | MHz | |
| Bandwidth at -2 dB | 60 | 72 | — | MHz | 1390–1450 MHz |
| Insertion loss (1390–1450 MHz) | — | 3.5 | 5.0 | dB | |
| Amplitude ripple (1390–1450 MHz) | — | 1.5 | 2.0 | dB | |
| I/O VSWR (1390–1450 MHz) | — | 2.0 | 2.5 | — | |
| Attenuation 50–1320 MHz | 42 | 62 | — | dB | Excellent OOB rejection |
| Attenuation 1530–3000 MHz | 42 | 52 | — | dB | |
| Attenuation 3000–4000 MHz | 30 | 38 | — | dB | |
| Attenuation 4000–6000 MHz | 15 | 27 | — | dB | |
| Input impedance | — | 200Ω balanced | — | — | With 22nH inductor |
| Output impedance | — | 50Ω | — | — | Single-ended |
| Package | — | 3.0×3.0mm SMD | — | — | |
| Operating temperature | -40 | — | +85 | °C | |

**Key characteristic:** The TA1077A has a **balanced 200Ω input** interface.
This is a balun-SAW topology — it accepts a balanced (differential) signal
from the QPL9547 output and converts to single-ended 50Ω output. This
provides inherent common-mode rejection in addition to frequency filtering.

The dramatically higher out-of-band rejection (42 dB minimum vs 24 dB
for the TA2494A) makes this the primary RFI rejection filter, correctly
placed first in the cascade where RFI amplitudes are highest.

---

## Component Data — SAW Filter 2 (TA2494A)

**Position:** After LNA2, before SMA output connector

| Parameter | Min | Typ | Max | Units | Notes |
|---|---|---|---|---|---|
| Part number | — | TA2494A | — | — | Tai-Saw Technology |
| Centre frequency | — | 1420 | — | MHz | |
| Passband | — | 1380–1460 | — | MHz | 80 MHz bandwidth |
| Insertion loss (1380–1460 MHz) | — | 3.5 | 4.2 | dB | |
| Amplitude ripple (1380–1460 MHz) | — | 1.0 | 1.8 | dB | |
| VSWR (1380–1460 MHz) | — | 1.9 | 2.5 | — | |
| Attenuation 10–1300 MHz | 24 | 28 | — | dB | |
| Attenuation 1550–3000 MHz | 24 | 30 | — | dB | |
| Input impedance | — | 50Ω | — | — | Single-ended |
| Output impedance | — | 50Ω | — | — | Single-ended |
| Package | — | 3.0×3.0mm SMD | — | — | |
| Operating temperature | -40 | — | +85 | °C | |

**Key characteristic:** The TA2494A is a conventional 50Ω single-ended
SAW filter. Wider passband (80 MHz) than the TA1077A, lower stopband
rejection, but adequate for final clean-up after the cascade. Correctly
placed second, after the heavy lifting has been done by the TA1077A.

---

## Cascaded Filter Performance

With both filters in series (TA1077A → LNA2 → TA2494A):

| Frequency region | TA1077A rejection | TA2494A rejection | Combined (min) |
|---|---|---|---|
| 50–1300 MHz | 42 dB | 24 dB | **66 dB** |
| 1530–3000 MHz | 42 dB | 24 dB | **66 dB** |

**66 dB minimum combined out-of-band rejection** below 1300 MHz and above
1530 MHz. In practice the typical values suggest ~90 dB combined rejection.

This is excellent performance for an urban RFI environment. The I-680
corridor RFI, cellular infrastructure, and other L-band signals are
attenuated by at minimum 66 dB before reaching the SDR ADC.

**GPS L1 at 1575 MHz:** Falls in the 1530–3000 MHz rejection band.
Combined rejection of 66 dB minimum — GPS signals (already ~-130 dBm
at ground level) are entirely below the noise floor. No GPS interference
concern confirmed.

---

## Friis Noise Budget Impact

With confirmed insertion loss values, the Friis contribution of both
SAW filters can now be calculated.

**SAW1 (TA1077A) — after LNA1:**

At 3.5 dB typical insertion loss:
$$F_{SAW1} = 10^{3.5/10} = 2.239$$
$$T_{SAW1} = 290 \times (2.239 - 1) = 359 \text{ K}$$

But SAW1 is after LNA1 (gain ~21.5 dB = factor 141):
$$T_{SAW1,contribution} = \frac{359}{141} = \mathbf{2.5 \text{ K}}$$

**SAW2 (TA2494A) — after LNA2:**

At 3.5 dB typical insertion loss, after LNA1 × SAW1 × LNA2 cascade
(total gain approximately 40 dB = factor 10,000):
$$T_{SAW2,contribution} = \frac{359}{10000} \approx \mathbf{0.04 \text{ K}}$$

SAW2 contribution is negligible. SAW1 adds ~2.5 K — small compared
with LNA1 noise temperature (~50 K equivalent at 0.17 dB NFmin).

These values feed directly into INV001 — update that document next.

---

## Analytical Framework

### Alias Vulnerability Frequencies

With SDR sample rate f_s, signals at f_LO ± f_s/2 alias directly into
the centre of the baseband. For LO = 1422 MHz at f_s = 2.4 Msps:

- Lower alias vulnerability: 1422 - 1.2 = **1420.8 MHz**
- Upper alias vulnerability: 1422 + 1.2 = **1423.2 MHz**

Both within the SAW passband — the filters cannot protect against
aliasing at these frequencies, which is correct behaviour. What matters
is that out-of-band signals do not alias.

At f_s = 10 Msps (Airspy R2 maximum):
- Lower: 1422 - 5 = **1417 MHz** — within passband ✓
- Upper: 1422 + 5 = **1427 MHz** — within passband ✓

**Required bandwidth for M31 full velocity range:**
M31 HI spans approximately -570 to -30 km/s LSR. At 1420 MHz:

$$\Delta f = \frac{f_{HI} \times \Delta v}{c} = \frac{1420.405 \times 540}{299792} \approx 2.56 \text{ MHz}$$

Minimum sample rate: ~3 Msps. Recommended: **4–5 Msps**.

### Passband Edge Effects on HI Observations

The SAW passband rolls off toward the band edges. M31 at -300 km/s
systemic velocity blueshifts the HI line to ~1422 MHz — well within
the flat passband. No concern for M31 observations.

Passband ripple (TA2494A: 1.0 dB typ, 1.8 dB max) introduces a
frequency-dependent gain variation requiring baseline subtraction.
See INV002 for polynomial baseline subtraction approach.

---

## Empirical Characterisation Plan

The sealed feed PCB means all characterisation must be done at the
assembly level via ADF4351 CAL-002 passband sweep.

### CAL-002 — Passband Shape (ADF4351 method)

**Method:** ADF4351 signal source sweep  
**Procedure:**
1. Connect ADF4351 → 30 dB attenuator → feed SMA input
2. Step ADF4351 from 1360 to 1480 MHz in 1 MHz steps
3. Record Airspy R2 power at each step
4. Normalise — reveals empirical combined passband of LNA1+SAW1+LNA2+SAW2
5. Compare with datasheet predicted cascade

**Expected result:** Flat from ~1390–1450 MHz, roll-off outside.
Ripple amplitude should be ≤ 2 dB (worst case TA2494A spec).

### Sky passband measurement

Point dish at cold sky (high elevation, away from Galactic plane),
record wideband power spectrum at maximum SDR bandwidth. Normalise
to flat response. Reveals installed passband shape including all
thermal and impedance mismatch effects.

### Stopband rejection (empirical)

GPS L1 at 1575 MHz: known spread-spectrum signal at approximately
-130 dBm at ground. Measure apparent level in SDR output vs expected
level without filtering. Gives lower bound on stopband rejection at
1575 MHz. Expected: > 66 dB — signal should be undetectable.

---

## Implications for Pipeline Design

**Baseline subtraction polynomial order (INV002):**
TA2494A passband ripple of 1.0–1.8 dB requires baseline subtraction.
Polynomial order 3–5 should be sufficient. Must not absorb the broad
HI line — use line-free channels for polynomial fitting.

**Usable velocity range:**
TA1077A passband -2dB bandwidth: 60–72 MHz (1384–1456 MHz).
TA2494A passband: 1380–1460 MHz.
Combined effective flat passband: approximately **1390–1450 MHz**.
Velocity range at 1390 MHz: +2100 km/s; at 1450 MHz: -6200 km/s.
All science targets well within range.

---

## Action Items

- [x] Identify SAW filter part numbers — TA1077A and TA2494A confirmed
- [x] Obtain datasheets — filed in equipment/datasheets/
- [x] Calculate Friis contributions — SAW1: 2.5K, SAW2: ~0K
- [ ] Complete INV001 with confirmed SAW insertion loss values
- [ ] Run CAL-002 passband sweep when ADF4351 arrives (~May 22)
- [ ] Compare empirical passband with datasheet cascade prediction
- [ ] Update DOWNCONVERSION_ARCHITECTURE.md with confirmed rejection data
- [ ] Update E002 equipment log when feed arrives (Aug 2026)
- [ ] Identify LNA2 chip from PCB — pending higher resolution image

---

## References

- Tai-Saw Technology TA1077A datasheet — equipment/datasheets/ (this repository)
- Tai-Saw Technology TA2494A datasheet — equipment/datasheets/ (this repository)
- QPL9547 datasheet — equipment/datasheets/ (this repository)
- Kraken_L-band_ACARS_feed.jpeg — PCB photo used for identification
- Morgan & Morgan — *Surface Acoustic Wave Filters* (2nd ed.)
- INV001_noise_budget — Friis noise analysis (this repository)
- DOWNCONVERSION_ARCHITECTURE.md — downconversion design (this repository)
- ADF4351_CALIBRATION.md — CAL-002 passband measurement procedure

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1 | 2026-04-30 | Initial framework — awaiting KrakenRF component data |
| 1.0 | 2026-05-06 | Major update — SAW filters identified as TA1077A (F1) and TA2494A (F2) from PCB inspection; full component data tables; Friis contributions calculated; cascaded rejection analysis; KrakenRF response no longer required |


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
