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
| Right-angle aluminium bracket | To purchase | For Tycon mounting — 25×25×2mm angle |
| Rivet nut kit (M3/M4) | To purchase | For mounting plate component fixing |
| Outdoor CAT6 cable | To purchase | House to DDOEE run |
| microSD card 32GB | To purchase | For Pi OS install |
| Leuchtturm plain lab notebook | Ordered direct from Lighthouse | Awaiting delivery |

---

## Hardware — Pending Decisions

| Decision | Options | Notes |
|---|---|---|
| Pi 5 vs Pi 3 + Pi 2 | Pi 5 preferred — single unit, USB 3.0 | Pi 3 adequate for Phase 2–3; Pi 5 needed before Phase 4 |
| Internal DDOEE ethernet cables | Cat5e unshielded | Short runs — shielding not required |
| Ferrite chokes on USB cables | Recommended | Cheap RFI mitigation — add to order list |

---

## Technical — Unresolved Questions

| Item | Context | Action needed |
|---|---|---|
| LNA2 identification | PCB photo shows U2 — different package from QPL9547 | Need higher resolution PCB image to identify |
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
| SAW_FILTER_DESIGN.md | Identify LNA2 chip if possible | When higher res PCB image available |
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
| SARA publication | SITE_ASSESSMENT_METHODOLOGY.md — after Blue Rock worked example complete |
| First Light Readiness reading | FL-6 and FL-7 before end May; FL-1 to FL-5 before August |

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
