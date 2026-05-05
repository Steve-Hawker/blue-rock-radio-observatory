# Blue Rock Radio Observatory — Learning Plan

**Observer:** Steve Hawker BEng MBA FRAS  
**Repository:** https://github.com/Steve-Hawker/blue-rock-radio-observatory  
**Plan version:** 1.4  
**Date:** 2026-05-04  

*This is a living document. Update it as reading is completed, understanding develops,
and new topics are identified. Commit each update with a version note.*

---

## Purpose

This document records the structured self-study programme supporting the Blue Rock
Radio Observatory observing programme and BSc Honours thesis. Each topic area
identifies the core knowledge required, the resources to consult, and tracks
progress over time.

The goal is not to read everything listed here — it is to develop sufficient
understanding of each topic to articulate and defend every decision made in
the research plan, observing methodology, and data reduction pipeline.

---

## Topic 1 — Physics of the 21cm Hydrogen Line

### Why this matters
The entire observing programme rests on understanding why neutral hydrogen emits
at 1420.405 MHz. This underpins every scientific claim made in the thesis.

### Core concepts to master
- Hyperfine structure of the hydrogen atom
- Spin-flip transition — parallel vs antiparallel proton/electron spin states
- Einstein A coefficient and spontaneous emission rate
- Why the line is so narrow and so stable in frequency
- Why HI is the dominant tracer of neutral ISM
- Optical depth and the transition from optically thin to thick regimes
- Column density and its relation to observed brightness temperature

### Resources

| Resource | Type | Priority | Status |
|---|---|---|---|
| Carroll & Ostlie — *Introduction to Modern Astrophysics* Ch. 31 (ISM) | Textbook | Essential | Not started |
| NRAO Essential Radio Astronomy — HI and ISM chapters | Online, free | Essential | Not started |
| Kalberla & Kerp 2009 — *ARA&A* 47, 27 "The HI Distribution of the Milky Way" | Review paper, free via NASA ADS | Essential | Not started |
| Dickey & Lockman 1990 — *ARA&A* 28, 215 "HI in the Galaxy" | Review paper, free via NASA ADS | Recommended | Not started |
| Lequeux — *The Interstellar Medium* | Textbook, request via interlibrary loan | Recommended | Not started |

**Access notes:**
- Carroll & Ostlie Ch. 31 — not available online via University of Lancashire library.
  Request physical copy via interlibrary loan, or use NRAO Essential Radio Astronomy
  as the primary free alternative — it covers the same material at equivalent depth.
- All review papers freely available via NASA ADS: `ui.adsabs.harvard.edu`
- NRAO Essential Radio Astronomy: `www.cv.nrao.edu/~sransom/web/xxx.html`
- NASA ADS has a direct Zotero connector — pull citation metadata into Zotero with one click

### Notes
*(Add notes here as reading progresses — key insights, questions, connections to observations)*

### Status
- [ ] Core concepts understood
- [ ] Can explain hyperfine transition from first principles
- [ ] Can derive column density from observed brightness temperature
- [ ] Understanding reflected in session logs

---

## Topic 2 — Radio Telescope Fundamentals

### Why this matters
To interpret observations correctly, calculate sensitivity limits, and design
the observing programme, a thorough understanding of how a radio telescope
works is essential. Every number in the research plan — SEFD, Tsys, integration
times — derives from these fundamentals.

### Core concepts to master
- Antenna gain and effective area
- Beam pattern, main lobe, sidelobes, beamwidth
- Antenna temperature
- System temperature and its components (receiver, sky, ground spillover)
- Noise figure and its physical meaning
- The Friis noise formula — cascaded noise in a signal chain
- The radiometer equation — sensitivity as a function of bandwidth and time
- SEFD and its relation to Tsys and Aeff
- Frequency switching and Dicke switching

### Resources

| Resource | Type | Priority | Status |
|---|---|---|---|
| Wilson, Rohlfs & Hüttemeister — *Tools of Radio Astronomy* Ch. 1, 4, 7 | Textbook | Essential | Not started |
| Kraus — *Radio Astronomy* Ch. 3, 7 | Textbook | Essential | Not started |
| Pozar — *Microwave Engineering* Ch. 10 (noise) | Textbook | Friis section only | Not started |
| NRAO Essential Radio Astronomy online course (public) | Online course | Highly recommended | Not started |
| SARA Journal — amateur receiver noise articles | Journal | Recommended | Not started |
| QPL9547 datasheet | Datasheet | Essential | Not started |
| SAW Filter datasheets (when obtained) | Datasheet | Essential | Not started |

### Notes
*(Add notes here as reading progresses)*

### Key derivations to work through personally
- Derive SEFD from first principles for Blue Rock setup
- Apply Friis formula to full signal chain (Antenna → LNA1 → F1 → LNA2 → F2 → SDR)
- Derive integration time required for M31 detection

### Status
- [ ] Friis formula understood and applied to Blue Rock signal chain
- [ ] Can derive SEFD from first principles
- [ ] Radiometer equation understood and applied
- [ ] Beam solid angle calculated and understood

---

## Topic 3 — HI in Galaxies and the ISM

### Why this matters
M31, M33, and the Milky Way HI emission are the primary science targets.
Understanding what the observations mean requires knowing how HI traces
galactic structure, rotation, and evolution.

### Core concepts to master
- HI in spiral galaxies — distribution, kinematics
- Rotation curves and what they reveal about dark matter
- The double-horned HI profile — why it occurs in inclined galaxies
- LSR (Local Standard of Rest) — definition and why it is used
- Velocity components — Galactic rotation, peculiar velocities
- High-velocity clouds — definition, origin theories, significance
- HI mass from observed flux

### Resources

| Resource | Type | Priority | Status |
|---|---|---|---|
| Binney & Merrifield — *Galactic Astronomy* Ch. 8 (HI and spiral structure) | Textbook | Essential | Not started |
| Chemin, Carignan & Foster 2009 — *AJ* 137, 3452 (M31 HI rotation curve) | Key paper | Essential | Not started |
| Wakker et al. 2007 — *ApJ* 670, L113 (Complex C distance) | Key paper | Essential | Not started |
| Wakker et al. 2008 — *ApJ* 672, 298 (Complex C metallicity) | Key paper | Essential | Not started |
| Ben Bekhti et al. 2016 — *A&A* 594, A116 (HI4PI survey) | Key paper | Essential | Not started |
| Roberts 1975 — M31 HI flux reference | Key paper | Recommended | Not started |

### Notes
*(Add notes here as reading progresses)*

### Status
- [ ] Can explain double-horned profile morphology from first principles
- [ ] Understand M31 velocity field and what it tells us
- [ ] Understand what Complex C is and why it is scientifically interesting
- [ ] Can calculate HI mass from observed flux density

---

## Topic 4 — Signal Processing and SDR

### Why this matters
The custom GNU Radio pipeline is a core deliverable of the programme.
Understanding digital signal processing is necessary to implement it correctly
and to explain every design decision.

### Core concepts to master
- Sampling theory and Nyquist criterion
- Fourier transforms and spectral analysis
- Spectral resolution and its relation to integration time
- Digital filtering — FIR, IIR
- Frequency switching implementation in software
- Baseline subtraction methods
- RFI flagging strategies
- GNU Radio flowgraph architecture
- SDR hardware — ADC, IQ sampling, dynamic range
- Direct conversion (zero-IF) architecture and its limitations
- DC offset, IQ imbalance, LO phase noise — mitigations in GNU Radio
- Receiver chain design — LNA, filters, mixer, ADC as a system

### Resources

| Resource | Type | Priority | Status |
|---|---|---|---|
| Clark & Clark — *Practical SDR* | Textbook | **Essential — primary GNU Radio reference** | Owned, skimmed |
| Laufer — *The Hobbyist's Guide to the RTL-SDR* | Textbook | **Essential — primary RTL-SDR reference** | Owned (assumed) |
| GNU Radio documentation and tutorials (gnuradio.org) | Online | Essential | Not started |
| EZRa documentation — read carefully for methodology | Online | Essential | Not started |
| Lyons — *Understanding Digital Signal Processing* | Textbook | Recommended | Not started |
| NRAO Essential Radio Astronomy — spectral line chapter | Online | Essential | Not started |
| Python NumPy/SciPy FFT documentation | Online | Essential | Not started |

### Clark & Clark — Practical SDR — Reading Guide

This is the course book for GNU Radio and the primary practical reference
for the signal processing pipeline. The three sections map directly onto
Blue Rock programme requirements:

**Section 1 — Building a Basic Receiver**
Practical GNU Radio flowgraph construction. Read alongside INV002 digital
filter design. The implementation counterpart to the theory in Topic 2.
Read during Phase 1 / early Phase 2 as GNU Radio pipeline development begins.

**Section 2 — Inside the Receiver**
Direct conversion architecture, DC offset, IQ imbalance, LO phase noise.
This section is the practical companion to DOWNCONVERSION_ARCHITECTURE.md
in the design/ directory. The book provides the GNU Radio implementation;
the design document provides the theoretical analysis and mitigation strategy.
Cross-reference these two sources actively.

**Section 3 — Working with SDR Hardware**

Particularly relevant chapters:

*Physics of Radio Signals* — bridges HI physics (Topic 1) and SDR
implementation. Read after Topic 1 foundations are established.

*GNU Radio Flowgraphs with SDR Hardware* — direct application to
Phase 2 pipeline development. Essential reading before building
the custom pipeline.

*SDR Hardware Under the Hood* — complements ADC_BIT_RESOLUTION.md
and DOWNCONVERSION_ARCHITECTURE.md. Real hardware behaviour vs
theoretical models.

*Peripheral Hardware* — relevant to dual-SDR architecture
(DUAL_SDR_ARCHITECTURE.md) and eventual interferometer array
(INTERFEROMETER_UPGRADE.md).

*Transmitting* — not applicable to this programme.

### Laufer — The Hobbyist's Guide to the RTL-SDR — Reading Guide

Written by Carl Laufer, the designer of the Discovery Dish, Feed,
Drive, and KrakenSDR — this book is the authoritative practical
reference for the RTL-SDR V4 hardware used in Chain A.

**Priority chapters for the Blue Rock programme:**

*Improving RTL-SDR performance* — **read first.** Real-world V4
performance characterisation, practical techniques for maximising
sensitivity and dynamic range. Directly informs INV001 noise budget
and ADC_BIT_RESOLUTION.md. The author knows the hardware intimately.

*Measuring filters and SWR with low cost equipment* — **read before
commissioning.** RTL-SDR based filter measurement techniques that
provide empirical SAW filter characterisation without a VNA. Directly
informs SAW_FILTER_DESIGN.md commissioning measurements — update
that document's measurement plan after reading this chapter.

*Guide to antennas, cables and adapters* — covers dipole construction,
cable selection, connector types. Complements DIPOLE_ANTENNA_DESIGN.md
and INTERFEROMETER_UPGRADE.md cable matching methodology.

*Introduction to GNU Radio* — Laufer's perspective on GNU Radio
complements Clark & Clark. Useful to read both — the hardware
author's view of the software vs the software-focused textbook.

*Receiving Inmarsat, AERO, Iridium L-Band* — these signals fall
near the HI feed passband (1530–1630 MHz). Understanding them
helps identify and characterise adjacent-band RFI in surveys.
Informs RFI_OVERVIEW.md and SURVEY_TEMPLATE.md.

*ADS-B aircraft radar* — aircraft transponders at 1090 MHz are
a potential RFI source. Understanding the signal character aids
identification in RFI surveys.

*RTL-SDR tricks and oddities* — essential commissioning reading.
Saves hours of debugging unexpected V4 behaviour during Phase 1.

**Chapters less relevant to this programme:**
Weather satellites, trunked radio, pagers, HF modes, digital voice —
fascinating but outside the Blue Rock science programme.

### Recommended reading sequence

1. Laufer — RTL-SDR tricks and performance chapter (before first use of V4)
2. Laufer — Antennas, cables, adapters (before building dipole)
3. Clark & Clark Section 1 (as GNU Radio installation begins)
4. Laufer — Measuring filters chapter (before commissioning)
5. Clark & Clark Section 2 (before custom pipeline development)
6. Clark & Clark Section 3 relevant chapters (as each topic becomes active)
7. Laufer — L-Band satellite chapters (during RFI survey programme)

### Notes
*(Add notes here as reading progresses)*

### Status
- [ ] Section 1 read — GNU Radio basics operational
- [ ] Section 2 read — direct conversion architecture understood in practice
- [ ] Section 3 Physics of Radio Signals read
- [ ] Section 3 GNU Radio Flowgraphs with SDR Hardware read
- [ ] Section 3 SDR Hardware Under the Hood read
- [ ] GNU Radio basics — can build and run a simple flowgraph
- [ ] Understand frequency switching and can implement it
- [ ] Understand baseline subtraction and can implement it
- [ ] RFI flagging strategy developed and implemented
- [ ] Custom pipeline producing results comparable to EZRa

---

## Topic 5 — Doppler Corrections and Reference Frames

### Why this matters
All velocities in the programme must be expressed in the LSR frame.
Incorrect Doppler corrections would invalidate all velocity measurements.
This must be understood thoroughly, not just implemented blindly via Astropy.

### Core concepts to master
- Topocentric, geocentric, heliocentric, and LSR reference frames
- Components of the Doppler correction — diurnal, annual, solar motion
- Standard solar motion (IAU definition)
- How seasonal variation affects observed HI frequency
- Implementation in Astropy — `radial_velocity_correction()`
- Validation strategy — checking corrections against known sources

### Resources

| Resource | Type | Priority | Status |
|---|---|---|---|
| Astropy docs — `radial_velocity_correction()` | Online | Essential | Not started |
| Binney & Merrifield — *Galactic Astronomy* Ch. 1 (coordinate systems) | Textbook | Essential | Not started |
| Gordon 1976 — LSR definition and solar motion | Paper | Recommended | Not started |
| HI4PI paper — methodology section on velocity frames | Paper | Recommended | Not started |

### Notes
*(Add notes here as reading progresses)*

### Validation plan
Verify Doppler pipeline against HI absorption features toward Cas A at known
LSR velocities: Perseus arm (~-47 km/s), Local arm (~-5 km/s).

### Status
- [ ] All reference frames understood conceptually
- [ ] Astropy implementation understood line by line
- [ ] Pipeline validated against Cas A absorption features
- [ ] Seasonal frequency shift for M31 calculated and documented

---

## Topic 6 — Calibration Methods

### Why this matters
All flux measurements depend on calibration. Without understanding calibration
methodology, results cannot be placed on an absolute scale or compared with
professional surveys.

### Core concepts to master
- Flux density standards in radio astronomy
- The Baars et al. 1977 flux scale
- Y-factor method for system temperature measurement
- Cas A as a calibration standard — flux, secular decrease, limitations
- Absolute vs relative calibration
- Pointing corrections and their effect on flux measurements
- Atmospheric opacity at 1420 MHz

### Resources

| Resource | Type | Priority | Status |
|---|---|---|---|
| Baars et al. 1977 — *A&A* 61, 99 (flux calibration scale) | Key paper | Essential | Not started |
| Reed et al. 1995 — Cas A secular decrease | Key paper | Essential | Not started |
| Wilson et al. — *Tools of Radio Astronomy* calibration chapters | Textbook | Essential | Not started |
| Perley & Butler 2017 — updated flux calibration scale | Paper | Recommended | Not started |

### Notes
*(Add notes here as reading progresses)*

### Status
- [ ] Y-factor method understood and implemented
- [ ] Cas A flux at current epoch calculated correctly
- [ ] System temperature time series established
- [ ] Calibration methodology documented in pipeline

---

## Topic 7 — Academic Writing and Thesis Structure

### Why this matters
The BSc thesis is the primary deliverable. Understanding how to structure and
write a scientific paper is a skill requiring deliberate development.

### Core concepts to master
- Structure of a scientific paper — Abstract, Introduction, Observations,
  Data Reduction, Results, Discussion, Conclusion
- How to write a literature review
- How to present data and errors correctly
- How to compare results with previous work
- Citation practice and academic integrity
- University of Lancashire thesis requirements

### Resources

| Resource | Type | Priority | Status |
|---|---|---|---|
| University of Lancashire BSc thesis guidelines | University document | Essential | Not started |
| Knuth — *Mathematical Writing* (free online) | Reference | Recommended | Not started |
| Read 3-4 published amateur radio astronomy papers in SARA Journal | Journal | Recommended | Not started |
| Read Chemin et al. 2009 as a model of how to present HI results | Paper | Recommended | Not started |
| Zotero documentation — citation management | Online | Essential | Not started |

### Notes
*(Add notes here as reading progresses)*

### Status
- [ ] Thesis structure understood
- [ ] Zotero workflow established and comfortable
- [ ] Literature review begun
- [ ] Draft introduction written

---

## Reading by Programme Phase

This section maps each learning topic to the programme phase where that
knowledge is needed. The goal is to complete each topic's core reading
**before** the corresponding phase begins — not during it.

### Phase 1 — Infrastructure and Planning ✓ Complete
*No specific reading prerequisite — this phase is about setting up the
programme, not conducting science.*

Reading to do **during Phase 1** (i.e. now):
- Topic 4: Laufer — RTL-SDR tricks and performance (before V4c arrives)
- Topic 4: Laufer — Antennas, cables and adapters (before dipole setup)
- Topic 2: QPL9547 datasheet — already in equipment/datasheets/

---

### Phase 2 — Site Survey (May 7 2026)
*Minimal reading prerequisite — site assessment is primarily practical.*

Reading to complete **before Phase 2:**
- Topic 4: Laufer — Measuring filters chapter (informs commissioning plan)

Reading to do **during Phase 2:**
- Begin Topic 2: Radio Telescope Fundamentals (Wilson et al. Ch. 1)
- Begin Topic 1: HI Physics (NRAO Essential Radio Astronomy)

---

### Phase 3 — RFI Commissioning (May–Aug 2026)
*Need enough SDR and signal chain knowledge to interpret what you're seeing.*

Reading to complete **before Phase 3:**
- Topic 4: Laufer — RTL-SDR tricks, performance, antennas ✓ (in progress)
- Topic 4: Clark & Clark Section 1 — GNU Radio basics
- Topic 2: NRAO Essential Radio Astronomy — receiver systems chapter

Reading to do **during Phase 3:**
- Topic 4: Clark & Clark Section 2 — Inside the Receiver
- Topic 2: Friis formula — apply to Blue Rock signal chain (INV001)
- Topic 4: Laufer — L-Band satellite chapters (identify RFI sources)

---

### Phase 4 — Basic HI Observations (Aug 2026–2027)
*This is where the science begins. Need solid foundations in HI physics,
telescope fundamentals, calibration, and Doppler corrections before
first light.*

Reading to complete **before Phase 4:**
- **Topic 1: HI Physics — complete** (understand what you're observing)
- **Topic 2: Radio Telescope Fundamentals — complete** (Friis, SEFD, radiometer)
- **Topic 6: Calibration Methods — complete** (Baars flux scale, Y-factor, Cas A)
- **Topic 5: Doppler Corrections — core concepts** (LSR frame, Astropy)
- Topic 4: Clark & Clark Section 2 — direct conversion architecture
- Topic 4: EZRa documentation — read before first use

Reading to do **during Phase 4:**
- Topic 3: HI in Galaxies — M31 rotation curve, double-horn profile
- Topic 5: Doppler pipeline implementation and validation
- Topic 6: Calibration pipeline validation against Cas A
- Topic 4: Clark & Clark Section 3 — GNU Radio with SDR hardware

---

### Phase 5 — Advanced HI Observations (2027–2030)
*Custom pipeline, offset pointing, co-addition. Need full command of
signal processing, data reduction, and the science of what M31 is telling you.*

Reading to complete **before Phase 5:**
- **Topic 3: HI in Galaxies — complete** (M31 kinematics, rotation curves)
- **Topic 4: Signal Processing — complete** (custom pipeline ready)
- **Topic 5: Doppler Corrections — complete** (pipeline validated)
- Topic 7: Begin academic writing — thesis outline discussions start Year 4

Reading to do **during Phase 5:**
- Topic 7: Academic Writing — thesis structure, literature review
- Topic 3: Deep dive into M31 velocity field literature
- Topic 6: Advanced calibration — HI4PI comparison, flux scale validation

---

### Phase 6 — Interferometry (2029–2031)
*Stretch goal. Requires additional reading beyond the current seven topics.*

Additional reading needed (not yet in learning plan):
- Thompson, Moran & Swenson — *Interferometry and Synthesis in Radio Astronomy*
- CASA documentation
- Phase calibration methodology

*Add these to the learning plan when Phase 6 planning begins in earnest.*

---

## Summary — Reading Priority by Date

| When | What | Topic | Why |
|---|---|---|---|
| **Now — May 2026** | Laufer — tricks, performance, antennas | 4 | Before V4c arrives |
| **Now — May 2026** | Laufer — measuring filters | 4 | Before commissioning |
| **May–Jul 2026** | Clark & Clark Section 1 | 4 | GNU Radio installation |
| **May–Jul 2026** | NRAO ERA — receiver systems | 2 | Before RFI surveys |
| **May–Jul 2026** | QPL9547 datasheet — study carefully | 2 | INV001 Friis calculation |
| **Jun–Aug 2026** | Clark & Clark Section 2 | 4 | Signal chain architecture |
| **Jun–Aug 2026** | Wilson et al. Ch. 1, 4 | 2 | Telescope fundamentals |
| **Before first light** | Baars et al. 1977 | 6 | Flux calibration — essential |
| **Before first light** | NRAO ERA — HI and ISM | 1 | HI physics foundations |
| **Before first light** | Astropy Doppler docs | 5 | LSR corrections |
| **Year 2** | Chemin et al. 2009 — M31 | 3 | Primary science context |
| **Year 2** | Ben Bekhti et al. 2016 — HI4PI | 3 | Comparison dataset |
| **Year 2** | Wakker et al. 2007, 2008 — Complex C | 3 | HVC science context |
| **Year 3–4** | Clark & Clark Section 3 | 4 | Custom pipeline |
| **Year 4** | University thesis guidelines | 7 | Thesis writing begins |
| **Year 4** | Chemin et al. as model paper | 7 | How to present HI results |

---

*Record each item completed here with date and brief note on key takeaways.*

| Date | Resource | Key takeaways |
|---|---|---|
| | | |

---

## Questions and Topics to Investigate

*Running list of questions arising from reading and observations — to be researched
and answered over time.*

- [ ] What is the exact beamwidth of the Blue Rock dish at 1420 MHz once feed is characterised?
- [ ] What RFI sources are known at 1420 MHz in San Jose specifically?
- [ ] What spectral resolution is needed to resolve M31's double-horn profile?
- [ ] How does filter insertion loss affect system temperature in the Friis calculation?
- [ ] What is the minimum detectable flux of Blue Rock after 1 hour integration?

---

## Plan Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-28 | Initial plan |
| 1.1 | 2026-04-30 | Topic 1 — corrected Carroll & Ostlie chapter number, added NRAO ERA and NASA ADS |
| 1.2 | 2026-04-30 | Topic 4 — added Clark & Clark Practical SDR as primary reference |
| 1.3 | 2026-04-30 | Topic 4 — added Laufer RTL-SDR guide, expanded reading guides, recommended sequence |
| 1.4 | 2026-05-04 | Add phase cross-reference section — reading mapped to all 6 programme phases with priority summary table |

---

*Update this document as reading progresses. Commit each update to Git with a
meaningful message such as "Learning plan — completed Topic 2 Friis formula".*
