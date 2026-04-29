# INV002 — Digital Filter Design for HI Spectroscopy Pipeline

**Observer:** Steve Hawker BEng MBA FRAS  
**Investigation ID:** INV002  
**Started:** 2026-04-28  
**Status:** Planned — target Year 2 alongside GNU Radio pipeline development  
**Target completion:** Mid Year 2 (2028)

---

## 1. Motivation

The custom GNU Radio pipeline (Phase 2 of the observing programme) requires
a series of digital filtering and signal processing stages. The design choices
for these stages — filter type, order, window function, cutoff frequencies —
directly affect sensitivity, spectral fidelity, and RFI rejection.

This investigation applies the author's professional background in digital
signal processing (DSP chip programming, digital telephony codec development,
LC and digital filter design) to make and justify these design choices from
first principles, rather than adopting defaults without understanding.

The result is a documented, analytically justified digital signal processing
chain for HI spectroscopy, with measured validation against EZRa output.

---

## 2. Background

### 2.1 Engineering Parallels

The author's background in digital telephony (G.711, G.722 codecs) provides
direct intuition for HI spectrometer design:

| Telephony | HI Spectrometer |
|---|---|
| 8 kHz sample rate, 300–3400 Hz passband | 2.4 Msps, ~2 MHz passband at 1420 MHz |
| Anti-alias filter before ADC | SAW filter before SDR ADC |
| μ-law/A-law companding for dynamic range | Gain staging LNA1→Filter→LNA2 |
| FFT for frequency domain analysis | FFT spectrometer for spectral lines |
| Codec roll-off above 3400 Hz | SAW filter roll-off outside HI band |
| DSP chip executing filter algorithms | GNU Radio executing on CPU/GPU |

The sharp roll-off rates of telephony codecs — brick-wall behaviour above
3400 Hz — are directly analogous to what the SAW filters must achieve at
1420 MHz band edges. The author's comfort with steep filter design translates
directly to understanding SAW filter specifications.

**Key lesson from telephony:** No digital processing recovers a signal once
the ADC clips. The analogue anti-alias filter is irreplaceable. The SAW filters
at Blue Rock play exactly this role.

### 2.2 Windowing Functions

FFT spectral analysis requires windowing to reduce spectral leakage — the
spreading of energy from a strong signal into adjacent frequency bins. For
HI spectroscopy where a weak line may sit adjacent to strong RFI, window
choice significantly affects detectability.

| Window | Sidelobe level | Main lobe width | Best use |
|---|---|---|---|
| Rectangular | -13 dB | Narrowest | Never — leakage too severe |
| Hann | -31 dB | Moderate | General spectroscopy |
| Blackman | -58 dB | Wider | When adjacent RFI is strong |
| Blackman-Harris | -92 dB | Widest | Extreme dynamic range situations |

For HI work, **Blackman** is the recommended starting point — the excellent
sidelobe suppression protects weak HI lines from nearby RFI at the cost of
slightly reduced spectral resolution. This matches the author's LC filter
intuition: you pay a bandwidth penalty for better selectivity.

### 2.3 FIR vs IIR for Spectral Line Work

| Parameter | FIR | IIR |
|---|---|---|
| Phase response | Linear (constant group delay) | Nonlinear |
| Computational cost | Higher (more taps needed) | Lower |
| Stability | Always stable | Can be unstable if poorly designed |
| Baseline ripple risk | Lower | Higher near band edges |

**For HI spectroscopy: FIR preferred.** The nonlinear phase of IIR filters
causes frequency-dependent group delay that distorts spectral baseline shape
near band edges. Since baseline subtraction is critical for weak line detection,
preserving flat baseline shape argues strongly for FIR linear phase response.

This is the same argument that applies in audio spectral analysis — phase
distortion makes spectral features harder to interpret correctly.

### 2.4 Frequency Switching

Frequency switching alternates the receiver between an on-line frequency
(centred on the HI line) and an off-line frequency (offset by a few MHz,
containing no HI emission). The difference between on and off spectra
removes the receiver noise baseline.

In DSP terms this is equivalent to a lock-in amplifier — the signal of
interest (HI line) appears in the difference, while correlated noise
(baseline ripple, gain variations) cancels. The author's experience with
signal detection in the presence of correlated noise provides direct
intuition here.

Implementation in GNU Radio: two alternating centre frequencies, switched
at regular intervals (typically 1–10 seconds), with difference taken in
post-processing.

---

## 3. Pipeline Design

### 3.1 Proposed signal processing chain

```
SDR IQ samples
    ↓
[1] Digital bandpass filter (FIR, Blackman window)
    ↓
[2] FFT spectrometer (configurable size, Blackman window)
    ↓
[3] Spectral averaging (N frames)
    ↓
[4] RFI flagging (threshold-based, see INV003)
    ↓
[5] Frequency switching difference
    ↓
[6] Polynomial baseline subtraction
    ↓
[7] Doppler correction to LSR (Astropy)
    ↓
[8] Write to FITS file with full header
```

### 3.2 Design parameters to determine

| Parameter | Design choice | Justification |
|---|---|---|
| FIR filter taps | TBD | Roll-off vs computation tradeoff |
| FFT size | TBD | Velocity resolution vs sensitivity |
| Window function | Blackman (provisional) | Sidelobe suppression for RFI rejection |
| Averaging time | TBD | Balance between time resolution and sensitivity |
| Frequency switch interval | TBD | Balance between baseline removal and observing efficiency |
| Baseline polynomial order | TBD | Low enough to not absorb broad HI features |

### 3.3 Spectral resolution requirement

Target velocity resolution: 1 km/s at 1420 MHz.

$$\Delta f = \frac{f_{HI} \times \Delta v}{c} = \frac{1420.405 \times 10^6 \times 1000}{3 \times 10^8} \approx 4.7 \text{ kHz}$$

Required FFT bin width: ≤ 4.7 kHz.  
For sample rate fs = 2.4 MHz: FFT size N ≥ fs / Δf = 2.4×10⁶ / 4700 ≈ 511.  
Round up to next power of 2: **N = 1024 minimum.**

Larger FFT (N = 4096 or 8192) gives finer resolution — useful for resolving
M31 double-horn profile structure.

---

## 4. Experimental Method

### 4.1 Validation against EZRa

The custom pipeline will be validated by:
1. Observing the same target simultaneously with EZRa and custom pipeline
2. Comparing integrated spectra — peak position, width, flux
3. Documenting any systematic differences and their causes
4. Iterating pipeline design until agreement is within measurement uncertainty

### 4.2 Window function comparison

Observe a session with known RFI present. Process same data with:
- Hann window
- Blackman window
- Blackman-Harris window

Compare HI line detectability and RFI rejection. Document which window
performs best for Blue Rock RFI environment specifically.

### 4.3 FIR filter order optimisation

Model the FIR filter frequency response as a function of tap count.
Measure computational cost on the Blue Rock computing platform.
Find minimum tap count that achieves required stopband rejection.

---

## 5. Results

*To be populated during Year 2.*

---

## 6. Conclusions

*To be completed at investigation close.*

---

## 7. References

- Lyons — *Understanding Digital Signal Processing* (filter design chapters)
- Harris 1978 — "On the use of windows for harmonic analysis with the DFT" *Proc. IEEE*
- GNU Radio documentation — filter design tools
- SciPy signal processing documentation — scipy.signal
- Thompson, Moran & Swenson — *Interferometry and Synthesis in Radio Astronomy*
  Ch. 8 (digital signal processing for radio astronomy)

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-28 | Initial investigation plan |
