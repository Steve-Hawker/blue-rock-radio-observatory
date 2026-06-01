# ADF4351 Signal Source — Calibration Design

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-02  
**Version:** 1.3  

---

## Hardware Status — 2026-05-29

| Item | Status |
|---|---|
| ADF4351 board | Arrived 2026-05-10 ✓ |
| RTL-SDR V4c | Arrived 2026-05-11 ✓ |
| 30 dB SMA attenuator | Arrived 2026-05-06 ✓ |
| **CAL-000 (V4c baseline)** | **READY TO PROCEED** |
| Airspy R2 | Deferred — Phase 4 |
| CAL-001 through CAL-004 | Pending — requires HI feed (due Aug 2026) |
| SPI software for ADF4351 | **To develop** — see scripts/adf4351_control.py |

---

## Overview

This document describes the use of an ADF4351 wideband PLL synthesiser
module as a calibration signal source for the Blue Rock Radio Observatory
signal chain. The ADF4351 covers 35 MHz to 4.4 GHz, comfortably spanning
the 1380–1460 MHz HI feed passband and the 1422 MHz LO operating frequency.

### What the ADF4351 can measure

The ADF4351 is injected at the **accessible coax output of the HI feed**
(after LNA1, SAW1, LNA2, SAW2) or directly at the **SDR input** (no feed).
It cannot be injected before the LNA chain — the QPL9547 LNAs and SAW
filters are sealed inside the feed enclosure at the focal point.

| Calibration | Accessible? | Method |
|---|---|---|
| SDR LO frequency accuracy | ✓ | ADF4351 → SDR direct (CAL-000) |
| SDR IQ imbalance | ✓ | ADF4351 → SDR direct (CAL-000, CAL-004) |
| SDR dynamic range | ✓ | ADF4351 → SDR direct (CAL-000) |
| SDR wideband response | ✓ | ADF4351 → SDR direct (CAL-000) |
| Feed output to SDR response | ✓ | ADF4351 → feed coax output → SDR (CAL-002 partial) |
| SAW filter passband shape | ✗ | Cannot inject before SAW filters — use sky survey comparison |
| Full chain gain (LNA + SAW + SDR) | ✗ | Cannot inject before LNA1 — use Cas A Y-factor |
| Absolute flux scale | ✗ | Use Cas A Y-factor (NIST-traceable via Baars 1977) |

### Absolute calibration — Cas A as primary standard

For parameters not accessible to the ADF4351, Cas A provides the
primary calibration reference. Cas A is the radio astronomy community's
primary flux calibration standard, anchored to absolute measurements by
Baars et al. (1977) — the closest equivalent to NIST traceability
available in radio astronomy.

| What | How | Reference |
|---|---|---|
| Absolute flux scale | Cas A Y-factor measurement | Baars et al. 1977 |
| System temperature (Tsys) | Derived from Cas A flux and Y-factor | Baars et al. 1977 |
| SEFD | Derived from Tsys and dish geometry | Baars et al. 1977 |
| Feed passband shape | Comparison with HI4PI all-sky survey | HI4PI (Ben Bekhti et al. 2016) |
| LNA gain consistency | Cas A Tsys consistent with Friis prediction? | INV001 noise budget |

The ADF4351 complements Cas A calibration — it handles SDR
characterisation and annual consistency checks. Cas A handles
everything requiring an absolute reference.

### Attenuation note

Only a 30 dB SMA attenuator is available (Gwave, DC-8GHz, arrived
2026-05-06). The original procedures specified 20 dB for SDR-only
connections. 30 dB is more conservative — reduces ADF4351 output
further below SDR input limits. This is safe and acceptable for all
procedures. No 20 dB attenuator is required.

---

## Hardware

### ADF4351 module

| Parameter | Value |
|---|---|
| Frequency range | 35 MHz — 4.4 GHz |
| Output power | Approximately 0 to -4 dBm (register adjustable) |
| Reference oscillator | 25 MHz TCXO (onboard) |
| Reference accuracy | ~10 ppm (onboard crystal) |
| Interface | SPI (controllable via USB dongle or Arduino) |
| Supply voltage | 5V USB |
| Cost | ~$25 |

### Required accessories

| Item | Purpose | Cost |
|---|---|---|
| SMA attenuator kit | Protect LNA from overdrive | ~$15 |
| SMA cables (15–30cm) | Bench connections | ~$10 |
| USB SPI controller or Arduino | ADF4351 frequency control | ~$10 |
| **Total** | | **~$60** |

### Optional upgrade — GPSDO reference

The onboard 25 MHz crystal reference provides ~10 ppm accuracy. At
1422 MHz, 10 ppm = 14.2 kHz frequency uncertainty = 3.0 km/s velocity
uncertainty. This is marginal for LO frequency verification.

A GPS-disciplined oscillator (GPSDO) reference improves accuracy to
~10 ppb — frequency uncertainty of 14 Hz at 1422 MHz = 0.003 km/s.
Recommended after Phase 1 commissioning if LO frequency verification
proves important.

| Option | Accuracy at 1422 MHz | Velocity equiv. | Cost |
|---|---|---|---|
| Onboard crystal | ~14.2 kHz | ~3.0 km/s | Included |
| GPSDO reference | ~14 Hz | ~0.003 km/s | ~$50–100 |
| Rubidium standard | ~1.4 Hz | ~0.0003 km/s | ~$200+ |

**Decision point:** After first LO frequency check with onboard crystal,
assess whether accuracy is sufficient for programme requirements.

---

## Safety — SDR Input Protection

**For CAL-000 (SDR direct connection, no feed):**

The V4c SDR input should not receive more than approximately -10 dBm
without risk of ADC saturation or damage. With ADF4351 at ~0 dBm and
the 30 dB attenuator in line, the SDR receives ~-30 dBm — well within
safe limits.

**Always verify the 30 dB attenuator is connected before powering
the ADF4351.** Note in session log.

**For CAL-001 through CAL-004 (feed coax output → SDR):**

When connecting to the feed coax output (after LNA1 + SAW1 + LNA2 +
SAW2), the signal has already passed through ~40 dB of gain. Do NOT
inject the ADF4351 into this point — it would overdrive the SDR
severely. The feed coax output connects only to the SDR input as
its intended destination.

**LNA protection note (informational):**
The QPL9547 LNA P1dB is approximately +17 dBm. Since the LNA input
is physically inaccessible (sealed in feed enclosure), inadvertent
injection before the LNA is not possible in normal operation. This
risk only arises if the feed enclosure is opened for servicing.

---

## Injection Points

**Physical reality of the BRRO signal chain:**

The HI feed is a sealed enclosure containing LNA1 (QPL9547), SAW1
(TA1077A), LNA2 (QPL9547), and SAW2 (TA2494A). The only external
connection points are:

- **Feed input** (before LNA1) — physically inside sealed enclosure,
  inaccessible without opening the feed. **Not available for injection.**
- **Feed coax output** (after SAW2) — the LMR240 coax that runs from
  the feed to the DDOEE. This is the accessible signal chain point.
- **SDR SMA input** — directly accessible on the V4c and Airspy R2.

### Accessible injection points

**Point B — SDR SMA input (no feed connected):**
Used for: CAL-000 SDR characterisation.
Configuration: ADF4351 → 30 dB attenuator → SDR SMA input directly.
Tests: SDR alone — frequency accuracy, IQ balance, dynamic range,
wideband response. Independent of feed and LNA chain.

**Point C — Feed coax output (feed connected, between feed and SDR):**
Used for: CAL-001 LO verification (with feed in circuit), future
consistency checks.
Configuration: Disconnect feed coax from SDR. Connect ADF4351 →
30 dB attenuator → SDR SMA input (feed disconnected). This tests
the SDR in its operating configuration without the feed signal.

**Note:** True end-to-end signal chain characterisation (LNA + SAW
+ SDR combined) requires an astronomical source — specifically Cas A.
See Absolute Calibration section above.

---

## Calibration Procedures

### CAL-000 — SDR Baseline (pre-feed, SDR only)

**Purpose:** Characterise each SDR independently before connection to
the HI feed or dipole. Establishes baseline frequency accuracy, dynamic
range, and IQ imbalance figures for the SDR alone — independent of the
feed and LNA chain. Enables direct comparison between V4c (Chain A)
and Airspy R2 (Chain B).

This procedure can be performed as soon as each SDR arrives — no feed,
no LNA, no dish required.

**Configuration:**
```
ADF4351 → 30 dB attenuator → SDR SMA input (no feed)
```

**Step 1 — LO frequency accuracy:**
- Open GQRX, set centre frequency to 1422.000 MHz
- Set ADF4351 to 1421.000 MHz
- Observe tone in baseband — should appear at -1.000 MHz offset
- Measure actual tone frequency to nearest 100 Hz
- Calculate LO error: error = (measured offset + 1.000 MHz)
- Calculate velocity equivalent: Δv = (Δf / 1,420,405,752) × 299,792 km/s
- Record in ADF4351_timeseries.csv

**Acceptance criterion:** LO error < 1 kHz (< 0.21 km/s velocity error)

**Step 2 — Wideband response:**
- Step ADF4351 from 1360 to 1480 MHz in 2 MHz steps
- Record SDR power at each step (read from GQRX)
- This reveals SDR's own frequency-dependent gain variation —
  independent of SAW filters; establishes the SDR contribution
  to the system passband

**Step 3 — IQ imbalance:**
- Set ADF4351 to 1422.500 MHz (LO + 500 kHz)
- Measure true tone amplitude at +500 kHz offset in GQRX
- Measure image tone amplitude at -500 kHz offset
- Record image rejection ratio (IRR) = true tone − image (dB)

**Step 4 — Dynamic range check:**
- Set ADF4351 to 1420.000 MHz
- Increase SDR gain until tone just saturates ADC
- Note maximum useful gain setting
- Record recommended operating gain for HI observations

**Record all results in calibration/ADF4351_timeseries.csv:**
- equipment_version: E001
- cal_procedure: CAL-000-V4c (or CAL-000-Airspy when Airspy arrives)

**Comparison value:** Running CAL-000 on both SDRs with identical
setup gives a direct hardware comparison — V4c vs Airspy R2 frequency
accuracy, IQ balance, and dynamic range.

**Frequency:** Once on SDR arrival, annually thereafter, and after
any SDR firmware update or replacement.

---

### CAL-002 — Passband Shape Measurement

**Purpose:** Characterise the combined passband shape of the signal
chain from feed output to SDR. Note: the SAW filter cascade is inside
the sealed feed enclosure — this procedure measures the feed output
response, not the raw SAW filter response in isolation.

**What this measures:** Passband shape as seen at the SDR input when
the feed is connected — includes any frequency-dependent loss in the
LMR240 coax cable run from feed to DDOEE. This is the operationally
relevant passband for science observations.

**What this cannot measure:** The SAW filter response in isolation
(requires injection before LNA1, which is inaccessible). The SAW
passband shape can alternatively be inferred by:
- Comparing observed sky spectrum with HI4PI expected spectrum
- Using the SAW filter datasheets (TA1077A, TA2494A) for the theoretical
  shape — pending KrakenRF confirmation

**Configuration:**
```
Sky (feed connected) → LMR240 → SDR
```
Then for ADF4351 passband sweep, disconnect feed and inject:
```
ADF4351 → 30 dB attenuator → SDR SMA input
```
This gives the SDR-only passband. Subtracting from the sky measurement
gives an estimate of the feed + cable contribution.

**Procedure:**
1. With feed connected: record noise floor power spectrum across
   1360–1480 MHz — this is the system response including feed
2. Disconnect feed coax from SDR
3. Connect ADF4351 → 30 dB attenuator → SDR SMA input
4. Step ADF4351 from 1360 MHz to 1480 MHz in 1 MHz steps
5. At each frequency: record SDR power, wait 2 seconds, step
6. Normalise — subtract mean power across flat region
7. Save plot and raw data to calibration/ directory
8. Compare with HI4PI sky comparison (when first light achieved)

**Frequency:** Once during commissioning, then annually

---

### CAL-003 — Gain Chain Verification

**Purpose:** Verify the signal chain is behaving consistently with
the Friis prediction from INV001. Since direct injection before LNA1
is not possible, this procedure uses two complementary approaches.

**Approach A — SDR gain measurement (ADF4351):**
Measures the SDR gain and response at the feed coax output connection
point. Confirms the SDR is operating correctly in the chain.

Configuration:
```
ADF4351 → 30 dB attenuator → SDR SMA input
```
1. Set ADF4351 to 1420.000 MHz at known register power setting
2. Record SDR signal level (dBFS)
3. Calculate: SDR_gain = SDR_level(dBFS) − ADF4351_power(dBm) + 30 dB
4. Record and track across sessions — consistency is the goal

**Approach B — Full chain gain via Cas A (primary method):**
The total system gain (LNA + SAW + cable + SDR) is derived from the
Cas A Y-factor measurement. When Tsys is measured from Cas A, the
total chain noise figure is implicitly validated against the Friis
prediction. Discrepancy between measured Tsys and Friis prediction
indicates either a gain chain problem or a noise figure problem.

See calibration/CAS_A_CALIBRATION.md (to be written before first light).

**Frequency:** During commissioning, then annually

---

### CAL-004 — IQ Imbalance Measurement

**Purpose:** Quantify IQ amplitude and phase imbalance to derive
correction coefficients for GNU Radio pipeline.

**Configuration:**
```
ADF4351 → 30 dB attenuator → SDR SMA input (no feed)
```

**Procedure:**
1. Open GQRX, set centre frequency to 1422.000 MHz
2. Set ADF4351 to 1422.500 MHz (LO + 500 kHz)
3. In a perfect IQ system: single tone appears at +500 kHz in baseband
4. Measure true tone amplitude: A_true (dBFS)
5. Measure image tone amplitude at -500 kHz: A_image (dBFS)
6. IQ image rejection ratio (IRR) = A_true − A_image (dB)
7. Apply IQ correction in GNU Radio and repeat — verify improvement
8. Record IRR before and after correction in ADF4351_timeseries.csv

**Typical values:**
- Uncorrected V4c: IRR ~30–35 dB
- Uncorrected Airspy R2: IRR ~35–40 dB
- After software correction: IRR ~55–65 dB

**Acceptance criterion:** IRR > 50 dB after correction  
**Frequency:** During commissioning, then after any SDR firmware update

---

### CAL-005 — Annual Comparative Calibration

**Purpose:** Track system performance over the five-year programme.
Detect gradual degradation before it affects science data.

**Procedure:** Run CAL-001 through CAL-004 in sequence. Record all
results in ADF4351_timeseries.csv with date and equipment version.

**Timing:** Start of each M31 observing season (September each year)

**What to look for:**
- LO frequency drift between seasons
- Passband shape changes (connector degradation, LNA aging)
- Gain chain changes (LNA gain drift, cable loss changes)
- IQ imbalance changes (SDR chip aging)

Any parameter changing by more than 1 dB between seasons warrants
investigation before the season's science observations begin.

---

## Python Automation Script

`scripts/adf4351_control.py` — to be developed before CAL-000.

Requirements derived from calibration procedures:
- Set a single frequency (for steps 1, 3, 4 of CAL-000)
- Step through a frequency range with dwell time (for CAL-000 step 2,
  CAL-002 passband sweep)
- Interactive mode — prompt user before each step for GQRX reading
- Log frequency and timestamp to CSV for automated sweeps

SPI connection method (Pi GPIO vs USB-SPI adapter) to be confirmed
from ADF4351 board pinout on arrival inspection.

See OPEN_ITEMS.md — ADF4351 SPI library research.

---

## Relationship to Other Calibration Methods

| Method | What it measures | Accessible? | Frequency |
|---|---|---|---|
| ADF4351 CAL-000 | SDR frequency accuracy, IQ balance, dynamic range, wideband response | ✓ Now | SDR arrival + annual |
| ADF4351 CAL-002 | SDR passband shape; partial feed+cable response | ✓ With feed | Commissioning + annual |
| ADF4351 CAL-003A | SDR gain at operating point | ✓ Now | Annual |
| ADF4351 CAL-004 | SDR IQ imbalance | ✓ Now | Commissioning + firmware updates |
| Cas A Y-factor | Tsys, SEFD, absolute flux scale, full chain gain | ✓ After first light | Every session |
| HI4PI comparison | Feed passband shape (inferred), integrated flux validation | ✓ After first light | Per target, per season |
| ADF4351 CAL-005 | Annual consistency check across all ADF4351 procedures | ✓ Annual | Start of M31 season |

---

## References

- Analog Devices ADF4351 datasheet — frequency synthesiser specifications
- SAW_FILTER_DESIGN.md — passband measurement context (this repository)
- DOWNCONVERSION_ARCHITECTURE.md — IQ imbalance mitigation (this repository)
- INV001_noise_budget — Friis gain chain (this repository)
- INV002_digital_filters — automation script development (this repository)
- Laufer — *The Hobbyist's Guide to the RTL-SDR* — filter measurement
  with low cost equipment

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-02 | Initial document — four calibration procedures, hardware specification, LNA protection requirements, annual programme |
| 1.1 | 2026-05-02 | Add CAL-000 SDR baseline — pre-feed V4c characterisation, direct V4c vs Airspy R2 comparison |
| 1.2 | 2026-05-13 | Add hardware status table — ADF4351 + V4c + attenuator all in hand; CAL-000 ready to proceed |
| 1.3 | 2026-05-29 | Major revision — reflect physical reality of sealed feed enclosure; LNA input inaccessible; injection points rewritten; absolute calibration via Cas A documented as primary method for full chain; CAL-002 reframed; CAL-003 dual approach (ADF4351 for SDR + Cas A for full chain); CAL-004 corrected; 30dB attenuator confirmed sufficient; calibration methods table updated; Python script requirements updated |
