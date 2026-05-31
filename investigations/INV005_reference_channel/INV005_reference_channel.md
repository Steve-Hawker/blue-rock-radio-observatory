# INV005 — Reference Channel Flagging Effectiveness

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-29  
**Version:** 0.1 — Concept capture  
**Status:** Pre-implementation — data collection begins Phase 3  

---

## Motivation

The Blue Rock dual-chain architecture (Chain A: RTL-SDR V4c + reference
dipole / Chain B: Airspy R2 + Discovery Dish) uses the reference dipole
as a flagging system for terrestrial RFI contamination in the science
channel. When Chain A sees a spike at 1420 MHz, that integration in
Chain B is flagged as potentially contaminated and excised.

This works in principle. But how well does it work in practice?

The flagging effectiveness of the reference channel is not a given.
It depends on:
- The dipole's sensitivity to the RFI sources that actually contaminate
  the dish
- The degree of spatial correlation between what the dipole sees and
  what the dish sees
- The polarisation match between the dipole and the RFI sources
- The time resolution of the flagging — does the flag arrive in time?

Characterising this empirically is a genuine methodology contribution.
A system that claims reference channel RFI mitigation should quantify
how well it actually works.

---

## Background

### The Flagging Architecture

The Discovery Dish has a 17° beam pointing at a specific patch of sky.
The reference dipole has an E-plane HPBW of ~78° and an omnidirectional
H-plane. They are looking at very different solid angles simultaneously.

Clean subtraction (cancellation) of dipole signal from dish signal is
not viable — the beam patterns are too different for coherent removal.
The dipole's role is therefore:

- **Correlated RFI** (present in both Chain A and Chain B) = terrestrial
  interference → flag and excise from science data
- **Uncorrelated signal** = potentially real astronomy

This is the architecture described by Briggs, Bell & Kesteven (2000),
adapted for a single-dish single-reference configuration.

### Key Questions

1. **Detection rate:** What fraction of RFI events that contaminate
   Chain B are detected in Chain A?

2. **Miss rate:** What fraction of Chain B contamination events does
   the dipole miss entirely? Why? (Wrong polarisation? Wrong azimuth?
   Below dipole noise floor?)

3. **False positive rate:** What fraction of Chain A flags correspond
   to events that do not actually contaminate Chain B? (False flags
   waste science data.)

4. **Latency:** Is the RFI event simultaneous in both chains, or is
   there a lag that affects flagging window design?

5. **Polarisation dependence:** Does the vertical dipole catch
   horizontally polarised RFI sources less effectively? Is this
   measurable in the data?

---

## Method

### Phase 3 — Simultaneous Dual-Chain Logging

From first RFI survey onwards, log both chains simultaneously with
aligned timestamps. This is the raw dataset for this investigation.

Required data per session:
- Chain A power spectrum (V4c, 1 MHz resolution, 1s cadence)
- Chain B power spectrum (Airspy R2, 1 MHz resolution, 1s cadence)
- Timestamps aligned to UTC — same clock reference
- Session metadata (pointing, LST, conditions)

See INV004_ml_rfi.md for full data schema requirements — this
investigation uses the same dataset.

### Phase 4 — Flagging Algorithm Development

Develop a basic cross-correlation flagging algorithm:

1. For each 1s integration, compute power in the HI passband for
   both chains
2. Define a flagging threshold — e.g. Chain A power > N×σ above
   running median → flag that integration in Chain B
3. Apply flags to Chain B data
4. Assess: what fraction of integrations are flagged? What does the
   flagged data look like?

### Phase 4 — Ground Truth Comparison

To measure detection and false positive rates, we need ground truth
— events that are definitely RFI in Chain B. Two approaches:

**Approach A — Injection test:**
Use ADF4351 to inject a known signal at 1420 MHz at known times.
Measure what fraction of injections are detected in Chain A.
Limitation: injected signal enters at the feed, not from the sky —
may not represent real RFI geometry.

**Approach B — Bright RFI events:**
Identify obvious RFI events in Chain B (strong, narrow, impulsive).
Check whether each was flagged by Chain A.
Limitation: selection bias toward strong events.

**Approach C — HI4PI comparison:**
Where Chain B spectrum deviates significantly from HI4PI expected
spectrum, that deviation is likely RFI. Check whether those
deviations were flagged by Chain A.
This is the most scientifically rigorous approach — uses the
expected clean signal as ground truth.

### Phase 5 — Statistical Analysis

With sufficient data (target: 1 year of sessions):

- Detection rate as a function of RFI strength
- Detection rate as a function of RFI azimuth (spatial correlation)
- False positive rate and its dependence on threshold
- Optimal flagging threshold for maximum science data retention
- Comparison with single-chain sigma clipping baseline

---

## Expected Outcomes

**Optimistic:** Reference channel catches >80% of significant RFI
events with <10% false positive rate. Strong case for dual-chain
architecture as best practice for urban single-dish HI.

**Realistic:** Reference channel catches 50–70% of events, misses
events with unfavourable geometry or polarisation. Characterising
the miss rate is itself a useful result — tells us what additional
mitigation is needed.

**Pessimistic:** Reference channel flagging is not significantly
better than single-chain sigma clipping. Would redirect effort
toward software-only mitigation (INV003, INV004).

All outcomes are scientifically useful. The goal is characterisation,
not validation of a prior assumption.

---

## Relationship to Other Investigations

| Investigation | Relationship |
|---|---|
| INV003 — RFI Flagging Algorithm | INV005 provides empirical performance data for INV003 algorithm evaluation |
| INV004 — ML RFI Mitigation | INV005 dataset is part of INV004 training corpus; flagging labels from INV005 could be ML training signal |
| INV001 — Noise Budget | Reference channel flags affect effective integration time — INV005 false positive rate feeds into sensitivity calculation |

---

## Relationship to Thesis

| Thesis chapter | INV005 contribution |
|---|---|
| Instrumentation | Reference channel architecture rationale |
| Methodology | Dual-chain flagging algorithm description |
| Results | Quantified flagging effectiveness — detection rate, false positive rate |
| Conclusions | Recommendations for urban single-dish HI methodology |

Potentially publishable in SARA journal as a standalone methodology paper.

---

## Dependencies

| Dependency | Status | Notes |
|---|---|---|
| Dual-chain simultaneous logging | Phase 3 | Requires Chain A + Chain B logging scripts |
| Aligned timestamps | Phase 3 | Both chains on same UTC clock |
| HI4PI lookup pipeline | Phase 3 | For Approach C ground truth |
| ADF4351 for injection tests | Available now | CAL-000 ready |
| INV003 flagging algorithm | Phase 4 | Cross-investigation dependency |

---

## Key References

| Reference | Relevance |
|---|---|
| Briggs, Bell & Kesteven (2000) — *AJ* 120, 3351 | Foundational reference channel flagging paper |
| Qin et al. (2025) arXiv:2508.00386 | Classical RFI mitigation baseline for comparison |
| design/DIPOLE_ANTENNA_DESIGN.md | Physical dipole specification and mounting |
| design/DUAL_SDR_ARCHITECTURE.md | Dual-chain system context |
| INV004_ml_rfi.md | Shared dataset; ML training labels |
| BRRO_references.bib | Full bibliography |

---

## Open Questions

- [ ] Define flagging threshold — fixed or adaptive?
- [ ] Define flagging window — flag single integration or ±N integrations?
- [ ] Determine minimum session count for statistically meaningful results
- [ ] Decide whether to implement Approach A (injection), B (bright events),
      or C (HI4PI comparison) first — or all three
- [ ] Verify Discovery Dish HI feed polarisation — affects interpretation
      of any polarisation-dependent miss rate

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1 | 2026-05-29 | Initial concept capture — motivation, key questions, method outline, expected outcomes, thesis chapter mapping |
