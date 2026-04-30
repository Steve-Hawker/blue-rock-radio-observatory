# Chapter Outline — Site Assessment for Amateur HI Radio Astronomy
## How to Compensate and Allow for Trees, Buildings, and Urban Constraints

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory, San Jose CA  
**Version:** 0.1 draft outline  
**Date:** 2026-04-30  
**Context:** Proposed chapter for amateur radio astronomy methodology guide,
arising from BSc Honours programme at University of Lancashire.
Intended audience: beginners setting up HI observations at a suburban or
urban site with real-world obstructions.

---

## Purpose of this Chapter

Most amateur radio astronomy guides assume an ideal site — open horizon,
no nearby structures, rural location. Most amateur radio astronomers have
none of these things. They have a suburban garden, a fence, a tree, a
neighbour's house, and a WiFi router next door.

This chapter addresses the real world. It provides a systematic methodology
for assessing any site, understanding what the obstructions actually mean
for HI observations at 1420 MHz, and designing an observing programme that
works within — and in some cases takes advantage of — those constraints.

The methodology is drawn from the author's experience establishing Blue Rock
Radio Observatory on a small urban patio in San Jose, California.

---

## Proposed Chapter Structure

---

### Section 1 — Why Site Assessment Matters

**Key points to cover:**
- At 1420 MHz the rules are different from optical astronomy
- Clouds, fog, and light pollution are irrelevant
- What does matter: physical obstructions, RFI, wind, ground reflections
- The good news: your targets transit at very high elevations from mid-latitudes
  — most obstructions are below the beam at transit
- The key insight: a systematic site assessment turns constraints into
  known, documented, manageable quantities

**Tone:** Reassuring. The urban site is not a disaster — it just needs
to be understood.

---

### Section 2 — Understanding 1420 MHz Propagation

**Key points to cover:**
- Wavelength = 21cm — what this means physically for diffraction and reflection
- What blocks 1420 MHz: metal, reinforced concrete, wet soil
- What is largely transparent: timber, composite fencing, dry vegetation,
  glass, plastic, dry deciduous trees in winter
- What partially attenuates: brick, dense wet foliage, some building materials
- Ground reflections and multipath — what causes them and when they matter
- Why a deciduous tree in autumn/winter (prime HI season) is nearly transparent

**Practical implication:** most suburban garden obstructions are less
problematic than they appear, particularly at the high transit elevations
of typical HI targets.

---

### Section 3 — The Geometry of Obstructions

**Key points to cover:**
- Angular height — the only number that matters, not physical height
- The formula: θ = arctan(h/d) — worked examples
- Why distance matters as much as height
- How to think about your beam: 17° beamwidth means the obstruction needs
  to be well below your pointing elevation to be irrelevant
- Transit elevation from your latitude — how to calculate it
- The clearance calculation: transit elevation minus obstruction angular height
- Worked example: Blue Rock Observatory tree at 175° — 50ft tall, 30ft away
  = 59° angular height, M31 transits at 76° — clearance = 17°

**Practical toolkit:**
- Smartphone theodolite apps for measuring elevation angles
- Compass apps for azimuth bearings (with magnetic declination correction)
- Stellarium for target transit elevations at your latitude
- Simple spreadsheet for clearance calculations

---

### Section 4 — Conducting a Formal Site Assessment

**Key points to cover:**
- What to measure: azimuth and elevation of every significant obstruction
- Equipment needed: smartphone with theodolite app, compass app, notepad
- The 36-point survey: measure every 10° of azimuth
- Recording the horizon profile — table format and polar plot
- Photographing the horizon in each direction for the permanent record
- Noting obstruction material (affects transparency at 1420 MHz)
- Noting seasonal variation — deciduous trees change significantly
- Documenting in the equipment log — site characteristics section
- How often to resurvey: annually, and after any significant site change

**Practical tip:** Do the survey from the exact position where the dish
will be mounted. A metre makes a difference.

---

### Section 5 — Calculating Target Visibility

**Key points to cover:**
- For each target: does the horizon profile block it at any point in its
  observable arc?
- Rising and setting times vs obstruction azimuths
- The difference between transit clearance (usually fine) and rising/setting
  clearance (often the limiting factor)
- How much observing time do you actually lose?
- Using Stellarium to animate target tracks across your horizon profile
- The concept of the "effective observing window" — when target is above
  both the physical horizon and your minimum useful elevation

**Worked example:** Blue Rock M31 session — house at 150° limits rising
time but transit is unaffected. Net loss ~1 hour per night. Over prime
season this is minor.

---

### Section 6 — RFI Environment Assessment

**Key points to cover:**
- Why urban RFI is a real problem but a manageable one
- The 1420 MHz band has statutory protection — but this doesn't mean silence
- What causes in-band interference: harmonics, intermodulation, spurious emissions
- The WiFi sniffer approach — mapping local transmitters
- Wideband SDR survey methodology — waterfall plots, time of day patterns
- Weekday vs weekend, daytime vs night — RFI has temporal patterns
- The SAW filter as your primary hardware defence
- ADC saturation — the critical failure mode to monitor for
- Documenting your RFI environment: the rfi/ directory approach

**Key message:** characterise your RFI environment systematically before
trying to do science. An hour of RFI surveying saves days of confused results.

---

### Section 7 — Compensation Strategies

**Key points to cover:**

**Physical strategies:**
- Optimal dish positioning on the patio — distance from walls, height
- The 2–3 wavelength rule for multipath reduction (>60cm from surfaces)
- Tripod height tradeoff — stability vs ground clearance
- Fence as wind shield — the urban enclosure has advantages
- Marking tripod position for repeatable setup
- Compass mount for consistent pointing regardless of exact tripod position

**Observational strategies:**
- Schedule observations around obstructions — observe targets near transit
  rather than near the horizon
- Daytime observing — at 1420 MHz this is entirely valid
- Seasonal scheduling — observe deciduous-tree-affected sightlines in winter
- Longer integrations compensate for lost rising/setting time

**Signal processing strategies:**
- Frequency switching removes correlated receiver noise and some RFI
- Digital filtering — sharp bandpass around 1420 MHz rejects adjacent interference
- RFI flagging — automated detection and excision of contaminated data
- Co-adding multiple sessions — the urban observer's most powerful tool

**Calibration strategies:**
- Frequent Cas A observations bracket every science session
- Complex C as independent velocity and beam efficiency calibration
- Comparison against HI4PI — discrepancies diagnose systematic problems

---

### Section 8 — Turning Constraints into Features

**Key points to cover:**
- The urban RFI environment is a research topic in its own right
- A systematic characterisation of 1420 MHz RFI from a named urban site
  is a citable contribution to the amateur community
- The fence and buildings provide wind shielding — stability advantage
- The large beam of a small dish means extended sources like Complex C
  are well matched — no pointing precision required
- Daytime availability means more total integration time than a night-only observer
- The constrained site forces rigorous methodology — which produces
  better documented science than an unconstrained site casually observed

**Key message:** the urban amateur with a systematic approach and a long
time baseline can produce results that a well-equipped but casual observer
cannot. Rigour compensates for aperture.

---

### Section 9 — A Worked Example: Blue Rock Radio Observatory

**Key points to cover:**
- Full site description: 8×20ft patio, SW facing, 210° open aspect
- Horizon profile: house at 150°, tree at 175°, composite fence
- Clearance calculations for all primary targets
- RFI environment: San Jose urban, SAW filter protection
- Scheduling strategy: daytime observations, prime M31 season Sep–Jan
- Results: viable programme despite urban constraints

This section grounds the abstract methodology in a real example with
real numbers, making it directly reproducible by other observers.

---

### Section 10 — Site Assessment Checklist and Templates

**Key points to cover:**
- One-page site assessment checklist
- Horizon profile table template
- Equipment log site characteristics section template
- Recommended smartphone apps
- Further reading

---

## Notes on Scope and Tone

This chapter should be written for someone who:
- Has just acquired a Discovery Dish or similar small dish
- Lives in a suburban house with a garden or patio
- Is worried their site is "not good enough"
- Has no prior radio astronomy experience but is technically capable

The tone should be practical, reassuring, and example-driven. Every
abstract point should have a concrete worked example. The Blue Rock
Observatory is the running example throughout.

The underlying message is: **a well-assessed constrained site is better
than a poorly understood open site.** Knowing your limitations precisely
is a strength, not a weakness.

---

## Relationship to thesis

This chapter methodology is embedded throughout the Blue Rock observing
programme documentation. The site assessment data in E001 equipment log,
the horizon profile, the RFI survey data, and the scheduling decisions
all instantiate this methodology in practice. The chapter writes itself
from the programme records.

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1 | 2026-04-30 | Initial outline |
