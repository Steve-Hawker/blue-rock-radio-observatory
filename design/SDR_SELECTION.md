# SDR Selection — Design Decisions and Rationale

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-04-30  
**Version:** 1.0  

---

## Purpose

This document records the engineering rationale behind SDR hardware selection
for the Blue Rock Radio Observatory programme. Decisions are documented with
explicit reasoning so that future equipment reviews can assess whether the
original rationale still applies.

---

## Requirements

The SDR must satisfy the following requirements for Phase 1 and Phase 2 use:

| Requirement | Reason |
|---|---|
| Coverage of 1420.405 MHz | HI line observation |
| Bias tee output 3.3–5V, ≥120mA | Powers Discovery Dish HI feed LNA chain |
| Adequate dynamic range for urban RFI environment | San Jose RFI — avoid ADC saturation |
| GNU Radio compatibility | Phase 2 custom pipeline |
| USB interface | Raspberry Pi 3 connectivity |
| Sample rate ≥ 2 Msps | Covers full M31 HI velocity range (~2.4 MHz) |

---

## Candidates Evaluated

### Candidate 1 — RTL-SDR Blog V4

| Parameter | Value |
|---|---|
| Chipset | RTL2832U + R828D |
| Frequency range | 500 kHz — 1766 MHz |
| Sample rate | Up to 3.2 Msps |
| ADC bits | 8 |
| Bias tee | Yes — 4.5V built-in |
| TCXO | 1 PPM |
| Dynamic range | ~80 dB (8-bit ADC limited) |
| GNU Radio support | Yes — well supported |
| Discovery Dish compatibility | Explicitly confirmed by KrakenRF |
| Price | ~$40 |

### Candidate 2 — RTL-SDR Blog V3

| Parameter | Value |
|---|---|
| Chipset | RTL2832U + R820T2 |
| Frequency range | 500 kHz — 1766 MHz |
| Sample rate | Up to 3.2 Msps |
| ADC bits | 8 |
| Bias tee | Yes — 4.5V (software enabled) |
| TCXO | 1 PPM |
| Dynamic range | ~80 dB |
| GNU Radio support | Yes |
| Discovery Dish compatibility | Compatible (same bias tee voltage) |
| Price | ~$30 |

### Candidate 3 — Nooelec NESDR Smart v5

| Parameter | Value |
|---|---|
| Chipset | RTL2832U + R820T2 |
| Frequency range | 25 MHz — 1750 MHz |
| Sample rate | Up to 3.2 Msps |
| ADC bits | 8 |
| Bias tee | No — external injector required |
| TCXO | 0.5 PPM |
| Dynamic range | ~80 dB |
| GNU Radio support | Yes |
| Discovery Dish compatibility | Requires external bias tee injector |
| Price | ~$25 + ~$12 bias tee injector = ~$37 |

### Candidate 4 — Airspy R2 (Phase 2 upgrade)

| Parameter | Value |
|---|---|
| Chipset | Airspy + R820T2 |
| Frequency range | 24 — 1800 MHz |
| Sample rate | Up to 10 Msps |
| ADC bits | 12 |
| Bias tee | Yes — 4.5V built-in |
| TCXO | 0.5 PPM |
| Dynamic range | ~80 dB spurious free, significantly better in practice |
| GNU Radio support | Yes — via SoapySDR |
| Discovery Dish compatibility | Explicitly confirmed by KrakenRF |
| Price | ~$169 |

### Candidate 5 — Airspy Mini (Phase 2 alternative)

| Parameter | Value |
|---|---|
| Chipset | Airspy + R820T2 |
| Frequency range | 24 — 1700 MHz |
| Sample rate | Up to 6 Msps |
| ADC bits | 12 |
| Bias tee | Yes — 4.5V built-in |
| TCXO | 0.5 PPM |
| Dynamic range | Better than RTL-SDR, slightly less than R2 |
| GNU Radio support | Yes — via SoapySDR |
| Discovery Dish compatibility | Explicitly confirmed by KrakenRF |
| Price | ~$99 |

---

## Decision 1 — Phase 1 SDR: RTL-SDR Blog V4

**Selected:** RTL-SDR Blog V4  
**Rejected:** RTL-SDR Blog V3, Nooelec NESDR Smart v5

### V4 vs V3

The V4 is the clear choice over the V3 for the following reasons:

**Improved tuner (R828D vs R820T2)** — the R828D tuner in the V4 has better
sensitivity and lower noise at frequencies below ~200 MHz, and marginally
improved performance across the band. At 1420 MHz the difference is modest
but the V4 is the current generation product with active support.

**Bias tee implementation** — the V4 bias tee is hardware-switched, more
reliable than the software-enabled V3 bias tee which could theoretically
fail to engage correctly on software reset. For a feed-powered system
where bias tee failure means no LNA power and no signal, hardware
reliability matters.

**Active development** — the V4 is the RTL-SDR Blog's current flagship
product with ongoing firmware updates and community support. The V3 is
a previous generation.

**Cost difference is negligible** — ~$10 premium over V3 for a meaningful
hardware improvement.

### V4 vs Nooelec NESDR Smart v5

The Nooelec v5 fails the bias tee requirement:

**No built-in bias tee** — the Discovery Dish HI feed requires 3.3–5V
bias tee power to operate the LNA chain. Without bias tee the feed
produces no output. The Nooelec v5 requires an external bias tee
injector, adding:
- Additional cost (~$12) — negating the price advantage
- An additional connector join in the signal chain
- An additional failure point
- Additional insertion loss (~0.1–0.2 dB per connector)

**TCXO advantage is irrelevant** — the Nooelec v5's 0.5 PPM TCXO vs
V4's 1 PPM makes no meaningful difference at 1420 MHz for HI spectroscopy.
The frequency error from 1 PPM at 1420 MHz is 1.42 kHz — equivalent to
~0.3 km/s velocity uncertainty, well below the spectral resolution of
any practical observation. Both are vastly more stable than required.

**Explicit compatibility confirmation** — KrakenRF explicitly lists the
RTL-SDR Blog as compatible with the Discovery Dish feed. The Nooelec
is not listed. While it would likely work with an external bias tee,
using the confirmed compatible hardware eliminates one variable during
commissioning.

### Phase 1 role

The V4 serves two roles:

**Pre-dish (Phase 1a):** Connected to RTL-SDR dipole set on Amazon Basics
tripod, used for wideband RFI surveys of the Blue Rock site at 1420 MHz
before the dish arrives. GQRX on MacBook Pro for waterfall display and
survey logging. No bias tee required for passive dipole.

**On dish (Phase 1b):** Connected to Discovery Dish HI feed via 6m LMR200
with bias tee enabled. EZRa on Raspberry Pi 3 for HI data acquisition.
First light, Cas A calibration, initial HI science observations.

### Upgrade decision criteria

The V4 will be retained unless one or more of the following conditions
is observed:

- ADC saturation events despite SAW filter chain — indicates dynamic
  range is insufficient for San Jose RFI environment
- Phase noise limiting spectral baseline quality
- Sample rate insufficient to cover required velocity range

If any of these conditions arise, upgrade to Airspy R2 (see Decision 2).
If conditions are not observed after one full M31 season, V4 is adequate
and upgrade budget is redirected.

---

## Decision 2 — Phase 2 SDR: Airspy R2 (deferred)

**Selected (deferred):** Airspy R2  
**Alternative considered:** Airspy Mini

### Why Airspy over continued V4 use

The 12-bit ADC of the Airspy series represents a fundamental improvement
over the 8-bit RTL-SDR ADCs. In radio astronomy terms:

**Dynamic range** — 8-bit ADC provides ~48 dB theoretical dynamic range
(6 dB per bit). 12-bit provides ~72 dB. In a dense urban RFI environment
this is a meaningful difference — strong RFI signals that would saturate
an 8-bit ADC may be accommodated within the 12-bit range, preserving
the weak HI signal.

**Effective number of bits (ENOB)** — in practice RTL-SDR achieves closer
to 7–7.5 ENOB due to ADC non-linearity. Airspy achieves closer to 11–11.5
ENOB. The gap in real-world performance is larger than the nominal bit
count suggests.

**Sample rate** — Airspy R2 supports up to 10 Msps vs 3.2 Msps for RTL-SDR.
At 10 Msps the full HI band can be captured simultaneously, enabling
wideband RFI monitoring alongside the science channel.

### R2 vs Mini

**Airspy R2 is the preferred Phase 2 SDR** over the Mini for the following
reasons:

**Higher maximum sample rate** — R2: 10 Msps, Mini: 6 Msps. The R2's
wider instantaneous bandwidth is useful for simultaneous science and RFI
monitoring.

**Better sensitivity** — the R2 has marginally better noise figure than
the Mini at 1420 MHz, though the difference is small and largely irrelevant
given the LNA gain preceding the SDR.

**DDOEE compatibility** — the R2 is a slightly larger form factor but
fits comfortably in the Discovery Dish Outdoor Electronics Enclosure
alongside a Raspberry Pi 3.

**Cost vs capability** — at ~$169 the R2 represents the best performance
per dollar in the Airspy range for this application. The Mini at ~$99
is adequate but the $70 premium for the R2 buys meaningful additional
capability over a 4-year programme.

### Phase 2 role

The Airspy R2 becomes the primary science SDR once installed. The RTL-SDR
V4 is retained as:
- Backup SDR in case of R2 failure
- Dedicated RFI survey instrument (dipole + V4 can run independently)
- Comparison instrument for pipeline validation

---

## Summary

| Phase | SDR | Role | Trigger |
|---|---|---|---|
| 1a (pre-dish) | RTL-SDR Blog V4 | RFI surveys with dipole | Immediate |
| 1b (dish arrival) | RTL-SDR Blog V4 | HI science — EZRa | July 2026 |
| 2 (upgrade) | Airspy R2 | HI science — custom pipeline | If V4 limiting, or Year 2 |
| Retained | RTL-SDR Blog V4 | Backup / RFI surveys | Indefinitely |

---

## References

- RTL-SDR Blog V4 product page and documentation
- Nooelec NESDR Smart v5 specifications
- Airspy R2 specifications — airspy.com
- KrakenRF Discovery Dish compatibility list
- INV001 — noise budget analysis (this repository)

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-30 | Initial document — V4 vs V3 vs Nooelec v5, Airspy R2 as Phase 2 |
