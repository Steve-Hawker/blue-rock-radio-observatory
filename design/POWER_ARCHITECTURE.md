# Power Architecture — Blue Rock Radio Observatory

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-04  
**Version:** 1.4  

---

## Overview

This document describes the power distribution architecture for the
Blue Rock Radio Observatory DDOEE (Discovery Outdoor Electronics
Enclosure) mounted on the tripod. A single Power over Ethernet (PoE)
cable runs from the house to the DDOEE, carrying both network data
and 60W of power. Inside the DDOEE, a PoE splitter distributes
regulated 5V and 12V to all components.

---

## Enclosure

**QILIPSU 304 Stainless Steel Electrical Box** replaces the KrakenRF DDOEE.

| Parameter | QILIPSU | KrakenRF DDOEE |
|---|---|---|
| External dimensions | 350 × 250 × 150mm | ~350 × 220 × 80mm |
| Internal volume | ~310 × 205 × 120mm | 304 × 184 × 60mm |
| Material | 304 stainless steel | Die-cast aluminium |
| IP rating | IP65 | IP65 |
| Mounting plate | 315 × 200mm galvanised steel · DIN compatible | Custom aluminium plate |
| Lock | Key lock included | Screws |
| Cable entry | Bottom access panel + gasket | Cable glands |
| Price | ~$90 | ~$165 |
| **Verdict** | **Selected — larger, cheaper, lockable** | Not selected |

**WiFi note:** The Discovery Drive mounts on the tripod mast above the
enclosure — it is not inside the enclosure. WiFi signal is unobstructed.
The QILIPSU houses only the SDRs, Pi, PoE splitter, and power components.

**Stainless steel drilling note:** 304 stainless steel requires hardened
stainless-rated hole saws or knockout punches for cable gland penetrations.
Standard HSS drill bits will work with patience and cutting fluid but
stainless work hardens quickly — use sharp bits, low speed, steady pressure.

---

## Selected Components

| Component | Role | Location |
|---|---|---|
| TP-Link TL-POE170S | PoE injector — 60W 802.3bt | Indoors, cable head |
| Tycon POE-SPLT-BT-UNI-P | PoE splitter — 12V selected + PoE passthrough | DDOEE (outdoors) |
| dkplnt DN510 | 12V→5V DC-DC converter — 50W 10A aluminium | DDOEE (outdoors) |
| CAT6 ethernet cable | Data + power to DDOEE | House to tripod |

### Why these components

**TL-POE170S:** 802.3bt (PoE++) at 60W — confirmed sufficient for
all loads with +20W headroom after cable losses. Indoor unit,
0°C to 45°C operating temperature — appropriate for house installation.

**Tycon POE-SPLT-BT-UNI-P:** Industrial grade, -40°C to +75°C
operating temperature — essential for outdoor DDOEE installation in
San Jose summer conditions where internal enclosure temperature could
exceed +40°C. VDC output is **selectable — one voltage at a time**.
Set to **12V** for this installation. 72W combined output from 90W
input. DIN mount metal housing.

**Important correction from earlier versions:** The Tycon splitter
does NOT simultaneously output 5V and 12V. The selector switch sets
ONE output voltage. Therefore a separate DC-DC converter is required
to generate the 5V rail from the 12V output.

**Murata DC-DC modules considered and rejected:** Not available for
this application.

**12V→5V DC-DC converter — dkplnt DN510 selected:**

| Parameter | Value |
|---|---|
| Part number | DN510 |
| Brand | dkplnt |
| Input voltage | 11–35V DC (12V/24V nominal) |
| Output voltage | 5V ±1.5% |
| Output current | 10A max |
| Output power | 50W max |
| Efficiency | 95% typical |
| Ripple and noise | 50 mVp-p typical |
| Load regulation | ±0.2% |
| Protections | Over-voltage, over-current, over-temperature, short circuit |
| Case material | **Aluminium** |
| Dimensions | 74 × 40 × 17.5mm |
| Weight | 40g |
| Mounting | Surface mount — 4 corner holes |
| Price | $9.99 |

## Mounting Strategy

All components mount directly to the galvanised steel mounting plate
(~315 × 200mm) via rivet nuts (rivnuts). No DIN rail required.

**Rivet nuts:** M3 or M4 rivnuts inserted into the galvanised plate
provide clean threaded fixings without welding. All components with
mounting holes bolt directly to the plate via rivnuts.

### Component mounting methods

**Tycon POE-SPLT-BT-UNI-P:**
The Tycon has a DIN mount bracket. Rather than using DIN rail, fabricate
a right-angle aluminium bracket (25×25×2mm angle aluminium, hardware
store, ~$2) and use the DIN mount as a drilling template/jig to mark
the hole positions on the angle aluminium. Bolt the angle aluminium to
the mounting plate via rivnuts, then attach the Tycon to the angle
aluminium using the DIN mount screw holes. The DIN bracket earns its
keep as a fabrication jig rather than for its intended purpose.

**dkplnt DN510 DC-DC converter:**
Four corner mounting holes — M3 or M4 rivnuts in plate, bolts through
converter feet. Mount with aluminium case in thermal contact with plate
for heat dissipation (trivial at ~1.3W dissipation).

**Raspberry Pi 3 / Pi 2:**
Standard Pi mounting holes — M2.5 standoffs into rivnuts, Pis sit
on standoffs above the plate.

**VCELINK M242 ethernet switch:**
Small unit (53×57mm) — adhesive mount or small L-bracket. Minimal
weight, not critical.

**Airspy R2 / RTL-SDR V4c:**
USB connected to Pi — secure with velcro or small cable bracket.
Position to keep SMA connectors accessible and coax runs short.

**ADF4351:**
Has mounting holes — rivnuts and bolts, position close to Pi GPIO header.

**Thermal:** At 95% efficiency with ~25W load, heat dissipation is
approximately 1.3W — trivial. Aluminium case mounted to galvanised
plate provides adequate thermal path to enclosure exterior.

**Tobsun EA50-5V considered and rejected:** Case appears to be composite/
plastic rather than metal despite visual similarity. Rejected in favour
of confirmed aluminium dkplnt DN510.

**Phihong POE48-120BT-R considered and rejected:** Maximum operating
temperature +40°C — insufficient for outdoor DDOEE installation.
See equipment/datasheets/README_DATASHEETS.md.

---

## PoE Standard Analysis

Analysis confirmed 802.3bt T3 (60W) as the correct standard for
this installation.

| Standard | Port budget | After cable loss | Headroom | Verdict |
|---|---|---|---|---|
| 802.3af (PoE) | 15.4W | ~12.5W | -12W deficit | Insufficient |
| 802.3at (PoE+) | 30W | ~24.5W | ~-0.2W | Marginal |
| **802.3bt T3 (PoE++)** | **60W** | **~52W** | **+20W spare** | **Recommended ✓** |
| 802.3bt T4 (PoE++) | 100W | ~90W | +58W spare | Over-specced |

The TL-POE170S is 802.3bt T3 rated at 60W — exactly the recommended
standard with comfortable headroom.

---

## Architecture Diagram

```
Cable head / router (indoors)
        |
        | standard ethernet
        |
TL-POE170S PoE injector (indoors)
        |
        | CAT6 ethernet (data + 48V PoE, up to 60W)
        | [single cable to DDOEE]
        |
Tycon POE-SPLT-BT-UNI-P (inside DDOEE) — set to 12V
        |                    |
        | RJ45 data          | 12V DC
        |                    |
    VCELINK switch      Discovery Drive
        |               12V→5V DC-DC converter (30-40W)
    Pi 3 ethernet               |
    Pi 2 ethernet           5V rail
                            Pi 3 (power)
                            Pi 2 (power)
                            VCELINK (USB-C)
                            Airspy R2
                            RTL-SDR V4c
                            ADF4351
                            HI Feed LNA (via bias tee)
```

---

## Power Budget — Current Architecture (Pi 3 + Pi 2)

*Phase 1–3: Two Raspberry Pi configuration*

| Component | Rail | Current | Power | Notes |
|---|---|---|---|---|
| Discovery Drive | 12V | ~975 mA | **11.70W** | Dominant load · spin-up spike |
| Raspberry Pi 3 | 5V | ~1000 mA | **5.00W** | Moderate load · 7.5W peak |
| Raspberry Pi 2 | 5V | ~600 mA | **3.00W** | Moderate load |
| Airspy R2 | 5V | ~350 mA | **1.75W** | |
| RTL-SDR V4c | 5V | ~300 mA | **1.50W** | Includes dipole bias tee |
| ADF4351 RF source | 5V | ~250 mA | **1.25W** | Calibration only — intermittent |
| HI Feed LNA | 5V | ~100 mA | **0.50W** | Via Airspy R2 bias tee |
| **Steady-state total** | | | **24.7W** | All components running |
| **Peak (spin-up + Pi burst)** | | | **~32W** | |
| **Recommended supply** | | | **≥40W** | 25% headroom |
| **TL-POE170S available (after cable loss)** | | | **~52W** | +20W above recommended |

**5V rail total:** ~13W steady-state  
**12V rail total:** ~12W steady-state  

---

## Power Budget — Phase 4 Architecture (Pi 5, pending decision)

*Planned upgrade — replaces Pi 3 + Pi 2 with single Raspberry Pi 5*  
*See E001 equipment log — pending hardware decision*

| Component | Rail | Current | Power | Notes |
|---|---|---|---|---|
| Discovery Drive | 12V | ~975 mA | **11.70W** | Unchanged |
| Raspberry Pi 5 | 5V | ~2500 mA | **12.50W** | Replaces Pi 3 + Pi 2 |
| Airspy R2 | 5V | ~350 mA | **1.75W** | Unchanged |
| RTL-SDR V4c | 5V | ~300 mA | **1.50W** | Unchanged |
| ADF4351 RF source | 5V | ~250 mA | **1.25W** | Unchanged |
| HI Feed LNA | 5V | ~100 mA | **0.50W** | Unchanged |
| **Steady-state total** | | | **29.2W** | +4.5W vs current |
| **Peak** | | | **~37W** | Pi 5 burst |
| **Recommended supply** | | | **≥46W** | 25% headroom |
| **TL-POE170S available (after cable loss)** | | | **~52W** | +6W above recommended |

**5V rail total:** ~17.5W steady-state (+4.5W vs current)  
**12V rail total:** ~12W steady-state (unchanged)  

**Note:** Pi 5 consumes more power than Pi 3 + Pi 2 combined but the
TL-POE170S still provides adequate headroom. The Tycon splitter's
5V @ 14A (70W) output has ample capacity for the Pi 5.

**Note on Pi 5 PoE:** If a Pi 5 PoE HAT is used, the Pi 5 draws
power directly from the PoE passthrough port of the Tycon splitter
rather than the 5V rail — this simplifies wiring but the total
power budget is unchanged.

---

## Thermal Considerations

The DDOEE is an aluminium IP65-rated enclosure mounted on a tripod
in direct San Jose sun. Worst case internal temperature:

- Ambient air: up to 38°C (San Jose summer maximum)
- Solar loading on enclosure: +10–15°C above ambient
- Internal component dissipation: +5–10°C above enclosure wall
- **Estimated internal peak: ~55–65°C**

Component temperature ratings:
- Tycon POE-SPLT-BT-UNI-P: **+75°C maximum** ✓
- Raspberry Pi 3/5: throttles at 80°C, safe to 85°C ✓
- Airspy R2: rated to 60°C — marginal in worst case
- RTL-SDR V4c: aluminium enclosure, thermal pad — adequate ✓

The DDOEE thermal pads are designed to sink heat to the enclosure
wall. Ensure all components are in thermal contact with the mounting
plate or thermal pads. The aluminium enclosure wall acts as a heatsink.

**Action:** Monitor Airspy R2 temperature during first summer session.
If thermal throttling occurs, add thermal pad between Airspy R2
enclosure and DDOEE wall.

---

## Wiring Notes

**5V rail wiring:** Use minimum 20AWG wire for 5V distribution.
At 3.5A (Phase 4 peak), 20AWG keeps voltage drop below 0.1V over
typical DDOEE internal runs of <300mm.

**12V rail wiring:** Use minimum 22AWG wire for Discovery Drive.
At 1A, voltage drop is negligible over short internal runs.

**Connector discipline:** Use consistent connector types throughout.
JST or Anderson Powerpole for power distribution — not bare wire
terminals that can short against the aluminium enclosure.

**Cable glands:** Route power and signal cables through separate
cable glands where possible to minimise RF interference from power
wiring entering the SDR signal chain.

---

## References

- equipment/datasheets/TP-Link_TL-POE170S.pdf
- equipment/datasheets/Tycon_POE-SPLT-BT-UNI-P.pdf
- equipment/datasheets/Phihong_POE48-120BT-R.pdf (rejected)
- equipment/E001_2026-04-30.md — Pi 5 pending hardware decision
- design/DUAL_SDR_ARCHITECTURE.md — signal chain context

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-04 | Initial document — TL-POE170S + Tycon splitter selected, dual power budget (Pi 3+2 current, Pi 5 Phase 4), thermal analysis |
| 1.1 | 2026-05-04 | Add QILIPSU enclosure section — replaces KrakenRF DDOEE, comparison table, WiFi note, stainless drilling note |
| 1.2 | 2026-05-07 | Correct Tycon output — single selectable voltage, set to 12V; add DC-DC converter requirement; Murata rejected; Meanwell candidate |
| 1.3 | 2026-05-07 | Select dkplnt DN510 — aluminium case, 50W, 95% efficiency, $9.99; Tobsun rejected (plastic case); rivet nut mounting to galvanised plate |
| 1.4 | 2026-05-07 | Remove DIN rail — not required; add full mounting strategy section; Tycon DIN bracket repurposed as drilling jig for angle aluminium bracket |
