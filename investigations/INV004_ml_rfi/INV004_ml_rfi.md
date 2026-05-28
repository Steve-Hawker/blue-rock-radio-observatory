# INV004 — Machine Learning RFI Mitigation

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-13  
**Version:** 0.1 — Concept capture  
**Status:** Pre-implementation — data collection begins Phase 3  

---

## Motivation

Blue Rock Radio Observatory operates in an urban San Jose RF environment.
The SAW filter chain (TA1077A → TA2494A) provides hardware rejection of
out-of-band interference, but in-band RFI at 1380–1460 MHz remains a
fundamental challenge for HI science. Classical mitigation strategies —
sigma clipping, median filtering, wavelet/morphology approaches — operate
on individual observations and have no memory of prior sessions.

Five years of continuous dual-chain operation (science dish + reference
dipole) at a fixed site generates a uniquely valuable dataset: a
longitudinal RFI characterisation of one urban location at 1420 MHz,
with simultaneous correlated reference channel data. This is the
training corpus for a neural network RFI mitigation pipeline.

---

## Concept

### MIT Lincoln Laboratory Approach

MIT Lincoln Laboratory has developed neural network systems for noise
removal that operate via continuous online training: the network removes
noise from the signal, and the removed noise is compared to an expected
noise model. The difference drives continuous weight updates. The network
improves as it operates.

Reference: MIT LL Technology Transfer —
*Neural Network Systems and Methods for Removing Noise from Signals*
https://www.ll.mit.edu/partner-us/available-technologies/neural-network-systems-and-methods-removing-noise-signals

The underlying patent or publication should be identified and cited in
preference to the technology transfer page for formal thesis references.
See BRRO_references.bib entry `mitll_nn_rfi` for tracking note.

### Adaptation for BRRO

The MIT LL framework maps directly onto the BRRO dual-chain architecture:

```
Science dish (Airspy R2)
    → raw HI spectrum with RFI
        → neural network
            → cleaned spectrum
            → removed noise component
                → compare to expected noise model
                    → continuous weight update
```

**Expected noise model:** HI4PI all-sky survey provides the expected
clean HI spectrum at BRRO's angular resolution (~20°) for any pointing.
For each observation, the expected signal at that sky coordinate and
LSR velocity is known from HI4PI. The network's residual (removed
noise) should not contain HI signal — any HI in the residual is a
training error signal.

**Reference channel as training signal:** The RTL-SDR V4c + reference
dipole (Chain A) provides a contemporaneous RFI measurement at the
same location with no dish gain — it sees the same terrestrial RFI
environment without the HI signal. Cross-correlating Chain A and
Chain B isolates RFI from astronomy. RFI correlated between channels
is terrestrial. Signal uncorrelated between channels is potentially
real astronomy.

This gives three training signals without manual annotation:
1. HI4PI expected spectrum — what the clean signal should look like
2. Reference channel correlation — real-time RFI identification
3. Network residual vs HI4PI — continuous weight update signal

---

## Data Collection Strategy

### Starting from Phase 3 (V4c commissioning)

Data collection for the training corpus begins immediately with Phase 3
RFI surveys — not at Phase 5. Every session contributes. The value of
the dataset grows with time and diversity of conditions.

**What to log every session:**

| Dataset | Chain | Format | Notes |
|---------|-------|--------|-------|
| Raw power spectrum | Chain A (V4c) | CSV, 1 MHz resolution | RFI reference channel |
| Raw power spectrum | Chain B (Airspy R2) | CSV, 1 MHz resolution | Science channel |
| Calibrated HI spectrum | Chain B | CSV, km/s velocity axis | After CAL-000+ |
| Environmental | Pi 2 BME280 + LSM6DSOX | CSV | Temperature, humidity, dish elevation |
| Session metadata | — | YAML/JSON | Date, time, LST, pointing, equipment version |

**Storage requirement estimate:**
- Per session: ~50 MB raw + calibrated spectra
- Per year at 3 sessions/week: ~7.8 GB
- Five years: ~40 GB
- Comfortably fits on a 256 GB microSD or NAS

### Labelling Strategy

No manual labelling required. Three automated label sources:

1. **HI4PI comparison:** For any pointing (l, b) and LSR velocity range,
   HI4PI provides expected brightness temperature. Label RFI as any
   excess above HI4PI + noise model.

2. **Reference channel correlation:** Flag frequency channels where Chain A
   and Chain B power are correlated above threshold — terrestrial RFI.

3. **Session quality flags:** Session logs already record observing
   conditions. Flagged sessions (high wind, equipment issues) excluded
   from training set.

---

## Phased Implementation Plan

### Phase 3 — Data Collection (2026–2027)

No ML implementation. Focus is raw data accumulation and characterisation.

- Log all sessions in standardised format from first light
- Characterise San Jose 1420 MHz RFI environment — time of day, day of
  week, seasonal patterns
- Identify persistent RFI sources (fixed frequency, fixed azimuth)
- Identify intermittent RFI (aircraft, occasional emitters)
- Build HI4PI comparison pipeline — automated per-pointing expected
  spectrum generation

**Deliverable:** RFI characterisation report for SARA publication and
BSc thesis site assessment chapter.

### Phase 4 — Classical Baseline (2027–2028)

Implement classical RFI mitigation as baseline for later ML comparison:

- Sigma clipping (3σ, iterative)
- Wavelet decomposition (Qin et al. 2025 methodology)
- Mathematical morphology (Qin et al. 2025 methodology)
- Reference channel subtraction (Chain A correlated excision)

Document performance metrics: false positive rate, false negative rate,
SNR improvement on known HI sources (Cas A, M31, Complex C).

**These metrics become the baseline the ML pipeline must beat.**

### Phase 5 — ML Pilot (2028–2029)

First ML implementation using accumulated Phase 3–4 data:

- Architecture: start with CNN (Akeret et al. 2017 baseline)
- Training data: 2 years of dual-chain observations with automated labels
- Validation: held-out sessions not used in training
- Compare to classical baseline from Phase 4

Consider autoencoder approach (Vos et al. 2019) if labelled data
proves insufficient — autoencoders are unsupervised.

Investigate continuous online training (MIT LL approach) — adapt
network to update weights during each session using HI4PI residual
as training signal.

**Deliverable:** ML vs classical comparison — publishable as MRes
contribution or SARA journal paper.

### Phase 6 — Interferometer Integration (2029–2031)

If KrakenSDR 5-element array is deployed, the spatial correlation
between array elements provides additional RFI discrimination. RFI
arrives from a fixed terrestrial direction; HI arrives from the sky.
ML pipeline extended to incorporate spatial correlation.

---

## Research Questions

These questions frame the investigation over the five-year programme:

1. **Characterisation:** What is the temporal and spectral structure of
   the San Jose 1420 MHz RFI environment? Are there predictable patterns
   (time of day, day of week, seasonal) that can be exploited?

2. **Reference channel utility:** How much SNR improvement does the
   dual-chain reference channel subtraction provide compared to
   single-chain classical mitigation?

3. **ML vs classical:** Does a CNN or autoencoder trained on BRRO data
   outperform classical wavelet/morphology mitigation on BRRO observations?
   By how much? Under what conditions?

4. **Online learning:** Can continuous HI4PI-guided weight updates improve
   the ML pipeline's performance over a session as it adapts to
   current RFI conditions?

5. **Transferability:** Does a model trained on San Jose 1420 MHz data
   generalise to other urban sites or frequencies? (Potential
   collaboration with other SARA members.)

---

## Relationship to Thesis

This investigation spans the full five-year programme and contributes
to multiple chapters:

| Thesis chapter | INV004 contribution |
|---|---|
| Site assessment | Phase 3 RFI characterisation |
| Instrumentation | Dual-chain architecture rationale |
| Methodology | Classical vs ML RFI mitigation comparison |
| Results | ML pipeline performance on M31, Complex C |
| Conclusions | Five-year RFI dataset as resource for community |

The longitudinal RFI dataset is itself a contribution — a five-year
characterisation of urban 1420 MHz interference from a fixed site is
not widely available in the literature and has value independent of
the ML application.

---

## Dependencies

| Dependency | Status | Notes |
|---|---|---|
| Phase 3 data collection | Begins when V4c commissioned | CAL-000 ready |
| HI4PI comparison pipeline | To develop | Python + Astropy |
| Reference channel correlation pipeline | To develop | Phase 3–4 |
| Chain A + Chain B simultaneous logging | To design | dish_sensors.py extension |
| Classical baseline implementation | Phase 4 | Qin et al. 2025 methodology |
| ML framework selection | Phase 5 | PyTorch or TensorFlow on Pi 5 |

---

## Key References

| Reference | Relevance |
|---|---|
| Qin et al. (2025) arXiv:2508.00386 | Classical baseline — wavelet + morphology |
| Akeret et al. (2017) A&C 18, 35 | CNN RFI mitigation — foundational |
| Vos et al. (2019) arXiv:1907.01546 | Autoencoder — unsupervised, no labels needed |
| Kerrigan et al. (2019) MNRAS 488, 2605 | Sparse RFI with deep learning |
| Sun et al. (2022) arXiv:2204.01482 | ML in radio astronomy — review |
| MIT LL tech transfer | Online learning architecture concept |
| Ben Bekhti et al. (2016) HI4PI | Expected signal model for training |
| BRRO_references.bib | Full bibliography with notes |

All references in `references/BRRO_references.bib`.

---

## Data Schema and Pipeline Compatibility

### Critical Requirement

The training corpus is only useful if the data format is consistent across
all five years of collection. The logging format must be finalised before
Phase 3 begins — retrofitting format changes across years of data is
expensive and error-prone.

### Design Principles

1. **Schema-first:** Define the complete data schema before writing any
   logging code. Every field needed for ML training must be present from
   session one.

2. **Both chains compatible:** Chain A (V4c, reference dipole) and Chain B
   (Airspy R2, science dish) must log in identical format with the same
   timestamp resolution. Cross-channel correlation requires aligned time axes.

3. **HI4PI lookup at session time:** The expected HI spectrum from HI4PI
   must be computed and logged for each observation pointing at the time of
   observation — not retrospectively. This requires the HI4PI lookup pipeline
   to be written and tested before Phase 3.

4. **Equipment version tagged:** Every data record must include the equipment
   version (E001, E002...) so training data from different hardware
   configurations can be separated or used appropriately.

### Minimum Required Fields Per Spectrum Record

```
timestamp_utc         : ISO 8601 — aligned across both chains
equipment_version     : E001, E002, etc.
chain                 : A (V4c/dipole) or B (Airspy R2/dish)
az_deg                : Dish azimuth (degrees)
el_deg                : Dish elevation — IMU measured (Chain B only)
el_deg_rotctl         : Dish elevation — rotctl commanded (Chain B only)
l_deg                 : Galactic longitude (derived)
b_deg                 : Galactic latitude (derived)
lst_hours             : Local sidereal time
freq_hz               : Centre frequency
bandwidth_hz          : Bandwidth
n_channels            : Number of spectral channels
spectrum_raw          : Raw power spectrum (counts or dBFS) — array
spectrum_calibrated   : Calibrated brightness temperature (K) — array
hi4pi_expected        : HI4PI expected spectrum at (l, b) — array
rfi_flag              : Per-channel boolean flag (reference channel)
session_id            : Links to session log
notes                 : Free text
```

### HI4PI Lookup Pipeline

Required before Phase 3. Inputs: (l, b, v_min, v_max). Output: expected
brightness temperature spectrum at BRRO angular resolution (~20°).

```python
# hi4pi_lookup.py — to be developed before Phase 3
# Inputs: galactic coordinates (l, b), velocity range
# Output: expected T_b spectrum from HI4PI survey
# Libraries: astropy, healpy (HI4PI uses HEALPix pixelisation)
# HI4PI data: available from CDS/Vizier as FITS files

def hi4pi_expected_spectrum(l_deg, b_deg, v_min_kms, v_max_kms):
    """
    Return expected HI brightness temperature from HI4PI at (l, b).
    Smoothed to BRRO beam (~20 arcmin) if required.
    """
    pass  # implement using healpy.get_interp_val on HI4PI FITS cube
```

### Relationship to dish_sensors.py

The `dish_sensors.py` script currently planned for Pi 2 handles
environmental and IMU data. The science chain logging (spectra) runs
on Pi 3 (Chain A) and Pi 5 (Chain B, Phase 4). All three streams must
write to a common session directory with aligned timestamps so the ML
pipeline can join them by timestamp.

Suggested session directory structure:

```
sessions/
└── 2027-09-15_M31/
    ├── session.yaml          ← metadata, equipment version, conditions
    ├── chainA_spectra.csv    ← V4c reference channel, 1 MHz resolution
    ├── chainB_spectra.csv    ← Airspy R2 science channel
    ├── sensors.csv           ← Pi 2 BME280 + LSM6DSOX
    └── hi4pi_expected.csv    ← pre-computed at session start
```

### Actions Before Phase 3

- [ ] Finalise data schema — all fields agreed before first logging session
- [ ] Write `hi4pi_lookup.py` — test against known HI4PI pointings
- [ ] Modify `dish_sensors.py` to write to shared session directory
- [ ] Write Chain A logging script (V4c → chainA_spectra.csv)
- [ ] Write Chain B logging script (Airspy R2 → chainB_spectra.csv, Phase 4)
- [ ] Write `session_init.py` — creates session directory, runs HI4PI
  lookup, writes session.yaml
- [ ] Test full pipeline on bench before first science session

---



- [ ] Identify MIT LL underlying patent or publication — find citable source
- [ ] Determine optimal spectral and temporal resolution for training data
- [ ] Design standardised session log format for ML pipeline compatibility
- [ ] Assess PyTorch vs TensorFlow for Pi 5 deployment in Phase 5
- [ ] Investigate SARA network — potential multi-site training data collaboration
- [ ] Assess compute requirements for online training — Pi 5 sufficient?
- [ ] Define success metrics for ML vs classical comparison

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1 | 2026-05-13 | Initial concept capture — MIT LL framework, dual-chain training strategy, phased implementation plan, research questions, thesis chapter mapping |
| 0.2 | 2026-05-13 | Add data schema section — minimum required fields, HI4PI lookup pipeline, session directory structure, actions before Phase 3 |
