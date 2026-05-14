# Hardware Design Documentation

## Overview

This directory contains the hardware design notes for the Discovery Dish radio astronomy installation. The system is a portable, demountable remote sensing enclosure housing SDR receivers, compute nodes, and environmental sensors, powered via a single PoE ethernet cable from an indoor infrastructure point.

The primary science goal is 21cm neutral hydrogen (HI) line observation at 1420.405 MHz from an urban environment (San Jose, CA). The design philosophy throughout is to maximise signal integrity and RF cleanliness while maintaining a portable, daily-use installation.

These documents represent design intent and rationale as of the pre-build phase. They should be updated as the build progresses and actual measurements replace estimates.

---

## System Summary

### Science Goals
- HI line observation at 1420.405 MHz
- Targets: M31, M33, M81, Cas A, Complex C, Milky Way galactic plane
- Long integration times — contaminated data flagged and excised rather than avoided
- Urban RF environment characterised and managed rather than assumed unworkable
- Long term: 5-dish KrakenSDR interferometer array

### Hardware Overview
| Component | Role |
|-----------|------|
| Discovery Dish + rotator | Primary science antenna, steerable |
| Airspy R2 | Science SDR receiver (1420MHz HI) |
| RTL-SDR Blog V4c | RFI reference receiver (1420MHz monitor) |
| Reference dipole | RFI reference antenna |
| Raspberry Pi 5 | Primary science compute |
| Raspberry Pi 3 | RFI reference pipeline |
| Raspberry Pi 2 | Environmental sensor management |
| BME280 (×2) | Environmental monitoring (enclosure + field) |
| IMU | Dish orientation tracking |
| Tycon POE-SPLT-BT-UNI-P | PoE splitter, 12V output |
| DC-DC 12V→5V (50W) | Pi cluster and SDR power — dkplnt DN510 |
| Discovery Drive | 12V direct from Tycon output |

### Enclosure
- **Outer:** QILIPSU 304 Stainless Steel IP65, 14"×10"×6" (355×254×152mm external)
- **Mounting plate:** 315×200mm galvanised steel (supplied with enclosure)
- **SDR shield:** Southwire 4"×2"×1-7/8" steel handy box (junction box)
- **Power:** Single Cat6 F/UTP shielded stranded outdoor cable, PoE++

---

## Document Index

### [ENCLOSURE_DESIGN.md](ENCLOSURE_DESIGN.md)
**Start here for the physical build.**

Covers the outer enclosure (QILIPSU specification and fit), internal mounting plate layout, SDR junction box construction, cable gland selection, grounding and bonding strategy, build sequence, and maintenance schedule.

Key decisions documented:
- QILIPSU 304 SS IP65 14"×10"×6" selected and specified
- Southwire handy box as SDR Faraday shield — dual purpose (shields SDRs from Pi 5 noise, shields USB noise from RF path)
- Component layout rationale — Pi cluster above, junction box below, thermal stack design
- 20-step build sequence — order matters, junction box must be closed before plate assembly

Open items: verify depth stack on arrival, tripod mounting method, Pi 5 heatsink selection.

---

### [RF_DESIGN.md](RF_DESIGN.md)
**Read before making any RF or shielding decisions.**

Covers RF signal path philosophy (direct SMA connections, no adapters), shielding strategy against Pi 5 noise, slot and gap control at 1420MHz (λ/20 = ~10mm), USB cable EMI management, ferrite choke specification, grounding architecture, and the RFI reference channel rationale.

Key decisions documented:
- Direct antenna-to-SDR SMA connection — no bulkhead connectors, no adapters
- Junction box lid faces upward toward Pi 5 — most critical shielding face
- Copper tape sealed lid joint — conductive adhesive type mandatory
- Cable egress wrapped in copper foil — converts weak point to shielded conduit
- Type 31 ferrite material specified — correct frequency range for 1420MHz

Open items: USB isolator selection, USB data line grounding verification on Pi 5.

---

### [HEAT_DESIGN.md](HEAT_DESIGN.md)
**Read before selecting thermal interface materials or finalising component placement.**

Covers the complete passive thermal chain from SDR cases to ambient air, thermal interface material selection (Shore hardness explained, brand recommendations), thermal monitoring via BME280, condensation risk management, San Jose climate considerations, and Raspberry Pi heatsink strategy.

Key decisions documented:
- Active cooling rejected — no large penetrations in sealed enclosure
- Passive thermal chain: SDR → thermal pad → junction box → thermal compound → plate → copper braid → stainless enclosure → ambient
- Stainless steel identified as weakest thermal link (~16 W/mK) — copper braid straps essential
- QILIPSU bonding studs used as copper braid attachment points
- BME280 inside junction box — monitors SDR thermals and condensation risk
- Total heat load: ~26W continuous

Open items: measure actual SDR-to-box-wall gap for thermal pad sizing, bench test Pi 5 under load, Pi 5 heatsink decision.

---

### [POWER_ARCHITECTURE.md](POWER_ARCHITECTURE.md)
**Read before purchasing power components or calculating cable sizing.**

Covers the complete PoE power architecture, power budget (23.75W at 5V + ~10W at 12V = ~38W total PoE draw), Tycon splitter configuration (set to **12V**), DN510 DC-DC converter specification (12V→5V, 50W, arrived 2026-05-13), voltage drop calculation for 22ft Cat6 run, Discovery Drive 12V supply (direct from Tycon — no second DC-DC required), and internal power distribution.

Key decisions documented:
- Single Cat6 cable carries both PoE power and ethernet data
- Tycon set to **12V output** — Discovery Drive powered direct from 12V
- DN510 DC-DC (12V→5V, 50W) — >2× margin on 5V loads
- 802.3bt PoE++ required at injector — TP-Link Omada PoE++ selected
- 24V architecture considered and rejected — single DC-DC simpler and adequate

---

### [I2C_DESIGN.md](I2C_DESIGN.md)
**Read before purchasing sensors, cables, or breakout boards.**

Covers I2C bus architecture (Standard mode 100kHz recommended for inter-enclosure run), capacitance budget (~90-110pF estimated vs 400pF limit), device address map (two BME280s at 0x76 and 0x77), pull-up resistor strategy, Qwiic daisy chain considerations, cable pair assignment, shield termination, and Python code examples including dew point calculation.

Key decisions documented:
- Belden 8102 or equivalent — 12.5pF/ft low capacitance shielded twisted pair
- BME280 #1 inside junction box (0x76) — SDR thermal monitoring
- BME280 #2 at remote dish location (0x77) — field environmental monitoring
- Shield grounded at Pi end only — prevents ground loops
- Standard mode (100kHz) recommended — most forgiving for inter-enclosure run

Open items: confirm IMU device selection and address, verify Qwiic pull-up situation, select BME280 breakout boards.

---

### [CABLE_DESIGN.md](CABLE_DESIGN.md)
**Read before purchasing any cables, conduit, or connectors.**

Covers the primary Cat6 cable specification (F/UTP stranded outdoor UV rated — Veeloon confirmed), conduit system design (white Schedule 40 PVC 3/4", dry fit, sweep elbows), conduit assembly method (slide fittings onto cable, assemble around cable), I2C inter-enclosure cable specification, USB cable specification (USB 2.0 mandatory for SDRs), ferrite choke specification and sourcing, connector specifications, and full bill of materials.

Key decisions documented:
- Cat6 F/UTP stranded — **Veeloon Cat6 FTP OFC Outdoor** identified and confirmed
- Stranded mandatory — daily coil/uncoil over 5-year design life
- White Schedule 40 PVC — WAF approved, available at big box stores
- Dry fit assembly only — no solvent cement
- Assembly method: slide all fittings onto cable first, assemble conduit around cable
- USB 2.0 for SDRs — USB 3.0 harmonics fall on 1420MHz
- Type 31 ferrite from Fair-Rite, Wurth, or TDK — not generic Amazon ferrites

Open items: measure cable ODs for gland sizing, confirm conduit section lengths from patio survey, USB isolator compatibility testing.

---

## Design Dependencies

Some decisions in one document depend on decisions in another. Key dependencies:

```
POWER_DESIGN
    └── Discovery Drive 12V UNRESOLVED
            └── affects internal layout in ENCLOSURE_DESIGN

ENCLOSURE_DESIGN
    └── depth stack verification (on arrival)
            └── affects Pi 5 heatsink choice in HEAT_DESIGN

HEAT_DESIGN
    └── SDR-to-box gap measurement (physical)
            └── affects thermal pad specification

I2C_DESIGN
    └── IMU device selection (TBD)
            └── affects address map and Qwiic chain in I2C_DESIGN

CABLE_DESIGN
    └── actual cable OD measurements (physical)
            └── affects gland sizing in ENCLOSURE_DESIGN
```

---

## Documents Not Yet Written

| Document | Content |
|----------|---------|
| SENSOR_DESIGN.md | Full sensor architecture, IMU selection, data schema |
| RFI_PIPELINE.md | Software RFI mitigation, wavelet/morphology pipeline, reference channel flagging |
| TARGETS.md | Observation targets, integration time estimates, expected flux densities |
| OBS_PROCEDURE.md | Session setup/teardown procedure, calibration routine |
| BENCH_TEST.md | Pre-deployment test procedures and acceptance criteria |

---

## Key References

| Reference | Relevance |
|-----------|-----------|
| Qin et al. (2025) arXiv:2508.00386 | RFI mitigation methodology — wavelet transform + mathematical morphology |
| Marr, Snell & Kurtz — Fundamentals of Radio Astronomy Vol 1 & 2 | Primary textbook reference |
| Fair-Rite Type 31 datasheet | Ferrite choke material specification |
| Belden 8102 datasheet | I2C cable capacitance specification |
| QILIPSU product drawing | Enclosure internal dimensions — verify on arrival |
| Airspy R2 documentation | SDR specifications |
| RTL-SDR Blog V4c documentation | SDR specifications |
| KrakenSDR documentation | Long-term interferometer reference |

---

## Build Status

| Item | Status |
|------|--------|
| Enclosure selected | ✅ QILIPSU 304 SS IP65 14"×10"×6" — ordered 2026-05-11 |
| Mounting plate | ✅ Supplied with enclosure |
| Primary cable selected | ✅ Veeloon Cat6 FTP OFC Outdoor — to order |
| SDR junction box | ✅ Southwire handy box — confirmed 2026-05-13 |
| SDRs | ✅ Airspy R2 (Phase 4) + RTL-SDR V4c (arrived 2026-05-11) |
| Raspberry Pi cluster | ✅ Pi 5 (Phase 4) + Pi 3 + Pi 2 |
| PoE splitter | ✅ Tycon POE-SPLT-BT-UNI-P — to order; set to 12V |
| DC-DC 12V→5V | ✅ dkplnt DN510 50W — arrived 2026-05-13 |
| Discovery Drive 12V supply | ✅ Direct from Tycon 12V output — no second DC-DC required |
| PoE injector | ✅ TP-Link Omada PoE++ — arrived 2026-05-10 |
| BME280 inside junction box | ✅ Confirmed 2026-05-13 — address 0x76 |
| BME280 at dish location | ✅ Adafruit breakout ordered 2026-05-08 — address 0x77 |
| IMU at dish location | ✅ Adafruit LSM6DSOX ordered 2026-05-08 |
| USB isolators | ❌ Not yet specified |
| Ferrite chokes | ❌ Not yet sourced (Type 31 specified) |
| Thermal pads | ❌ Gap not yet measured |
| Copper braid straps | ❌ Not yet sourced |
| Conduit and fittings | ❌ Not yet purchased |
| I2C cable | ❌ Belden 8102 or equivalent — not yet purchased |

---

*Document status: Pre-build*
*Last updated: May 2026*
*See parent README.md for project overview and research context*
