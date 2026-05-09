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
| ~~VCELINK M242 ethernet switch~~ | **SUPERSEDED 2026-05-08** | Replaced by DUOPURUI 1→3 switch — see below |
| DUOPURUI ethernet switch 1→3 | To order | 3-port gigabit switch — Pi 2 + Pi 3 + Pi 5; replaces VCELINK M242; needs 5V USB-C power from DN510 rail; 2.8"×2.8" fits on top of Tycon; ASIN B0FCLKWGZ1 ~$18.99 |
| QILIPSU 304 SS enclosure | To order | 350×250×150mm IP65 |
| TP-Link TL-POE170S | To order | 60W PoE injector — indoors |
| Raspberry Pi 5 (4GB) | Pending decision | Needed before Phase 4 |
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
| BME280 breakout × 2 | To order | ~$8-10 each — one internal (Pi 3 GPIO), one in dish sensor ABS box (Pi 2) |
| LSM6DSOX IMU breakout | To order | ~$5-10 — dish position verification in ABS box on dish mounting plate |
| Combined anemometer + wind vane unit | To order | ~$25-35 — single mount, pulse + analog output |
| MCP3008 ADC | To order | ~$4 — analog to digital for wind vane voltage on Pi 2 SPI bus |
| ABS project box | To purchase | Dish sensor enclosure — mounts on underside of Discovery Dish mounting plate; houses BME280 + LSM6DSOX on lid; see design notes below |
| M3 brass standoffs | To purchase | Equal height both sides — BME280 and LSM6DSOX boards on lid |
| M4 bolts | To purchase | ABS box mounting to dish plate |
| Sticky-backed foam sheet | To purchase | Lid seal — weather zone / IMU zone separation at open face |
| ~~Weatherproof housing for external BME280~~ | **SUPERSEDED 2026-05-08** | Replaced by ABS box solution — see Dish Sensor Box Design below |

---

## DDOEE — Confirmed Component Inventory

All components accounted for in Keynote layout v1:

| Component | Location on plate | Notes |
|---|---|---|
| Tycon POE-SPLT-BT-UNI-P | Left, on side | Angle bracket mount |
| DUOPURUI ethernet switch 1→3 | On top of Tycon | Velcro; replaces VCELINK M242 |
| dkplnt DN510 | Under stripboard | Rivnuts |
| EPLZON stripboard | Top, on 25mm standoffs over DN510 | USB-C sockets + voltmeters |
| Raspberry Pi 3 | Right, lower | V4c · RFI monitoring · BME280 internal sensor |
| Raspberry Pi 2 | Stacked on Pi 3 | External weather station · dish sensor ABS box via I2C cable |
| RTL-SDR V4c | Bottom centre | USB to Pi 3 |
| Airspy R2 | Bottom centre | USB to Pi 5 (Phase 4) |
| BME280 (internal) | On Pi 3 GPIO | Enclosure temp/humidity/pressure — electronics health, condensation risk |
| BME280 (external) | In dish sensor ABS box on dish mounting plate | True observing conditions — Pi 2 I2C |
| LSM6DSOX | In dish sensor ABS box on dish mounting plate | Dish elevation verification — Pi 2 I2C |
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
- I2C cable to dish sensor ABS box exits via Gland 2 bundle or small additional penetration

---

## Decisions — Resolved

| Decision | Resolution | Notes |
|---|---|---|
| Pi 5 vs Pi 3 + Pi 2 | Pi 5 preferred — single unit, USB 3.0 | Pi 3 adequate for Phase 2–3; Pi 5 needed before Phase 4 |
| Internal DDOEE ethernet cables | Cat5e unshielded | Short runs — shielding not required |
| Ferrite chokes on USB cables | Recommended | Cheap RFI mitigation — add to order list |
| 5V power distribution | Custom USB-C hub — 3-4 panel mount sockets | See POWER_ARCHITECTURE.md |
| Environmental monitoring sensor | BME280 × 2 + LSM6DSOX × 1 | Waveshare Sense HAT (C) rejected — wrong form factor, wrong sensors, wrong library ecosystem |
| Ethernet switch | DUOPURUI 1→3 gigabit switch | VCELINK M242 (1→2) superseded — three Pis require three ports; DUOPURUI needs 5V USB-C power |
| Dish sensor enclosure | ABS project box on dish mounting plate underside | See Dish Sensor Box Design below |
| Sensor board selection | Adafruit BME280 + Adafruit LSM6DSOX breakouts | Confirmed over Waveshare Sense HAT (C) — 2026-05-08 |

### Revised Pi Architecture (Phase 4)

| Device | Role | Sensor |
|---|---|---|
| Pi 5 | Airspy R2 · science chain · rotctl · EZRa | — |
| Pi 3 | V4c · RFI monitoring (rtl_power) | BME280 internal — enclosure environment, electronics health, condensation risk |
| Pi 2 | Dish sensor station — dedicated, always running | BME280 + LSM6DSOX in ABS box on dish plate; anemometer + wind vane |

**Pi 2 notes:**
- ABS sensor box mounted on underside of Discovery Dish mounting plate — moves with dish in both azimuth and elevation
- I2C cable from Pi 2 GPIO through DDOEE gland to ABS box on dish plate
- Python script logging to CSV with timestamp
- Data accessible over ethernet via DUOPURUI switch
- Power from 5V rail distribution board inside DDOEE
- Runs independently — crash does not affect science chain

---

## Dish Sensor Box Design — RESOLVED 2026-05-08

Design finalised in session. See also design/DISH_POSITION_CALIBRATION.md.

### Physical arrangement

- **Box:** ABS project box, open-bottomed shell
- **Mounting:** Underside of Discovery Dish mounting plate via M4 bolts — moves with dish in elevation and azimuth
- **Lid:** Closes open face; carries both sensor boards on equal-height M3 brass standoffs; carries cable gland
- **Separation plate:** Fixed to box walls, hangs from top wall (dish-plate side), stops short of open face leaving wiring gap. Divides interior into two zones:
  - **Weather zone:** Vented — BME280 directly below quarter-ball vent in top wall
  - **IMU zone:** Sealed — LSM6DSOX, no vent
- **Vent:** Semicircular hole in top wall of box, entirely within weather zone. Quarter-ball cap (hollow ball cap or ornament, cut and glued) provides rain protection with omnidirectional airflow
- **Lid seal:** Sticky-backed foam on lid; separation plate edge provides compression with small cutout for wiring — blocks convective mixing between zones without crushing cables
- **Gland:** In lid, weather zone side — I2C cable enters weather zone, routes under separation plate gap to reach LSM6DSOX in IMU zone

### BME280 notes
- Board on standoffs, sensor element faces upward toward vent hole
- Direct line to ambient air through quarter-ball cap
- First read after long idle periods returns stale cached value — read twice, discard first (Adafruit datasheet)

### LSM6DSOX notes
- Board on standoffs, fully enclosed in sealed IMU zone
- Z-axis perpendicular to lid surface = perpendicular to dish mounting plate
- Elevation angle: arctan2(gz, √(gx²+gy²)) after sensor mounting calibration
- See DISH_POSITION_CALIBRATION.md for full calibration procedure (Steps 1–5)

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
| POWER_ARCHITECTURE.md | Update power budget — DUOPURUI switch adds 5V USB-C load; Pi 5 decision pending | Before Phase 4 |
| DDOEE_mounting_plate_v2.svg | Redraw — DUOPURUI replaces VCELINK M242; update for Phase 4 when Pi 5 confirmed | Before Phase 4 |
| INV001_noise_budget | Complete Friis with QPL9547 real values + SAW insertion loss | Before first light |
| SAW_FILTER_DESIGN.md | ~~Identify LNA2~~ RESOLVED — QPL9547; SAW confirmation from KrakenRF pending | Soon |
| TOOLS_PLAN.md | Refresh for Stellarium, rotctl, dual-SDR, ADF4351 | Before Phase 3 |
| QUICK_REFERENCE.md | Update LO offset to 1422 MHz | Soon |
| SDR_SELECTION.md | Note V4c triplexer improvement | Soon |
| RFI_OVERVIEW.md | Note V4c triplexer improvement; skin depth calculation for QILIPSU 304SS confirmed adequate | Soon |
| DISH_POSITION_CALIBRATION.md | Update mounting location — underside of dish mounting plate confirmed; ABS box design finalised | Soon |

---

## Site Assessment — Pending

| Item | Notes |
|---|---|
| Formal site survey with tripod | Tripod arrived 2026-05-07 — not yet out of box as of 2026-05-08 |
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
| Phelps 2024 paper | **REVIEWED 2026-05-08** — filed in reading_notes/; useful baseline comparison for thesis; setup inferior to BRRO but demonstrates 1m dish urban HI detection is achievable |

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

## Dish Sensor Python Development — Requirements and Design

*Full implementation deferred — capture all objectives here first
before writing any code. See design/DISH_POSITION_CALIBRATION.md
for hardware design.*

### Objectives

1. Continuous logging of BME280 environmental data and LSM6DSOX
   position/motion data from Pi 2
2. Data accessible on MacBook via SSH session
3. Scripts run interactively over SSH — no daemon or autostart required
   initially
4. All data timestamped in UTC
5. CSV output — compatible with Python/pandas on MacBook for analysis

### Scripts planned

| Script | Purpose |
|---|---|
| `dish_sensors.py` | Core continuous logging — BME280 + LSM6DSOX to CSV |
| `sensor_calibration.py` | One-time orientation calibration at known dish position |
| `weather_summary.py` | Session summary — mean/min/max over time window |
| `position_monitor.py` | Real-time position verification vs rotctl commanded position |

### Library decision — BME280

Two candidate libraries. Decision factors to evaluate:

| Factor | Adafruit CircuitPython | bme280 (pip) |
|---|---|---|
| Installation complexity | Requires blinka + adafruit stack | Single pip install |
| Pi 2 compatibility | Blinka supports Pi 2 — verify | Pure Python — works everywhere |
| Active maintenance | Actively maintained by Adafruit | Less actively maintained |
| LSM6DSOX compatibility | Same ecosystem as LSM6DS library | Different ecosystem |
| Documentation quality | Excellent | Adequate |
| Dependency footprint | Large (blinka stack) | Minimal |
| Community support | Large | Smaller |

**Recommendation to evaluate:** If LSM6DSOX Adafruit library works
cleanly on Pi 2, use full Adafruit CircuitPython stack for both sensors
— consistent ecosystem, one import style, better documentation.
If Pi 2 compatibility is problematic, use `bme280` pip package for
BME280 and `smbus2` for LSM6DSOX direct register access.

**Decision point:** Confirm Adafruit blinka compatibility with Pi 2
(ARMv7, 32-bit) before committing to library choice.

### Data flow

```
Pi 2 (I2C sensors)
    → dish_sensors.py writes CSV to ~/data/sensors/YYYY-MM-DD.csv
    → MacBook SSH session reads/copies files as needed
    → pandas analysis on MacBook
```

No NFS mount required — SSH file transfer (scp or rsync) sufficient
for post-session analysis. Real-time monitoring via SSH and tail -f.

### CSV format

```
timestamp_utc, temp_c, humidity_pct, pressure_hpa,
accel_x_g, accel_y_g, accel_z_g,
gyro_x_dps, gyro_y_dps, gyro_z_dps,
elevation_deg_imu, elevation_deg_rotctl, position_flag
```

`position_flag` = 1 if |IMU elevation − rotctl elevation| > 0.5°

### Calibration design — critical

The IMU measures acceleration in its own sensor frame. To convert to
meaningful dish elevation angles, we must relate the sensor frame to
the dish frame and the dish frame to the sky frame.

**Step 1 — Sensor mounting calibration (one time):**
Mount sensor rigidly on lid of ABS box on dish mounting plate underside.
Record accelerometer vector when dish is at known elevation (e.g.
horizontal park position = 0°). This defines the sensor-to-dish
rotation matrix R_sd.

**Step 2 — Tripod levelling verification:**
Use spirit level on tripod head. Record accelerometer vector when
tripod is level. Any deviation from vertical gives the tripod tilt
correction T.

**Step 3 — Elevation angle derivation:**
For any dish position, apply R_sd and T to measured acceleration vector,
then compute elevation from gravity component:

```
elevation = arctan2(g_z_corrected,
            sqrt(g_x_corrected² + g_y_corrected²))
```

**Step 4 — Validation against Cas A transit:**
During commissioning, track Cas A across a range of elevations.
Compare IMU-derived elevation with rotctl commanded elevation and
with theoretical Cas A elevation from ephemeris. Three-way comparison
validates the calibration.

**Step 5 — Seasonal re-calibration:**
Repeat Steps 1-4 at start of each observing season. Log calibration
parameters in calibration/IMU_calibration.csv.

**Calibration uncertainty budget:**

| Source | Contribution |
|---|---|
| Accelerometer noise | ~0.06° (16-bit, ±2g, 100 sample average) |
| Sensor mounting alignment | ~0.1-0.5° (depends on mounting quality) |
| Tripod levelling | ~0.1° (good spirit level) |
| **Total estimated** | **~0.2-0.6°** |

Target: verify dish position to better than 0.5° — achievable with
careful mounting and calibration.

### Additional ideas — capture here before implementation

- [ ] Wind speed proxy — RMS accelerometer noise during integration
      as a measure of dish vibration / wind loading
- [ ] **Anemometer** — direct wind speed measurement preferred over
      IMU proxy. Options:
      - Simple pulse-counting cup anemometer (~$15-20) on Pi 2 GPIO
        pin — each rotation = pulse, count pulses/sec, convert to m/s.
        Simple, cheap, reliable. One additional GPIO wire.
      - Ultrasonic anemometer — no moving parts, more reliable,
        but ~$50-200. Likely overkill for this application.
      - **Preferred:** Low cost cup anemometer on GPIO pulse counter.
        Set observation quality thresholds (e.g. don't observe if
        wind > X m/s). Five years of wind data correlated with
        observation quality is genuinely useful.
- [ ] **Wind direction** — requires wind vane in addition to anemometer.
      Options:
      - Separate resistive wind vane (~$10-15) — outputs voltage
        proportional to direction, needs MCP3008 ADC on SPI bus (~$4).
        8 or 16 positions (45° or 22.5° resolution).
      - **Combined anemometer + wind vane unit (~$25-35)** — single
        mount, one cable run, both measurements. Ecowitt or generic
        Amazon units in this price range. Recommended.
      - Skip wind direction — wind speed is the critical parameter
        for observation quality; direction is useful metadata but
        not essential. Could defer.
      - **Preferred:** Combined unit ~$30. Minimal extra cost for
        both measurements from one mount.
      - **Interface:** Anemometer pulse on GPIO, wind vane voltage
        via MCP3008 ADC on SPI bus. Pi 2 handles both alongside
        I2C sensors.
- [ ] Slew settling detection — monitor IMU until position stable
      before beginning integration
- [ ] Session start/end weather report — auto-generated from CSV,
      appended to session log
- [ ] Alert if humidity > 85% inside DDOEE (condensation risk)
- [ ] Temperature compensation for ADF4351 LO frequency drift
      (use internal BME280 on Pi 3)
- [ ] Cross-reference internal vs external temperature to monitor
      DDOEE thermal performance

### Open questions before implementation

- [ ] Confirm Adafruit blinka works on Pi 2 (ARMv7 32-bit)
- [ ] Confirm LSM6DSOX I2C address does not conflict with BME280
      on same bus (LSM6DSOX: 0x6A, BME280: 0x76 — no conflict ✓)
- [ ] Determine sample rate — 1 Hz adequate for weather, 10-100 Hz
      for wind/vibration monitoring
- [ ] Decide whether position_monitor.py queries rotctl via network
      or reads a shared file written by the science Pi
- [ ] Select specific combined anemometer + wind vane unit — confirm
      pulse output for anemometer and resistive/voltage output for
      wind vane before ordering
- [ ] Determine wind speed threshold for observation quality flag —
      requires empirical testing once installed
- [ ] Confirm MCP3008 SPI bus does not conflict with other SPI devices
      on Pi 2

---

*When starting a new Claude session, paste this section as context:*

**Project:** Blue Rock Radio Observatory — BSc Honours Astronomy (UCLan)  
**Observer:** Steve Hawker BEng MBA FRAS, San Jose CA  
**GitHub:** https://github.com/Steve-Hawker/blue-rock-radio-observatory  
**Current phase:** Phase 2 — Site Survey (tripod arrived 2026-05-07, not yet deployed as of 2026-05-08)  
**Next milestone:** Site survey on patio → V4c + ADF4351 arrive ~May 22 → CAL-000  
**Key documents:** See README.md for full repository structure  
**This file:** OPEN_ITEMS.md — start here for current state  

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-07 | Initial document — hardware pending, technical questions, documentation updates, site survey items, calibration schedule, academic items, session handoff notes |
| 2.0 | 2026-05-08 | VCELINK M242 superseded by DUOPURUI 1→3 switch (3 Pis require 3 ports); ABS dish sensor box design finalised (separation plate, quarter-ball vent, lid arrangement, foam seal); BME280 + LSM6DSOX confirmed over Waveshare Sense HAT (C); sensor box mounting location confirmed (dish mounting plate underside); Pi architecture re-confirmed with enclosure BME280 on Pi 3; Phelps 2024 paper reviewed; DDOEE component inventory updated throughout |
