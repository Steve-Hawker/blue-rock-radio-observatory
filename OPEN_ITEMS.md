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
| dkplnt DN510 DC-DC 12V→5V 50W | **Arrived 2026-05-13** ✓ | ASIN B0DYK93WX8; screw terminal input; crimped ferrules required |
| DUOPURUI ethernet switch 1→3 | **Arrived 2026-05-10** ✓ | ASIN B0FCLKWGZ1; USB-C power cable included |
| EPLZON breadboard kit | **Arrived 2026-05-10** ✓ | ASIN B0DCRKNW5H |
| ADF4351 RF signal source board | **Arrived 2026-05-10** ✓ | Early — window was May 12–22 |
| RTL-SDR Blog V4c | **Arrived 2026-05-11** ✓ | Early — window was May 21–Jun 12 |
| RTL-SDR Dipole Set | **Arrived 2026-05-11** ✓ | Early — window was May 21–Jun 12 |
| Rivet nut kit (M3/M4) + setter tool | **Arrived 2026-05-09** ✓ | Same-day delivery |
| Anker USB-C to USB-C cables (2× 2-pack = 4) | **Arrived 2026-05-12** ✓ | Pi 2, Pi 3, Pi 5 (Phase 4), 1 spare |
| Cermant USB-C breakout boards (20-pack) | **Arrived 2026-05-12** ✓ | 6 on EPLZON stripboard |
| Leuchtturm plain lab notebook | **Arrived 2026-05-12** ✓ | |
| Cat6A shielded ethernet jumpers 1ft (5-pack) | **Arrived 2026-05-13** ✓ | Internal DDOEE jumpers |
| KSEIBI #5 HSS step drill | **Arrived 2026-05-13** ✓ | For cable gland holes in galvanised base plate |
| LED modules (stripboard voltage indicators) | **Arrived 2026-05-13** ✓ | Ordered 2026-05-11 |
| Cat6 patch cables (internal DDOEE) | **Arrived 2026-05-13** ✓ | Ordered 2026-05-11 |
| Rust-Oleum cold galvanising compound spray | Ordered 2026-05-11 | Due 2026-05-13 |
| Adafruit BME280 breakout | Ordered 2026-05-08 | Awaiting delivery |
| Adafruit LSM6DSOX breakout | Ordered 2026-05-08 | Awaiting delivery |
| Qwiic flat 4-pole cables × 3 | Ordered 2026-05-08 | Two in box, one spare |
| Hammond 1591DBU enclosure | Ordered 2026-05-08 | Awaiting delivery |
| QILIPSU 304 SS enclosure | Ordered 2026-05-11 | ASIN B0F12TVFC6; due 2026-05-21; shell 304 SS; DIN plate + base plate galvanised steel |
| Outdoor Cat6 cable 30ft × 2 | To order | Outdoor rated; house to DDOEE run |
| Raspberry Pi 5 (4GB) | Pending decision | Needed before Phase 4 |
| Cable gland 3/4" (19mm) × 3 | To order | Gland 1: Cat6 PoE; Gland 2: 12V DC + Cat6 sensor cable; Gland 3: RF coax |
| IP65 membrane vent | To check | QILIPSU may include one — verify on receipt; positioned between Gland 2 and Gland 3 |
| Ferrite chokes for USB cables | To order | RFI mitigation |
| Short SMA cables (internal) | To order | SDR to coax connections inside enclosure |
| M5 threaded rod (brass) | To purchase | Custom dipole elements |
| Right-angle aluminium bracket | To purchase | For Tycon mounting — 25×25×2mm |
| microSD card 32GB | To purchase | For Pi OS install |
| M3 brass standoffs | To purchase | Equal height both sides in Hammond box |
| Mounting bolts | To purchase | Hammond box to Drive bracket |
| Sticky-backed foam sheet | To purchase | Lid seal on Hammond box |
| Squash balls (40mm standard, 4-pack) | To purchase | Vent cap — ~$7 eBay; diagonal cut |
| Star point lug (brass or copper) | To purchase | Internal DDOEE grounding star point |
| AWG 12 ground wire | To purchase | Internal DDOEE ground bonds — 2.5mm² minimum |
| Ferrule kit (1.5mm² + 2.5mm²) | To check/purchase | Crimped terminals for DN510 screw terminals |
| Credit card (expired) | On hand ✓ | Separation plate — fits card guides in Hammond 1591DBU |

---

## DDOEE — Confirmed Component Inventory

| Component | Location on plate | Notes |
|---|---|---|
| Tycon POE-SPLT-BT-UNI-P | Left, on side | Angle bracket mount |
| DUOPURUI ethernet switch 1→3 | On top of Tycon | Velcro; replaces VCELINK M242 |
| dkplnt DN510 | Under stripboard | Rivnuts |
| EPLZON stripboard | Top, on 25mm standoffs over DN510 | 6× USB-C breakout sockets + voltmeters |
| Raspberry Pi 3 | Right, lower | V4c · RFI monitoring · dump1090 ADS-B |
| Raspberry Pi 2 | Stacked on Pi 3 | Dish sensor station · Hammond box via Cat6 sensor cable |
| RTL-SDR V4c | Bottom centre | USB to Pi 3 |
| Airspy R2 | Bottom centre | USB to Pi 5 (Phase 4) |
| Southwire steel handy box (SDR junction box) | On plate, bottom | Faraday shield for Airspy R2 + V4c; lid faces Pi cluster; copper tape sealed |
| BME280 (internal — junction box) | Inside SDR junction box | SDR thermal + condensation monitoring; address 0x76; I2C to Pi 2 |
| LSM6DSOX | In Hammond 1591DBU on Drive bracket | Dish elevation verification — Pi 2 I2C via Cat6 sensor cable |
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

**Bottom removable panel — 4 penetrations:**

| Position | Type | Size | Contents |
|---|---|---|---|
| 1 | Gland | 3/4" (19mm) | Cat6 PoE ethernet only — separated from all other cables |
| 2 | Gland | 3/4" (19mm) | 12V DC to Discovery Drive + Cat6 sensor cable (RJ45s cut, pairs used for I2C to Hammond box) |
| 3 | Vent | TBD | IP65 membrane vent + anti-insect mesh — check if included with QILIPSU |
| 4 | Gland | 3/4" (19mm) | RF: HI feed coax (LMR240 ~6mm OD) + dipole coax (RG174 ~2.8mm OD) |

**Notes:**
- RF cables isolated in their own gland — maximum separation from power and data
- Cat6 sensor cable: outdoor-rated Cat6, RJ45s removed, individual pairs used for I2C (SDA, SCL, VCC, GND) with spare pairs for future use; twisted pairs provide noise rejection
- ~~Combined anemometer + wind vane~~ — **REMOVED 2026-05-10**; wind data obtainable from external source
- ~~MCP3008 ADC~~ — **REMOVED 2026-05-10**; no longer required

---

## Decisions — Resolved

| Decision | Resolution | Notes |
|---|---|---|
| Internal DDOEE ethernet cables | Cat6A shielded 1ft jumpers | Arrived 2026-05-13 ✓ |
| Ferrite chokes on USB cables | Recommended | Cheap RFI mitigation |
| 5V power distribution | 6× Cermant USB-C breakout boards on EPLZON stripboard | 3 Pis + switch + 2 spare |
| Environmental monitoring sensor | BME280 + LSM6DSOX only | Waveshare Sense HAT (C) rejected; anemometer/wind vane removed |
| Ethernet switch | DUOPURUI 1→3 gigabit | Replaces VCELINK M242 — 3 Pis need 3 ports |
| PoE injector | TP-Link Omada PoE++ | Replaces TL-POE170S — ordered 2026-05-08 |
| Dish sensor enclosure | Hammond 1591DBU blue ABS | Card guides; credit card as separation plate; outside face of Drive bracket |
| Dish sensor mounting | Outside face of Discovery Drive bracket | Plate underside ruled out — fouling confirmed from photos |
| Sensor board interconnect | Qwiic flat 4-pole cable chain | BME280 → LSM6DSOX → pigtail to Pi 2 I2C |
| Sensor cable to DDOEE | Outdoor Cat6, RJ45s cut, pairs used for I2C | Twisted pairs, noise rejection, spare pairs for future |
| Separation plate material | Expired credit card | Fits card guides in Hammond 1591DBU exactly |
| Vent cap material | Standard 40mm squash ball, diagonal cut | Omnidirectional rain protection; ~$7/4-pack eBay |
| ADS-B monitoring | dump1090 on Pi 3 via V4c — Phase 3 | No extra hardware; validates V4c + SAW rejection at 1090 MHz |
| Cable gland arrangement | 4 penetrations: PoE / DC+sensor / vent / RF | RF isolated in own gland |
| Wind data | External source — no hardware required | Anemometer + MCP3008 removed from BOM |
| SDR junction box (Faraday shield) | Southwire 4"×2"×1-7/8" steel handy box | ~$2 Home Depot; shields SDRs from Pi 5 noise; lid faces Pi cluster; copper tape seal; verify SDR fit before closing |
| Internal DDOEE BME280 | **CONFIRMED 2026-05-13** — inside SDR junction box | Address 0x76 (SDO to GND); SDR thermal + condensation monitoring; exits via copper foil wrapped egress |
| Power architecture | 12V Tycon + DN510 12V→5V + Drive direct from 12V | 24V architecture considered and rejected — single DC-DC simpler; confirmed 2026-05-13 |

### Pi Architecture (Phase 4)

| Device | Role | Sensors / Software |
|---|---|---|
| Pi 5 | Airspy R2 · science chain · rotctl · EZRa | Phase 4 addition |
| Pi 3 | V4c · RFI monitoring · dump1090 ADS-B | Always present; (internal BME280 — pending) |
| Pi 2 | Dish sensor station — always running | BME280 + LSM6DSOX via I2C/Cat6 cable |

---

## Hammond 1591DBU Sensor Box Design — RESOLVED 2026-05-08

### Physical arrangement

- **Box:** Hammond 1591DBU — blue ABS, ~111×61×27mm, card guide channels
- **Separation plate:** Expired credit card — slots into card guides; divides interior into weather zone (BME280) and IMU zone (LSM6DSOX); small notch at bottom edge for cable routing
- **Lid:** Closes open face; carries both sensor boards on equal-height M3 brass standoffs; carries cable gland
- **Lid seal:** Sticky-backed foam; separation plate edge provides compression; cutout over wiring to avoid crushing
- **Mounting:** Outside face of Discovery Drive bracket via bolts — moves with dish in azimuth; elevation tracked by LSM6DSOX
- **Vent:** Squash ball (40mm standard, diagonal cut) glued over ~15-20mm hole in box wall, entirely within weather zone
- **Gland:** In lid, weather zone side — Cat6 sensor cable pairs enter, route under credit card gap to LSM6DSOX in IMU zone
- **Qwiic chain inside box:** LSM6DSOX → flat Qwiic cable → BME280

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
| ADF4351 SPI library for Pi | Python library needed | **V4c arrived — research now** |
| GPSDO reference for ADF4351 | Deferred | If LO error >1 kHz after CAL-001, upgrade to GPSDO (~$75) |
| TP-Link Omada PoE++ output wattage | Not yet confirmed | Pull datasheet when arrives; update power budget |

---

## Documentation — Updates Required

| Document | Update needed | Priority |
|---|---|---|
| DIPOLE_ANTENNA_DESIGN.md | Confirm M5 thread when dipole kit arrives | When V4c arrives |
| E001 → E002 | Create E002 when Phase 3 begins | When V4c arrives |
| POWER_ARCHITECTURE.md | **Updated v3.0 — absorbs POWER_DESIGN.md** | Done |
| ENCLOSURE_DESIGN.md | **New v1.0 — QILIPSU, junction box, build sequence** | Done |
| RF_DESIGN.md | **New v1.0 — RF shielding, ferrite spec, junction box** | Done |
| HEAT_DESIGN.md | **New v1.0 — thermal chain, interface materials, BME280** | Done |
| I2C_DESIGN.md | **New v1.0 — I2C bus, sensor addresses, cable spec** | Done |
| CABLE_DESIGN.md | **New v1.0 — Cat6, conduit, USB, ferrite BOM** | Done |
| DESIGN_README.md | **New v1.0 — design/ directory index** | Done |
| DDOEE_mounting_plate_v2.svg | Redraw — DUOPURUI replaces VCELINK M242; 6-socket power strip | Before Phase 4 |
| INV001_noise_budget | Complete Friis with QPL9547 interpolated values + SAW IL | Before first light |
| SAW_FILTER_DESIGN.md | SAW confirmation from KrakenRF pending | Soon |
| TOOLS_PLAN.md | Add dump1090 · Stellarium · rotctl · ADF4351 | Before Phase 3 |
| QUICK_REFERENCE.md | Update LO offset to 1422 MHz | Soon |
| SDR_SELECTION.md | Note V4c triplexer improvement | Soon |
| RFI_OVERVIEW.md | V4c triplexer; QILIPSU skin depth; ADS-B field validation plan | Soon |
| DISH_POSITION_CALIBRATION.md | Outside face of Drive bracket; Hammond 1591DBU + Cat6 sensor cable | Soon |

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
| Physical log book | Leuchtturm arrived 2026-05-12 ✓ — ready to use |

---

## Calibration — Pending

| Procedure | When | Notes |
|---|---|---|
| **CAL-000-V4c** | **READY TO PROCEED** | ADF4351 arrived 2026-05-10; V4c arrived 2026-05-11; both in hand |
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

- [ ] Wind speed proxy via RMS accelerometer noise (no hardware required)
- [ ] Slew settling detection before integration begins
- [ ] Session start/end weather report auto-appended to session log
- [ ] Humidity alert if internal DDOEE >85% (if internal BME280 fitted)
- [ ] ADF4351 LO temperature compensation via internal BME280 (if fitted)
- [ ] Internal vs external temperature delta — DDOEE thermal performance

### Open questions

- [ ] Confirm Adafruit blinka on Pi 2 (ARMv7 32-bit)
- [ ] Sample rate — 1 Hz weather, 10–100 Hz vibration monitoring
- [ ] position_monitor.py — query rotctl via network or shared file?

---

*When starting a new Claude session, paste this section as context:*

**Project:** Blue Rock Radio Observatory — BSc Honours Astronomy (UCLan)  
**Observer:** Steve Hawker BEng MBA FRAS, San Jose CA  
**GitHub:** https://github.com/Steve-Hawker/blue-rock-radio-observatory  
**Current phase:** Phase 2 — Site Survey (tripod arrived 2026-05-07, not yet deployed)  
**Next milestone:** Site survey on patio → **CAL-000 READY NOW** → dump1090 ADS-B → first RFI survey  
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
| 5.0 | 2026-05-10 | Arrivals: ADF4351, Omada PoE++, DUOPURUI switch, EPLZON breadboard, rivet nut kit; added outdoor Cat6 + grounding items; Tycon flagged critical path |
| 6.0 | 2026-05-10 | Ordered: QILIPSU enclosure, Cat6A shielded jumpers, step drill, cold galv spray, Cermant USB-C boards, Anker USB-C cables; ferrule kit added |
| 7.0 | 2026-05-10 | Anemometer + MCP3008 removed; cable glands revised to 4 penetrations; sensor cable = Cat6 pairs; RF isolated; POWER_ARCHITECTURE v2.0; Phase 4 power budget corrected |
| 8.0 | 2026-05-11 | V4c + dipole arrived early; CAL-000 unblocked and ready to proceed |
| 10.0 | 2026-05-13 | dkplnt DN510 arrived; Southwire junction box confirmed; internal BME280 confirmed (inside junction box, 0x76); 12V power architecture confirmed; 7 new design documents added to design/ |
