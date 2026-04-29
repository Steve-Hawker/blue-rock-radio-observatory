# Blue Rock Radio Observatory — Learning Plan

**Observer:** Steve Hawker BEng MBA FRAS  
**Repository:** https://github.com/Steve-Hawker/blue-rock-radio-observatory  
**Plan version:** 1.0  
**Date:** 2026-04-28  

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
| Carroll & Ostlie — *Introduction to Modern Astrophysics* Ch. 12 (ISM) | Textbook | Essential | Not started |
| Kalberla & Kerp 2009 — *ARA&A* 47, 27 "The HI Distribution of the Milky Way" | Review paper | Essential | Not started |
| Rohlfs & Wilson — *Tools of Radio Astronomy* Ch. 1-2 | Textbook | Essential | Not started |
| Dickey & Lockman 1990 — *ARA&A* 28, 215 "HI in the Galaxy" | Review paper | Recommended | Not started |

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

### Resources

| Resource | Type | Priority | Status |
|---|---|---|---|
| GNU Radio documentation and tutorials (gnuradio.org) | Online | Essential | Not started |
| EZRa documentation — read carefully for methodology | Online | Essential | Not started |
| Lyons — *Understanding Digital Signal Processing* | Textbook | Recommended | Not started |
| NRAO Essential Radio Astronomy — spectral line chapter | Online | Essential | Not started |
| Python NumPy/SciPy FFT documentation | Online | Essential | Not started |

### Notes
*(Add notes here as reading progresses)*

### Status
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

## Reading Progress Log

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

---

*Update this document as reading progresses. Commit each update to Git with a
meaningful message such as "Learning plan — completed Topic 2 Friis formula".*
