# Cable and Conduit Design Notes

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-13  
**Version:** 1.0  

---

## Overview

This document covers all external cabling between the indoor network/power infrastructure and the remote sensing enclosure at the Discovery Dish tripod location. It also covers internal cabling philosophy and specifications.

The installation is **portable and demountable** — the entire outdoor run is assembled and disassembled daily during observing sessions. This requirement drives many of the cable and conduit decisions documented here.

---

## Design Constraints

- **Portable:** Entire outdoor run assembled and disassembled per session
- **Daily use:** Minimum 5-year design life at ~365 cycles/year = ~1,825 assembly cycles
- **WAF (Wife Acceptance Factor):** Installation must be visually tidy when assembled, completely removable when not in use
- **Environment:** Outdoor patio, San Jose CA — UV exposure significant, rain minimal (sheltered microclimate), summer heat significant
- **Route:** Approximately 22ft with 5 direction changes
- **Single cable philosophy:** One Cat6 cable carries both PoE power and ethernet data — minimise cable count

---

## Primary Cable — Cat6 Shielded Outdoor

### Specification
| Parameter | Specification |
|-----------|--------------|
| Category | Cat6 |
| Shield | F/UTP (overall foil shield + drain wire) |
| Conductor | Stranded — 7/0.12TC (7 × 0.12mm tinned copper) |
| AWG equivalent | ~26 AWG |
| Jacket | UV resistant LLDPE outdoor rated |
| Additional jacket | Waterproof HDPE per pair insulation |
| OD | 7-8.5mm (verify before ordering gland) |
| PoE rating | PoE++ capable |
| Temperature | Rated for outdoor use — verify manufacturer spec |

### Why These Specifications

**Stranded (not solid):**
- Daily assembly/disassembly — cable coiled and stored when not in use
- 5 direction changes through conduit fittings — repeated flexing
- Solid conductor work-hardens at bend points and fails within the 5-year design life
- Stranded conductor: 7/0.12TC — flexible, corrosion resistant (tinned), maintains conductivity

**F/UTP (foil shielded):**
- SDR receivers are sensitive to RFI at 1420MHz
- Cat6 cable runs alongside I2C bus in conduit — shielding reduces cross-coupling
- San Jose urban RF environment — shielding reduces ingress
- Foil shield (F/UTP) is sufficient for this application — full braid (S/FTP) unnecessary

**Outdoor UV rated:**
- San Jose sun is strong — standard PVC jacket degrades within 2-3 years
- LLDPE jacket UV resistant — full 5-year design life without degradation

**OFC (Oxygen Free Copper):**
- Better conductivity than standard copper
- Confirms genuine copper conductor not CCA (Copper Clad Aluminium)
- CCA not suitable for PoE — higher resistance causes voltage drop and heat
- Verify OFC claim: genuine OFC conductors appear golden, CCA appears silver

### Quantities
- Outdoor run: 22ft (6.7m)
- Purchase: 30ft minimum — allows for routing slack, termination tails, and one re-termination if needed
- **Product identified:** Veeloon Cat6 FTP OFC Outdoor Ethernet Cable
  - Confirmed stranded: 7/0.12TC tinned copper conductors
  - Confirmed OFC
  - UV resistant LLDPE jacket
  - FTP shielded

---

## Conduit System

### Specification
- **Material:** White Schedule 40 PVC, 3/4" nominal
- **Colour:** White — visually acceptable, does not stand out on patio
- **Assembly:** Dry fit only — no solvent cement — fully demountable
- **Fittings:** Matching white PVC sweep elbows and end fittings

### Why Schedule 40
- Rated for electrical conduit use — standard for cable protection
- Available in white — WAF requirement
- 3/4" internal diameter (~20.9mm) — passes Cat6 cable (~7-8mm OD) easily
- Passes RJ45 connector body (~18-20mm) — tight but viable for assembly method used
- Available at big box hardware stores (Home Depot, Lowe's) — pennies per foot

### Why Dry Fit (No Solvent Cement)
- Entire installation must be demountable per session
- Solvent cement creates permanent bond — unacceptable
- Friction fit of Schedule 40 fittings is adequate for a ground-level run not subject to mechanical stress
- Self-amalgamating tape at joints optional — provides weather resistance when assembled, peels off cleanly for disassembly

### Conduit Route
Starting at indoor wall exit, proceeding to tripod:

| Section | Direction Change | Fitting |
|---------|-----------------|---------|
| Wall exit to first bend | — | End cap with grommet |
| First bend | Window → patio | Sweep elbow |
| Second bend | Patio → door/wall | Sweep elbow |
| Third bend | Wall → corner | Sweep elbow |
| Fourth bend | Corner → parallel to tripod | Sweep elbow |
| Fifth bend (if needed) | Parallel → under tripod | Sweep elbow |
| Tripod end | — | End fitting to enclosure |

**Total direction changes: 4-5 × 90° sweep elbows**

### Sweep Elbows vs LB Conduit Bodies
**Decision: Sweep elbows (plumbing style)**

Rationale:
- Dry fit assembly — no glue
- Cable threaded through conduit during assembly (conduit assembled around cable)
- No need for removable cover access on LB bodies
- Sweep elbows: smaller profile, better WAF, cheaper
- Internal radius generous enough for stranded Cat6

**Assembly method eliminates the cable-pulling problem:**
Rather than pulling cable through assembled conduit, conduit is assembled around the cable:
1. Slide all fittings onto cable in correct sequence and orientation before any assembly
2. Lay cable along intended route
3. Assemble conduit section by section starting at enclosure end
4. Push fit each section and elbow progressively back toward indoor end
5. End cap/grommet at indoor end goes on cable first — before any other fittings

**Critical: Plan fitting sequence and orientation before threading cable.**
Dry run with conduit components laid out flat before threading cable to establish correct order.

### End Fittings

**Indoor end (wall entry):**
- Through-wall hole, angled slightly downward toward exterior (~3-5°) for drainage
- Snug grommet in wall hole — not sealed permanently, cable passes through daily
- No conduit inside — just cable through wall with grommet
- Cable on interior side connects directly to PoE injector/switch

**Outdoor enclosure end:**
- Conduit runs to enclosure
- Cable exits conduit through end cap with snug grommet
- Cable enters enclosure via cable gland on enclosure body
- **Note:** RJ45 connector will not pass through standard cable gland
- **Solution:** Terminate cable inside enclosure — pass bare cable through gland, crimp/terminate RJ45 inside enclosure

### Storage
When dismantled, cable remains threaded through all loose conduit fittings. Coil entire assembly together for storage. Next session: lay out and push-fit back together. No re-threading required.

---

## I2C Inter-Enclosure Cable

### Specification
| Parameter | Specification |
|-----------|--------------|
| Type | Low capacitance shielded twisted pair |
| Reference | Belden 8102 or equivalent |
| AWG | 24 AWG (7/0.2 metric equivalent) |
| Pairs | 2 pair |
| Capacitance | ~12.5 pF/ft (Belden 8102) |
| Shield | Beldfoil (100% foil) + tinned copper braid (65%) + drain wire |
| Voltage rating | 300V |
| Stranding | 7×32 stranded — flexible |

### Why Low Capacitance
I2C specification: maximum 400 pF total bus capacitance.
At 5ft with Belden 8102: ~62 pF — leaves excellent margin for device capacitance.
Standard Cat5e at ~30-50 pF/ft would use 150-250 pF for cable alone — still within spec but less margin.

### Pair Assignment
| Pair | Signals |
|------|---------|
| Pair 1 (Orange/Orange-White) | SDA + GND |
| Pair 2 (Green/Green-White) | SCL + GND |
| Pair 3 (Blue/Blue-White) | VCC 3.3V + GND (if powering sensors remotely) |
| Pair 4 (Brown/Brown-White) | Spare |

### Shield Termination
- Drain wire connected to GND at **Pi end only**
- Far end (sensor enclosure) drain wire left floating or insulated
- Prevents ground loops while maintaining EMI rejection

### Routing
- Runs alongside Cat6 in PVC conduit
- Shielding on both cables reduces cross-coupling between PoE power and I2C signals
- Inside enclosures: routed along walls, away from Pi 5 and DC-DC converters

---

## USB Cables — Internal

### Power-Only USB (Pi power supplies)
| Parameter | Specification |
|-----------|--------------|
| Type | USB-A to appropriate connector per Pi |
| Pi 5 | USB-C |
| Pi 3 | Micro USB |
| Pi 2 | Micro USB |
| Shield | Shielded preferred |
| Length | Minimum needed — no excess |
| Ferrite | Type 31, both ends |

**Data line treatment:**
- Pi 2/3 micro USB: data lines may be grounded — verify no adverse effect on boot/power behaviour
- Pi 5 USB-C: CC lines must NOT be grounded — used for power delivery negotiation

### SDR USB Cables (data carrying — critical)
| Parameter | Specification |
|-----------|--------------|
| Type | USB-A to USB-B or USB-C per SDR |
| Standard | USB 2.0 — do not use USB 3.0 |
| Shield | Shielded — mandatory |
| Length | Minimum needed |
| Ferrite | Type 31, multiple turns, both ends |
| Isolator | USB isolator (ADuM4160 based) — strongly recommended |

**Why USB 2.0:**
USB 3.0 generates broadband RF noise with harmonics that fall directly on 1420MHz. USB 2.0 is sufficient bandwidth for both Airspy R2 and RTL-SDR V4c and dramatically reduces RFI profile.

---

## Ferrite Choke Specification

### Core Material
- **Type 31** — Fair-Rite or equivalent
- Optimum frequency range: 1-300 MHz
- Covers 1420MHz with useful attenuation
- Do NOT use unspecified or cheap ferrites — frequency range and impedance unknown

### Impedance
- Minimum 100Ω at frequency of interest
- Higher is better
- Must be specified in manufacturer datasheet — if not specified, reject

### Physical
- Core must fit snugly around cable — air gaps reduce effectiveness
- Multiple turns through core dramatically increases impedance
- Power-only cables: single turn acceptable
- SDR USB cables: 3-5 turns where physically possible

### Sources
- Fair-Rite: direct or via Mouser/Digikey
- Wurth Elektronik: WE-CBF series — well specified
- TDK: ZCAT series
- **Avoid:** Amazon/AliExpress mystery ferrites — material and frequency range unknown

---

## Connector Specifications

### SMA (RF signal path)
- Direct antenna to SDR connection — no bulkhead, no adapter, no extension
- Every additional connector: insertion loss + impedance mismatch + noise ingress
- Coax terminated with SMA inside junction box — single termination only
- Quality crimp or solder termination — no push-fit SMA connectors

### RJ45 (Cat6 ethernet/PoE)
- Shielded RJ45 connectors to match shielded Cat6
- Gold plated contacts — corrosion resistance for outdoor/demountable use
- Strain relief boots — cable subject to repeated handling
- Terminate inside enclosure — RJ45 will not pass through cable gland

### I2C Terminations
- Screw terminals or soldered connections preferred over pluggable connectors
- Pluggable connectors acceptable inside enclosures for serviceability
- No RJ45 for I2C — dedicated cable only

---

## Cable Management Inside Enclosures

### Main Enclosure
- All cables routed along walls of galvanised plate
- USB and I2C cables exit junction box through single hole — copper foil wrapped
- No cable crossing RF signal path between antenna and SDR
- Minimum bend radius respected for all cables
- Cable ties at regular intervals — no loose cables vibrating against enclosure walls

### Remote Sensor Enclosure
- Short Qwiic cables for BME280 to IMU daisy chain
- I2C cable from main enclosure terminates at screw terminals
- RF coax from Discovery Dish enters directly to junction box via cable gland

---

## Cable Identification

All cables should be identified at both ends:
- Permanent marker on cable jacket
- Or colour coded heat shrink at termination points
- Document colour/label scheme here when finalised

Suggested scheme:
| Colour | Cable |
|--------|-------|
| Blue | Cat6 PoE/Ethernet |
| Red | I2C inter-enclosure |
| Black | USB power (Pi 2) |
| Black | USB power (Pi 3) |
| Black | USB power (Pi 5) |
| Yellow | SDR USB (Airspy R2) |
| Yellow | SDR USB (RTL-SDR V4c) |

---

## Bill of Materials — Cables and Conduit

| Item | Specification | Quantity | Source |
|------|--------------|----------|--------|
| Cat6 outdoor FTP stranded | Veeloon or equivalent, 30ft | 1 | Amazon |
| I2C cable | Belden 8102 or equivalent, 10ft | 1 | Mouser/Digikey |
| PVC conduit 3/4" white | Schedule 40, cut to length | ~25ft | Home Depot |
| Sweep elbows 3/4" white | Schedule 40 | 5 | Home Depot |
| End caps 3/4" white | Schedule 40 | 2 | Home Depot |
| Grommets | Sized to cable OD | 4 | Hardware store |
| Cable glands | Sized to cable OD (Cat6 ~8mm) | 2 | Amazon/Mouser |
| Ferrite chokes Type 31 | Fair-Rite or Wurth | 10 | Mouser/Digikey |
| Conductive copper tape | 3M 1181 or equivalent | 1 roll | Amazon/Mouser |
| Self-amalgamating tape | For conduit joints | 1 roll | Hardware store |
| USB isolator | ADuM4160 based | 2 | Adafruit/Mouser |
| Shielded USB cables | USB 2.0, short | 4 | Amazon |

*Quantities and sources to be confirmed during procurement phase.*

---

## Open Questions / Future Work

- [ ] Measure Cat6 cable OD precisely — confirm gland sizing
- [ ] Confirm RJ45 termination method inside enclosure — crimp tool required on site
- [ ] Verify sweep elbow internal radius is adequate for Cat6 minimum bend radius
- [ ] Confirm Belden 8102 availability and pricing — identify alternative if unavailable
- [ ] Finalise cable identification colour scheme
- [ ] Determine self-amalgamating tape reuse life — how many assembly cycles before replacement needed
- [ ] Test dry-fit conduit joint retention — verify friction fit holds under thermal cycling
- [ ] Measure actual conduit section lengths after routing survey on patio
- [ ] Confirm USB isolator compatibility with Airspy R2 and RTL-SDR V4c

---

## Related Documents
- RF_DESIGN.md — RFI mitigation, ferrite choke specification, junction box design
- HEAT_DESIGN.md — thermal management, enclosure design
- I2C_DESIGN.md — I2C bus specification, pair assignment, shield termination
- POWER_DESIGN.md — PoE architecture, voltage drop calculation
- ENCLOSURE_DESIGN.md — cable glands, mechanical installation

---

*Document status: Initial design notes — pre-build*
*Last updated: May 2026*
