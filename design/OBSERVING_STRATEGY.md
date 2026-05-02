# Observing Strategy — Blue Rock Radio Observatory

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory, San Jose CA (37.3382°N)  
**Date:** 2026-04-30  
**Version:** 1.0  

---

## Overview

This document defines the observing strategy for the Blue Rock programme —
how targets are sequenced within sessions, how sessions are distributed
across seasons, and how the co-addition principle drives the integration
time allocation. The strategy is designed to maximise science output from
a dual-SDR system (Airspy R2 on dish + RTL-SDR V4 on dipole) running
simultaneously.

The MacBook Pro running Stellarium connected to the Discovery Drive allows
session planning well in advance. Slewing between targets is a single click
— planning is the work, not execution.

---

## Site and System Constraints

| Constraint | Value | Implication |
|---|---|---|
| Minimum useful elevation | 30° | Targets below this are too attenuated |
| Preferred minimum elevation | 45° | Better beam efficiency, less atmosphere |
| Cas A calibration overhead | 30 min/session (15 open + 15 close) | Fixed cost per session |
| Dish beamwidth | ~17° | All targets unresolved — pointing accuracy ±1.5° adequate |
| Chain A (V4 + dipole) | Continuous RFI monitoring | Runs throughout all sessions |
| Galactic centre (dec -29°) | Max elevation 24° — never usefully observable | Removed from active target list |

---

## Target Reference Data

| Target | Dec | Transit El | Hrs/day >30° | Type | Priority |
|---|---|---|---|---|---|
| Cas A | +58.8° | 68.5° | 12.3 | Calibrator | Primary |
| M31 | +41.3° | 86.1° | 10.7 | Extragalactic | Primary science |
| Complex C | +55.0° | 72.3° | 11.9 | HVC | Primary science |
| M1 | +22.0° | 74.7° | 9.1 | Calibrator/SNR | Secondary |
| M33 | +30.7° | 83.3° | 9.8 | Extragalactic | Secondary |
| M81 | +69.1° | 58.3° | 13.8 | Extragalactic | Stretch goal |
| Galactic centre | -29.0° | 23.7° | 0.0 | Galactic | Removed — too low |

*All elevations calculated for San Jose 37.3382°N.*  
*Transit elevations confirmed: M31 at 86° and M33 at 83° are nearly overhead — well clear of all site obstructions.*

---

## Monthly Observing Quality

Shows the time of day when each target transits — indicating whether
sessions will be daytime or evening/overnight. At 1420 MHz all symbols
represent valid observing conditions — this is not an availability table,
it is a scheduling guide.

| Target | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cas A | ○ | ○ | ○ | ○ | ○ | ○ | ◑ | ● | ● | ● | ◑ | ◑ |
| M31 | ○ | ○ | ○ | ○ | ○ | ○ | ◑ | ◑ | ● | ● | ● | ◑ |
| Complex C | ○ | ○ | ◑ | ● | ● | ● | ◑ | ◑ | ○ | ○ | ○ | ○ |
| M1 | ● | ◑ | ◑ | ○ | ○ | ○ | ○ | ○ | ○ | ◑ | ● | ● |
| M33 | ◑ | ○ | ○ | ○ | ○ | ○ | ○ | ◑ | ● | ● | ● | ◑ |
| M81 | ● | ● | ● | ◑ | ◑ | ○ | ○ | ○ | ○ | ○ | ○ | ◑ |

**Key:**
- ● Target transits at night — evening or overnight sessions
- ◑ Target transits near dawn or dusk — flexible scheduling
- ○ Target transits during the day — daytime sessions
- ✗ Never rises above 30° — not observable (Galactic centre)

All three symbols represent valid observing conditions at 1420 MHz.
The observer has full schedule flexibility and exploits daytime
windows actively. Solar separation >20–30° must be maintained
regardless of time of day.

**Practical implication:**

- M31 ○ in Jan–Jun — transits midday, perfectly observable on a
  calm weekday morning or afternoon
- Complex C ○ in Sep–Dec — transits overnight in M31 season,
  natural fill-in target between M31 integrations
- M81 ● in Jan–Mar — transits at night in winter, natural
  complement to M31 season targets

---

## Seasonal Programmes

### Autumn/Winter — September to February (M31 Primary Season)

The core science season. M31, M33, M1, and Cas A are all well placed
at night simultaneously. Maximum session frequency — target 4–5 sessions
per week where conditions permit.

**Standard session sequence:**

```
Cas A          15 min    Opening calibration
M31             2–3 hr   Primary science — maximum integration
M33            30–60 min Secondary science (if M31 well covered recently)
M1             30 min    Secondary calibration check / science
Cas A          15 min    Closing calibration
─────────────────────────────────────────
Total          ~3.5–5 hrs per session
Active science ~3–4 hrs
```

**M33-focus session (when M31 has recent good coverage):**

```
Cas A          15 min
M33             2 hrs
M1              1 hr
Cas A          15 min
─────────────────────────────────────────
Total          ~3.5 hrs
```

**Integration targets per month (M31 season):**

| Target | Sessions/month | Per session | Monthly total |
|---|---|---|---|
| M31 | 15–20 | 2–3 hrs | 30–60 hrs |
| M33 | 4–8 | 1–2 hrs | 4–16 hrs |
| M1 | 8–12 | 30 min | 4–6 hrs |
| Cas A | Every session | 30 min | ~8 hrs |

---

### Spring — March to May (Transition Season)

M31 becomes difficult as it moves into the evening sky. Complex C rises
to prominence. Pipeline development and software work fill the remaining
time productively.

**Standard session sequence:**

```
Cas A          15 min
Complex C       2–3 hrs   Primary target this season
Galactic HI    30–60 min  Spiral arm sightlines — pipeline validation
Cas A          15 min
─────────────────────────────────────────
Total          ~3–4.5 hrs
```

**Engineering focus:** Spring is the natural GNU Radio pipeline development
season — science targets are less compelling, leaving time for INV002
digital filter work and pipeline validation against EZRa.

---

### Summer — June to August (Southern/Engineering Season)

M31 is essentially unavailable at night (though daytime sessions remain
viable). Complex C, M81, and engineering work dominate.

**Standard session sequence:**

```
Cas A          15 min
Complex C       2 hrs
M81             1 hr     Stretch goal — build dataset opportunistically
Cas A          15 min
─────────────────────────────────────────
Total          ~3.5 hrs
```

**Engineering focus:** Summer is peak engineering season — RFI survey
programme, pipeline development, INV001 noise budget measurements,
equipment upgrades (DDOEE installation in October at season end).

---

## Daily Sequencing Principles

**1. Cas A always brackets science sessions**
Every session opens and closes with a Cas A observation. Non-negotiable.
This gives a before/after system temperature measurement and catches any
gain drift during the session.

**2. M31 gets priority in its season**
When M31 is available, it gets the longest single block of integration
time in the session. Secondary targets fill around it, not the reverse.

**3. Don't fragment integrations unnecessarily**
A 3-hour M31 integration is more valuable than three 1-hour M31
integrations interrupted by slewing to other targets. Co-addition
works best with clean, uninterrupted integrations. Slew to secondary
targets at natural break points.

**4. Complex C is always available**
Complex C's anomalous velocity means it can be observed whenever it's
above 30° elevation regardless of season. It serves as a fill-in target
when primary targets are unavailable or have been well covered.

**5. Session length is flexible**
A 90-minute session with Cas A + M31 integration is better than no
session. Don't skip sessions because the full sequence isn't possible.
Partial sessions co-add just as well as full ones.

**6. Log the reason for any deviation**
If the planned sequence is changed — weather, RFI, software issue —
note it in the session log. The deviation itself is scientifically
useful information about site conditions.

---

## Co-addition Strategy

The power of the Blue Rock programme lies in co-addition across the
four-year baseline. Key principles:

**LSR velocity alignment** — all sessions must be Doppler corrected
to LSR before co-addition. Failure to do this correctly means sessions
from different epochs add incoherently, degrading rather than improving
SNR. Astropy `radial_velocity_correction()` is mandatory for every session.

**Consistent pointing** — for each target, always use the same pointing
position (RA/Dec). Vary pointing only for deliberate mapping programmes,
which are logged separately.

**Weight by integration time** — when co-adding sessions of different
lengths, weight each session by its integration time before averaging.

**Flag before co-adding** — apply RFI flagging to individual sessions
before co-adding. Co-adding unflagged data propagates RFI artefacts
into the integrated spectrum.

**Baseline subtraction per session** — apply polynomial baseline
subtraction to each session individually before co-adding. Do not
apply baseline subtraction only to the co-added spectrum.

---

## Stellarium Planning Workflow

The MacBook Pro runs Stellarium connected to the Discovery Drive via
the Stellarium Remote Control plugin. Pre-session planning:

1. Open Stellarium — set date and time to planned session start
2. Check each target's elevation arc through the planned session window
3. Confirm solar separation >30° for all planned pointings
4. Plan the sequence — note slew times between targets
5. Confirm Cas A is available for opening and closing calibration
6. Note any elevation constraints from site horizon profile
7. Record planned sequence in session log before observing begins

During session:
- Click target in Stellarium → dish slews automatically
- Stellarium shows real-time elevation and solar separation
- Adjust sequence in real time if conditions change

---

## Annual Review

At the end of each observing season (approximately February each year),
conduct a brief review:

- Total integration time accumulated per target vs plan
- SNR achieved vs expected from radiometer equation
- RFI environment changes noted
- Equipment changes planned for next season
- Adjust following season's session targets if needed

Document the review as a dated entry in this file under a new
**Season Review** section.

---

## Galactic Centre — Removed from Active List

The Galactic centre (dec -29°) reaches only 23.7° maximum elevation
from San Jose. This is below the 30° minimum useful elevation threshold.
At this elevation atmospheric effects, ground spillover, and site
obstructions combine to make clean HI observations impractical.

The Galactic centre is formally removed from the active target list.
It may be revisited if site conditions or equipment improve significantly,
but is not planned for the current programme.

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-30 | Initial document — seasonal schedule, monthly availability table, sequencing principles, co-addition strategy |
| 1.1 | 2026-04-30 | Renamed monthly table to "Monthly Observing Quality" — reframed as scheduling guide not availability, updated key |
