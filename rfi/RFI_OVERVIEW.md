# RFI Characterisation — Blue Rock Radio Observatory

**Observer:** Steve Hawker BEng MBA FRAS  
**Site:** Blue Rock Court, San Jose, California, USA (37.3382°N, 121.8863°W)  
**Started:** 2026-04-28  

---

## Purpose

This directory contains systematic characterisation of the radio frequency
interference environment at 1420 MHz from the Blue Rock Radio Observatory site.
RFI characterisation is both a scientific contribution in its own right and a
necessary foundation for all HI science programmes conducted at this site.

A well-documented RFI environment analysis from an urban California site is
directly useful to the amateur radio astronomy community and forms a methodology
chapter in the BSc thesis.

---

## Background

The 1420.405 MHz hydrogen line band has statutory protection under ITU Radio
Regulations — passive use only is permitted in the band 1400–1427 MHz. However,
statutory protection does not prevent interference from:

- Spurious emissions from nearby transmitters
- Intermodulation products from strong adjacent signals
- Harmonics of lower frequency transmitters
- Local oscillator leakage from consumer electronics
- Industrial, scientific and medical (ISM) equipment

San Jose is a dense urban environment with significant commercial, industrial,
and residential RF activity. Characterising this environment systematically is
essential for understanding data quality and developing effective flagging strategies.

---

## RFI Classification

### By persistence
| Class | Definition | Impact |
|---|---|---|
| Persistent | Present >90% of observations | Must flag or accept as noise floor elevation |
| Intermittent | Present 10–90% of observations | Requires time-domain flagging |
| Transient | Present <10% of observations | Spike flagging sufficient |

### By origin
| Class | Examples | Typical character |
|---|---|---|
| Fixed local | WiFi harmonics, cable TV leakage | Persistent, stable frequency |
| Mobile | Aircraft radar, vehicle ignition | Transient, may be Doppler shifted |
| Scheduled | Industrial equipment, timed transmitters | Intermittent, time-correlated |
| Impulsive | Electrical switching, lightning | Broadband, transient |

---

## Vulnerability Analysis

The SAW filters provide the primary hardware RFI defence. However, signals
within the filter passband or strong enough to cause ADC saturation or LNA
compression require additional mitigation.

### ADC saturation risk
If strong out-of-band signals are not sufficiently attenuated by the SAW filters
before reaching the SDR ADC, the ADC saturates and produces intermodulation
distortion products throughout the passband. No digital processing can recover
from ADC saturation — the information is irretrievably lost.

**This is the critical failure mode.** Monitoring for ADC saturation is a
priority during commissioning.

### LNA compression risk
Strong signals at or near 1420 MHz can drive LNA1 into compression, reducing
gain and introducing nonlinearity. The P1dB (1dB compression point) of the
QPL9547 should be noted from the datasheet and compared against expected
signal levels.

### Alias frequencies
With SDR sample rate fs, signals at 1420.405 ± fs/2 MHz alias directly into
the centre of the band. At fs = 2.4 Msps, vulnerability frequencies are:
- 1420.405 - 1.2 = **1419.205 MHz**
- 1420.405 + 1.2 = **1421.605 MHz**

Check ITU frequency allocation tables for known users at these frequencies.
Update this section with findings.

---

## Measurement Methodology

### Equipment
- Full Blue Rock signal chain (see current equipment log version)
- SDR in wideband mode — maximum available bandwidth
- GQRX or GNU Radio wideband capture flowgraph

### Observation schedule
RFI surveys should be conducted at:
- Weekday 09:00–10:00 local (business hours peak)
- Weekday 13:00–14:00 local (business hours midday)
- Weekday 22:00–23:00 local (night minimum)
- Weekend 10:00–11:00 local (weekend daytime)
- Weekend 02:00–03:00 local (weekend night minimum)

Each survey: minimum 30 minutes continuous wideband recording.
Waterfall plot saved as PNG. Power spectral density saved as CSV.

### Seasonal coverage
Conduct full survey set at:
- Winter (December–February)
- Spring (March–May)
- Summer (June–August)
- Autumn (September–November)

---

## File Naming Convention

```
rfi/
├── README.md                          ← this file
├── surveys/
│   ├── YYYY-MM-DD_HHMM_survey.md     ← survey session log
│   ├── YYYY-MM-DD_HHMM_waterfall.png ← waterfall image
│   └── YYYY-MM-DD_HHMM_psd.csv      ← power spectral density data
├── persistent_sources.md              ← catalogue of identified persistent RFI
├── flagging_strategy.md               ← developed flagging approach
└── SURVEY_TEMPLATE.md                 ← copy this for each new survey
```

---

## Persistent RFI Sources Log

*To be populated as sources are identified. Update persistent_sources.md.*

| Frequency (MHz) | Bandwidth | Class | Suspected source | First seen | Notes |
|---|---|---|---|---|---|
| | | | | | |

---

## Flagging Strategy

*To be developed during Year 1 based on survey results. Document in flagging_strategy.md.*

Current approach: manual inspection of waterfall plots.
Target approach: automated flagging in GNU Radio / Python pipeline.

---

## References

- ITU Radio Regulations, Article 5 — frequency allocations
- Ofcom/FCC spectrum assignment databases — check for licensed users near 1420 MHz
- Thompson, Moran & Swenson — *Interferometry and Synthesis in Radio Astronomy* Ch. 16 (RFI)
- SARA Journal — RFI mitigation articles (search archive)
