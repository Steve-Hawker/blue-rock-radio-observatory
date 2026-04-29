# Quick Reference — Before Every Session

## Pre-session checklist

- [ ] Check equipment version still current (any changes since last session?)
- [ ] If equipment changed → create new E00X file BEFORE observing
- [ ] Confirm LNA power supply on
- [ ] Confirm SDR connected and recognised by OS
- [ ] Confirm tracking drive responding
- [ ] Note current weather conditions
- [ ] Note any unusual local RF activity (events, construction, etc.)
- [ ] Record LST at session start

## Key frequencies

| Line | Rest frequency |
|---|---|
| HI 21cm | 1420.405752 MHz |
| M31 HI (systemic) | ~1422.2 MHz (blueshifted, -300 km/s) |
| M31 HI (full range) | ~1419 — 1423 MHz (cover full velocity width) |

## Doppler formula (quick check)

v_obs = v_rest × (1 - v_radial/c)

For M31 approaching at ~300 km/s:
f_obs = 1420.405 × (1 + 300/299792) ≈ 1421.8 MHz

**Always use Astropy for precise corrections — this is for sanity checks only.**

## Key coordinates

| Target | RA (J2000) | Dec (J2000) | Notes |
|---|---|---|---|
| M31 | 00h 42m 44.3s | +41° 16' 09" | Best: Sep-Jan |
| Cas A | 23h 23m 27.9s | +58° 48' 42" | Calibrator, year-round |
| Complex C (centre) | ~15h 30m | ~+55° | HVC, year-round |
| M33 | 01h 33m 50.9s | +30° 39' 37" | Best: Sep-Jan |

## Cas A flux (calibration)

F(year) = 2723 × (1 - 0.0077)^(year - 2000) Jy

2026: 2567 Jy | 2027: 2547 Jy | 2028: 2528 Jy | 2029: 2508 Jy

## File naming convention

Sessions: YYYY-MM-DD_TARGET_NNN.md  (NNN = 001, 002 if multiple same day)  
Equipment: E001_YYYY-MM-DD.md  (increment E number on any system change)  
Raw data: YYYY-MM-DD_TARGET_NNN_raw.[ext]  

## Post-session checklist

- [ ] Session log completed and saved
- [ ] Raw data backed up to secondary location
- [ ] Calibration CSV updated if Cas A was observed
- [ ] Git commit with meaningful message (e.g. "Session 2026-05-03 M31 3hr integration")
- [ ] Any equipment issues noted for follow-up
