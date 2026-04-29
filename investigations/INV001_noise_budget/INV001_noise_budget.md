# INV001 — Signal Chain Noise Budget and Upgrade Path Analysis

**Observer:** Steve Hawker BEng MBA FRAS  
**Investigation ID:** INV001  
**Started:** 2026-04-28  
**Status:** In planning — awaiting component datasheets and baseline Cas A measurements  
**Target completion:** End of Year 1 (2027)

---

## 1. Motivation

The sensitivity of Blue Rock Radio Observatory is determined by the noise
performance of its signal chain. Every component from feed to SDR contributes
noise, and the relative contribution of each component determines where
engineering effort is best invested for maximum sensitivity improvement.

This investigation applies the Friis cascaded noise formula to:

1. Calculate the theoretical system noise temperature from component specifications
2. Validate the theoretical prediction against measured system temperature (from Cas A)
3. Determine which component upgrades yield the greatest sensitivity improvement
4. Produce a ranked upgrade path with quantitative predictions for each option

The result is an analytically rigorous upgrade roadmap — spending is directed
by calculation rather than intuition. The comparison between predicted and
measured improvement after any upgrade is itself a scientific validation.

This investigation is expected to be publishable in SARA proceedings as a
worked example useful to the amateur radio astronomy community.

---

## 2. Background

### 2.1 The Friis Cascaded Noise Formula

For a signal chain of N stages, the total noise factor is:

$$F_{total} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \frac{F_4 - 1}{G_1 G_2 G_3} + \cdots$$

Where:
- F_n = noise factor of stage n (linear, not dB)
- G_n = gain of stage n (linear, not dB)
- Noise factor F relates to noise figure NF by: F = 10^(NF/10)

**Key insight:** The noise contribution of each stage is divided by the
cumulative gain of all preceding stages. A high-gain, low-noise first stage
(LNA1) suppresses the noise contribution of everything downstream. This is
why LNA1 placement and performance is critical.

**Conversion between noise figure and noise temperature:**

$$T_{receiver} = T_0 (F_{total} - 1)$$

Where T_0 = 290K (standard reference temperature).

**System temperature:**

$$T_{sys} = T_{sky} + T_{spillover} + T_{receiver}$$

At 1420 MHz pointing away from the Galactic plane, T_sky ≈ 5–10K.
T_spillover (ground radiation entering feed sidelobes) ≈ 10–30K (estimate).
T_receiver dominates for an uncooled system.

**SEFD from system temperature:**

$$SEFD = \frac{2 k_B T_{sys}}{A_{eff}}$$

Where A_eff = η × π(D/2)² and η is aperture efficiency (~0.7–0.8 for a
well-designed feed).

### 2.2 Blue Rock Signal Chain

```
Feed → Cable → LNA1 → Filter1 → LNA2 → Filter2 → SDR
```

Each element contributes to the noise budget:

| Stage | Type | Role |
|---|---|---|
| Feed → LNA1 cable | Passive loss | Noise — adds directly to Tsys |
| LNA1 (QPL9547) | Active gain | Dominant noise contributor — sets floor |
| Filter 1 (SAW) | Passive loss | Noise — divided by G_LNA1 |
| LNA2 | Active gain | Noise — divided by G_LNA1 × G_Filter1 |
| Filter 2 (SAW) | Passive loss | Noise — divided by G_LNA1 × G_Filter1 × G_LNA2 |
| SDR | Active | Noise — heavily suppressed by preceding gain |

### 2.3 Engineering Background — Telephony Parallel

The author's background in digital telephony codecs (G.711/G.722) provides
direct intuition for this analysis. The SAW filters perform the same role
as anti-aliasing filters before a codec ADC — they must provide sufficient
attenuation before the sampling stage to prevent aliasing and ADC saturation.

Just as no amount of digital processing recovers a signal once the codec ADC
clips, no digital processing recovers information once the SDR ADC saturates
due to insufficient SAW filter rejection. The analogue domain constraints are
irreducible regardless of downstream digital sophistication.

This parallel also informs the gain staging analysis: in telephony, codec
dynamic range management (companding, gain control) ensures the signal is
neither lost in quantisation noise nor saturating the ADC. The Blue Rock
gain staging problem is identical — sufficient gain to lift the HI signal
above SDR quantisation noise, but not so much that RFI saturates the ADC.

---

## 3. Analytical Prediction

### 3.1 Component Parameter Table

*To be completed from datasheets. Obtain measured values where possible.*

| Stage | Component | NF (dB) | NF (linear F) | Gain (dB) | Gain (linear G) | Source |
|---|---|---|---|---|---|---|
| Feed→LNA1 cable | | — | — | (negative) | | Measured |
| LNA1 | QPL9547 | ~0.6 | | | | Datasheet |
| Filter 1 | SAW (TBD) | = insertion loss | | (negative) | | Datasheet |
| LNA2 | TBD | | | | | Datasheet |
| Filter 2 | SAW (TBD) | = insertion loss | | (negative) | | Datasheet |
| SDR | TBD | | | | | Datasheet |

*Note: For passive lossy components (cables, filters), noise figure equals
insertion loss in dB. This is a fundamental result from thermodynamics —
a passive attenuator at room temperature has noise figure equal to its loss.*

### 3.2 Friis Calculation

*To be completed once component parameters are obtained.*

```python
# See analysis.py for full Python implementation
# Preliminary structure:

import numpy as np

def db_to_linear(db):
    return 10 ** (db / 10)

def linear_to_db(linear):
    return 10 * np.log10(linear)

def friis_noise_factor(noise_factors, gains):
    """
    Calculate cascaded noise factor using Friis formula.
    noise_factors: list of linear noise factors [F1, F2, F3, ...]
    gains: list of linear gains [G1, G2, G3, ...]
    Returns: total noise factor (linear)
    """
    F_total = noise_factors[0]
    cumulative_gain = gains[0]
    for i in range(1, len(noise_factors)):
        F_total += (noise_factors[i] - 1) / cumulative_gain
        cumulative_gain *= gains[i]
    return F_total

def noise_factor_to_temp(F, T0=290):
    return T0 * (F - 1)

def sefd(Tsys, dish_diameter=0.70, efficiency=0.75):
    k_B = 1.38e-23
    A_eff = efficiency * np.pi * (dish_diameter/2)**2
    return (2 * k_B * Tsys) / A_eff * 1e26  # in Jansky

# Component values — fill in from datasheets
components = {
    'cable':    {'nf_db': None, 'gain_db': None},
    'lna1':     {'nf_db': 0.6,  'gain_db': None},  # QPL9547 datasheet
    'filter1':  {'nf_db': None, 'gain_db': None},  # SAW datasheet
    'lna2':     {'nf_db': None, 'gain_db': None},
    'filter2':  {'nf_db': None, 'gain_db': None},
    'sdr':      {'nf_db': None, 'gain_db': 0},     # SDR is last stage
}
```

### 3.3 Upgrade Scenario Predictions

*To be calculated once baseline is established.*

**Scenario A — Baseline (current hardware)**
- Predicted Tsys: TBD K
- Predicted SEFD: TBD Jy
- M31 integration for SNR=5: TBD minutes

**Scenario B — Improved Filter 1 (lower insertion loss)**
- Parameter changed: Filter 1 insertion loss reduced from X dB to Y dB
- Predicted Tsys improvement: TBD K
- Predicted SEFD improvement: TBD Jy
- Improvement factor: TBD
- Assessment: Modest improvement — divided by G_LNA1 in Friis sum

**Scenario C — Improved LNA1 (lower noise figure)**
- Parameter changed: LNA1 NF reduced from 0.6 dB to Z dB
- Predicted Tsys improvement: TBD K
- Predicted SEFD improvement: TBD Jy
- Improvement factor: TBD
- Assessment: Maximum leverage — F_LNA1 enters Friis sum undivided

**Scenario D — Minimise feed-to-LNA1 cable length**
- Parameter changed: Cable loss reduced from X dB to near zero
- Predicted Tsys improvement: TBD K
- Assessment: Cable loss before LNA1 adds directly to Tsys — minimise

**Scenario E — Cryogenic LNA1**
- Physical temperature: ~20K
- Achievable NF: ~0.1 dB
- Predicted Tsys: ~25–30K
- Predicted SEFD: TBD Jy
- Improvement factor vs baseline: ~5–6×
- Assessment: Technically demanding, significant cost, but transforms
  capability — Virgo cluster galaxies become potentially detectable
- Feasibility: Long-term stretch goal

**Scenario F — Additional pre-LNA1 filtering**
- Motivation: If LNA1 is being compressed by strong out-of-band RFI,
  a cavity or helical filter before LNA1 could improve effective linearity
  despite adding noise figure
- Note: This is a tradeoff with no universal answer — depends on actual
  RFI environment at Blue Rock site. Requires RFI survey data (see INV003)
- Assessment: Investigate after RFI characterisation complete

---

## 4. Experimental Method

### 4.1 Baseline system temperature measurement

Using Cas A as flux calibration standard:

1. Observe Cas A at known flux density (see targets/CasA.md for epoch-corrected value)
2. Measure on-source and off-source antenna temperatures
3. Apply Y-factor method: Y = T_on / T_off = (T_sys + T_source) / T_sys
4. Derive T_sys = T_source / (Y - 1)
5. Derive SEFD = 2 k_B T_sys / A_eff

Repeat minimum 5 sessions to establish reliable baseline with uncertainty estimate.

### 4.2 Component characterisation

Where possible, measure rather than rely on datasheet values:
- Cable loss: measure with SDR before and after cable insertion
- SAW filter insertion loss: measure with SDR and known signal source
- LNA gain: harder to measure directly — use datasheet with caution

### 4.3 Upgrade validation

After any hardware upgrade:
1. Create new equipment log version immediately
2. Repeat Cas A measurement within first week
3. Compare measured Tsys with prediction from Friis model
4. Document agreement or discrepancy and investigate causes

---

## 5. Results

*To be populated as measurements are made.*

### 5.1 Measured component parameters

*(fill in as datasheets obtained and measurements made)*

### 5.2 Measured baseline system temperature

| Session | Date | Tsys (K) | SEFD (Jy) | Notes |
|---|---|---|---|---|
| | | | | |

**Mean Tsys:** K  
**Standard deviation:** K  
**Predicted Tsys:** K  
**Agreement:** %

### 5.3 Upgrade results

*(fill in as upgrades are implemented)*

---

## 6. Conclusions

*To be completed at investigation close.*

---

## 7. References

- Friis, H.T. 1944 — "Noise figures of radio receivers" *Proc. IRE* 32, 419
- Kraus — *Radio Astronomy* Ch. 7 (system temperature and sensitivity)
- Wilson, Rohlfs & Hüttemeister — *Tools of Radio Astronomy* Ch. 4
- QPL9547 datasheet — Qorvo
- SAW filter datasheets — (add when components identified)
- Baars et al. 1977 — Cas A flux calibration standard

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-28 | Initial investigation plan |
