# Enclosure Design Notes

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-13  
**Version:** 1.0  

---

## Overview

The remote sensing enclosure (DDOEE) houses all active electronics for the
Discovery Dish radio astronomy installation. It is mounted at or near the tripod
base, connected to indoor infrastructure via a single Cat6 shielded ethernet
cable carrying PoE power and data.

The enclosure must satisfy several competing requirements:
- **Weatherproof** — outdoor use, San Jose climate
- **RF shielded** — sensitive SDR receivers operating at 1420MHz
- **Thermally managed** — sealed enclosure with ~26W continuous heat load
- **Portable** — entire installation assembled and disassembled per session
- **Accessible** — one-time internal build, then sealed for operation

---

## Outer Enclosure

### Product: QILIPSU 304 Stainless Steel Electrical Box

| Parameter | Value |
|---|---|
| External dimensions | 355 × 254 × 152mm (14"×10"×6") |
| Internal dimensions | ~346 × 246 × 147mm (verify against product drawing on arrival) |
| IP Rating | IP65 + NEMA 4 |
| Material | 304 stainless steel, wire drawing finish |
| Access | Hinged cover with turn latch — lockable |
| Included | Mounting plate, bonding studs (base + cover), wall brackets, NPT1/2" + NPT3/4" connectors |
| Status | Ordered 2026-05-11 — due 2026-05-21 |

### Material: 304 Stainless Steel
- Weatherproof — corrosion resistant without painting or coating
- RF shielding — adequate at 1420MHz despite lower conductivity than aluminium
- Structural — robust for repeated handling in portable installation
- Thermal conductivity: ~16 W/mK — weakest link in thermal chain; mitigated
  by copper braid straps (see HEAT_DESIGN.md)
- Wire drawing finish — good surface contact for bonding

### Material Note
- **Shell:** 304 stainless steel
- **Internal DIN plate:** galvanised steel (315×200mm, supplied with enclosure)
- **Base plate:** galvanised steel
- All drilling for cable glands goes into the galvanised base plate — not
  the stainless shell
- Apply Rust-Oleum cold galvanising compound to all cut edges after drilling

### Depth Stack Height Estimate

| Layer | Height |
|---|---|
| Plate standoffs to enclosure rear | ~10mm |
| Galvanised plate thickness | ~1.5mm |
| Component standoffs | ~10mm |
| Pi board thickness | ~4mm |
| Pi heatsink | ~15–25mm |
| Clearance to lid | ~10mm |
| **Estimated total** | **~51–61mm** |

Remaining depth (~86–96mm) available for cable management above components.
Junction box sits on plate surface — adds ~48mm (1-7/8") toward lid.

**Verify depth stack on arrival before drilling anything — tightest constraint
in the build.**

### Built-in Features

- **Bonding studs on base and cover** — primary copper braid strap attachment
  points for plate-to-enclosure grounding
- **NPT cable connectors included** — evaluate before ordering separate cable
  glands; verify IP rating
- **Wall brackets** — useful for tripod mounting with appropriate adapter

---

## Internal Mounting Plate

### Specification
- **Material:** Galvanised steel
- **Dimensions:** 315 × 200mm
- **Source:** Supplied with QILIPSU enclosure
- **Role:** Structural ground plane, RF barrier, passive heat sink

### Functions

**Structural:** All components mount to plate. Single structural element
simplifies build and maintenance.

**RF Ground Plane:** Continuous conductive surface beneath Pi cluster and
above SDR junction box. First RF barrier between Pi 5 noise source and SDRs.
Must be bonded to outer enclosure at multiple points.

**Heat Sink:** Conducts heat from all mounted components, distributes across
plate area, transfers to outer enclosure via copper braid straps. Thermal
compound at all component-to-plate interfaces.

### Component Layout

```
┌─────────────────────────────────────────┐
│           STAINLESS ENCLOSURE           │
│  ┌───────────────────────────────────┐  │
│  │       GALVANISED PLATE            │  │
│  │                                   │  │
│  │  [Pi 5]    [Pi 3]    [Pi 2]       │  │
│  │  (standoffs)                      │  │
│  │                                   │  │
│  │  [Tycon]   [DN510]  [EPLZON]      │  │
│  │                                   │  │
│  │  ┌──────────────────────────┐     │  │
│  │  │   SDR JUNCTION BOX       │     │  │
│  │  │  [Airspy R2][RTL-SDR V4c]│     │  │
│  │  │  [BME280]                │     │  │
│  │  └──────────────────────────┘     │  │
│  └───────────────────────────────────┘  │
│                                         │
│  [Cable glands on base plate]           │
└─────────────────────────────────────────┘
```

**Layout rationale:**
- Pi cluster at top — heat rises away from SDRs
- Power components mid-plate — central distribution, thermal path to plate
- Junction box at bottom — maximum separation from Pi 5
- Pi 5 physically furthest from junction box — dominant RF and heat source
- Discovery Drive powered direct from Tycon 12V output via cable gland

---

## SDR Junction Box

### Product: Southwire 4"×2"×1-7/8" Steel Handy Box (1-Gang Drawn)

| Parameter | Value |
|---|---|
| Material | Zinc plated drawn steel |
| External dimensions | ~102 × 51 × 48mm |
| Cost | ~$2 (Home Depot) |
| Lid | Fabricated from second identical box |

### Purpose
Dual-function Faraday shield:
1. **Shields SDRs FROM Pi 5 RF noise** — Pi 5 at 12.5W is the dominant
   internal broadband noise source; physical steel enclosure provides
   significant attenuation at 1420MHz
2. **Shields USB switching noise FROM RF signal path** — SDR USB cables
   generate switching harmonics; containing them inside the junction box
   prevents coupling to the antenna path

### Internal Layout

Both SDRs oriented on sides:

```
┌─────────────────────────────────────┐
│         JUNCTION BOX LID            │
│  (faces upward toward Pi cluster)   │
├─────────────────────────────────────┤
│                                     │
│  [Airspy R2 — on side]              │
│  [RTL-SDR V4c — on side]            │
│  [BME280 — fitted to wall]          │
│                                     │
│  ←30mm→ cable space                 │
├─────────────────────────────────────┤
│  Mounted on galvanised plate        │
│  (thermal compound interface)       │
└─────────────────────────────────────┘
```

**Physical fit:** Verify Airspy R2 (64×35×29mm) + V4c (69×23×13mm) fit
on sides within 102×51mm footprint before closing box. Dry fit first.

### Sealing

- Lid joint: conductive copper tape — full perimeter
- **Must use conductive adhesive copper tape** — not merely metalised tape
- Recommended: 3M 1181 or equivalent
- Gaps in mm not cm — adequate for 1420MHz shielding (λ/20 = ~10mm)
- Re-seal with fresh tape if lid ever opened
- Lid faces upward toward Pi cluster — most critical shielding face

### RF Penetrations

**RF coax entry (×2 — one per SDR):**
- Drilled holes — NOT knock-outs (irregular gaps unacceptable)
- Hole sized to snug fit of coax OD
- Copper foil tape wrapped around coax at penetration point
- SMA terminated inside junction box on coax tail
- Direct SDR connection inside shielded environment — no adapters, no bulkheads

**USB and I2C cable egress (×1 bundle):**
- Single hole near inner wall
- Bundle wrapped in copper foil tape bonded to junction box
- Creates shielded conduit at exit point
- Ferrites on all cables immediately at exit point

**BME280 I2C egress:**
- Exits via same copper-foil-wrapped bundle
- No additional penetration required

### BME280 Inside Junction Box

**Confirmed: BME280 fitted inside junction box.**

Rationale:
- Monitors SDR thermal environment directly — early warning of thermal
  excursion approaching operating limits
- Detects condensation risk during temperature cycling (especially overnight
  San Jose temperature swings)
- I2C connection exits through copper foil wrapped cable egress
- Adds negligible thermal load
- I2C address: 0x76 (SDO to GND)

See I2C_DESIGN.md and HEAT_DESIGN.md for integration details.

---

## Cable Gland Plan

**Galvanised base plate — 4 penetrations, drilled on bench with KSEIBI #5
HSS step drill before plate installation:**

| Position | Type | Contents |
|---|---|---|
| 1 | 3/4" gland | Cat6 PoE ethernet only — separated from all other cables |
| 2 | 3/4" gland | 12V DC to Discovery Drive + Cat6 sensor cable (RJ45s removed; pairs used for I2C to Hammond box) |
| 3 | IP65 vent | Membrane vent + anti-insect mesh — check if included with QILIPSU |
| 4 | 3/4" gland | RF: HI feed coax (LMR240 ~6mm OD) + dipole coax (RG174 ~2.8mm OD) |

**Notes:**
- RF in own gland — maximum separation from power and data
- Apply cold galvanising compound to all drilled edges
- Seal cables in glands with neutral-cure RTV silicone
- Evaluate QILIPSU included NPT connectors before ordering separate glands

---

## Grounding and Bonding

### Philosophy
A ground plane is only effective if continuous. Every discontinuity —
loose joint, plastic washer, unconnected shield — creates a gap in both
RF and thermal performance.

### Bond Points

**Plate to outer enclosure:**
- QILIPSU bonding studs (base and cover) — primary attachment points
- Minimum 4× copper braid straps — one at each corner of plate to nearest stud
- Braid: ~400 W/mK thermal conductivity vs stainless ~16 W/mK — essential
- Large surface area contact at termination, mechanically fastened

**Junction box to plate:**
- Thermal compound provides thermal bond
- Mechanical fastening provides RF bond
- Verify metal-to-metal contact — no paint or anodising at contact points

**Cable shields:**
- Cat6 shield drain wire: connect to enclosure ground at entry gland
- I2C cable shield: connect at Pi end only (see I2C_DESIGN.md)
- RF coax shields: via SMA connector shell

**Single point ground:**
- All DC negative returns tied to one point on galvanised plate
- Plate is system ground reference, bonded to enclosure, bonded to Cat6 shield

---

## Raspberry Pi Mounting

### Standoffs
- Material: aluminium or copper preferred — better thermal conductivity
- Height: minimum 10mm for cable routing under boards
- Thermal compound at standoff-to-plate contact point
- Re-check torque after first thermal cycle

### Pi Layout
- Pi 5: furthest from junction box — dominant RF and thermal source
- Pi 2: nearest to I2C cable entry — shortest I2C cable run
- Pi 3: nearest to reference dipole cable entry

### Heatsinks
- **Pi 5:** Large passive heatsink conducting to plate via standoffs, or
  official Pi active cooler. Active cooler vibration transmitted through
  standoffs — bench test before deciding. **Decision deferred to bench test.**
- **Pi 3:** Passive heatsink on SoC
- **Pi 2:** Passive heatsink on SoC

---

## Power Component Mounting

| Component | Method |
|---|---|
| Tycon POE-SPLT-BT-UNI-P | Angle bracket (25×25×2mm Al) + rivnuts; DIN bracket as drilling jig |
| dkplnt DN510 | 4× corner rivnuts; aluminium case to plate with thermal compound |
| EPLZON stripboard | 25mm standoffs above DN510; rivnuts into plate |
| DUOPURUI switch | Velcro on top of Tycon |

---

## External Sensor Package

### Hammond 1591DBU at Discovery Drive Bracket

- Blue ABS box with card guide channels
- Mounted on outside face of Discovery Drive bracket — moves with dish in
  azimuth; elevation tracked by LSM6DSOX
- BME280 (0x77, SDO to VCC) — field ambient environment
- LSM6DSOX IMU — dish elevation verification
- Qwiic chain: LSM6DSOX → flat Qwiic cable → BME280
- Credit card as separation plate in card guides — weather zone / IMU zone
- Squash ball vent cap (40mm standard, diagonal cut) over weather zone hole
- Cat6 sensor cable from DDOEE (RJ45s cut, pairs used for I2C) enters via
  gland in lid

See OPEN_ITEMS.md — Hammond 1591DBU Sensor Box Design for full detail.

---

## Build Sequence

Recommended assembly order to avoid rework:

1. **Verify internal dimensions** of QILIPSU on arrival — confirm depth stack height
2. **Evaluate included NPT connectors** — determine which glands to purchase
3. **Drill base plate** — cable gland holes on bench before plate installation;
   apply cold galvanising compound to all cut edges
4. **Prepare galvanised plate** — drill component mounting holes, deburr, clean
5. **Mount junction box** — thermal compound, mechanical fastening, metal-to-metal
6. **Install BME280 inside junction box** — before closing
7. **Thread coax into junction box** — before closing, generous tail inside
8. **Terminate SMA on coax** inside junction box
9. **Place SDRs** — thermal pads, connect SMA directly
10. **Route USB and I2C cables** through egress hole — copper foil wrap
11. **Close junction box lid** — copper tape seal full perimeter
12. **Mount Pi cluster** — standoffs, thermal compound, heatsinks
13. **Mount power components** — thermal compound; verify output voltages
    before connecting loads
14. **Route all internal cables** — ties, along walls, away from RF path
15. **Install rivnuts in plate** — all component mounting points
16. **Install plate in enclosure** — copper braid straps to bonding studs
17. **Install cable glands in base plate**
18. **Thread Cat6 through gland** — crimp RJ45 inside enclosure (T568B)
19. **Thread Cat6 sensor cable and RF coax through glands**
20. **Connect all internal connections** — verify before closing
21. **Bench test** — power up, all devices detected, check temperatures
22. **Seal enclosure** — verify gasket, close and fasten
23. **Field test** — full session simulation before first science run

---

## Inspection and Maintenance

### Per Session
- Visual inspection of cable glands — no movement, no moisture ingress
- Check conduit fittings properly push-fitted

### Monthly
- Check BME280 humidity readings — rising trend indicates seal issue
- Inspect copper tape on junction box lid — replace if lifting
- Check copper braid strap connections — re-torque if loose

### Annual
- Open enclosure — inspect all internal connections
- Re-apply thermal compound if components shifted
- Replace junction box copper tape seal
- Replace self-amalgamating tape on conduit joints
- Inspect cable gland seals and enclosure gasket

---

## Open Questions

- [ ] **Verify internal dimensions on arrival** — especially depth (147mm estimated)
- [ ] **Verify depth stack height** — junction box + heatsinks must clear lid
- [ ] **Evaluate included NPT connectors** — verify IP rating before ordering glands
- [ ] **Determine tripod mounting method** — wall brackets included, need adapter
- [ ] **Determine enclosure orientation** — cable gland face down preferred
- [ ] Measure all component dimensions before drilling plate
- [ ] Pi 5 heatsink: active vs passive — bench test required
- [ ] Specify copper braid strap dimensions — use QILIPSU bonding studs
- [ ] Confirm cable gland sizes against actual cable OD measurements
- [ ] Verify QILIPSU gasket material — silicone preferred over neoprene for UV

---

## Related Documents

- POWER_ARCHITECTURE.md — PoE power architecture, power budget
- RF_DESIGN.md — RF shielding, junction box detail, grounding
- HEAT_DESIGN.md — thermal management, interface materials, monitoring
- I2C_DESIGN.md — sensor integration, cable specification
- CABLE_DESIGN.md — cable specifications, conduit design, gland sizing

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-13 | Initial document — QILIPSU selected, Southwire junction box confirmed, BME280 inside junction box confirmed, 12V power architecture, 4-gland plan, 23-step build sequence |
