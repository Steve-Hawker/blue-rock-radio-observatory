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
| Tycon POE-SPLT-BT-UNI-P | **To order — critical path** | PoE splitter — set to 12V; nothing works without this |
| ~~VCELINK M242 ethernet switch~~ | **SUPERSEDED 2026-05-08** | Replaced by DUOPURUI 1→3 switch |
| ~~TP-Link TL-POE170S~~ | **SUPERSEDED 2026-05-08** | Replaced by TP-Link Omada PoE++ |
| TP-Link Omada PoE++ injector | **Arrived 2026-05-10** ✓ | ASIN B09SXSN3XT — confirm output wattage from datasheet |
| dkplnt DN510 DC-DC 12V→5V 50W | Ordered 2026-05-08 | ASIN B0DYK93WX8 — awaiting delivery |
| DUOPURUI ethernet switch 1→3 | **Arrived 2026-05-10** ✓ | ASIN B0FCLKWGZ1 |
| EPLZON breadboard kit | **Arrived 2026-05-10** ✓ | ASIN B0DCRKNW5H |
| ADF4351 RF signal source board | **Arrived 2026-05-10** ✓ | Early — window was May 12–22 |
| Rivet nut kit (M3/M4) + setter tool | **Arrived 2026-05-09** ✓ | Same-day delivery |
| Adafruit BME280 breakout | Ordered 2026-05-08 | Awaiting delivery |
| Adafruit LSM6DSOX breakout | Ordered 2026-05-08 | Awaiting delivery |
| Qwiic flat 4-pole cables × 3 | Ordered 2026-05-08 | Two in box, one spare |
| Hammond 1591DBU enclosure | Ordered 2026-05-08 | Ships ~May 11 |
| QILIPSU 304 SS enclosure | To order | 350×250×150mm IP65 |
| Outdoor Cat6 cable 30ft × 2 | To order | Outdoor rated; house to DDOEE run |
| Raspberry Pi 5 (4GB) | Pending decision | Needed before Phase 4 |
| Cermant USB-C breakout boards (20-pack) | To order | 6 on EPLZON stripboard; $8.99/20 |
| Cable gland 3/4" (19mm) × 2 | To order | Gland 1: Cat6 PoE; Gland 2: multi-cable |
| IP65 membrane vent | To check | QILIPSU may include one — verify on receipt |
| Ferrite chokes for USB cables | To order | RFI mitigation |
| Short SMA cables (internal) | To order | SDR to coax connections inside enclosure |
| Combined anemometer + wind vane unit | To order | ~$25-35 — single mount |
| MCP3008 ADC | To order | ~$4 — wind vane voltage on Pi 2 SPI bus |
| M5 threaded rod (brass) | To purchase | Custom dipole elements |
| Right-angle aluminium bracket | To purchase | For Tycon mounting — 25×25×2mm |
| microSD card 32GB | To purchase | For Pi OS install |
| M3 brass standoffs | To purchase | Equal height both sides in Hammond box |
| Mounting bolts | To purchase | Hammond box to Drive bracket |
| Sticky-backed foam sheet | To purchase | Lid seal on Hammond box |
| Squash balls (40mm standard, 4-pack) | To purchase | Vent cap — ~$7 eBay; diagonal cut |
| Star point lug (brass or copper) | To purchase | Internal DDOEE grounding star point |
| AWG 12 ground wire | To purchase | Internal DDOEE ground bonds — 2.5mm² minimum |
| Credit card (expired) | On hand ✓ | Separation plate — fits card guides in Hammond 1591DBU |
| Leuchtturm plain lab notebook | Ordered — Lighthouse | Awaiting delivery |

---

## DDOEE — Confirmed Component Inventory

| Component | Location on plate | Notes |
|---|---|---|
| Tycon POE-SPLT-BT-UNI-P | Left, on side | Angle bracket mount |
| DUOPURUI ethernet switch 1→3 | On top of Tycon | Velcro; replaces VCELINK M242 |
| dkplnt DN510 | Under stripboard | Rivnuts |
| EPLZON stripboard | Top, on 25mm standoffs over DN510 | 6× USB-C breakout sockets + voltmeters |
| Raspberry Pi 3 | Right, lower | V4c · RFI monitoring · dump1090 ADS-B |
| Raspberry Pi 2 | Stacked on Pi 3 | Dish sensor station · Hammond box via I2C/Qwiic cable |
| RTL-SDR V4c | Bottom centre | USB to Pi 3 |
| Airspy R2 | Bottom centre | USB to Pi 5 (Phase 4) |
| BME280 (external) | In Hammond 1591DBU on Drive bracket | True observing conditions — Pi 2 Qwiic/I2C |
| LSM6DSOX | In Hammond 1591DBU on Drive bracket | Dish elevation verification — Pi 2 Qwiic/I2C |
| ADF4351 + 30dB attenuator | Removable — stored together | Insert for calibration only |
| Voltmeters × 2 | Lower half of stripboard | 12V and 5V monitoring |

**Note:** Internal DDOEE BME280 on Pi 3 — decision pending. Leaning against.
Advantage modest: condensation risk monitoring and enclosure thermal tracking.
Not a science instrument. Can be added later if warranted.

### 5V USB-C power rail — 6 sockets

| Socket | Device | Notes |
|---|---|---|
| 1 | Raspberry Pi 2 | Dish sensor station |
| 2 | Raspberry Pi 3 | RFI monitoring + ADS-B |
| 3 | Raspberry Pi 5 | Science chain (Phase 4) |
| 4 | DUOPURUI ethernet switch | Needs 5V USB-C |
| 5 | Spare | Available |
| 6 | Spare | Available |

## DDOEE — Cable Gland Plan

**Bottom removable panel — 3 penetrations:**

| Gland | Size | Contents |
|---|---|---|
| Gland 1 | 3/4" (19mm) | Cat6 PoE ethernet only — separated from RF |
| Gland 2 | 3/4" (19mm) | HI feed coax (LMR240) + dipole coax (RG174) + 12V DC to Discovery Drive + I2C/Qwiic cable to Hammond box |
| Vent | TBD | IP65 membrane vent with anti-insect mesh — check if included with QILIPSU |

---

## Decisions — Resolved

| Decision | Resolution | Notes |
|---|---|---|
| Internal DDOEE ethernet cables | Cat5e unshielded | Short runs |
| Ferrite chokes on USB cables | Recommended | Cheap RFI mitigation |
| 5V power distribution | 6× Cermant USB-C breakout boards on EPLZON stripboard | 3 Pis + switch + 2 spare |
| Environmental monitoring sensor | BME280 + LSM6DSOX | Waveshare Sense HAT (C) rejected |
| Ethernet switch | DUOPURUI 1→3 gigabit | Replaces VCELINK M242 — 3 Pis need 3 ports |
| PoE injector | TP-Link Omada PoE++ | Replaces TL-POE170S — ordered 2026-05-08 |
| Dish sensor enclosure | Hammond 1591DBU blue ABS | Card guides; credit card as separation plate; outside face of Drive bracket |
| Dish sensor mounting | Outside face of Discovery Drive bracket | Plate underside ruled out — fouling confirmed from photos |
| Sensor board interconnect | Qwiic flat 4-pole cable chain | BME280 → LSM6DSOX → pigtail to Pi 2; both boards have dual Qwiic ports |
| Separation plate material | Expired credit card | Fits card guides in Hammond 1591DBU exactly; rigid, waterproof, no fabrication |
| Vent cap material | Standard 40mm squash ball, diagonal cut | Omnidirectional rain protection; ~$7/4-pack eBay |
| ADS-B monitoring | dump1090 on Pi 3 via V4c — Phase 3 | No extra hardware; validates V4c + SAW rejection at 1090 MHz |
| Internal DDOEE BME280 | **PENDING** — leaning against | Advantage modest; not a science instrument; can be added later |

### Pi Architecture (Phase 4)

| Device | Role | Sensors / Software |
|---|---|---|
| Pi 5 | Airspy R2 · science chain · rotctl · EZRa | — |
| Pi 3 | V4c · RFI monitoring · dump1090 ADS-B | (internal BME280 — pending decision) |
| Pi 2 | Dish sensor station — always running | BME280 + LSM6DSOX via Qwiic; anemometer + wind vane |

---

## Hammond 1591DBU Sensor Box Design — RESOLVED 2026-05-08

### Physical arrangement

- **Box:** Hammond 1591DBU — blue ABS, ~111×61×27mm, card guide channels
- **Separation plate:** Expired credit card — slots into card guides; divides interior into weather zone (BME280) and IMU zone (LSM6DSOX); small notch at bottom edge for Qwiic cable routing
- **Lid:** Closes open face; carries both sensor boards on equal-height M3 brass standoffs; carries cable gland
- **Lid seal:** Sticky-backed foam; separation plate edge provides compression; cutout over wiring to avoid crushing
- **Mounting:** Outside face of Discovery Drive bracket via bolts — moves with dish in azimuth; elevation tracked by LSM6DSOX
- **Vent:** Squash ball (40mm standard, diagonal cut) glued over ~15-20mm hole in box wall, entirely within weather zone
- **Gland:** In lid, weather zone side — Qwiic/I2C cable enters, routes under credit card gap to LSM6DSOX in IMU zone
- **Qwiic chain:** Pi 2 I2C GPIO → pigtail → LSM6DSOX → flat Qwiic cable → BME280

### BME280 notes
- Sensor element faces toward vent hole
- First read after long idle returns stale cached value — read twice, discard first
- I2C address: 0x77 (default)

### LSM6DSOX notes
- Fully enclosed in sealed IMU zone
- Z-axis perpendicular to lid surface
- I2C address: 0x6A (default) — no conflict with BME280 ✓
- Elevation: arctan2(gz, √(gx²+gy²)) after calibration
- See DISH_POSITION_CALIBRATION.md

### ADS-B / dump1090 — Phase 3 activity

ADS-B at 1090 MHz — SJC airspace is busy. Running dump1090 on Pi 3 via V4c:

1. Confirms V4c working before HI feed arrives
2. Characterises SJC traffic density for RFI survey
3. Validates SAW filter rejection at 1090 MHz in field
4. Optional: contributes to FlightAware/FlightRadar24

Document results in rfi/RFI_OVERVIEW.md.

---

## Technical — Unresolved Questions

| Item | Context | Action needed |
|---|---|---|
| ~~LNA2 identification~~ | **RESOLVED 2026-05-07** — QPL9547 | ✓ |
| SAW filter confirmation | TA1077A + TA2494A from PCB analysis — not yet confirmed by KrakenRF | Follow-up message sent |
| Tycon DIN bracket screw hole spacing | Drilling jig for angle bracket | Measure when arrives |
| dkplnt DN510 operating temperature | Not stated in listing | Check datasheet |
| Discovery Drive power consumption under slew | Estimated ~12W | Measure when arrives |
| ADF4351 SPI library for Pi | Python library needed | Research before V4c arrives |
| GPSDO reference for ADF4351 | Deferred | If LO error >1 kHz after CAL-001, upgrade to GPSDO (~$75) |
| TP-Link Omada PoE++ output wattage | Not yet confirmed | Pull datasheet when arrives; update power budget |

---

## Documentation — Updates Required

| Document | Update needed | Priority |
|---|---|---|
| DIPOLE_ANTENNA_DESIGN.md | Confirm M5 thread when dipole kit arrives | When V4c arrives |
| E001 → E002 | Create E002 when Phase 3 begins | When V4c arrives |
| POWER_ARCHITECTURE.md | 6× USB-C sockets; DUOPURUI + Omada PoE++; Pi 5 pending | Before Phase 4 |
| DDOEE_mounting_plate_v2.svg | Redraw — DUOPURUI replaces VCELINK M242; 6-socket power strip | Before Phase 4 |
| INV001_noise_budget | Complete Friis with QPL9547 interpolated values + SAW IL | Before first light |
| SAW_FILTER_DESIGN.md | SAW confirmation from KrakenRF pending | Soon |
| TOOLS_PLAN.md | Add dump1090 · Stellarium · rotctl · ADF4351 | Before Phase 3 |
| QUICK_REFERENCE.md | Update LO offset to 1422 MHz | Soon |
| SDR_SELECTION.md | Note V4c triplexer improvement | Soon |
| RFI_OVERVIEW.md | V4c triplexer; QILIPSU skin depth; ADS-B field validation plan | Soon |
| DISH_POSITION_CALIBRATION.md | Outside face of Drive bracket; Hammond 1591DBU + Qwiic chain | Soon |

---

## Site Assessment — Pending

| Item | Notes |
|---|---|
| Formal site survey with tripod | Tripod arrived 2026-05-07 — not yet deployed |
| Elevation angle to 2515 boundary tree | Priority measurement |
| Bearing and elevation to pine top | Confirm NW bearing |
| Confirm southern horizon open at 180° | Verify with theodolite |
| Mark dish position on patio | Tape / chalk / adhesive dots |
| Photo panorama 360° | Every 45°, upload to build/photos/ |
| Physical log book | Leuchtturm not yet arrived |

---

## Calibration — Pending

| Procedure | When | Notes |
|---|---|---|
| CAL-000-V4c | ADF4351 due May 12–22; V4c due May 21–Jun 12 | Both must be in hand |
| CAL-001 LO verification | Commissioning | Requires ADF4351 |
| CAL-002 passband sweep | Commissioning | Requires ADF4351 + dish |
| First RFI survey | When V4c arrives | Chain A baseline |
| ADS-B field validation | Phase 3 | 1090 MHz SAW rejection; document in RFI_OVERVIEW.md |

---

## Academic — Pending

| Item | Notes |
|---|---|
| Response from Dr Megan Argo | Email sent 2026-05-04 — awaiting reply |
| Response from Jason Kirk | Same email — awaiting reply |
| KrakenRF SAW filters | Follow-up message needed — see below |
| SARA publication | After Blue Rock worked example complete |
| First Light Readiness reading | FL-6 + FL-7 before end May; FL-1 to FL-5 before August |
| Phelps 2024 paper | Reviewed 2026-05-08 — filed in reading_notes/ |

### KrakenRF — SAW confirmation pending

Signal chain confirmed 2026-05-07:
```
Antenna → QPL9547 (LNA1) → TA1077A (SAW1) → QPL9547 (LNA2) → TA2494A (SAW2) → Output
```

SAW IDs from PCB analysis — not yet confirmed by KrakenRF. Send follow-up via eBay:

> Thank you for confirming both LNAs are QPL9547 — very helpful.
> Could you also confirm the SAW filter part numbers? From the PCB
> we believe F1 is a TA1077A and F2 is a TA2494A, both from Tai-Saw
> Technology. We want to make sure our Friis noise budget uses the
> correct insertion loss figures.

---

## Dish Sensor Python Development — Requirements and Design

*Full implementation deferred. See design/DISH_POSITION_CALIBRATION.md.*

### Scripts planned

| Script | Purpose |
|---|---|
| `dish_sensors.py` | Continuous logging — BME280 + LSM6DSOX to CSV |
| `sensor_calibration.py` | One-time orientation calibration at known dish position |
| `weather_summary.py` | Session summary — mean/min/max over time window |
| `position_monitor.py` | Real-time position verification vs rotctl |

### Library decision — pending

Prefer Adafruit CircuitPython stack (blinka) for both sensors if Pi 2 (ARMv7 32-bit)
compatibility confirmed. Fallback: `bme280` pip + `smbus2` for LSM6DSOX.

### CSV format

```
timestamp_utc, temp_c, humidity_pct, pressure_hpa,
accel_x_g, accel_y_g, accel_z_g,
gyro_x_dps, gyro_y_dps, gyro_z_dps,
elevation_deg_imu, elevation_deg_rotctl, position_flag
```

`position_flag` = 1 if |IMU elevation − rotctl elevation| > 0.5°

### Calibration design

**Step 1:** Record accelerometer vector at known elevation (park = 0°) → rotation matrix R_sd  
**Step 2:** Spirit level verification → tripod tilt correction T  
**Step 3:** elevation = arctan2(g_z_corrected, √(g_x² + g_y²))  
**Step 4:** Validate against Cas A transit — three-way comparison IMU / rotctl / ephemeris  
**Step 5:** Seasonal re-calibration → calibration/IMU_calibration.csv  

| Source | Uncertainty |
|---|---|
| Accelerometer noise | ~0.06° |
| Sensor mounting alignment | ~0.1–0.5° |
| Tripod levelling | ~0.1° |
| **Total estimated** | **~0.2–0.6°** |

### Ideas to capture

- [ ] Wind speed proxy via RMS accelerometer noise
- [ ] Combined anemometer + wind vane — pulse GPIO + MCP3008 SPI
- [ ] Slew settling detection before integration begins
- [ ] Session start/end weather report auto-appended to session log
- [ ] Humidity alert if internal DDOEE >85% (if internal BME280 fitted)
- [ ] ADF4351 LO temperature compensation via internal BME280 (if fitted)
- [ ] Internal vs external temperature delta — DDOEE thermal performance

### Open questions

- [ ] Confirm Adafruit blinka on Pi 2 (ARMv7 32-bit)
- [ ] Sample rate — 1 Hz weather, 10–100 Hz vibration monitoring
- [ ] position_monitor.py — query rotctl via network or shared file?
- [ ] Wind speed observation quality threshold — empirical
- [ ] MCP3008 SPI conflict check on Pi 2

---

*When starting a new Claude session, paste this section as context:*

**Project:** Blue Rock Radio Observatory — BSc Honours Astronomy (UCLan)  
**Observer:** Steve Hawker BEng MBA FRAS, San Jose CA  
**GitHub:** https://github.com/Steve-Hawker/blue-rock-radio-observatory  
**Current phase:** Phase 2 — Site Survey (tripod arrived 2026-05-07, not yet deployed)  
**Next milestone:** Site survey on patio → ADF4351 May 12–22 → V4c May 21–Jun 12 → CAL-000  
**Key documents:** README.md for repo structure; this file for current state  
**This file:** OPEN_ITEMS.md  

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-07 | Initial document |
| 2.0 | 2026-05-08 | DUOPURUI switch; ABS sensor box design; BME280 + LSM6DSOX confirmed; Pi architecture; Phelps reviewed |
| 3.0 | 2026-05-08 | Drive bracket mounting confirmed; Cermant USB-C boards; Qwiic chain; squash ball vent; ADS-B/dump1090; ADF4351 delivery window |
| 4.0 | 2026-05-08 | TL-POE170S → Omada PoE++; Hammond 1591DBU ordered; credit card separation plate; sensors + Qwiic cables ordered; internal DDOEE BME280 decision pending; EPLZON breadboard ordered |
| 5.0 | 2026-05-10 | Arrivals: ADF4351, Omada PoE++, DUOPURUI switch, EPLZON breadboard, rivet nut kit; added outdoor Cat6 30ft × 2 to order list; added star point lug + AWG 12 ground wire; Tycon flagged as critical path |
