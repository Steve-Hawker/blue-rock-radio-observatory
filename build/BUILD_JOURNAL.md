# Build Journal — Blue Rock Radio Observatory

**Observer:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory, San Jose CA  
**Date started:** 2026-04-30  

*Running record of observatory construction — assembly notes, observations,
problems encountered, solutions found, measurements made, and photos.
Informal by design. Add entries chronologically. Cross-reference the
equipment log (equipment/E00X) for formal system state documentation.*

*Photos go in build/photos/ and are referenced inline.*

---

## How to add an entry

```
### YYYY-MM-DD — [Component / Activity]

[Free text — observations, measurements, problems, solutions, thoughts]

![Caption](photos/YYYY-MM-DD_description.jpg)

**Cross-references:** E001, design/BEAM_AND_RESOLUTION.md, etc.
```

---

## Component Arrival Log

| Component | Ordered | Est. delivery | Arrived | Notes |
|---|---|---|---|---|
| Discovery Drive | 2026-04-28 | TBC | | Crowdfunding — awaiting |
| Discovery Dish (70cm) | 2026-04-30 | 2026-07-31 | | |
| HI Feed (1380–1460 MHz) | 2026-04-30 | 2026-08-14 | | |
| Laufer — RTL-SDR book | 2026-04-30 | 2026-05-04 | 2026-05-04 | May the 4th! |
| SMA fixed attenuator 30dB | 2026-05-04 | 2026-05-06 | 2026-05-06 | |
| Amazon Basics Tripod | 2026-05-02 | 2026-05-07 | 2026-05-07 | |
| Rivet nut kit (M3/M4) + setter | 2026-05-09 | 2026-05-09 | 2026-05-09 | Same-day delivery |
| ADF4351 RF signal source board | 2026-05-04 | May 12–22 | 2026-05-10 | Arrived early |
| TP-Link Omada PoE++ injector | 2026-05-08 | TBC | 2026-05-10 | |
| DUOPURUI ethernet switch 1→3 | 2026-05-08 | TBC | 2026-05-10 | |
| EPLZON breadboard kit | 2026-05-08 | TBC | 2026-05-10 | |
| RTL-SDR Blog V4c | 2026-05-02 | May 21–Jun 12 | 2026-05-11 | Arrived early |
| RTL-SDR Dipole Set | 2026-05-02 | May 21–Jun 12 | 2026-05-11 | Arrived early |
| Anker USB-C cables (4×) | 2026-05-11 | TBC | 2026-05-12 | |
| Cermant USB-C breakout boards (20×) | 2026-05-11 | TBC | 2026-05-12 | |
| Leuchtturm lab notebook | — | — | 2026-05-12 | UCLan entitlement |
| Rust-Oleum cold galvanising spray | 2026-05-11 | 2026-05-13 | 2026-05-13 | |
| Cat6A shielded ethernet jumpers 1ft (5×) | 2026-05-11 | TBC | 2026-05-13 | |
| KSEIBI #5 HSS step drill | 2026-05-11 | TBC | 2026-05-13 | |
| LED modules (stripboard) | 2026-05-11 | TBC | 2026-05-13 | |
| Cat6 patch cables | 2026-05-11 | TBC | 2026-05-13 | |
| dkplnt DN510 DC-DC 12V→5V | 2026-05-08 | TBC | 2026-05-13 | |
| Adafruit BME280 breakout | 2026-05-08 | TBC | 2026-05-20 | |
| Adafruit LSM6DSOX IMU breakout | 2026-05-08 | TBC | 2026-05-20 | |
| Qwiic flat 4-pole cables × 3 | 2026-05-08 | TBC | 2026-05-20 | |
| Hammond 1591DBU enclosure (blue) | 2026-05-08 | TBC | 2026-05-20 | |
| Squash balls 40mm 4-pack | 2026-05-23 | ~2026-06-07 | | eBay |
| QILIPSU 304 SS enclosure | 2026-05-11 | 2026-05-21 | 2026-05-24 | |
| Tycon POE-SPLT-BT-UNI-P | 2026-05-27 | ~2026-06-10 | 2026-05-29 | Includes mounting brackets |
| Airspy R2 | — | Phase 4 | | Deferred |
| Raspberry Pi 5 (4GB) | — | Before Phase 4 | | Pending decision |
| microSD card (32GB) | — | TBC | | Still to purchase |

*Update Arrived column and add build journal entry when each component
is received and assembled.*

---

## Build Milestones

| Milestone | Target | Achieved | Entry |
|---|---|---|---|
| Repository and documentation complete | Apr 2026 | 2026-04-30 | 2026-04-30 |
| Tripod assembled and tested | May 2026 | 2026-05-07 | 2026-05-07 |
| ADF4351 + V4c both in hand — CAL-000 unblocked | May 2026 | 2026-05-11 | 2026-05-11 |
| DDOEE enclosure (QILIPSU) received | May 2026 | 2026-05-24 | 2026-05-24 |
| All core DDOEE electronics in hand | May 2026 | 2026-05-29 | 2026-05-29 |
| CAL-000 — V4c SDR baseline with ADF4351 | When V4c + ADF4351 in hand | **READY** | |
| Pi 3 fresh OS install | Before dish arrives | | |
| DDOEE internal build — stripboard, rivnuts, wiring | Before dish arrives | | |
| Hammond 1591DBU sensor box build | Before dish arrives | | |
| EZRa installed and tested | Before dish arrives | | |
| First RFI survey — dipole + V4c | Before dish arrives | | |
| dump1090 ADS-B — SAW filter validation | Before dish arrives | | |
| Discovery Drive mounted on tripod | On arrival | | |
| Dish assembled | Aug 2026 | | |
| Feed mounted and connected | Aug 2026 | | |
| Full signal chain connected | Aug 2026 | | |
| Pointing verified on known source | Aug 2026 | | |
| First light — Cas A detected | Aug/Sep 2026 | | |
| E002 equipment log created | After first light | | |

---

## Journal Entries

*(entries below — most recent last)*

---

### 2026-04-30 — Programme Start

Observatory programme formally initiated. All planning documentation
committed to GitHub repository. Hardware on order.

Current state: no hardware assembled. Repository infrastructure complete.
Awaiting delivery of first components.

**Repository:** https://github.com/Steve-Hawker/blue-rock-radio-observatory

---

### 2026-05-07 — Tripod Arrived

Amazon Basics tripod received. Not yet assembled or deployed to patio.
Tripod mast diameter 1.5" (38.1mm) — confirmed within Discovery Drive
2.0–5.0cm acceptance range.

Formal site survey on patio pending — tripod is the instrument.

**Cross-references:** E001, OPEN_ITEMS.md — Site Assessment

---

### 2026-05-10 — ADF4351, Omada PoE++, DUOPURUI, EPLZON Arrived

ADF4351 arrived early (window was May 12–22). TP-Link Omada PoE++,
DUOPURUI ethernet switch, and EPLZON breadboard kit also arrived.

ADF4351 is the calibration signal source — needed alongside V4c for
CAL-000. Both items now needed before calibration can proceed.

---

### 2026-05-11 — V4c and Dipole Arrived — CAL-000 Unblocked

RTL-SDR Blog V4c and dipole set both arrived early (window was May 21–Jun 12).

With ADF4351 also in hand, CAL-000 (V4c SDR baseline) is now ready to
execute. Procedure in design/ADF4351_CALIBRATION.md.

This is a significant milestone — the core science chain receiver is in hand
ahead of schedule. dump1090 ADS-B can also be run immediately on Pi 3 to
validate the V4c and characterise San Jose 1090 MHz traffic.

**Cross-references:** design/ADF4351_CALIBRATION.md — CAL-000 procedure

---

### 2026-05-13 — DN510, Cat6A Jumpers, Step Drill, LED Modules, Patch Cables Arrived

dkplnt DN510 DC-DC converter arrived. Also received: Cat6A shielded 1ft
ethernet jumpers (5-pack), KSEIBI #5 HSS step drill, LED modules for
stripboard, and Cat6 patch cables.

Key design decisions confirmed this session:
- Southwire 4"×2"×1-7/8" steel handy box as SDR Faraday shield inside QILIPSU — confirmed
- BME280 inside junction box (SDR thermal + condensation monitoring) — confirmed
- 12V Tycon architecture — confirmed (24V considered and rejected)

Seven new design documents committed to design/ directory.

**Cross-references:** design/ENCLOSURE_DESIGN.md, design/RF_DESIGN.md,
design/HEAT_DESIGN.md, design/POWER_ARCHITECTURE.md

---

### 2026-05-20 — Adafruit Sensors, Qwiic Cables, Hammond 1591DBU Arrived

Adafruit BME280 breakout, Adafruit LSM6DSOX IMU breakout, three Qwiic
flat 4-pole cables, and Hammond 1591DBU blue ABS enclosure all arrived.

Hammond 1591DBU is the dish sensor enclosure — houses BME280 (field
ambient environment, 0x77) and LSM6DSOX (dish elevation verification).
Card guides accept a credit card as the separation plate between the
weather zone and IMU zone.

**Cross-references:** OPEN_ITEMS.md — Hammond 1591DBU Sensor Box Design

---

### 2026-05-24 — QILIPSU Enclosure Arrived

QILIPSU 304 stainless steel IP65 enclosure arrived. Shell is 304 SS;
internal DIN mounting plate and base plate are galvanised steel.

**On arrival checks needed:**
- [ ] Verify internal dimensions against product drawing — especially depth (147mm estimated)
- [ ] Check for included membrane vent between cable glands
- [ ] Evaluate included NPT connectors before ordering separate cable glands
- [ ] Inspect gasket material
- [ ] Note bonding stud positions for copper braid strap planning

**Cross-references:** design/ENCLOSURE_DESIGN.md

---

### 2026-05-29 — Tycon POE-SPLT-BT-UNI-P Arrived

Tycon PoE splitter arrived. Includes mounting brackets — aluminium angle
bar not required. This was the last critical-path item for the DDOEE power
chain. All core DDOEE electronics are now in hand.

**Items still outstanding before DDOEE build can begin:**
- Squash balls (ordered May 23, ~Jun 7) — Hammond box vent cap
- Southwire handy box (~$2, Home Depot) — SDR Faraday shield
- Cable glands 3/4" × 3
- Short SMA cables (internal RF connections)
- Ferrite chokes (Type 31)
- Star point lug + AWG 12 ground wire
- Ferrule kit (1.5mm² + 2.5mm²)
- M3 brass standoffs (Hammond box sensor boards)
- Sticky-backed foam (Hammond box lid seal)
- Copper braid straps (plate-to-enclosure bonding)
- Thermal pads (SDR-to-junction-box gap — measure first)
- Outdoor Cat6 cable 30ft × 2

**Cross-references:** design/ENCLOSURE_DESIGN.md — Build Sequence,
POWER_ARCHITECTURE.md, OPEN_ITEMS.md

---

*(add entries here as build progresses)*

---

## Notes on Photography

Good build photos to take for each component:

**Tripod:**
- Box on arrival (always satisfying)
- Parts laid out before assembly
- Each stage of assembly
- Fully assembled — showing height adjustment
- Positioned on patio — showing site context

**Discovery Drive:**
- Unboxing
- Compass shelf detail
- Mounted on tripod mast
- WiFi antenna attached
- Web UI on MacBook showing connection confirmed

**RTL-SDR V4 + dipole:**
- Unboxing
- Dipole arms at 5.25cm setting (show measurement)
- Connected to MacBook
- First GQRX waterfall screenshot

**Discovery Dish:**
- Three petals unboxed
- Assembly sequence
- Feed mounting detail — focal length measurement
- Completed dish on mount
- Full system on patio — wide shot

**First light:**
- Screenshot of first Cas A spectrum
- System on patio during observation
- MacBook showing EZRa or GQRX

*Photos are part of the scientific record — they document the
physical configuration at each stage and support the equipment log.*
