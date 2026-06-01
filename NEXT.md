# What To Do Next — Blue Rock Radio Observatory

*Single reference for session start. Updated end of each session.
For full detail see OPEN_ITEMS.md, BUILD_JOURNAL.md, LEARNING_PLAN.md.*

**Last updated:** 2026-06-01 — ADF4351 script + guide complete; NEXT.md updated  
**Current phase:** Phase 2 → Phase 3 transition  

---

## Do Now — No Dependencies

These are ready to execute today.

### Build
- [ ] **QILIPSU arrival inspection** — open the box, take measurements,
      complete inspection checklist in `build/INSPECTION_LOG.md`
      — especially depth stack verification (tightest constraint in build)
      and check for included membrane vent
- [ ] **Tycon inspection** — complete `build/INSPECTION_LOG.md` entry;
      measure mounting bracket hole spacing for rivnut placement;
      confirm 12V selector position
- [ ] **Home Depot run** — Southwire 4"×2"×1-7/8" steel handy box (~$2);
      pick up while there: M3 brass standoffs, mounting bolts for Hammond box,
      sticky-backed foam sheet, AWG 12 ground wire, star point lug,
      ferrule kit (1.5mm² + 2.5mm²), copper braid straps

### Calibration
- [ ] **CAL-000** — V4c SDR baseline with ADF4351 — hardware ready, script ready
      Procedure: `design/ADF4351_CALIBRATION.md`
      Script: `python3 scripts/adf4351_control.py --cal000`
      Guide: `design/ADF4351_CONTROL_GUIDE.md`
      Prerequisites: Pi 3 OS installed, SPI enabled, dependencies installed, ADF4351 wired

### Software
- [x] **ADF4351 SPI Python script written** — `scripts/adf4351_control.py` ✓
- [x] **ADF4351 user guide written** — `design/ADF4351_CONTROL_GUIDE.md` ✓
- [ ] **Enable SPI on Pi 3** — `sudo raspi-config` → Interface Options → SPI
- [ ] **Install Python dependencies on Pi 3** — `pip3 install RPi.GPIO spidev`
- [ ] **Wire ADF4351 to Pi 3 GPIO** — see `design/ADF4351_CONTROL_GUIDE.md`
- [ ] **Install Raspberry Pi OS on Pi 3** — fresh install on microSD

### Learning
- [ ] **Ansys half-wave dipole course** — free, do before dipole installation
      https://innovationspace.ansys.com/product/design-of-the-half-wave-dipole/
- [ ] **Write first LEARNING_LOG entry** — dipole session + antenna current
      question; pass to Claude to append

---

## Waiting On Deliveries

| Item | Est. arrival | What it unblocks |
|---|---|---|
| Squash balls 40mm × 4 | ~2026-06-07 | Hammond 1591DBU sensor box build |
| Marr, Snell & Kurtz Vol. 1 + Vol. 2 | ~mid-Jun 2026 | Structured reading programme |
| UCLan library response | ~mid-Jun 2026 | Confirms textbook availability |

---

## Waiting On Other Steps

| Item | Blocked by | Notes |
|---|---|---|
| Hammond 1591DBU build | Squash balls (vent cap) | All other parts in hand |
| DDOEE internal build | Southwire handy box + remaining BOM items | See bench build sequence below |
| First RFI survey | Pi 3 OS install + dipole mounted | |
| dump1090 ADS-B | V4c connected to Pi 3 | SAW filter field validation |
| CAL-001 through CAL-004 | HI feed (due Aug 2026) | ADF4351 + feed + dish required |
| First light — Cas A | Discovery Dish + Drive (due Aug 2026) | |

---

## Bench Build Sequence

When ready to build the DDOEE — do in this order:

1. Complete all inspections (`build/INSPECTION_LOG.md`)
2. Verify QILIPSU depth stack — confirm Pi heatsink clears lid
3. Drill cable gland holes in galvanised base plate (bench, before installation)
   — apply Rust-Oleum cold galv to all cut edges immediately
4. Prepare galvanised DIN plate — drill component holes, deburr, clean
5. Mount junction box (Southwire handy box) to plate — thermal compound
6. Install BME280 inside junction box (0x76, SDO to GND)
7. Thread RF coax into junction box — generous tail inside
8. Terminate SMA on coax inside junction box
9. Place SDRs — thermal pads, connect SMA directly
10. Route USB + I2C cables through egress — copper foil wrap
11. Close junction box lid — copper tape seal full perimeter
12. Mount Pi cluster — standoffs, thermal compound, heatsinks
13. Mount power components (Tycon, DN510, EPLZON stripboard)
    — verify output voltages before connecting loads
14. Solder 6× Cermant USB-C breakout boards to EPLZON stripboard
15. Route all internal cables — ties, along walls
16. Install plate in QILIPSU — copper braid straps to bonding studs
17. Install cable glands in base plate
18. Thread and terminate all external cables
19. **Bench test** — power up, all devices detected, check temperatures
20. Seal enclosure

*Full detail: `design/ENCLOSURE_DESIGN.md` — Build Sequence*

---

## Still To Order / Purchase

| Item | Where | Notes |
|---|---|---|
| Outdoor Cat6 cable 30ft × 2 | Amazon | Outdoor rated, stranded |
| Cable glands 3/4" × 3 | Amazon/hardware | Check QILIPSU NPT connectors first |
| Short SMA cables (internal) | Amazon | SDR to coax connections |
| Ferrite chokes Type 31 | Mouser/Digikey | Not generic Amazon ferrites |
| microSD card 32GB | Amazon/local | Pi OS install |
| Thermal pads | Amazon | Measure SDR-to-box gap first |
| Copper braid straps | Amazon/electronics | Plate-to-enclosure bonding |
| Silica gel desiccant | Amazon | Inside QILIPSU |

---

## Learning Queue

In priority order:

1. Ansys half-wave dipole course — **now, before installation**
2. Laufer — tricks, performance, antennas chapters — **now, V4c in hand**
3. Clark & Clark — Section 1 (GNU Radio installation and basics) — **May–Jul 2026**
4. Briggs, Bell & Kesteven 2000 — abstract + intro — **soon**
5. Urban RFI paper arXiv:2505.19372 — **soon, site assessment context**
6. Marr Vol. 1 — when received from UCLan library
7. NRAO ERA — receiver systems — before first RFI survey

---

## Open Academic Items

- [ ] Response from Dr Megan Argo re: AI use policy — sent 2026-05-04
- [ ] Response from Jason Kirk — same email
- [ ] KrakenRF SAW filter confirmation (TA1077A / TA2494A) — follow-up needed
- [ ] Verify Discovery Dish HI feed polarisation — before dipole installation

---

*Full details always in OPEN_ITEMS.md.  
Build narrative in build/BUILD_JOURNAL.md.  
Learning curriculum in LEARNING_PLAN.md.*
