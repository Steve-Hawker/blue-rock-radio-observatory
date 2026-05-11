# Power Architecture — Blue Rock Radio Observatory

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-04  
**Version:** 2.0  

---

## Overview

This document describes the power distribution architecture for the
Blue Rock Radio Observatory DDOEE (Discovery Outdoor Electronics
Enclosure) mounted on the tripod. A single Power over Ethernet (PoE)
cable runs from the house to the DDOEE, carrying both network data
and power. Inside the DDOEE, a PoE splitter distributes regulated
12V to the Discovery Drive and to a DC-DC converter which provides
5V to all computing components.

---

## Enclosure

**QILIPSU 304 Stainless Steel Electrical Box** replaces the KrakenRF DDOEE.

| Parameter | QILIPSU | KrakenRF DDOEE |
|---|---|---|
| External dimensions | 350 × 250 × 150mm | ~350 × 220 × 80mm |
| Internal volume | ~310 × 205 × 120mm | 304 × 184 × 60mm |
| Shell material | 304 stainless steel | Die-cast aluminium |
| Internal DIN plate | Galvanised steel · 315 × 200mm · DIN compatible | Custom aluminium plate |
| Base plate | Galvanised steel | — |
| IP rating | IP65 | IP65 |
| Lock | Key lock included | Screws |
| Cable entry | Bottom access panel + gasket | Cable glands |
| Price | ~$90 | ~$165 |
| **Verdict** | **Selected — larger, cheaper, lockable** | Not selected |

**Material note:** The QILIPSU shell is 304 stainless steel. The
internal DIN mounting plate and removable base plate are galvanised
steel. Drilling for cable glands is into the galvanised base plate
only — not the stainless shell. Apply Rust-Oleum cold galvanising
compound to all cut edges after drilling to maintain corrosion protection.

**WiFi note:** The Discovery Drive mounts on the tripod mast above the
enclosure — it is not inside the enclosure. WiFi signal is unobstructed.

---

## Selected Components

| Component | Role | Location | Status |
|---|---|---|---|
| TP-Link Omada PoE++ | PoE injector — 802.3bt | Indoors, cable head | Arrived 2026-05-10 |
| Tycon POE-SPLT-BT-UNI-P | PoE splitter — 12V selected | DDOEE (outdoors) | To order |
| dkplnt DN510 | 12V→5V DC-DC converter — 50W 10A | DDOEE (outdoors) | Ordered 2026-05-08 |
| CAT6 outdoor ethernet cable | Data + power to DDOEE | House to tripod | To order (30ft × 2) |

### Why these components

**TP-Link Omada PoE++:** 802.3bt rated — output wattage to be confirmed
from datasheet on arrival. Replaces TL-POE170S (deprecated 2026-05-08).
Indoor unit, appropriate for house installation.

**Tycon POE-SPLT-BT-UNI-P:** Industrial grade, -40°C to +75°C
operating temperature — essential for outdoor DDOEE in San Jose
summer where internal enclosure temperature could exceed +40°C.
VDC output is **selectable — one voltage at a time, set to 12V**.
DIN mount metal housing.

**Important:** The Tycon splitter does NOT simultaneously output 5V
and 12V. The selector switch sets ONE output voltage. A separate
DC-DC converter generates the 5V rail from the 12V output.

**dkplnt DN510 — 12V→5V DC-DC converter:**

| Parameter | Value |
|---|---|
| Part number | DN510 |
| Input voltage | 11–35V DC |
| Output voltage | 5V ±1.5% |
| Output current | 10A max |
| Output power | 50W max |
| Efficiency | 95% typical |
| Ripple and noise | 50 mVp-p typical |
| Protections | Over-voltage, over-current, over-temperature, short circuit |
| Case material | Aluminium |
| Dimensions | 74 × 40 × 17.5mm |
| Mounting | Surface mount — 4 corner holes |
| Input connection | Screw terminals — crimped ferrules required |
| Price | $9.99 |

---

## Mounting Strategy

All components mount to the galvanised steel DIN plate (~315 × 200mm)
via rivet nuts (rivnuts). No DIN rail required.

### Component mounting methods

**Tycon POE-SPLT-BT-UNI-P:**
Fabricate right-angle aluminium bracket (25×25×2mm angle, ~$2).
Use DIN mount bracket as drilling jig to mark hole positions.
Bolt bracket to plate via rivnuts, attach Tycon to bracket.

**dkplnt DN510:**
Four corner holes — M3 or M4 rivnuts in plate, bolts through
converter feet. Aluminium case in thermal contact with plate.

**Raspberry Pi 2 / Pi 3:**
M2.5 standoffs into rivnuts, stacked above plate.

**DUOPURUI ethernet switch:**
Velcro or small L-bracket on top of Tycon.

**Airspy R2 / RTL-SDR V4c:**
Velcro or cable bracket. Position for short SMA coax runs.

**ADF4351:**
Rivnuts and bolts, close to Pi GPIO.

**EPLZON stripboard (power distribution):**
25mm standoffs over DN510, rivnuts into plate.

---

## PoE Standard Analysis

| Standard | Port budget | After cable loss | Verdict |
|---|---|---|---|
| 802.3af (PoE) | 15.4W | ~12.5W | Insufficient |
| 802.3at (PoE+) | 30W | ~24.5W | Marginal |
| **802.3bt T3 (PoE++)** | **60W** | **~52W** | **Selected ✓** |
| 802.3bt T4 (PoE++) | 100W | ~90W | Over-specced |

---

## Cable Gland Plan

**Bottom removable galvanised base plate — 4 penetrations, drilled on bench with HSS step drill:**

| Position | Type | Size | Contents |
|---|---|---|---|
| 1 | Gland | 3/4" (19mm) | Cat6 PoE ethernet only — separated from all other cables |
| 2 | Gland | 3/4" (19mm) | 12V DC to Discovery Drive + Cat6 sensor cable (RJ45s removed; individual pairs used for I2C to Hammond box) |
| 3 | Vent | TBD | IP65 membrane vent + anti-insect mesh — check if included with QILIPSU |
| 4 | Gland | 3/4" (19mm) | RF: HI feed coax (LMR240 ~6mm OD) + dipole coax (RG174 ~2.8mm OD) |

**Notes:**
- RF cables in own dedicated gland — maximum separation from power and data
- Cat6 sensor cable uses twisted pairs for I2C noise rejection; spare pairs available for future use
- Apply cold galvanising compound to all drilled edges
- Seal cables in glands with neutral-cure RTV silicone

---

## 5V Power Distribution

Power from DN510 5V output distributed via custom stripboard:

- 6× Cermant USB-C breakout boards (20-pack, $8.99) soldered to EPLZON stripboard
- Wired directly to 5V/GND rail from DN510 screw terminal output
- Mounts on 25mm standoffs above DN510, bolted via rivnuts
- Full rail current available at each socket

### USB-C power socket allocation

| Socket | Device | Cable |
|---|---|---|
| 1 | Raspberry Pi 2 | Anker USB-C to USB-C |
| 2 | Raspberry Pi 3 | Anker USB-C to USB-C |
| 3 | Raspberry Pi 5 (Phase 4) | Anker USB-C to USB-C |
| 4 | DUOPURUI ethernet switch | Included with switch |
| 5 | Spare | — |
| 6 | Spare | — |

---

## Grounding

**Internal star point:** Brass or copper lug bonded to QILIPSU enclosure
wall (use existing ground lug). All internal ground connections tie to
this single point — no daisy-chaining. AWG 12 (2.5mm²) minimum for
ground bonds.

**External earth:** Not required for safety at these power levels —
earth path provided via house wiring through indoor PoE injector.
Reassess after first RFI survey if noise floor improvement needed.

---

## System Diagram

```
Router / network (indoors)
        |
        | standard ethernet
        |
TP-Link Omada PoE++ (indoors)
        |
        | CAT6 outdoor ethernet (data + PoE power)
        | [single cable to DDOEE — 30ft]
        |
Tycon POE-SPLT-BT-UNI-P (inside DDOEE) — set to 12V
        |                    |
        | RJ45 data          | 12V DC
        |                    |
  DUOPURUI switch      Discovery Drive (12V direct)
        |               dkplnt DN510 DC-DC converter
    Pi 2 ethernet               |
    Pi 3 ethernet           5V rail (DN510 output)
    Pi 5 ethernet               |
                        ┌───────┼───────┬───────┬───────┐
                        Pi 2   Pi 3    Pi 5   DUOPURUI  Spare×2
                      (USB-C) (USB-C) (USB-C) (USB-C)
```

---

## Power Budget — Phase 1–3 (Pi 2 + Pi 3, no Pi 5)

| Component | Rail | Current | Power | Notes |
|---|---|---|---|---|
| Discovery Drive | 12V | ~975 mA | **11.70W** | Dominant load · spin-up spike |
| Raspberry Pi 3 | 5V | ~1000 mA | **5.00W** | 7.5W peak |
| Raspberry Pi 2 | 5V | ~600 mA | **3.00W** | |
| RTL-SDR V4c | 5V | ~300 mA | **1.50W** | Includes dipole bias tee |
| ADF4351 RF source | 5V | ~250 mA | **1.25W** | Calibration only — intermittent |
| HI Feed LNA | 5V | ~100 mA | **0.50W** | Via Airspy R2 bias tee |
| DUOPURUI switch | 5V | ~200 mA | **1.00W** | |
| **Steady-state total** | | | **23.95W** | |
| **Peak (spin-up + Pi burst)** | | | **~32W** | |
| **Recommended supply** | | | **≥40W** | 25% headroom |
| **Omada PoE++ available** | | | **TBC** | Confirm from datasheet |

**5V rail:** ~12.25W steady-state  
**12V rail:** ~11.70W steady-state  

---

## Power Budget — Phase 4 (Pi 2 + Pi 3 + Pi 5)

*Pi 5 is an addition in Phase 4. Pi 2 and Pi 3 remain throughout all phases.*

| Component | Rail | Current | Power | Notes |
|---|---|---|---|---|
| Discovery Drive | 12V | ~975 mA | **11.70W** | Unchanged |
| Raspberry Pi 5 | 5V | ~2500 mA | **12.50W** | Science chain — Phase 4 addition |
| Raspberry Pi 3 | 5V | ~1000 mA | **5.00W** | Unchanged |
| Raspberry Pi 2 | 5V | ~600 mA | **3.00W** | Unchanged |
| Airspy R2 | 5V | ~350 mA | **1.75W** | Phase 4 — replaces V4c on science chain |
| RTL-SDR V4c | 5V | ~300 mA | **1.50W** | Retained for RFI monitoring on Pi 3 |
| ADF4351 RF source | 5V | ~250 mA | **1.25W** | Calibration only |
| HI Feed LNA | 5V | ~100 mA | **0.50W** | Via Airspy R2 bias tee |
| DUOPURUI switch | 5V | ~200 mA | **1.00W** | Unchanged |
| **Steady-state total** | | | **38.20W** | |
| **Peak** | | | **~48W** | Pi 5 + Pi 3 burst + Drive spin-up |
| **Recommended supply** | | | **≥52W** | 25% headroom above steady-state |
| **Omada PoE++ available** | | | **TBC** | Confirm from datasheet — must exceed 52W |

**5V rail:** ~26.50W steady-state  
**12V rail:** ~11.70W steady-state  

**Critical:** Confirm Omada PoE++ output wattage exceeds 52W before committing
to Phase 4 architecture. If headroom is insufficient, upgrade PoE injector.

---

## Thermal Considerations

San Jose summer worst case:

- Ambient air: up to 38°C
- Solar loading on enclosure: +10–15°C above ambient
- Component dissipation: +5–10°C above enclosure wall
- **Estimated internal peak: ~55–65°C**

| Component | Max rated temp | Margin |
|---|---|---|
| Tycon POE-SPLT-BT-UNI-P | +75°C | ✓ adequate |
| Raspberry Pi 2/3/5 | throttles 80°C, safe to 85°C | ✓ adequate |
| Airspy R2 | ~60°C | Marginal — monitor first summer |
| RTL-SDR V4c | aluminium enclosure + thermal pad | ✓ adequate |
| dkplnt DN510 | aluminium case — thermal contact with plate | ✓ adequate |

Monitor Airspy R2 temperature during first summer session. If throttling
occurs, add thermal pad between Airspy R2 and enclosure wall.

---

## Wiring Notes

**5V distribution:** AWG 20 minimum. At 5.3A (Phase 4 5V peak), keeps
voltage drop below 0.1V over DDOEE internal runs of <300mm.

**12V to Drive:** AWG 22 adequate at ~1A over short internal runs.

**DN510 input:** Crimped ferrule terminals (1.5mm² or 2.5mm²) into
screw terminal block. Stranded wire without ferrules is not acceptable —
fraying risk over time in vibrating outdoor installation.

**Grounding:** AWG 12 (2.5mm²) star point bonds. No daisy-chaining.

---

## References

- equipment/datasheets/TP-Link_Omada_PoE_Plus_Plus.pdf
- equipment/datasheets/Tycon_POE-SPLT-BT-UNI-P.pdf
- equipment/datasheets/Phihong_POE48-120BT-R.pdf (rejected)
- equipment/datasheets/TP-Link_TL-POE170S.pdf (deprecated)
- equipment/E001_2026-04-30.md
- design/DUAL_SDR_ARCHITECTURE.md

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-04 | Initial document |
| 1.1 | 2026-05-04 | Add QILIPSU enclosure section |
| 1.2 | 2026-05-07 | Correct Tycon output — single selectable voltage |
| 1.3 | 2026-05-07 | Select dkplnt DN510 |
| 1.4 | 2026-05-07 | Remove DIN rail; add mounting strategy |
| 1.5 | 2026-05-07 | Add custom USB-C power distribution board |
| 1.6 | 2026-05-07 | Add cable gland plan |
| 2.0 | 2026-05-10 | TL-POE170S → Omada PoE++; 3-gland plan revised to 4 penetrations (PoE / DC+sensor / vent / RF); RF isolated in own gland; sensor cable = Cat6 pairs; DUOPURUI switch added to architecture; grounding section added; Phase 1–3 budget updated for 2-Pi + DUOPURUI; Phase 4 budget corrected — Pi 2 + Pi 3 + Pi 5 all present (Pi 5 is addition not replacement); galvanised vs stainless distinction clarified; ferrule requirement noted |
