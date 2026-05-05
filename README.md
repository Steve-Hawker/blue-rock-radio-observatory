# Blue Rock Radio Observatory

**HI Observation Log**

![Blue Rock Radio Observatory Target Map](branding/BRRO_target_map.svg)

**Observer:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory, Blue Rock Court, San Jose, California, USA  
**Latitude:** 37.3382° N  
**Longitude:** -121.8863° W  
**Elevation:** ~25m ASL  
**Programme start:** 2026-04-30  
**Repository:** https://github.com/Steve-Hawker/blue-rock-radio-observatory

---

## Observer

Steve Hawker BEng MBA FRAS  
BSc Honours Astronomy (Distance Learning), University of Lancashire  
Fellow of the Royal Astronomical Society (FRAS)  
Member, Society of Amateur Radio Astronomers (SARA)  
Member, San Jose Astronomical Association (SJAA)

*Blue Rock Radio Observatory is located on Blue Rock Court, San Jose, California.*

---

## Programme Purpose

Systematic hydrogen line (HI, 1420.405 MHz) observing programme in support
of BSc Honours thesis and potential MRes research. Central motivation: develop
and validate techniques for low-cost, small-aperture HI spectroscopy from an
urban site, producing scientifically meaningful results comparable with
professional survey data.

---

## Equipment Summary

- **Antenna:** 70cm Discovery Dish parabolic dish, AZ/EL tracking mount
- **Mount:** Discovery Drive — WiFi controlled, 0–90° elevation, rotctl compatible
- **Signal chain:** Feed (LNA1 QPL9547 → SAW Filter → LNA2 → SAW Filter) → SDR
- **Chain A (RFI monitoring):** RTL-SDR Blog V4c + dipole antenna
- **Chain B (Science):** Airspy R2 + Discovery Dish HI Feed
- **Enclosure:** QILIPSU 304 stainless steel IP65 350×250×150mm — replaces KrakenRF DDOEE
- **Target frequency:** 1420.405 MHz (hydrogen line)
- **Software:** EZRa (Phase 1) / GNU Radio (Phase 2)

Full equipment details in `equipment/` directory.

---

## Primary Targets

| Target | Type | Priority | Transit El | Best season |
|---|---|---|---|---|
| Cas A | SNR / calibrator | Primary | 68.5° | Year-round |
| M31 | Spiral galaxy | Primary science | 86.1° | Sep — Jan |
| Complex C | High-velocity cloud | Primary science | 72.3° | Year-round |
| M1 | Pulsar wind nebula | Secondary / calibrator | 74.7° | Oct — Feb |
| M33 | Spiral galaxy | Secondary | 83.3° | Sep — Jan |
| M81 | Spiral galaxy | Stretch goal | 58.3° | Year-round |

---

## Repository Structure

```
blue-rock-radio-observatory/
│
├── README.md                        ← this file
├── RESEARCH_PLAN.md                 ← full programme plan 2026–2031
├── LEARNING_PLAN.md                 ← structured self-study programme
├── TOOLS_PLAN.md                    ← tools roles and workflow
├── QUICK_REFERENCE.md               ← pre/post session checklists
├── .gitignore                       ← excluded files
│
├── equipment/                       ← versioned equipment state records
│   ├── E001_2026-04-30.md          ← initial system — hardware on order
│   └── datasheets/                  ← component datasheets and product docs
│       ├── README_DATASHEETS.md     ← index with key extracted values
│       ├── QPL9547_Data_Sheet.pdf
│       ├── RTLSDR_V4_Datasheet_V_1_0.pdf
│       ├── Discovery_Dish_CrowdSupply.pdf
│       ├── RTL-SDR_Dipole_Set_eBay.pdf
│       ├── ADF4351_board_eBay.pdf
│       └── SMA_attenuator_30dB_eBay.pdf
│
├── sessions/                        ← per-observation session logs
│   └── SESSION_TEMPLATE.md
│
├── calibration/                     ← calibration time series data
│   ├── CasA_timeseries.csv
│   └── ADF4351_timeseries.csv       ← annual system calibration record
│
├── targets/                         ← reference data for each target
│   ├── CasA.md
│   ├── ComplexC_HVC.md
│   ├── M1_CrabNebula.md
│   ├── M31.md
│   ├── M33.md
│   └── M81.md
│
├── rfi/                             ← RFI environment characterisation
│   ├── RFI_OVERVIEW.md
│   └── SURVEY_TEMPLATE.md
│
├── design/                          ← engineering design decisions and rationale
│   ├── diagrams/                    ← system architecture diagrams
│   │   ├── BRRO_system_architecture_v5.svg
│   │   ├── BRRO_system_architecture_v5.mermaid
│   │   └── DDOEE_mounting_plate_v2.svg  ← two-Pi layout, Phase 2–3
│   ├── ADC_BIT_RESOLUTION.md
│   ├── ADF4351_CALIBRATION.md       ← signal source calibration procedures v1.1
│   ├── BEAM_AND_RESOLUTION.md
│   ├── DAILY_OBSERVING_WINDOWS.md
│   ├── DIPOLE_ANTENNA_DESIGN.md
│   ├── DOWNCONVERSION_ARCHITECTURE.md
│   ├── DUAL_SDR_ARCHITECTURE.md
│   ├── GALACTIC_PLANE_TRACKING.md
│   ├── INTERFEROMETER_UPGRADE.md   ← v0.2 KrakenSDR 5-element array
│   ├── OBSERVING_STRATEGY.md
│   ├── POWER_ARCHITECTURE.md       ← PoE power distribution, dual budget (Pi3+2 / Pi5)
│   ├── SAW_FILTER_DESIGN.md        ← v0.1 pending KrakenRF response
│   └── SDR_SELECTION.md
│
├── investigations/                  ← system performance investigations
│   ├── INVESTIGATIONS.md
│   ├── INV001_noise_budget/
│   │   └── INV001_noise_budget.md
│   ├── INV002_digital_filters/
│   │   └── INV002_digital_filters.md
│   └── INV003_rfi_flagging/
│       └── INV003_rfi_flagging.md
│
├── writing/                         ← thesis drafts and chapter outlines
│   ├── M1_VECTOR_ANALYSIS.md
│   ├── SITE_ASSESSMENT_CHAPTER_OUTLINE.md
│   └── SITE_ASSESSMENT_METHODOLOGY.md  ← v0.1 for SARA publication
│
├── reading_notes/                   ← notes on papers and books read
│   ├── README_READING_NOTES.md
│   └── NOTES_TEMPLATE.md
│
├── build/                           ← construction journal and photos
│   ├── BUILD_JOURNAL.md
│   └── photos/
│
├── calendar/                        ← observing window calendar files
│   └── BRRO_observing_windows_202609_202701.ics
│
├── scripts/                         ← Python utility scripts
│   ├── target_visibility.py         ← transit elevations and availability
│   ├── generate_calendar.py         ← generate .ics observing windows
│   └── galactic_plane_track.py      ← Galactic plane coordinate transforms
│
├── branding/                        ← visual identity
│   ├── BRRO_target_map.svg          ← full annotated target map
│   ├── BRRO_target_map_badge.svg    ← minimal badge version
│   ├── LOGO_DESIGN_BRIEF.md
│   └── LOGO_DESIGN_BRIEF.html       ← self-contained with embedded SVGs
│
└── setup/                           ← hardware and software setup guides
    ├── RASPBERRY_PI_SETUP.md
    └── SITE_ASSESSMENT_CHECKLIST.md ← field measurement checklist
```

---

## Equipment Log Versioning

Every change to the signal chain creates a new equipment version (E001, E002...).
Session logs reference the equipment version in effect at time of observation.

## Time Standard

All times in UTC. LST recorded at session start.

## Calibration Standard

Cassiopeia A — primary flux calibration standard.
Reference flux: 2723 Jy at 1420 MHz (J2000, Baars et al. 1977).
Secular decrease: 0.77% per year.
Expected 2026: ~2567 Jy.
