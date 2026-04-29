# Investigations — Blue Rock Radio Observatory

**Observer:** Steve Hawker BEng MBA FRAS  
**Repository:** https://github.com/Steve-Hawker/blue-rock-radio-observatory  

---

## Purpose

This directory contains structured engineering and scientific investigations
conducted at Blue Rock Radio Observatory. Each investigation follows a formal
methodology: analytical prediction, experimental measurement, validation of
prediction against measurement, and conclusions.

Investigations are distinct from routine observations. They address specific
technical or scientific questions about system performance, upgrade paths,
or methodology, and are intended to produce results useful beyond this
specific programme — potentially publishable in SARA proceedings.

---

## Investigation Index

| ID | Title | Status | Started | Completed |
|---|---|---|---|---|
| INV001 | Signal Chain Noise Budget and Upgrade Path Analysis | In planning | 2026-04-28 | |
| INV002 | Digital Filter Design for HI Spectroscopy Pipeline | Planned | | |
| INV003 | RFI Flagging Algorithm Development and Validation | Planned | | |

---

## Investigation Methodology

Each investigation follows this structure:

1. **Motivation** — why this question matters
2. **Background** — relevant theory and prior work
3. **Analytical prediction** — calculate expected result before measuring
4. **Experimental method** — how measurements will be made
5. **Results** — measured data
6. **Validation** — comparison of prediction vs measurement
7. **Conclusions** — what was learned, what follows
8. **References**

This structure mirrors a journal paper and provides practice for thesis writing.

---

## File Naming

```
investigations/
├── INVESTIGATIONS.md                    ← this file
├── INV001_noise_budget/
│   ├── INVESTIGATIONS.md                ← investigation overview and status
│   ├── analysis.py              ← Python Friis model
│   ├── measurements.csv         ← measured data
│   └── results.md               ← findings and conclusions
├── INV002_digital_filters/
└── INV003_rfi_flagging/
```
