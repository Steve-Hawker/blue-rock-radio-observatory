# Power Architecture — Blue Rock Radio Observatory

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-04  
**Version:** 3.0  

---

## Overview

The remote sensing enclosure (DDOEE) is powered entirely via a single Cat6 shielded
outdoor ethernet cable carrying Power over Ethernet (PoE). This single-cable
architecture eliminates the need for a separate power run, supporting the
portable/demountable design requirement.

Power is sourced from a PoE injector indoors, carried over the Cat6 cable to the
DDOEE, split and converted to the required voltages by the Tycon
POE-SPLT-BT-UNI-P, and distributed to all components.

---

## Design Requirements

- Single cable power and data to remote enclosure
- Portable / demountable installation — assembled and disassembled per session
- Support all compute and SDR loads simultaneously
- 12V direct to Discovery Drive; 5V rail for all computing and SDR components
- No active cooling — passive thermal management only (see HEAT_DESIGN.md)

---

## Enclosure

**QILIPSU 304 Stainless Steel Electrical Box** — ordered 2026-05-11, due 2026-05-21.

| Parameter | QILIPSU | KrakenRF DDOEE |
|---|---|---|
| External dimensions | 355 × 254 × 152mm (14"×10"×6") | ~350 × 220 × 80mm |
| Internal dimensions | ~346 × 246 × 147mm (verify on arrival) | 304 × 184 × 60mm |
| Shell material | 304 stainless steel | Die-cast aluminium |
| Internal DIN plate | 315 × 200mm galvanised steel | Custom aluminium plate |
| Base plate | Galvanised steel | — |
| IP rating | IP65 + NEMA 4 | IP65 |
| Lock | Key lock + turn latch | Screws |
| Cable entry | NPT connectors included + cable glands | Cable glands |
| Included | Mounting plate, bonding studs, wall brackets, NPT connectors | — |
| Price | ~$90 | ~$165 |
| **Verdict** | **Selected** | Not selected |

**Material note:** Shell is 304 stainless steel. Internal DIN plate and base plate
are galvanised steel. All drilling for cable glands is into the galvanised base
plate — not the stainless shell. Apply Rust-Oleum cold galvanising compound to
all cut edges after drilling.

**WiFi note:** The Discovery Drive mounts on the tripod mast above the enclosure.
WiFi signal is unobstructed.

See ENCLOSURE_DESIGN.md for full enclosure specification, layout, build sequence,
and maintenance schedule.

---

## Selected Components

| Component | Role | Location | Status |
|---|---|---|---|
| TP-Link Omada PoE++ | PoE injector — 802.3bt | Indoors | Arrived 2026-05-10 ✓ |
| Tycon POE-SPLT-BT-UNI-P | PoE splitter — set to **12V** | DDOEE (outdoors) | To order |
| dkplnt DN510 | 12V→5V DC-DC — 50W 10A | DDOEE (outdoors) | Arrived 2026-05-13 ✓ |
| CAT6 F/UTP stranded outdoor | Data + power to DDOEE | House to tripod | To order (30ft × 2) |

---

## Power Architecture

### Voltage Architecture

**Tycon set to 12V output.**

- 12V goes directly to Discovery Drive (~10W)
- 12V feeds the DN510 DC-DC converter → 5V rail for all Pi and SDR loads
- Single Tycon output voltage — simpler than 24V architecture
- DN510 input range 11–35V — 12V is well within specification

### Why Not 24V

A 24V Tycon output was considered. At 24V, the DN510 would operate with
higher input-to-output ratio, marginally improving efficiency. However:

- The Discovery Drive requires 12V — a 24V architecture requires a second
  DC-DC converter (24V→12V) adding cost, complexity, heat, and a failure point
- The DN510 at 12V input is within spec and delivers 50W at 10A — more than
  adequate for the 5V loads
- 12V architecture uses one converter, not two
- **Decision: 12V Tycon output. Single DC-DC. Discovery Drive direct from 12V.**

---

## Power Budget

### 5V Loads

| Device | Power | Notes |
|--------|-------|-------|
| Raspberry Pi 5 | 12.5W | Phase 4 addition |
| Raspberry Pi 3 | 5.0W | RFI monitoring + ADS-B |
| Raspberry Pi 2 | 3.0W | Dish sensor station |
| Airspy R2 | 1.75W | Phase 4 |
| RTL-SDR Blog V4c | 1.5W | Chain A |
| DUOPURUI switch | 1.0W | |
| **5V Subtotal** | **24.75W** | Phase 4 fully loaded |

### 12V Loads

| Device | Power | Notes |
|--------|-------|-------|
| Discovery Drive rotator | ~10W | Direct from Tycon 12V output |
| **12V Subtotal** | **~10W** | |

### System Total

| Section | Power |
|---------|-------|
| 5V loads | 24.75W |
| 12V loads | ~10W |
| DN510 losses (~95% efficiency) | ~1.3W |
| Tycon splitter losses (estimated) | ~2W |
| **Total PoE draw** | **~38W** |

### Phase 1–3 Budget (Pi 2 + Pi 3 only, no Pi 5 or Airspy R2)

| Component | Rail | Power |
|---|---|---|
| Discovery Drive | 12V | ~10W |
| Raspberry Pi 3 | 5V | 5.0W |
| Raspberry Pi 2 | 5V | 3.0W |
| RTL-SDR V4c | 5V | 1.5W |
| DUOPURUI switch | 5V | 1.0W |
| ADF4351 (calibration only) | 5V | 1.25W |
| HI Feed LNA (via bias tee) | 5V | 0.5W |
| **Steady-state total** | | **~23.25W** |
| **Peak** | | **~30W** |

---

## Key Component Specifications

### TP-Link Omada PoE++ Injector (indoor)

- 802.3bt rated — confirm output wattage from datasheet on arrival
- Indoor unit — appropriate for house installation
- Replaces TL-POE170S (deprecated 2026-05-08)
- **Action:** Confirm output wattage and update budget headroom calculation

### Tycon POE-SPLT-BT-UNI-P (outdoor, inside DDOEE)

| Parameter | Value |
|---|---|
| Operating temperature | -40°C to +75°C |
| Output voltage | Selectable — **set to 12V** |
| Combined output power | Up to 72W from 90W input |
| Mounting | DIN mount (use as jig for angle bracket — see ENCLOSURE_DESIGN.md) |
| Housing | Metal |

**Important:** The Tycon outputs ONE voltage. The selector switch must be
set to 12V before installation. Verify with voltmeter before connecting loads.

### dkplnt DN510 DC-DC Converter (12V→5V)

| Parameter | Value |
|---|---|
| Input voltage | 11–35V DC (12V from Tycon) |
| Output voltage | 5V ±1.5% |
| Output current | 10A max |
| Output power | 50W max |
| Efficiency | 95% typical |
| Ripple and noise | 50 mVp-p typical |
| Protections | OVP, OCP, OTP, SCP |
| Case material | Aluminium |
| Dimensions | 74 × 40 × 17.5mm |
| Input connection | Screw terminals — **crimped ferrules required** |
| Price | $9.99 |
| Status | Arrived 2026-05-13 ✓ |

**EMI note:** DC-DC converters are switching regulators generating RF noise.
Mount on galvanised plate physically separated from SDR junction box.
Ferrite chokes on output cables. Output ripple <50mV required — excessive
ripple appears as noise on SDR baseline.

---

## PoE Standard Analysis

| Standard | Port budget | After cable loss | Verdict |
|---|---|---|---|
| 802.3af (PoE) | 15.4W | ~12.5W | Insufficient |
| 802.3at (PoE+) | 30W | ~24.5W | Insufficient |
| **802.3bt T3 (PoE++)** | **60W** | **~52W** | **Selected ✓** |
| 802.3bt T4 (PoE++) | 100W | ~90W | Over-specced |

---

## Voltage Drop Calculation

Cat6 F/UTP stranded, 26 AWG equivalent, 22ft (6.7m) run:

- 26 AWG resistance: ~138 mΩ/m
- Loop resistance (out + return): 138 × 13.4m = ~1.85Ω
- At 12V output, estimated ~3.2A PoE current for 38W load:
  - Voltage drop: 3.2A × 1.85Ω = ~5.9V on the PoE cable
  - **Note:** PoE injector transmits at 48V (802.3bt standard), not 12V
  - At 48V, current for 38W load = 0.79A
  - Voltage drop: 0.79A × 1.85Ω = ~1.5V
  - 48V - 1.5V = ~46.5V at Tycon input — well within spec ✓

---

## Cable Gland Plan

**Galvanised base plate — 4 penetrations, drilled on bench with KSEIBI HSS step drill:**

| Position | Type | Size | Contents |
|---|---|---|---|
| 1 | Gland | 3/4" (19mm) | Cat6 PoE ethernet only |
| 2 | Gland | 3/4" (19mm) | 12V DC to Discovery Drive + Cat6 sensor cable (pairs used for I2C to Hammond box) |
| 3 | Vent | TBD | IP65 membrane vent + anti-insect mesh — check if included with QILIPSU |
| 4 | Gland | 3/4" (19mm) | RF: HI feed coax (LMR240) + dipole coax (RG174) |

**Notes:**
- RF cables in own dedicated gland — maximum separation from power and data
- Cat6 sensor cable: outdoor-rated Cat6, RJ45s removed; twisted pairs used for
  I2C (SDA, SCL, VCC, GND) with spare pairs for future use
- Apply cold galvanising compound to all drilled edges
- Seal cables in glands with neutral-cure RTV silicone
- QILIPSU includes NPT connectors — evaluate for any penetration before purchasing
  separate glands

---

## 5V Power Distribution

DN510 5V output distributed via custom stripboard:

- 6× Cermant USB-C breakout boards on EPLZON stripboard
- Wired directly to 5V/GND rail from DN510 screw terminal output
- Mounted on 25mm standoffs above DN510, bolted via rivnuts
- Full rail current available at each socket

### USB-C Power Socket Allocation

| Socket | Device | Cable | Notes |
|---|---|---|---|
| 1 | Raspberry Pi 2 | Anker USB-C to USB-C | |
| 2 | Raspberry Pi 3 | Anker USB-C to USB-C | |
| 3 | Raspberry Pi 5 | Anker USB-C to USB-C | Phase 4 |
| 4 | DUOPURUI switch | Included with switch | |
| 5 | Spare | — | |
| 6 | Spare | — | |

---

## Internal Power Distribution Wiring

```
PoE injector (indoors, 48V 802.3bt)
        |
        | Cat6 F/UTP shielded stranded outdoor (22ft)
        |
Tycon POE-SPLT-BT-UNI-P (inside DDOEE) — set to 12V
        |                         |
        | 12V DC                  | RJ45 ethernet data
        |                         |
        +── Discovery Drive       DUOPURUI switch
        |   (~10W direct)              |
        |                         Pi 2 / Pi 3 / Pi 5 (ethernet)
        |
dkplnt DN510 (12V→5V, 50W)
        |
        | 5V rail
        |
EPLZON stripboard (6× USB-C sockets)
        |
        +── Pi 2 (3W)
        +── Pi 3 (5W)
        +── Pi 5 (12.5W, Phase 4)
        +── RTL-SDR V4c (1.5W, USB to Pi 3)
        +── Airspy R2 (1.75W, Phase 4, USB to Pi 5)
        +── DUOPURUI switch (1W)
```

---

## Grounding and Bonding

### Single Point Ground
- All DC negative returns tied to single point on galvanised plate
- Plate bonded to stainless outer enclosure via copper braid straps at QILIPSU
  bonding studs
- Outer enclosure bonded to Cat6 shield drain wire — referenced to indoor ground
- Star point: brass or copper lug, to purchase

### Internal Bond Points
- Junction box to plate — thermal compound + mechanical fastening
- Plate to enclosure — minimum 4× copper braid straps at bonding studs
- All metal-to-metal contacts — no plastic isolators at thermal/RF bond points

### Wiring Specifications
- 5V distribution: AWG 20 minimum — <0.1V drop at 5A over <300mm internal runs
- 12V to Discovery Drive: AWG 22 minimum — adequate at ~1A
- DN510 input: **crimped ferrule terminals (1.5mm² or 2.5mm²)** into screw block
  — stranded wire without ferrules is not acceptable (fraying risk in outdoor
  vibrating installation)
- Ground bonds: AWG 12 (2.5mm²) — 2× margin on current, low resistance

### RF Considerations
- DN510 switching noise: mount on plate separated from SDR junction box;
  ferrite chokes on output cables; output ripple <50mV
- PoE switching transients: Tycon includes internal filtering; physical
  separation of PoE cable from I2C and RF inside enclosure
- USB cable EMI: USB 2.0 mandatory for SDR connections (USB 3.0 harmonics
  fall on 1420MHz); Type 31 ferrite chokes both ends; USB isolators recommended
  for SDR cables — see RF_DESIGN.md

---

## Thermal Considerations

San Jose summer worst case:

- Ambient air: up to 38°C
- Solar loading on enclosure: +10–15°C above ambient
- Component dissipation: +5–10°C above enclosure wall
- **Estimated internal peak: ~55–65°C**

| Component | Max rated temp | Status |
|---|---|---|
| Tycon POE-SPLT-BT-UNI-P | +75°C | ✓ |
| dkplnt DN510 | Aluminium case — thermal path to plate | ✓ |
| Raspberry Pi 2/3 | Throttles 80°C, safe to 85°C | ✓ |
| Raspberry Pi 5 | Throttles 80°C — dominant heat source | Monitor |
| Airspy R2 | ~60°C rated | Monitor first summer |
| RTL-SDR V4c | Metal enclosure + thermal pad | ✓ |

See HEAT_DESIGN.md for full thermal chain specification and interface material
selection.

---

## Mounting Strategy

All components mount to the 315×200mm galvanised steel DIN plate via rivet nuts
(rivnuts). No DIN rail required.

| Component | Method | Notes |
|---|---|---|
| Tycon POE-SPLT-BT-UNI-P | Angle bracket (25×25×2mm Al) + rivnuts | DIN bracket used as drilling jig |
| dkplnt DN510 | 4× corner rivnuts, bolted | Aluminium case to plate for heat path |
| Raspberry Pi 2/3/5 | M2.5 standoffs into rivnuts | Al/Cu standoffs preferred |
| DUOPURUI switch | Velcro on top of Tycon | Minimal weight |
| RTL-SDR V4c / Airspy R2 | Inside SDR junction box | See ENCLOSURE_DESIGN.md |
| EPLZON stripboard | 25mm standoffs above DN510 | |

---

## Power Sequencing

No specific power sequencing required — all devices tolerate simultaneous power-up.

- Discovery Drive: confirm parked/idle before power removal
- Raspberry Pis: clean shutdown preferred before power removal
- Sudden power loss during SD card write can corrupt Pi filesystem
- Future enhancement: graceful shutdown trigger from indoor location

---

## Open Questions

- [ ] Confirm TP-Link Omada PoE++ output wattage — update headroom calculation
- [ ] Verify DN510 output ripple <50mV — oscilloscope bench test
- [ ] Evaluate USB isolators (ADuM4160 based) for SDR USB cables
- [ ] Check/purchase ferrule kit (1.5mm² + 2.5mm²) for DN510 screw terminals
- [ ] Purchase star point lug (brass or copper)
- [ ] Purchase AWG 12 ground wire for internal bonds
- [ ] Order cable glands 3/4" × 3
- [ ] Confirm QILIPSU NPT connectors — evaluate before ordering separate glands
- [ ] Specify copper braid strap dimensions — use QILIPSU bonding studs

---

## References

- equipment/datasheets/TP-Link_Omada_PoE_Plus_Plus.pdf
- equipment/datasheets/Tycon_POE-SPLT-BT-UNI-P.pdf
- equipment/datasheets/dkplnt_DN510_DC-DC_converter.pdf
- equipment/datasheets/Phihong_POE48-120BT-R.pdf (rejected)
- equipment/datasheets/TP-Link_TL-POE170S.pdf (deprecated)
- design/ENCLOSURE_DESIGN.md
- design/RF_DESIGN.md
- design/HEAT_DESIGN.md
- design/CABLE_DESIGN.md

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-04 | Initial document |
| 1.1 | 2026-05-04 | Add QILIPSU enclosure section |
| 1.2 | 2026-05-07 | Correct Tycon output — single selectable voltage, set to 12V |
| 1.3 | 2026-05-07 | Select dkplnt DN510 |
| 1.4 | 2026-05-07 | Remove DIN rail; add mounting strategy |
| 1.5 | 2026-05-07 | Add custom USB-C power distribution board |
| 1.6 | 2026-05-07 | Add cable gland plan |
| 2.0 | 2026-05-10 | TL-POE170S → Omada PoE++; 4-gland plan; RF in own gland; sensor cable = Cat6 pairs; DUOPURUI added; grounding section; Phase 4 budget corrected to 3 Pis; galvanised vs stainless clarified |
| 3.0 | 2026-05-13 | Absorb POWER_DESIGN.md content; 24V architecture considered and rejected — 12V confirmed (single DC-DC, Drive direct from 12V); voltage drop calculation added; full wiring diagram; power sequencing; QILIPSU dimensions confirmed; DN510 arrived; USB EMI section added; cross-references to ENCLOSURE_DESIGN, RF_DESIGN, HEAT_DESIGN, CABLE_DESIGN |
