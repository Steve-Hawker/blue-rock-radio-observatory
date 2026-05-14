# Thermal Management Design Notes

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-13  
**Version:** 1.0  

---

## Overview

The remote sensing enclosure is a sealed stainless steel weatherproof unit housing:
- Three Raspberry Pi compute nodes (Pi 2, Pi 3, Pi 5)
- Two SDR receivers (Airspy R2, RTL-SDR Blog V4c) in a shielded junction box
- Power distribution components (Tycon PoE splitter, DC-DC converter)
- Environmental sensors (BME280)

Active cooling (fans, Peltier devices) is not viable — no large penetrations in the outer enclosure are acceptable for both weatherproofing and RF shielding reasons.

**Design principle:** Intentional passive thermal bonding through a continuous conductive chain from heat sources to the outer enclosure, which acts as the ultimate heat sink to ambient air.

---

## Heat Sources

### Raspberry Pi 5 — Primary Heat Source
- Typical power consumption: 12.5W
- Runs significantly warmer than Pi 2/3
- CPU, memory interface, USB controller all generate heat
- Also the dominant internal RF noise source — see RF_DESIGN.md

### Raspberry Pi 3
- Typical power consumption: 5W
- Moderate heat source

### Raspberry Pi 2
- Typical power consumption: 3W
- Lowest heat source in Pi cluster

### Airspy R2
- Power consumption: 1.75W
- Metal (aluminium) enclosure — self-conducting
- Designed to run warm
- Metal housing can reach 60-70°C under heavy load

### RTL-SDR Blog V4c
- Power consumption: 1.5W
- Metal enclosure — self-conducting
- Designed to run warm
- Metal housing can reach 60-70°C under heavy load

### Total Thermal Load
| Component | Power |
|-----------|-------|
| Raspberry Pi 5 | 12.5W |
| Raspberry Pi 3 | 5.0W |
| Raspberry Pi 2 | 3.0W |
| Airspy R2 | 1.75W |
| RTL-SDR V4c | 1.5W |
| PoE splitter / DC-DC converter | ~2W (estimated losses) |
| **Total** | **~26W** |

26W continuous dissipation into a sealed enclosure requires careful thermal path design.

---

## Thermal Chain

### SDR Junction Box Chain

```
SDR metal cases (60-70°C operating)
    ↓ thermal pad
Junction box steel walls
    ↓ thermal compound
Galvanised steel mounting plate
    ↓ copper braid straps
Stainless steel outer enclosure
    ↓ convection + radiation
Ambient air
```

### Raspberry Pi Chain

```
Pi SoC / board components
    ↓ heatsink (fitted to each Pi)
Pi board
    ↓ metal standoffs (deliberate thermal contact)
Galvanised steel mounting plate
    ↓ copper braid straps
Stainless steel outer enclosure
    ↓ convection + radiation
Ambient air
```

### Power Components Chain
- Tycon PoE splitter and DC-DC converter mounted directly to galvanised plate
- Thermal compound at mounting interface
- Heat conducts through plate to outer enclosure

---

## Thermal Interface Materials

### Principle
Every metal-to-metal interface has microscopic surface irregularities. Air trapped in these gaps is a poor thermal conductor (~0.025 W/mK). Thermal interface materials displace air and provide a conductive path.

### Shore Hardness
Thermal pads are rated on the Shore A scale (soft/flexible materials):

| Shore A | Behaviour | Suitability |
|---------|-----------|-------------|
| Below 20 | Very soft — flows and migrates under heat cycling | Poor — degrades over time |
| 30-60 | Conforms to surface irregularities, stable long term | **Optimal range** |
| Above 80 | Too hard — won't conform, air gaps remain | Poor — defeats purpose |

**Always verify Shore A rating in manufacturer datasheet before purchasing.**

### Material Selection by Interface

**SDR case to junction box wall (inside junction box):**
- Thermal pad preferred over compound — easier to manage in confined space
- Measure actual gap with feeler gauge before ordering
- Pad should be slightly compressed when assembled — not over or under compressed
- Recommended brands: Bergquist, Fujipoly
- Verify Shore A 30-60
- Verify thermal conductivity — minimum 3 W/mK, higher is better

**Junction box to galvanised plate:**
- Thermal compound — generous application
- Mating surfaces must be flat, clean, and degreased before application
- Recommended: Arctic Silver 5 or equivalent quality
- Avoid cheap white compound — thermal conductivity significantly lower
- Do not use silicone-based compound near RF connectors — silicone outgassing can contaminate contacts

**Galvanised plate to outer enclosure:**
- Copper braid straps at multiple points
- Maximum contact area at each strap termination
- Copper thermal conductivity ~400 W/mK vs stainless ~16 W/mK — braid straps dramatically improve the weakest link in the chain

**Pi standoffs to galvanised plate:**
- Metal standoffs only — no plastic
- Thermal compound at standoff-to-plate contact point
- Consider aluminium or copper standoffs rather than steel for better conductivity

### Thermal Conductivity Reference

| Material | Thermal Conductivity (W/mK) |
|----------|---------------------------|
| Copper | ~400 |
| Aluminium | ~205 |
| Galvanised steel | ~50 |
| Stainless steel | ~16 |
| Arctic Silver 5 | ~8.7 |
| Good thermal pad | 3-6 |
| Air | ~0.025 |

The stainless outer enclosure (~16 W/mK) is the weakest thermal link. Copper braid straps bypass this limitation at the plate-to-enclosure interface.

---

## Thermal Monitoring

### BME280 Inside Junction Box
- Monitors temperature, humidity, and barometric pressure
- Located inside junction box — monitors SDR thermal environment directly
- Connected to Pi 2 via I2C bus — see I2C_DESIGN.md
- Provides early warning of:
  - SDR thermal excursion approaching operating limits
  - Condensation risk during temperature cycling
  - Humidity ingress into sealed enclosure

### Condensation Risk
San Jose experiences significant day/night temperature cycling:
- Summer days: 35-38°C ambient
- Summer nights: 15-20°C ambient
- Delta of 15-20°C creates condensation risk in sealed metal enclosures

The BME280 dew point calculation (derived from temperature and humidity readings) provides actionable warning before condensation occurs.

**Mitigation options if condensation detected:**
- Silica gel desiccant pack inside outer enclosure — passive, requires periodic replacement
- Monitor humidity trend — rising humidity indicates seal integrity issue

### Recommended Monitoring Thresholds
| Parameter | Warning | Critical |
|-----------|---------|---------|
| Junction box temperature | 50°C | 60°C |
| Relative humidity inside | 70% | 85% |
| Dew point margin | <5°C | <2°C |

*Thresholds to be validated against actual operating data during commissioning.*

---

## Environmental Considerations — San Jose, CA

### Summer Operation
- Ambient: up to 38°C
- Solar gain on outer enclosure: potentially significant
- Enclosure in direct sun could reach 50-60°C surface temperature
- **Shade the enclosure where target acquisition allows**
- Night observing — ambient drops to 15-20°C, thermal load much reduced

### Winter Operation
- Mild — San Jose winters rarely below 5°C
- Thermal management less critical
- Condensation risk increases with lower night temperatures

### Humidity
- Generally low — dry climate aids thermal management
- Coastal influence occasionally raises humidity
- BME280 monitoring provides early warning

---

## Raspberry Pi Thermal Management

### Heatsinks
All three Pis should have heatsinks fitted:
- Pi 5 — active cooler or large passive heatsink strongly recommended
- Pi 3 — passive heatsink adequate
- Pi 2 — passive heatsink adequate

Pi 5 official active cooler is well regarded — however fan noise and vibration may be considerations for a sealed enclosure. A large passive heatsink with good contact to the mounting plate via standoffs may be preferable.

### Pi 5 Specific
At 12.5W the Pi 5 is the dominant heat source. Thermal throttling begins when SoC temperature exceeds 80°C. In a sealed enclosure without active cooling, thermal management of the Pi 5 is the primary design constraint.

**Verify Pi 5 temperatures under representative load during bench testing before field deployment.**

### Standoff Selection
- Material: aluminium or copper preferred over steel
- Size: sufficient height to allow airflow between Pi board and mounting plate
- Thermal compound at plate contact point
- Firm mechanical contact — loose standoffs create thermal gaps

---

## Heatsink Compound Application Notes

### Preparation
1. Clean all mating surfaces with isopropyl alcohol (90%+ purity)
2. Allow to dry completely
3. Inspect for burrs or high spots — sand flat if necessary
4. Degrease immediately before application

### Application
- Thermal compound: pea-sized amount at centre of smaller surface
- Spreads under clamping pressure — do not pre-spread
- Thermal pad: cut to size, remove both protective films, position carefully
- No air bubbles — apply pad flat, no angles

### Curing
- Arctic Silver 5 requires break-in period — thermal performance improves after first heat cycles
- Allow 200+ hours of operation for full cure
- Re-torque mounting fasteners after first thermal cycle

---

## Open Questions / Future Work

- [ ] Measure actual gap between SDR cases and junction box walls — determine correct thermal pad thickness
- [ ] Bench test Pi 5 temperatures under representative SDR processing load in sealed enclosure mockup
- [ ] Determine if Pi 5 active cooler fan vibration is acceptable or passive heatsink preferred
- [ ] Select and specify copper braid strap dimensions and termination method
- [ ] Specify silica gel desiccant quantity for outer enclosure volume
- [ ] Validate BME280 monitoring thresholds against real operating data
- [ ] Characterise outer enclosure surface temperature under full load in summer conditions
- [ ] Evaluate thermal paint or anodising on outer enclosure to improve radiative dissipation

---

## Related Documents
- RF_DESIGN.md — RF shielding strategy, junction box design, grounding
- I2C_DESIGN.md — BME280 sensor integration, I2C bus specification
- SENSOR_DESIGN.md — full sensor architecture
- POWER_DESIGN.md — PoE architecture, power budget, DC-DC conversion

---

*Document status: Initial design notes — pre-build*
*Last updated: May 2026*
