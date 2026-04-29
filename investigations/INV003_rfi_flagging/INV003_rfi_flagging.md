# INV003 — RFI Flagging Algorithm Development and Validation

**Observer:** Steve Hawker BEng MBA FRAS  
**Investigation ID:** INV003  
**Started:** 2026-04-28  
**Status:** Planned — begins with RFI survey data from Year 1  
**Target completion:** Year 2 (2028)

---

## 1. Motivation

San Jose is a challenging urban RFI environment. Unmitigated RFI entering
the HI band will corrupt spectra, inflate noise, and in severe cases make
observations unusable. A robust, automated RFI flagging pipeline is essential
for producing science-quality data from Blue Rock Radio Observatory.

This investigation develops and validates an automated flagging algorithm
tailored to the specific RFI environment characterised in the rfi/ directory.
The algorithm will be integrated into the custom GNU Radio pipeline (INV002).

---

## 2. Background

### 2.1 RFI Flagging Strategies

**Threshold flagging** — flag any sample or channel exceeding a threshold
above the local noise floor. Simple and effective for impulsive RFI.
Risk: setting threshold too low flags genuine astronomical signals;
too high misses faint RFI.

**Median absolute deviation (MAD)** — more robust than simple standard
deviation for setting thresholds in the presence of non-Gaussian noise.
Standard approach in professional radio astronomy pipelines (used in CASA,
AOFlagger). Recommended starting point.

**Time-frequency flagging** — flag in both time and frequency dimensions
simultaneously. A feature that is narrow in frequency but extended in time
is likely RFI (a transmitter). A feature that is extended in frequency but
brief in time is likely broadband impulsive RFI. A genuine HI spectral line
is narrow in frequency and persistent in time — the opposite signature from
most RFI.

**AOFlagger algorithm** — the professional standard, developed for LOFAR
and used widely. Based on the SumThreshold method. Complex to implement
from scratch but worth studying as a reference.

**Known frequency masking** — maintain a list of known RFI frequencies
identified from the rfi/ survey programme and mask those channels in every
observation regardless of instantaneous power. Simple and effective for
persistent narrowband RFI.

### 2.2 The Flagging Tradeoff

Aggressive flagging removes more RFI but also removes more good data,
reducing effective integration time and sensitivity. Conservative flagging
preserves more data but allows RFI contamination.

The optimum flagging strategy minimises total noise in the final spectrum —
this is not simply "flag everything suspicious" but a genuine optimisation
problem. The author's engineering background in signal detection theory
(threshold detection, ROC curves) provides relevant intuition.

### 2.3 Frequency Switching as RFI Mitigation

Frequency switching (see INV002) provides inherent RFI rejection for
persistent narrowband RFI that appears in both on-line and off-line spectra —
it cancels in the difference. This is a powerful first line of defence.

RFI that appears only in the on-line band, or that varies between switch
cycles, will not cancel and requires explicit flagging.

---

## 3. Algorithm Design

### 3.1 Proposed flagging pipeline

```
Raw spectrum
    ↓
[1] Known frequency mask (from rfi/persistent_sources.md)
    ↓
[2] MAD-based threshold flagging (per channel, per time sample)
    ↓
[3] Time-frequency consistency check
    (flag channels that are intermittently bright — RFI signature)
    ↓
[4] Interpolation over flagged channels
    (for narrow flags only — wide flags leave gap)
    ↓
[5] Flag fraction check
    (if >X% of spectrum flagged, reject entire integration)
    ↓
Cleaned spectrum
```

### 3.2 Parameters to determine from RFI survey data

- MAD threshold multiplier (typically 3–5σ)
- Minimum flag width (channels)
- Maximum interpolatable gap width (channels)
- Session rejection threshold (% flagged)

These parameters will be tuned using RFI survey data from the rfi/ directory
to minimise false positive rate while achieving adequate RFI rejection.

---

## 4. Experimental Method

### 4.1 Algorithm development

1. Apply candidate algorithm to RFI survey datasets (known RFI content)
2. Manually inspect flagged vs unflagged data
3. Measure false positive rate (good data incorrectly flagged)
4. Measure false negative rate (RFI incorrectly passed)
5. Iterate algorithm parameters to optimise

### 4.2 Validation on astronomical data

1. Apply algorithm to M31 and Cas A observations
2. Compare flagged vs unflagged integrated spectra
3. Verify HI line is not being flagged (it has the wrong signature for RFI)
4. Measure improvement in spectral RMS after flagging

### 4.3 Comparison with manual flagging

Manually flag a subset of observations by visual inspection of waterfall plots.
Compare manual flags with algorithm flags. Disagreements reveal algorithm
failure modes.

---

## 5. Results

*To be populated as algorithm is developed and tested.*

---

## 6. Conclusions

*To be completed at investigation close.*

---

## 7. References

- Offringa et al. 2012 — "A morphological algorithm for improving radio-frequency
  interference detection" *A&A* 539, A95 (AOFlagger paper)
- Offringa et al. 2010 — "Post-correlation radio frequency interference
  classification methods" *MNRAS* 405, 155
- CASA documentation — flagging chapter
- rfi/RFI_OVERVIEW.md — Blue Rock RFI characterisation (this repository)
- INV002_digital_filters.md — Digital filter pipeline (this repository)

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-28 | Initial investigation plan |
