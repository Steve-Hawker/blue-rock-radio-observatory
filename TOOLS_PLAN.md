# Blue Rock Radio Observatory — Tools Plan

**Observer:** Steve Hawker BEng MBA FRAS  
**Repository:** https://github.com/Steve-Hawker/blue-rock-radio-observatory  
**Plan version:** 1.0  
**Date:** 2026-04-28  

*This document describes the tools used at Blue Rock Radio Observatory,
their purpose, current status, and learning resources. Update as tools
are adopted, upgraded, or replaced.*

---

## Tool Roles — Summary

| Tool | Role | Status |
|---|---|---|
| Physical log book | Real-time observing notes, primary raw record | Active |
| Git / GitHub | Version control, session logs, equipment logs, research plan | Active |
| VS Code | Editing all Markdown and code files | Active |
| Zotero | Citation management, PDF storage, thesis references | Active |
| EZRa | HI data acquisition — Phase 1 primary | To be installed |
| GNU Radio | Signal processing, custom pipeline — Phase 2 primary | To be installed |
| Python / Astropy | Data reduction, Doppler correction, analysis | To be installed |
| SDR software | SDR hardware interface | To be confirmed |

---

## Tool 1 — Physical Log Book

### Role
Real-time primary observing record. Captures observations, sketches, anomalies,
and thoughts in the moment — before they are filtered or formalised.

### Why physical
A physical log book is a legally and scientifically strong primary record.
It cannot be backdated, silently edited, or corrupted. This is standard
engineering practice and remains valid in scientific research.

### Cross-referencing with Git
Each physical log entry should note the Git session ID.
Each Git session log should note the physical log book page reference:

```
Physical log book reference: pp. 23-24
```

This creates a bidirectional link between the raw record and the structured record.

### Format
- Indexed notebook (engineering log book format preferred)
- Each entry: date (UTC), time (UTC), target, numbered pages
- Index maintained at front of book
- Each volume archived when full, volume number noted

### Current status
- Volume 1: Active
- Started: 2026-04-28

---

## Tool 2 — Git / GitHub

### Role
Version control for all structured records: session logs, equipment logs,
research plan, learning plan, tools plan, reading notes, and eventually
data reduction scripts.

### Why Git
- Every change is timestamped and attributed
- Complete history is preserved permanently
- Provides tamper-evident audit trail for scientific record
- Free, open, and will remain accessible indefinitely
- Repository can be cited in publications and thesis

### Repository
https://github.com/Steve-Hawker/blue-rock-radio-observatory

### Daily workflow
```bash
cd ~/Documents/blue-rock-radio-observatory
git add .
git commit -m "Descriptive message"
git push
```

### Commit message conventions
Messages should be specific and informative:

| Good | Poor |
|---|---|
| `Session 2026-09-14 M31 3hr integration SNR~4` | `update` |
| `E002 equipment log — replaced Filter 1` | `changes` |
| `Learning plan — completed Topic 2 Friis formula` | `notes` |
| `Research plan v1.1 — added M81 to target list` | `edit` |

### Current status
- Repository: Live at https://github.com/Steve-Hawker/blue-rock-radio-observatory
- Installed on: MacBook Pro (Sonoma 14.3)
- Git version: (check with `git --version`)

### Resources
- GitHub documentation: docs.github.com
- Git cheat sheet: education.github.com/git-cheat-sheet-education.pdf

---

## Tool 3 — Visual Studio Code

### Role
Primary editor for all Markdown files (logs, plans, notes) and all code
(Python, GNU Radio, shell scripts). One tool for everything text-based.

### Key features in use
- Markdown preview: `Cmd+Shift+V`
- Git integration: source control panel (branch icon, left sidebar)
- File renaming: right-click in sidebar → Rename
- Folder view: File → Open Folder → blue-rock-radio-observatory

### Recommended extensions to install
| Extension | Purpose |
|---|---|
| Python | Syntax highlighting, linting for Python scripts |
| Markdown All in One | Enhanced Markdown editing |
| GitLens | Enhanced Git history visibility |
| GNU Radio (if available) | GNU Radio flowgraph support |

### Current status
- Installed on: MacBook Pro (Sonoma 14.3)
- Version: (check Help → About)

### Resources
- VS Code documentation: code.visualstudio.com/docs
- Markdown in VS Code: code.visualstudio.com/docs/languages/markdown

---

## Tool 4 — Zotero

### Role
Citation management and PDF storage. Manages all academic references,
formats citations for the thesis, and stores annotated PDFs of key papers.

### What Zotero does that Git cannot
- Pulls citation metadata automatically from DOIs
- Formats references in any citation style (required for thesis)
- Integrates with Word/LibreOffice for inline citations
- Stores and annotates PDFs
- Syncs across devices

### What Git does that Zotero cannot
- Stores reading notes and personal analysis of papers
- Tracks when and how understanding developed over time
- Provides citable, timestamped record of intellectual development

### Division of responsibility
| Item | Zotero | Git |
|---|---|---|
| Paper PDF storage | ✓ | |
| Citation metadata | ✓ | |
| Thesis bibliography | ✓ | |
| Reading notes / analysis | | ✓ (`reading_notes/`) |
| "What this paper means for my programme" | | ✓ |

### Collections to create in Zotero
- HI Physics
- Radio Telescope Fundamentals
- M31 references
- High-Velocity Clouds
- Calibration standards
- HI Surveys
- Amateur Radio Astronomy

### Key references to add immediately
| Reference | DOI / source |
|---|---|
| Ben Bekhti et al. 2016 (HI4PI) | 10.1051/0004-6361/201629178 |
| Chemin et al. 2009 (M31 rotation curve) | 10.1088/0004-6256/137/2/3452 |
| Baars et al. 1977 (flux calibration) | 1977A&A....61...99B |
| Wakker et al. 2007 (Complex C distance) | 10.1086/523302 |
| Kalberla & Kerp 2009 (HI in MW) | 10.1146/annurev.astro.46.060407.145154 |

### Current status
- Installed: Yes
- Syncing to: (note your sync destination)
- University of Lancashire library integration: (check with library)

### Resources
- Zotero documentation: zotero.org/support
- University of Lancashire Zotero guidance: (check library website)

---

## Tool 5 — EZRa

### Role
Primary HI data acquisition software — Phase 1 (Year 1) of the programme.
Handles frequency switching, baseline subtraction, and Doppler correction
automatically. Produces science-ready spectra.

### Why EZRa first
EZRa allows observations to begin immediately without requiring a custom
pipeline. Phase 1 priority is accumulating data and characterising the system.
EZRa's automatic processing provides a reliable reference for validating the
custom GNU Radio pipeline in Phase 2.

### Installation
- Platform: Linux preferred; also runs on Mac
- Source: (add URL when confirmed)
- Documentation: (add URL when confirmed)

### Current status
- Installed: No
- Target installation date: Before first light

### Notes
*(Add configuration notes, known issues, version in use)*

---

## Tool 6 — GNU Radio

### Role
Custom signal processing pipeline development — Phase 2 (Year 2) onwards.
Allows full control over every stage of data acquisition and reduction.
Pipeline development is a core original contribution of the programme.

### Why GNU Radio
- Open source, actively maintained
- Industry-standard software-defined radio toolkit
- Runs on Linux and Mac
- Thesis-worthy: implementing frequency switching, Doppler correction,
  and RFI flagging from scratch demonstrates deep understanding
- Skills transferable to further research

### Key pipeline components to implement
- Frequency switching (on/off line alternation)
- Spectral averaging and integration
- Doppler correction to LSR (via Astropy)
- RFI detection and flagging
- Baseline polynomial subtraction
- Session co-addition with velocity alignment
- FITS output for archiving

### Installation
- Platform: Linux preferred; MacOS possible but more complex
- Website: gnuradio.org
- Documentation: wiki.gnuradio.org

### Current status
- Installed: No
- Target: Year 2 (2027-2028)
- Development platform: Linux (Mac Mini or resurrected Linux machine)

### Resources
- GNU Radio tutorials: wiki.gnuradio.org/index.php/Tutorials
- SARA proceedings — GNU Radio for HI (search SARA journal)

---

## Tool 7 — Python / Astropy / NumPy / SciPy

### Role
Data reduction, analysis, Doppler correction, visualisation, and FITS I/O.
The core scientific computing stack.

### Key libraries

| Library | Purpose |
|---|---|
| NumPy | Array operations, FFT, numerical computing |
| SciPy | Signal processing, statistics, fitting |
| Astropy | Doppler corrections, coordinates, FITS I/O, units |
| Matplotlib | Plotting spectra, maps, time series |
| Healpy | All-sky maps (if needed for survey comparison) |

### Critical Astropy functions
- `astropy.coordinates.SkyCoord.radial_velocity_correction()` — LSR Doppler correction
- `astropy.io.fits` — reading and writing FITS files
- `astropy.units` — unit handling throughout pipeline
- `astropy.time.Time` — UTC and LST time handling

### Installation
```bash
pip install astropy numpy scipy matplotlib healpy
```

### Current status
- Python installed: (check with `python3 --version`)
- Astropy installed: (check with `python3 -c "import astropy; print(astropy.__version__)"`)

### Resources
- Astropy documentation: docs.astropy.org
- Astropy tutorials: learn.astropy.org
- NumPy documentation: numpy.org/doc

---

## Tool 8 — SDR Hardware Interface

### Role
Interface between the SDR receiver hardware and the software pipeline.
Exact tool depends on SDR model chosen.

### Common options
| SDR Model | Software Interface | Notes |
|---|---|---|
| RTL-SDR | rtl-sdr drivers, SDR# (Mac) | Very common, low cost |
| Airspy | Airspy drivers | Higher dynamic range |
| SDRplay | SDRuno, SoapySDR | Good performance |

### SoapySDR
SoapySDR is a hardware abstraction layer that allows GNU Radio and other
software to work with multiple SDR hardware types through a single interface.
Recommended for GNU Radio integration regardless of hardware choice.

### Current status
- SDR model: (to be confirmed)
- Driver installed: No
- SoapySDR installed: No

---

## Platform Notes

### MacBook Pro (Sonoma 14.3) — primary machine
Used for: Git, VS Code, Zotero, writing, analysis
Not ideal for: GNU Radio (possible but complex on Mac)

### Linux machine — secondary / pipeline development
Used for: GNU Radio, EZRa, SDR interface, long observing sessions
Options: Mac Mini with Linux, resurrected existing Linux machine
Recommended OS: Ubuntu 22.04 LTS or 24.04 LTS

### Cross-platform workflow
All files committed to Git are automatically available on both machines
via `git pull`. Raw data files should be stored with clear paths noted
in session logs, with backup to a second location.

---

## Plan Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-28 | Initial plan |

---

*Update this document when any tool is installed, upgraded, or replaced.
Commit each update to Git with a meaningful message.*
