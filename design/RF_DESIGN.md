# RF Enclosure Design Notes

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-13  
**Version:** 1.0  

---

This document covers the RF shielding, thermal management, and EMI mitigation strategy for the remote sensing enclosure housing the Airspy R2 and RTL-SDR Blog V4c SDR receivers, along with supporting Raspberry Pi compute nodes.

The primary science target is the 21cm hydrogen line at 1420.405 MHz. The urban RF environment (San Jose, CA) and proximity of noisy compute hardware (particularly Raspberry Pi 5) make careful RF design essential.

---

## System Architecture

### Outer Enclosure
- Stainless steel weatherproof enclosure
- Provides primary mechanical and weather protection
- Secondary RF shielding — stainless has lower conductivity than aluminium but provides useful magnetic shielding at lower frequencies
- Ultimate passive heat sink for the entire assembly

### Internal Mounting Plate
- 315mm x 200mm galvanised steel
- Dual role: structural ground plane and conductive heat sink
- All components mounted to this plate
- Provides RF barrier between Pi cluster (above) and SDR junction box (below)
- Must be bonded to outer enclosure at multiple points

### SDR Junction Box
- Southwire 4" x 2" x 1-7/8" steel handy box (~$2, Home Depot)
- Zinc plated drawn steel construction — good continuous conductivity
- Houses Airspy R2 and RTL-SDR Blog V4c
- Serves dual purpose:
  - Shields SDRs FROM Pi 5 RF noise
  - Shields SDR USB noise from RF signal path
- Lid fabricated from second identical box
- All joints sealed with conductive copper tape (3M 1181 or equivalent — must be conductive adhesive type)

### Raspberry Pi Cluster
- Pi 5 — primary science compute
- Pi 3 — RFI reference monitoring (dipole antenna at 1420MHz)
- Pi 2 — environmental sensor management
- Mounted on standoffs above galvanised plate
- Pi 5 is the dominant internal RF noise source — physically separated from SDRs by plate and junction box

---

## SDR Physical Specifications

| Device | Dimensions | Case |
|--------|-----------|------|
| Airspy R2 | 64 x 35 x 29mm | Aluminium |
| RTL-SDR Blog V4c | 23 x 13 x 69mm | Metal |

Oriented on sides, both fit within junction box leaving approximately 30mm for cable ingress/egress.

---

## RF Signal Path

### Design Principle
Minimise the number of connections, adapters, and cable lengths in the RF signal path. Every adapter, bulkhead connector, and extension cable introduces:
- Insertion loss
- Potential impedance mismatch
- Additional noise ingress points

### Implementation
- Antenna connects directly to SDR SMA input — no bulkhead connectors, no adapters, no extension cables
- Coax enters junction box through drilled hole (not knock-out) sized to snug fit
- SMA terminated inside junction box on coax tail
- Direct SDR connection inside shielded environment

### Antenna Connections
- Discovery Dish → Airspy R2 (science channel, 1420MHz HI)
- Reference dipole → RTL-SDR V4c (RFI monitoring channel, 1420MHz)
- All connections SMA

---

## USB and I2C Cable Management

### Power-Only USB (Pi power cables)
- Lower noise concern — no data switching
- Primary noise source is switching regulator harmonics
- Type 31 ferrite, single turn, at each end
- Converted to power-only by tying data lines to ground where safe
  - **Caution:** Pi 5 USB-C CC lines used for power negotiation — verify before grounding

### SDR USB Cables (data carrying — critical)
- USB 2.0 sufficient for both Airspy R2 and RTL-SDR V4c
- Use USB 2.0 rather than 3.0 where possible — significantly lower RFI profile
- Shielded USB cables throughout
- Type 31 ferrite, multiple turns, at both device and host ends
- Consider USB isolators (ADuM4160 / ADUM3160 based) for galvanic isolation
  - Breaks ground loops
  - Prevents Pi USB controller noise conducting directly into SDR
  - USB 2.0 bandwidth sufficient

### Cable Egress Point
- Single hole near inner wall of junction box for all cable exits
- Bundle wrapped in copper foil tape bonded to junction box and galvanised plate
- Creates shielded conduit — converts potential weak point into controlled penetration
- Ferrites on all cables immediately at exit point

### I2C Bus
- Runs from Pi 2 to BME280 environmental sensor
- BME280 located inside junction box for SDR thermal monitoring
- I2C exits junction box through copper foil wrapped egress point
- See I2C_DESIGN.md for cable specification and bus details

---

## Shielding Strategy

### Pi 5 RF Noise Mitigation
The Raspberry Pi 5 generates significant broadband RF noise including:
- CPU and memory interface harmonics
- HDMI emissions
- Onboard switching regulator noise
- USB controller noise

Mitigation layers (Pi 5 → SDRs):
1. Physical separation — Pi cluster mounted above, SDRs below
2. Galvanised steel mounting plate — first RF barrier and ground plane
3. Junction box steel walls — second RF barrier
4. Copper tape sealed lid on junction box — facing toward Pi 5, most critical face

### Slot and Gap Control
At 1420MHz, λ = 21cm. Any slot or gap longer than λ/20 (~1cm) becomes an effective antenna.

- Junction box construction — drawn steel, no seams, excellent
- Lid joint — sealed with conductive copper tape, gaps in mm not cm
- Cable penetrations — drilled holes sized to snug fit, wrapped in copper foil
- Knock-outs NOT used — irregular fit unacceptable

### Shielding Materials

| Material | Conductivity | Notes |
|----------|-------------|-------|
| Copper tape | ~400 W/mK | Best — used for sealing joints and cable egress |
| Aluminium | ~205 W/mK | Excellent at 1420MHz, skin depth ~2.2µm |
| Galvanised steel | ~50 W/mK | Good broadband, adds magnetic shielding |
| Stainless steel | ~16 W/mK | Lower conductivity, adequate for outer enclosure |

### Grounding and Bonding
- All metal elements bonded together deliberately
- Junction box to plate — thermal compound interface plus mechanical bond
- Plate to outer enclosure — multiple bond points, copper braid straps preferred
- Copper braid conductivity (~400 W/mK) dramatically better than stainless for bonding straps
- A ground plane with gaps is not a ground plane

---

## Thermal Management

### Design Principle
Active cooling (fans) in a sealed enclosure merely redistributes heat internally. No large penetrations in the outer enclosure are acceptable. Solution: intentional passive thermal bonding through the enclosure hierarchy.

### Thermal Chain

```
SDR cases
    → thermal pad (inside junction box)
        → junction box steel walls
            → thermal compound (junction box to plate interface)
                → galvanised steel plate (ground plane / heat sink)
                    → copper braid straps
                        → stainless outer enclosure
                            → ambient air
```

### SDR Operating Temperatures
- Nominal range: -10°C to +40°C ambient
- Metal housings can reach 60-70°C under heavy load
- San Jose summer ambient: up to 38°C
- Enclosure solar gain: potentially significant — shade where possible

### Thermal Interface Materials

**Junction box to galvanised plate:**
- Thermal compound, generous application
- Arctic Silver or equivalent quality — avoid cheap white compound
- Mating surfaces must be flat, clean, and degreased

**SDR cases to junction box walls (inside):**
- Thermal pads preferred over compound in confined space
- Quality brands: Bergquist, Fujipoly
- Match pad thickness to gap — slight compression optimal
- Avoid pads that are too hard (won't conform) or too soft (flows under compression)

**Plate to outer enclosure:**
- Copper braid straps at multiple points
- Maximum contact area

### Thermal Monitoring
- BME280 sensor located inside junction box
- Monitors: temperature, humidity, barometric pressure
- Provides early warning of:
  - Thermal excursion approaching SDR limits
  - Condensation risk (temperature cycling, especially overnight)
  - Humidity ingress into sealed enclosure

### San Jose Climate Considerations
- Dry heat — reduced humidity-related thermal issues
- Night observing — ambient drops significantly, typically below 20°C
- Temperature cycling between day and night creates condensation risk in sealed enclosures
- BME280 monitoring addresses this directly

---

## Environmental Sensor Integration

### BME280 Placement — Inside Junction Box
Rationale:
- Monitors SDR thermal environment directly
- Detects condensation risk before damage occurs
- I2C connection exits through copper foil wrapped cable egress
- Adds negligible thermal load

### Additional Environmental Context
- Second BME280 or equivalent at dish/antenna location
- IMU for dish orientation tracking
- See SENSOR_DESIGN.md for full sensor architecture

---

## RFI Reference Channel

### Pi 3 + Dipole Antenna Architecture
The Pi 3 runs a reference dipole antenna also tuned to 1420MHz. This serves as a hardware-assisted RFI monitoring system:

- RFI correlated between reference dipole and science dish = terrestrial interference → flag and excise
- Signal uncorrelated between channels = potentially real astronomy
- Inspired by multi-station correlation methodology (Qin et al. 2025, arXiv:2508.00386)

This architecture converts the urban RF environment from a liability into a characterised and managed parameter.

---

## Known RFI Sources — San Jose Urban Environment

At 1420MHz in Silicon Valley:
- Dense WiFi environment (2.4GHz adjacent, harmonics)
- Cellular infrastructure
- General urban broadband RF noise floor

Mitigation:
- Shielded cabling throughout (Cat6 F/UTP, shielded USB, SMA direct connection)
- Reference channel RFI flagging pipeline
- Long integration times with contaminated data excision
- See RFI_PIPELINE.md for software mitigation strategy

---

## Key References

- Qin et al. (2025) — Noise Reduction Method for Radio Astronomy Single Station Observation Based on Wavelet Transform and Mathematical Morphology. arXiv:2508.00386 [astro-ph.IM]
- RTL-SDR Blog V4 documentation
- Airspy R2 technical specifications
- Fair-Rite Type 31 and Type 43 core material datasheets

---

## Open Questions / Future Work

- [ ] Verify Pi 5 USB-C CC line behaviour before grounding data lines
- [ ] Confirm Airspy R2 enclosure material (aluminium vs plastic)
- [ ] Select and specify USB isolator model
- [ ] Measure actual junction box internal temperature under operating load
- [ ] Characterise San Jose RFI environment at 1420MHz before first light
- [ ] Evaluate need for additional thermal monitoring outside junction box
- [ ] Document final thermal interface material selections and part numbers

---

*Document status: Initial design notes — pre-build*
*Last updated: May 2026*
*See also: I2C_DESIGN.md, SENSOR_DESIGN.md, RFI_PIPELINE.md, POWER_DESIGN.md*
