# Open Items — Blue Rock Radio Observatory

**Maintained by:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Purpose:** Running list of unresolved questions, pending decisions,
and items to carry forward across sessions. Update as items are
resolved or new ones arise.

---

## Hardware — Pending Orders

| Item | Status | Notes |
|---|---|---|
| Tycon POE-SPLT-BT-UNI-P | To order | PoE splitter — set to 12V |
| dkplnt DN510 DC-DC converter | To order | 12V→5V 50W for 5V rail |
| VCELINK M242 ethernet switch | To order | 1→2 gigabit switch for Pi 3 + Pi 2 |
| QILIPSU 304 SS enclosure | To order | 350×250×150mm IP65 |
| TP-Link TL-POE170S | To order | 60W PoE injector — indoors |
| Raspberry Pi 5 (4GB) | Pending decision | Replaces Pi 3 + Pi 2 — needed before Phase 4 |
| M5 threaded rod (brass) | To purchase | Custom dipole elements — 3.3cm for 1420MHz, 2.76cm for 1575MHz |
| Right-angle aluminium bracket | To purchase | For Tycon mounting — 25×25×2mm angle, 1/16" thick |
| Rivet nut kit (M3/M4) | To purchase | For mounting plate component fixing — carbon steel zinc plated |
| Rivnut setter tool | To purchase | ~$15-20 hand tool |
| Outdoor CAT6 cable | To purchase | House to DDOEE run |
| microSD card 32GB | To purchase | For Pi OS install |
| Leuchtturm plain lab notebook | Ordered direct from Lighthouse | Awaiting delivery |
| USB-C panel mount sockets (CY flat screw mount) | To order | 5-pack $9.99 — 4 for power distribution, 1 spare |
| EPLZON stripboard 88.9×52.1mm | To order | USB-C sockets + voltmeters on one board |
| Cable gland 3/4" (19mm) × 2 | To order | Gland 1: Cat6 PoE; Gland 2: multi-cable |
| IP65 membrane vent | To check | QILIPSU may include one — verify on receipt |
| Ferrite chokes for USB cables | To order | RFI mitigation — add to Amazon order |
| Short SMA cables (internal) | To order | SDR to coax connections inside enclosure |
| BME280 breakout × 2 | To order | ~$8-10 each — one internal (Pi 3), one external (Pi 2 weather station) |
| Weatherproof housing for external BME280 | To purchase | Small junction box with IP65 vent — mounts on mast |

---

## DDOEE — Confirmed Component Inventory

All components accounted for in Keynote layout v1:

| Component | Location on plate | Notes |
|---|---|---|
| Tycon POE-SPLT-BT-UNI-P | Left, on side | Angle bracket mount |
| VCELINK M242 | On top of Tycon | Velcro |
| dkplnt DN510 | Under stripboard | Rivnuts |
| EPLZON stripboard | Top, on 25mm standoffs over DN510 | USB-C sockets + voltmeters |
| Raspberry Pi 3 | Right, lower | V4c · RFI monitoring · BME280 internal sensor |
| Raspberry Pi 2 | Stacked on Pi 3 | External weather station · BME280 sensor outside enclosure via I2C cable |
| RTL-SDR V4c | Bottom centre | USB to Pi 3 |
| Airspy R2 | Bottom centre | USB to Pi 5 (Phase 4) |
| BME280 (internal) | On Pi 3 GPIO | Enclosure temp/humidity/pressure |
| BME280 (external) | On Pi 2 GPIO — sensor outside enclosure | True observing conditions — sensor in weatherproof housing on mast |
| ADF4351 + 30dB attenuator | Removable — stored together | Insert for calibration only |
| Voltmeters × 2 | Lower half of stripboard | 12V and 5V monitoring |

## DDOEE — Cable Gland Plan

**Bottom removable panel — 3 penetrations:**

| Gland | Size | Contents |
|---|---|---|
| Gland 1 | 3/4" (19mm) | Cat6 PoE ethernet only — separated from RF |
| Gland 2 | 3/4" (19mm) | HI feed coax (LMR240, ~6mm OD) + dipole coax (RG174, ~2.8mm OD) + 12V DC to Discovery Drive |
| Vent | TBD | IP65 membrane vent with anti-insect mesh — check if included with QILIPSU |

**Notes:**
- Gland 2 bundle ~12-15mm total — 19mm gland gives adequate clearance
- RJ45 plug (~11.5mm wide) passes through 19mm gland comfortably
- Cat6 separated from RF cables to minimise interference coupling
- All internal RF connections via short SMA cables
- ADF4351 + attenuator stored as one unit, inserted for calibration only
- Ground wire (pre-connected in QILIPSU) to bond to tripod mast

---

| Decision | Options | Notes |
|---|---|---|
| Pi 5 vs Pi 3 + Pi 2 | Pi 5 preferred — single unit, USB 3.0 | Pi 3 adequate for Phase 2–3; Pi 5 needed before Phase 4 |
| Internal DDOEE ethernet cables | Cat5e unshielded | Short runs — shielding not required |
| Ferrite chokes on USB cables | Recommended | Cheap RFI mitigation — add to order list |
| 5V power distribution | Custom USB-C hub — 3-4 panel mount sockets | See POWER_ARCHITECTURE.md |
| Environmental monitoring sensor | 2× BME280 (~$8-10 each) — see revised Pi architecture below | Wavesense Sense HAT rejected — unnecessary extras |

### Revised Pi Architecture (Phase 4)

| Device | Role | Sensor |
|---|---|---|
| Pi 5 | Airspy R2 · science chain · rotctl · EZRa | — |
| Pi 3 | V4c · RFI monitoring (rtl_power) | BME280 internal — enclosure environment, electronics health, condensation risk |
| Pi 2 | External weather station — dedicated, always running | BME280 external — true observing conditions (temp/humidity/pressure outside) |

**Pi 2 weather station notes:**
- BME280 sensor mounted outside DDOEE in small weatherproof housing on mast
- I2C cable from Pi 2 GPIO through gland or small hole to external sensor (~1m safe for I2C)
- Python script logging to CSV with timestamp
- Data accessible over ethernet via VCELINK switch
- Power from 5V rail distribution board inside DDOEE
- Runs independently — crash does not affect science chain
- Pi 2 board remains inside DDOEE, only sensor is external

**Cable gland update:** I2C sensor cable needs to exit enclosure — add to Gland 2 bundle or use a small additional penetration.

---

## Technical — Unresolved Questions

| Item | Context | Action needed |
|---|---|---|
| ~~LNA2 identification~~ | **RESOLVED 2026-05-07** — QPL9547, same as LNA1 | ✓ Complete |
| SAW filter confirmation | TA1077A + TA2494A identified from PCB — not yet confirmed by KrakenRF | Follow-up message sent |
| Tycon DIN bracket screw hole spacing | Will use as drilling jig for angle bracket | Measure when unit arrives |
| dkplnt DN510 operating temperature | Not stated in listing | Check if datasheet available from dkplnt; automotive grade likely -40 to +85°C |
| Discovery Drive power consumption under slew | Estimated ~12W — may be higher under load | Measure when unit arrives; revisit power budget if >15W |
| ADF4351 SPI library for Pi | Python library needed | Research before V4c arrives — see INV002 |
| GPSDO reference for ADF4351 | Deferred — assess after onboard crystal CAL-001 | Decision point: if LO error >1 kHz, upgrade to GPSDO (~$75) |

---

## Documentation — Updates Required

| Document | Update needed | Priority |
|---|---|---|
| DIPOLE_ANTENNA_DESIGN.md | Confirm M5 thread when dipole kit arrives | When V4c arrives |
| E001 → E002 | Create E002 when Phase 3 begins (V4c + dipole assembled) | When V4c arrives |
| POWER_ARCHITECTURE.md | Update power budget when Pi 5 decision confirmed | Before Phase 4 |
| DDOEE_mounting_plate_v2.svg | Redraw for Phase 4 when Pi 5 confirmed | Before Phase 4 |
| INV001_noise_budget | Complete Friis with QPL9547 real values + SAW insertion loss | Before first light |
| SAW_FILTER_DESIGN.md | ~~Identify LNA2~~ RESOLVED — QPL9547; SAW confirmation from KrakenRF pending | Soon |
| TOOLS_PLAN.md | Refresh for Stellarium, rotctl, dual-SDR, ADF4351 | Before Phase 3 |
| QUICK_REFERENCE.md | Update LO offset to 1422 MHz | Soon |
| SDR_SELECTION.md | Note V4c triplexer improvement | Soon |
| RFI_OVERVIEW.md | Note V4c triplexer improvement | Soon |

---

## Site Assessment — Pending (Today, 2026-05-07)

| Item | Notes |
|---|---|
| Formal site survey with tripod | Tripod ready — no assembly required |
| Elevation angle to 2515 boundary tree | Priority measurement — closest to transit bearing |
| Bearing and elevation to pine top | Confirm NW bearing, not on transit bearing |
| Confirm southern horizon open at 180° | Imagery suggests open — verify with theodolite |
| Mark dish position on patio | Tape / chalk / adhesive dots |
| Photo panorama 360° | Every 45°, upload to build/photos/ |
| Physical log book | Leuchtturm not yet arrived — use temporary notepad, transfer later |

---

## Calibration — Pending

| Procedure | When | Notes |
|---|---|---|
| CAL-000-V4c | When V4c + ADF4351 both arrive (~May 22) | SDR baseline before feed |
| CAL-001 LO verification | Commissioning | Requires ADF4351 |
| CAL-002 passband sweep | Commissioning | Requires ADF4351 + dish |
| First RFI survey | When V4c arrives | Chain A baseline |

---

## Academic — Pending

| Item | Notes |
|---|---|
| Response from Dr Megan Argo | Email sent 2026-05-04 re: AI use policy — awaiting reply |
| Response from Jason Kirk | Same email — awaiting reply |
| KrakenRF LNA2 | ~~RESOLVED 2026-05-07~~ — both LNAs are QPL9547 | ✓ |
| KrakenRF SAW filters | Follow-up message needed — see below | Pending |
| SARA publication | SITE_ASSESSMENT_METHODOLOGY.md — after Blue Rock worked example complete |
| First Light Readiness reading | FL-6 and FL-7 before end May; FL-1 to FL-5 before August |

### KrakenRF — LNA2 resolved, SAW confirmation pending

**LNA2 RESOLVED 2026-05-07:** Both LNAs confirmed as QPL9547 by
KrakenRF via eBay. Signal chain now confirmed:

```
Antenna → QPL9547 (LNA1) → SAW1 → QPL9547 (LNA2) → SAW2 → Output
```

**SAW filters — follow-up message needed:**

Our identification of TA1077A (F1) and TA2494A (F2) is based on PCB
photo analysis and datasheet matching — not yet confirmed by KrakenRF.
Send follow-up via eBay:

> Thank you for confirming both LNAs are QPL9547 — very helpful.
> Could you also confirm the SAW filter part numbers? From the PCB
> we believe F1 is a TA1077A and F2 is a TA2494A, both from Tai-Saw
> Technology. We want to make sure our Friis noise budget uses the
> correct insertion loss figures.

**Status:** Awaiting SAW confirmation.

---

---

## New Session Handoff Notes

*When starting a new Claude session, paste this section as context:*

**Project:** Blue Rock Radio Observatory — BSc Honours Astronomy (UCLan)  
**Observer:** Steve Hawker BEng MBA FRAS, San Jose CA  
**GitHub:** https://github.com/Steve-Hawker/blue-rock-radio-observatory  
**Current phase:** Phase 2 — Site Survey (tripod arrived 2026-05-07)  
**Next milestone:** V4c + ADF4351 arrive ~May 22 → CAL-000  
**Key documents:** See README.md for full repository structure  
**This file:** OPEN_ITEMS.md — start here for current state  

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-07 | Initial document — hardware pending, technical questions, documentation updates, site survey items, calibration schedule, academic items, session handoff notes |
