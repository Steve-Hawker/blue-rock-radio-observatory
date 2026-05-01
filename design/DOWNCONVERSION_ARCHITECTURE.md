# Downconversion Architecture — Design Limitations and Mitigations

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-04-30  
**Version:** 1.0  

---

## Overview

This document analyses the downconversion architecture used in the Blue Rock
Observatory SDR receivers (RTL-SDR V4 and Airspy R2), identifies the design
limitations inherent in direct conversion (zero-IF) architecture, and
documents the hardware and software mitigations applied to manage these
limitations for HI spectroscopy.

Understanding these limitations is essential for correct interpretation of
spectral data and for designing the GNU Radio pipeline (INV002).

---

## Architecture — Direct Conversion (Zero-IF)

Both the RTL-SDR V4 and Airspy R2 use **direct conversion** (also called
zero-IF or homodyne) architecture. This differs fundamentally from the
traditional superheterodyne (IF-based) architecture used in professional
radio astronomy receivers.

### Direct conversion signal path

```
Antenna signal at 1420 MHz
        ↓
HI Feed: LNA1 (QPL9547) → SAW Filter 1 → LNA2 → SAW Filter 2
        ↓
SDR input at 1420 MHz
        ↓
Quadrature mixer — multiplied by local oscillator (LO) at ~1420 MHz
        ↓
I channel (in-phase) and Q channel (quadrature, 90° offset)
        ↓
Low-pass filter — removes sum frequency (~2840 MHz)
        ↓
ADC — samples I and Q at 2–10 Msps
        ↓
Complex baseband IQ signal (DC to ±sample_rate/2)
```

The local oscillator runs at or near the signal frequency. Mixing produces
sum (rejected by low-pass filter) and difference (retained) frequencies.
The difference signal is the RF signal shifted to near DC — baseband.

The IQ output preserves both amplitude and phase information from the
original RF signal, enabling full spectral analysis of a bandwidth
equal to the sample rate.

### Comparison with superheterodyne architecture

Professional radio astronomy receivers typically use superheterodyne
architecture — converting the RF signal to a fixed intermediate frequency
(IF) before final detection:

```
RF at 1420 MHz → RF preselector → Mixer → IF at ~100 MHz → IF filter → Detector
```

| Parameter | Direct conversion | Superheterodyne |
|---|---|---|
| DC offset problem | Yes — significant | No — signal away from DC |
| Image rejection | At baseband only | At RF — easier to filter |
| IF selectivity | Digital (flexible) | Analogue crystal/SAW (sharp) |
| Even-order distortion | More susceptible | Less susceptible |
| Complexity | Lower — fewer stages | Higher — IF strip required |
| Cost | Lower | Higher |
| Dynamic range | Lower (historically) | Higher (historically) |
| Reconfigurability | High — digital | Low — fixed IF filters |
| Used in | Consumer SDRs | Professional receivers |

Professional receivers at Effelsberg, Parkes, and the VLA use superhet
architecture for its superior dynamic range and image rejection. The Blue
Rock SDRs use direct conversion — a known design compromise accepted in
exchange for low cost and flexibility.

---

## Design Limitations

### Limitation 1 — DC Offset

**Mechanism:**
The local oscillator signal leaks back through the mixer to its own
input and mixes with itself, producing a large DC component (0 Hz) at
the baseband output. This is an unavoidable consequence of direct
conversion architecture.

**Manifestation:**
A large spike appears at exactly the centre of the spectrum display —
the tuned frequency. The DC offset corrupts a band of frequencies
around the exact LO frequency, typically ±10–50 kHz depending on the
device and temperature.

**Impact on HI observations:**
If the SDR LO is tuned to exactly 1420.405 MHz (the HI rest frequency),
the DC spike sits directly on top of the HI line. The HI signal is
undetectable in that channel.

**Severity:** High without mitigation. Negligible with LO offset tuning.

---

### Limitation 2 — IQ Imbalance

**Mechanism:**
The I and Q channels should be exactly 90° apart in phase with identical
gain. Manufacturing tolerances produce amplitude and phase errors between
the two channels — typically 0.1–1° phase error and 0.1–1 dB amplitude
imbalance in consumer SDRs.

**Manifestation:**
IQ imbalance causes imperfect image rejection. A signal at frequency
+f MHz from the LO produces a ghost image at -f MHz. The image is
typically 30–40 dB below the true signal in uncorrected hardware.

**Impact on HI observations:**
The HI line itself produces a weak ghost image — at 30–40 dB below the
true line this is negligible. More concerning is the image of a strong
nearby RFI source appearing as a spurious spectral feature in the HI
band. A strong RFI signal 30 dB above the noise at +2 MHz from the LO
could produce an image at -2 MHz that sits above the noise floor.

**Severity:** Moderate. Manageable with software IQ correction.

---

### Limitation 3 — LO Phase Noise

**Mechanism:**
No oscillator is perfectly stable. Phase noise represents rapid random
frequency fluctuations of the LO, appearing as a noise pedestal around
the carrier that falls off with distance from the centre frequency.

**Manifestation:**
Raised noise floor close to the centre frequency, decreasing with
increasing offset. Strong signals close to the centre frequency spread
into adjacent channels.

**Impact on HI observations:**
At 1420 MHz with a 1 PPM TCXO (V4) or 0.5 PPM TCXO (Airspy R2):

$$\Delta f = f \times \text{stability} = 1420 \times 10^6 \times 10^{-6} = 1420 \text{ Hz} \approx 0.3 \text{ km/s}$$

Frequency stability is adequate for HI velocity resolution requirements.
The phase noise skirt is more concerning for detecting weak spectral
features close to strong RFI signals.

**Severity:** Low with TCXO. Manageable.

---

### Limitation 4 — Even-Order Intermodulation Distortion

**Mechanism:**
Direct conversion mixers are particularly susceptible to even-order
intermodulation distortion (IMD2). Two strong signals at frequencies
f1 and f2 produce distortion products at f1-f2, which can be near or
at DC — directly in the baseband passband.

For two signals at 1418 MHz and 1422 MHz (both within the HI feed
passband), the IMD2 product falls at 4 MHz — in baseband but away
from the HI line. For signals at 1420 MHz and 1420.5 MHz, the product
falls at 500 kHz — potentially overlapping the HI line.

**Manifestation:**
Spurious spectral features at difference frequencies of strong in-band
signals. These can be time-varying if the RFI sources are intermittent,
making them difficult to identify and flag.

**Impact on HI observations:**
Primarily a concern when multiple strong RFI signals are present within
the SAW filter passband simultaneously. The SAW filters reject
out-of-band signals, reducing but not eliminating IMD2 from the
strongest in-band sources.

**Severity:** Moderate in urban RFI environment. Mitigated primarily
by SAW filters.

---

### Limitation 5 — Mixer Noise Contribution

**Mechanism:**
The downconversion mixer adds noise during the conversion process.
Active mixers in SDR chips have a noise figure contribution, appearing
in the Friis cascade as an additional noise stage.

**Impact on system temperature:**
In the Friis cascade the mixer appears after the feed LNA chain
with ~30–40 dB of preceding gain. Per Friis:

$$F_{mixer\_contribution} = \frac{F_{mixer} - 1}{G_{LNA1} \cdot G_{F1} \cdot G_{LNA2} \cdot G_{F2}}$$

With 30 dB (factor of 1000) of preceding gain, even a mixer with
5 dB noise figure contributes only 5/1000 = 0.005 dB to the total
system noise figure — completely negligible.

**Severity:** Negligible. No mitigation required.

---

## Mitigations

### Hardware Mitigations

#### M1 — LO Offset Tuning (DC Offset)

**Method:** Tune the SDR LO to a frequency offset from the HI line,
so the HI line appears away from DC in the baseband spectrum.

**Recommended setting:**
- LO frequency: 1422.000 MHz
- HI rest frequency appears at: 1420.405 - 1422.000 = **-1.595 MHz** in baseband
- M31 HI (blueshifted ~300 km/s): appears at approximately **-1.595 + 1.42 = -0.175 MHz**
  — still clear of DC

The full M31 velocity range (-570 to -30 km/s) in frequency:
- At -570 km/s: Δf = 1420.405 × 570/299792 = +2.70 MHz → baseband: +2.70 - 1.595 = +1.10 MHz
- At -30 km/s: Δf = 1420.405 × 30/299792 = +0.142 MHz → baseband: +0.142 - 1.595 = -1.45 MHz

Full M31 profile spans approximately **-1.45 to +1.10 MHz** in baseband
at LO = 1422 MHz. Well clear of DC. Passband easily accommodated.

EZRa applies this offset automatically. GNU Radio flowgraph must be
configured with the correct LO offset — document in session log.

#### M2 — SAW Filter Chain (Even-Order Distortion, IQ Imbalance)

The SAW filter chain (Filter 1 and Filter 2) in the HI feed rejects
out-of-band signals before they reach the SDR mixer. This is the
primary hardware mitigation for even-order distortion — by preventing
strong out-of-band signals from reaching the mixer, the amplitude of
potential IMD2 products is dramatically reduced.

The SAW filters also reduce the signal amplitude range arriving at the
mixer, reducing the probability of operating in the non-linear region
where distortion products are generated.

Full SAW filter analysis: see SAW_FILTER_DESIGN.md (to be created).

#### M3 — High Quality TCXO (Phase Noise)

Both selected SDRs include temperature-compensated crystal oscillators:
- RTL-SDR V4: 1 PPM TCXO
- Airspy R2: 0.5 PPM TCXO

These provide adequate LO stability for HI spectroscopy. No additional
hardware mitigation required for phase noise.

---

### Software Mitigations

#### S1 — DC Spike Removal

**Method:** Subtract a running average of the DC component from each
spectrum before integration.

**Implementation:**
- EZRa: handles automatically
- GNU Radio: DC blocker block (`dc_blocker_xx`) — configure with
  appropriate time constant
- Python post-processing: subtract mean of line-free channels from
  each spectrum

**Effectiveness:** Removes the DC spike but leaves residual noise in
channels near DC. Combined with LO offset tuning (M1), the DC spike
is moved away from the HI line and DC removal cleans up any residual.

#### S2 — IQ Correction

**Method:** Measure IQ amplitude and phase imbalance using a stable
reference signal, then apply correction coefficients to subsequent data.

**Implementation in GNU Radio:**
```python
# IQ correction block
iq_correct = gr.hier_block2(...)
# Measure imbalance from known tone
# Apply amplitude and phase correction matrices
```

Several GNU Radio out-of-tree modules implement IQ correction. The
DC auto-correction in the Airspy R2 driver also helps.

**Effectiveness:** Improves image rejection from ~30–40 dB (uncorrected)
to ~60+ dB (corrected). Reduces spurious RFI images significantly.

**Commissioning procedure:**
1. Tune to 1422 MHz LO
2. Inject a known stable tone at 1421 MHz (or use a strong stable
   RFI source of known frequency)
3. Measure apparent image at 1423 MHz
4. Calculate correction coefficients
5. Apply correction and verify image suppression
6. Document coefficients in equipment log

#### S3 — Frequency Switching (DC Offset, Baseline)

**Method:** Alternate between on-line (HI line in band) and off-line
(HI line out of band) frequencies. Subtract off-line from on-line.

The DC offset is identical in both switched states — it cancels in
the subtraction. This inherently removes DC offset without requiring
explicit DC removal, and simultaneously removes the receiver noise
baseline.

**Implementation:** EZRa implements frequency switching automatically.
GNU Radio Phase 2 pipeline must implement frequency switching explicitly
— see INV002_digital_filters.

**Effectiveness:** DC offset cancellation is effectively complete.
Also removes LO phase noise contribution near DC that survives DC
blocking. Frequency switching is the most effective single mitigation
for direct conversion artefacts in HI spectroscopy.

#### S4 — Notch Filtering

**Method:** Apply narrow digital notch filters at known RFI frequencies
that produce persistent distortion products.

**Implementation:**
```python
from scipy import signal
# Design notch filter at known IMD2 product frequency
b, a = signal.iirnotch(f_notch, Q=30, fs=sample_rate)
filtered = signal.filtfilt(b, a, spectrum)
```

**When to apply:** Only when specific persistent distortion products
are identified in the RFI survey data (rfi/). Do not apply blindly —
notch filters also remove any genuine signal at the notched frequency.
Document each notch filter applied in session logs.

#### S5 — RFI Flagging (All Distortion Effects)

Distortion products from strong RFI are intermittent when the RFI
source is intermittent. Time-domain flagging of corrupted samples
before spectral averaging removes distortion events that are not
persistent enough to address with notch filtering.

See INV003_rfi_flagging for flagging algorithm development.

---

## Mitigation Priority and Effectiveness Summary

| Limitation | Severity | Primary mitigation | Secondary mitigation | Residual impact |
|---|---|---|---|---|
| DC offset | High | M1 — LO offset tuning | S1 — DC removal, S3 — freq switching | Negligible |
| IQ imbalance | Moderate | S2 — IQ correction | M2 — SAW filters (reduce RFI images) | Low |
| LO phase noise | Low | M3 — TCXO | S3 — freq switching | Negligible |
| Even-order IMD | Moderate | M2 — SAW filters | S4 — notch filtering, S5 — flagging | Low–moderate |
| Mixer noise | Negligible | None needed | — | Negligible |

---

## Implications for GNU Radio Pipeline Design

The INV002 digital filter pipeline must implement the following in order:

```
IQ samples from SDR (LO at 1422 MHz)
        ↓
[S2] IQ correction — amplitude and phase imbalance correction
        ↓
[S1] DC blocker — remove residual DC component
        ↓
[S3] Frequency switching — on/off line alternation and subtraction
        ↓
Digital bandpass filter (see INV002)
        ↓
FFT spectrometer
        ↓
[S4] Notch filters (if required from RFI survey)
        ↓
[S5] RFI flagging
        ↓
Spectral averaging and integration
        ↓
Doppler correction to LSR
        ↓
FITS output
```

The ordering matters — IQ correction and DC removal must precede the
FFT to avoid spreading artefacts across the spectrum.

---

## Comparison with Professional Receiver Mitigation

Professional radio astronomy receivers address these same problems
differently:

| Problem | Amateur (direct conversion) | Professional (superhet) |
|---|---|---|
| DC offset | LO offset + freq switching | No DC offset — signal at IF |
| IQ imbalance | Software correction | Single-channel IF — no IQ |
| Phase noise | TCXO, freq switching | Cryogenic LO, cavity oscillators |
| Even-order IMD | SAW filters + software | Bandpass preselector + high IP2 mixer |

The professional approach eliminates most problems at hardware level.
The amateur approach manages them at software level. Both produce
science-quality data with appropriate methodology — but the amateur
approach requires more careful commissioning, characterisation, and
pipeline design.

This is a legitimate thesis contribution: demonstrating that direct
conversion architecture with appropriate software mitigation is
viable for HI spectroscopy from an urban site.

---

## References

- Razavi 1997 — "Design considerations for direct-conversion receivers"
  *IEEE Transactions on Circuits and Systems II* 44(6)
- Wilson, Rohlfs & Hüttemeister — *Tools of Radio Astronomy* Ch. 4
  (receiver systems)
- GNU Radio documentation — DC blocker, IQ correction blocks
- INV002_digital_filters — pipeline design (this repository)
- INV003_rfi_flagging — flagging algorithm (this repository)
- SAW_FILTER_DESIGN.md — SAW filter analysis (this repository,
  to be created)

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-30 | Initial document — direct conversion limitations, hardware and software mitigations, pipeline implications |
