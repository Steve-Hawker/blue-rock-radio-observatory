# Inspection Log — Blue Rock Radio Observatory

**Observer:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory, San Jose CA  
**Started:** 2026-05-29  

*Physical inspection record for all components. One entry per component,
in arrival order. Record condition on arrival, measurements taken,
anything unexpected, and any decisions or BOM changes triggered.*

*This log complements the Build Journal (build/BUILD_JOURNAL.md) and
the equipment log (equipment/E001_2026-04-30.md). Cross-reference as
appropriate.*

*Items marked ⬜ are pending inspection. Items marked ✓ are complete.*

---

## How to add an entry

```
### [Component name] — Arrived [date] — [⬜ Pending / ✓ Complete]

**Condition on arrival:** [packaging, physical state]
**Measurements taken:** [dimensions, weights, electrical — as relevant]
**Found vs expected:** [anything different from listing/datasheet]
**Decisions/BOM changes triggered:** [anything this changes]
**Photos:** [photos/YYYY-MM-DD_component.jpg]
**Cross-references:** [E001, design/X.md, etc.]
**Notes:** [anything else worth recording]
```

---

## Index

| Component | Arrived | Inspection |
|---|---|---|
| Laufer — RTL-SDR book | 2026-05-04 | ⬜ Pending |
| SMA fixed attenuator 30dB | 2026-05-06 | ⬜ Pending |
| Amazon Basics Tripod | 2026-05-07 | ⬜ Pending |
| Rivet nut kit (M3/M4) + setter | 2026-05-09 | ⬜ Pending |
| ADF4351 RF signal source board | 2026-05-10 | ⬜ Pending |
| TP-Link Omada PoE++ injector | 2026-05-10 | ⬜ Pending |
| DUOPURUI ethernet switch 1→3 | 2026-05-10 | ⬜ Pending |
| EPLZON breadboard kit | 2026-05-10 | ⬜ Pending |
| RTL-SDR Blog V4c | 2026-05-11 | ⬜ Pending |
| RTL-SDR Dipole Set | 2026-05-11 | ⬜ Pending |
| Anker USB-C cables (4×) | 2026-05-12 | ⬜ Pending |
| Cermant USB-C breakout boards (20×) | 2026-05-12 | ⬜ Pending |
| Leuchtturm lab notebook | 2026-05-12 | ⬜ Pending |
| Rust-Oleum cold galvanising spray | 2026-05-13 | ⬜ Pending |
| Cat6A shielded ethernet jumpers 1ft (5×) | 2026-05-13 | ⬜ Pending |
| KSEIBI #5 HSS step drill | 2026-05-13 | ⬜ Pending |
| LED modules (stripboard) | 2026-05-13 | ⬜ Pending |
| Cat6 patch cables | 2026-05-13 | ⬜ Pending |
| dkplnt DN510 DC-DC 12V→5V | 2026-05-13 | ⬜ Pending |
| Adafruit BME280 breakout | 2026-05-20 | ⬜ Pending |
| Adafruit LSM6DSOX IMU breakout | 2026-05-20 | ⬜ Pending |
| Qwiic flat 4-pole cables × 3 | 2026-05-20 | ⬜ Pending |
| Hammond 1591DBU enclosure (blue) | 2026-05-20 | ⬜ Pending |
| QILIPSU 304 SS enclosure | 2026-05-24 | ⬜ Pending — priority |
| Tycon POE-SPLT-BT-UNI-P | 2026-05-29 | ⬜ Partial — see entry |

---

## Entries

---

### Laufer — *The Hobbyist's Guide to the RTL-SDR* — Arrived 2026-05-04 — ⬜ Pending

**Condition on arrival:**  
**Found vs expected:**  
**Notes:**  

---

### SMA Fixed Attenuator 30dB — Arrived 2026-05-06 — ⬜ Pending

**Condition on arrival:**  
**Measurements taken:**  
**Found vs expected:**  
**Notes:** Gwave brand. DC-8GHz, brass body, SMA M-F. Required for CAL-000
to protect V4c input — ADF4351 output ~0 dBm; 30dB attenuation gives
~-30 dBm at SDR input.  
**Cross-references:** design/ADF4351_CALIBRATION.md — LNA protection

---

### Amazon Basics Tripod — Arrived 2026-05-07 — ⬜ Pending

**Condition on arrival:**  
**Measurements taken:**  
- Mast diameter: (measure — expected 1.5" / 38.1mm; must be within Discovery Drive 2.0–5.0cm range)
- Operating height at 52": (confirm)  

**Found vs expected:**  
**Notes:** Not yet deployed to patio. Formal site survey pending.  
**Cross-references:** E001 — Tripod section

---

### Rivet Nut Kit (M3/M4) + Setter Tool — Arrived 2026-05-09 — ⬜ Pending

**Condition on arrival:**  
**Contents check:**  
- [ ] M3 rivnuts present
- [ ] M4 rivnuts present
- [ ] Setter tool complete
- [ ] Instructions included  

**Notes:** For mounting all components to QILIPSU galvanised steel plate.  
**Cross-references:** design/ENCLOSURE_DESIGN.md — Mounting Strategy

---

### ADF4351 RF Signal Source Board — Arrived 2026-05-10 — ⬜ Pending

**Condition on arrival:**  
**Measurements taken:**  
**Found vs expected:**  
**Functional check:**  
- [ ] Powers up via USB
- [ ] SPI interface accessible
- [ ] Output confirmed on test SDR  

**Notes:** 35MHz–4.4GHz. Onboard 25MHz TCXO (~10ppm). Required for
CAL-000 through CAL-004. Store with 30dB attenuator as one unit —
never connect to feed input without attenuator.  
**Cross-references:** design/ADF4351_CALIBRATION.md

---

### TP-Link Omada PoE++ Injector — Arrived 2026-05-10 — ⬜ Pending

**Condition on arrival:**  
**Measurements taken:**  
**Found vs expected:**  
**Key checks:**  
- [ ] Confirm output wattage from datasheet — must exceed 52W for Phase 4
- [ ] Confirm 802.3bt rated
- [ ] Note model number for documentation  

**Notes:** Replaces TL-POE170S. Output wattage not yet confirmed —
critical for Phase 4 power budget headroom.  
**Cross-references:** design/POWER_ARCHITECTURE.md

---

### DUOPURUI Ethernet Switch 1→3 — Arrived 2026-05-10 — ⬜ Pending

**Condition on arrival:**  
**Contents check:**  
- [ ] USB-C power cable included (expected)
- [ ] Dimensions: expected 2.8"×2.8"  

**Notes:** Replaces VCELINK M242. Three gigabit ports for Pi 2, Pi 3, Pi 5.
Powered via USB-C from DN510 5V rail.  
**Cross-references:** design/POWER_ARCHITECTURE.md

---

### EPLZON Breadboard Kit — Arrived 2026-05-10 — ⬜ Pending

**Condition on arrival:**  
**Contents check:**  
- [ ] 2× 6.8"×2.05" boards present
- [ ] 2× 3.5"×2.05" boards present
- [ ] Strip pattern confirmed — suitable for USB-C breakout board pitch (2.54mm)  

**Notes:** Larger boards for USB-C power distribution stripboard.
Smaller boards for secondary use TBD.  
**Cross-references:** design/POWER_ARCHITECTURE.md — 5V Distribution

---

### RTL-SDR Blog V4c — Arrived 2026-05-11 — ⬜ Pending

**Condition on arrival:**  
**Measurements taken:**  
- Physical dimensions: expected 23×13×69mm  

**Found vs expected:**  
**Contents check:**  
- [ ] V4c dongle
- [ ] USB cable included
- [ ] SMA connector accessible  

**Functional check:**  
- [ ] Recognised by rtl_sdr on Pi 3 or MacBook
- [ ] GQRX waterfall visible
- [ ] Bias tee functional (4.5V on SMA)  

**Notes:** Chain A RFI monitoring SDR. Also used for CAL-000, dump1090
ADS-B, and Phase 3 RFI surveys. 8-bit ADC, 1PPM TCXO, triplexer provides
28-43dB OOB isolation at 1420MHz.  
**Cross-references:** design/ADF4351_CALIBRATION.md — CAL-000

---

### RTL-SDR Dipole Set — Arrived 2026-05-11 — ⬜ Pending

**Condition on arrival:**  
**Contents check:**  
- [ ] Telescopic dipole arms (×2)
- [ ] Mounting hardware
- [ ] SMA connector  

**Measurements:**  
- [ ] Set arms to 5.25cm per element for 1420MHz (λ/4)
- [ ] Confirm arm adjustment range includes 5.25cm  

**Notes:** Phase 3 RFI monitoring antenna. Not used with dish.  
**Cross-references:** design/DIPOLE_ANTENNA_DESIGN.md

---

### Anker USB-C to USB-C Cables (4×) — Arrived 2026-05-12 — ⬜ Pending

**Condition on arrival:**  
**Contents check:**  
- [ ] 4 cables present (2× 2-pack)
- [ ] Cable lengths noted  

**Notes:** Power distribution from EPLZON stripboard to Pi 2, Pi 3,
Pi 5 (Phase 4), and one spare.

---

### Cermant USB-C Breakout Boards (20×) — Arrived 2026-05-12 — ⬜ Pending

**Condition on arrival:**  
**Contents check:**  
- [ ] 20 boards present
- [ ] 2.54mm pin pitch confirmed — fits EPLZON stripboard  

**Notes:** 6 boards will be soldered to EPLZON stripboard for 5V
power distribution rail. CC pins not connected — irrelevant for
straight 5V application from DN510 (no PD negotiation required).  
**Cross-references:** design/POWER_ARCHITECTURE.md

---

### Leuchtturm Lab Notebook — Arrived 2026-05-12 — ⬜ Pending

**Condition on arrival:**  
**Notes:** Physical observing log. Plain paper preferred for sketches
and diagrams. Numbered pages for cross-referencing with digital records.

---

### Rust-Oleum Cold Galvanising Compound Spray — Arrived 2026-05-13 — ⬜ Pending

**Condition on arrival:**  
**Notes:** For protecting cut edges on galvanised steel DIN plate and
base plate after drilling cable gland holes. Apply immediately after
drilling — before any moisture contact.  
**Cross-references:** design/ENCLOSURE_DESIGN.md — Build Sequence step 4

---

### Cat6A Shielded Ethernet Jumpers 1ft (5×) — Arrived 2026-05-13 — ⬜ Pending

**Condition on arrival:**  
**Contents check:**  
- [ ] 5 cables present
- [ ] Shielded (STP) confirmed — check connector housing is metal not plastic
- [ ] RJ45 connectors undamaged  

**Notes:** Internal DDOEE jumpers from DUOPURUI switch to Raspberry Pis.
Shielded spec is marginal improvement over Cat5e for short internal runs.

---

### KSEIBI #5 HSS Step Drill — Arrived 2026-05-13 — ⬜ Pending

**Condition on arrival:**  
**Check:**  
- [ ] Confirm step sizes include 3/4" (19mm) for cable glands
- [ ] Cutting edges sharp — no damage in transit  

**Notes:** For drilling cable gland holes in galvanised steel base plate.
Use low speed, steady pressure, cutting fluid. Drill on bench before plate
installation. Apply cold galvanising spray to all cut edges immediately.  
**Cross-references:** design/ENCLOSURE_DESIGN.md — Build Sequence step 3

---

### LED Modules (Stripboard Voltage Indicators) — Arrived 2026-05-13 — ⬜ Pending

**Condition on arrival:**  
**Contents check:**  
- [ ] Quantity and type noted
- [ ] Voltage rating confirmed suitable for 5V and 12V monitoring  

**Notes:** For visual voltage indication on EPLZON stripboard.

---

### Cat6 Patch Cables (Internal DDOEE) — Arrived 2026-05-13 — ⬜ Pending

**Condition on arrival:**  
**Contents check:**  
- [ ] Quantity noted
- [ ] RJ45 connectors undamaged  

**Notes:** Internal network connections within DDOEE.

---

### dkplnt DN510 DC-DC Converter (12V→5V) — Arrived 2026-05-13 — ⬜ Pending

**Condition on arrival:**  
**Measurements taken:**  
- Physical dimensions: expected 74×40×17.5mm — confirm  
- Screw terminal spacing: measure for ferrule selection  

**Found vs expected:**  
**Key checks:**  
- [ ] Aluminium case confirmed (not plastic)
- [ ] Screw terminal input — confirmed
- [ ] Input/output labelling clear
- [ ] Mounting hole positions measured for rivnut placement  

**Functional check (bench, before installation):**  
- [ ] Input 12V from bench supply → output measures 5.0V ±0.1V
- [ ] Output ripple <50mV (oscilloscope if available)
- [ ] No audible switching noise at operating frequency  

**Notes:** 12V→5V, 50W, 10A. Crimped ferrule terminals required for
screw input — do not use bare stranded wire. Aluminium case conducts
heat to mounting plate.  
**Cross-references:** design/POWER_ARCHITECTURE.md

---

### Adafruit BME280 Breakout — Arrived 2026-05-20 — ⬜ Pending

**Condition on arrival:**  
**Contents check:**  
- [ ] Board undamaged
- [ ] Qwiic connector(s) present — confirm dual port (in + out)
- [ ] SDO pin accessible for address selection  

**Address configuration:**  
- External dish sensor: SDO to VCC → address 0x77
- Internal junction box: SDO to GND → address 0x76  

**Notes:** Two units ordered — one for Hammond 1591DBU dish sensor box
(0x77), one for inside SDR junction box (0x76). Confirm dual Qwiic
ports before planning chain layout.  
**Cross-references:** design/I2C_DESIGN.md, OPEN_ITEMS.md — Sensor Box Design

---

### Adafruit LSM6DSOX IMU Breakout — Arrived 2026-05-20 — ⬜ Pending

**Condition on arrival:**  
**Contents check:**  
- [ ] Board undamaged
- [ ] Qwiic connector(s) present — confirm dual port  

**Address check:**  
- Default I2C address: 0x6A — no conflict with BME280 at 0x77 ✓  

**Notes:** Dish elevation angle verification. Z-axis perpendicular to
lid of Hammond box = perpendicular to dish mounting plate.
Elevation: arctan2(gz, √(gx²+gy²)) after calibration.  
**Cross-references:** design/I2C_DESIGN.md, DISH_POSITION_CALIBRATION.md

---

### Qwiic Flat 4-Pole Cables × 3 — Arrived 2026-05-20 — ⬜ Pending

**Condition on arrival:**  
**Contents check:**  
- [ ] 3 cables present
- [ ] Flat profile confirmed — fits inside Hammond 1591DBU without bunching
- [ ] JST connectors undamaged
- [ ] Cable lengths noted  

**Notes:** Two for inside Hammond box (BME280 → LSM6DSOX chain),
one spare. Flat profile important for lid clearance in compact ABS box.

---

### Hammond 1591DBU Enclosure (Blue ABS) — Arrived 2026-05-20 — ⬜ Pending

**Condition on arrival:**  
**Measurements taken:**  
- External dimensions: confirm ~111×61×27mm
- Internal dimensions: measure — credit card width is 85.6mm; confirm fits
- Card guide channel depth: measure — must accept credit card thickness 0.76mm
- Lid thickness: measure — affects standoff height selection for sensor boards  

**Found vs expected:**  
**Key checks:**  
- [ ] Credit card fits card guide channels — dry fit test
- [ ] Lid closes fully with credit card separator in place
- [ ] Wall thickness adequate for squash ball vent hole (~15-20mm)
- [ ] Gland hole location — lid, weather zone side
- [ ] M3 standoff hole positions viable for both BME280 and LSM6DSOX boards  

**Notes:** Blue ABS, card guides for credit card separation plate.
Weather zone (BME280 + squash ball vent) and IMU zone (LSM6DSOX, sealed).
Mounts on outside face of Discovery Drive bracket.  
**Cross-references:** OPEN_ITEMS.md — Hammond 1591DBU Sensor Box Design,
design/I2C_DESIGN.md

---

### QILIPSU 304 SS Enclosure — Arrived 2026-05-24 — ⬜ Pending — PRIORITY

**Condition on arrival:**  
**Measurements taken:**  
- External: confirm 355×254×152mm (14"×10"×6")
- Internal: measure — especially depth (estimated 147mm; tightest constraint)
- DIN plate dimensions: confirm ~315×200mm
- Base plate dimensions: measure
- Bonding stud positions: measure and note (for copper braid strap planning)
- NPT connector sizes included: note 1/2" and 3/4" counts  

**Depth stack check (critical):**

| Layer | Estimated | Measured |
|---|---|---|
| Plate standoffs to enclosure rear | ~10mm | |
| Galvanised plate thickness | ~1.5mm | |
| Component standoffs | ~10mm | |
| Pi board thickness | ~4mm | |
| Pi heatsink | ~15–25mm | |
| Clearance to lid | ~10mm | |
| **Total** | **~51–61mm** | |
| Remaining for cables/junction box | ~86–96mm | |

Junction box height: 1-7/8" (48mm) — must clear with margin.

**Included accessories check:**  
- [ ] DIN mounting plate present
- [ ] Bonding studs — base and cover — count and note positions
- [ ] Wall mounting brackets present
- [ ] NPT 1/2" connectors — count
- [ ] NPT 3/4" connectors — count
- [ ] Membrane vent included? (check — may eliminate separate purchase)
- [ ] Gasket material — note type (silicone preferred over neoprene)
- [ ] Key and lock functional
- [ ] Turn latch operates smoothly  

**Surface and finish check:**  
- [ ] No damage to stainless shell
- [ ] Wire drawing finish on exterior — good surface for bonding
- [ ] Galvanised plate finish — no rust or damage
- [ ] Galvanised base plate — check for any pre-drilled holes  

**Decisions triggered:**  
- If membrane vent included → remove from order list
- If NPT connectors are IP65 rated → evaluate before ordering separate cable glands
- If depth stack tighter than estimated → revise heatsink or component layout  

**Notes:** This is the primary DDOEE enclosure. All subsequent build
steps depend on confirmed internal dimensions. Do not drill anything
until measurements are taken and depth stack verified.  
**Cross-references:** design/ENCLOSURE_DESIGN.md — Open Questions

---

### Tycon POE-SPLT-BT-UNI-P — Arrived 2026-05-29 — ⬜ Partial

**Condition on arrival:** Good  
**Found vs expected:**  
- **Includes mounting brackets — not in listing description**
- Aluminium angle bar therefore not required — removed from BOM  

**Contents check:**  
- [ ] Unit undamaged
- [ ] Mounting brackets present — note dimensions and hole spacing
- [ ] Voltage selector switch accessible — confirm position
- [ ] Output voltage selector range — confirm 12V position
- [ ] DIN rails or screws for bracket included?
- [ ] Ethernet passthrough port present  

**Key checks:**  
- [ ] Set voltage selector to 12V before any connection
- [ ] Verify 12V output with voltmeter before connecting DN510
- [ ] Note input/output port labelling  

**Measurements:**  
- Mounting bracket hole spacing: measure — for rivnut placement in plate
- Unit dimensions: confirm  

**Decisions triggered:**  
- Aluminium angle bracket removed from BOM — confirmed 2026-05-29  

**Notes:** Last critical-path item for DDOEE power chain. Set to 12V.
Discovery Drive powered direct from 12V output. DN510 DC-DC powered
from 12V output → 5V rail for all Pis and SDRs.  
**Cross-references:** design/POWER_ARCHITECTURE.md, design/ENCLOSURE_DESIGN.md

---

*(add entries here as inspections are completed)*

---

## Pending Arrivals

| Component | Ordered | Est. arrival | Inspection template ready |
|---|---|---|---|
| Squash balls 40mm 4-pack | 2026-05-23 | ~2026-06-07 | Add on arrival |

---

*Last updated: 2026-05-29*
