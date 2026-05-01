# Dual SDR Architecture — Design Decision

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-04-30  
**Version:** 1.0  

---

## Overview

Blue Rock Radio Observatory operates two simultaneous SDR chains rather
than a single SDR that is upgraded over time. This document records the
rationale for this architecture and the role of each chain.

---

## Architecture

```
Chain A — RFI Monitoring (continuous)
─────────────────────────────────────
Dipole antenna (tuned to 1420 MHz, 5.25cm elements)
    ↓
RTL-SDR Blog V4 (bias tee OFF — passive antenna)
    ↓ USB
Raspberry Pi (model TBC — Pi 2 or Pi 3)
    ↓ WiFi
MacBook Pro — RFI log storage and review

Chain B — Science Observations
───────────────────────────────
Discovery Dish HI Feed (1380–1460 MHz)
    ↓ 6m LMR200
Airspy R2 (bias tee ON — powers feed LNA chain)
    ↓ USB
Raspberry Pi 3
    ↓ WiFi
MacBook Pro — EZRa / GNU Radio science pipeline
```

Both chains run simultaneously during science sessions. The RFI monitoring
chain runs continuously whenever the observatory is powered, including
during non-science periods.

---

## Rationale

### 1. Contemporaneous RFI record

While Chain B integrates on a science target for several hours, Chain A
continuously logs the RFI environment at the site. Every science session
automatically produces a paired dataset:

- Science spectrum (Airspy R2, dish, pointed at target)
- Contemporaneous RFI log (V4, dipole, omnidirectional)

When investigating anomalous features in science data, the RFI log from
exactly that session is immediately available for cross-reference. This
is fundamentally more useful than periodic RFI surveys conducted at
different times from science observations.

### 2. Correlated flagging

If Chain A detects a strong RFI event at a specific UTC time, the
corresponding time samples in Chain B data can be flagged with high
confidence. The two datasets inform each other directly — RFI flagging
is no longer based solely on statistical outlier detection in the science
data, but can be triggered by independent confirmation from the monitoring
chain.

### 3. Spatial RFI discrimination

The dipole is nearly omnidirectional at 1420 MHz. The dish has a 17°
beam. Comparing simultaneous spectra from both reveals the spatial
character of RFI events:

- Feature present in both chains → likely omnidirectional source
  (e.g. broadband electrical interference, nearby transmitter)
- Feature present in dish chain only → likely directional source
  entering the main beam or a near sidelobe
- Feature present in dipole chain only → source in a direction
  the dish is not pointing

This spatial discrimination is not available from a single SDR system
and adds genuine diagnostic capability at no additional cost beyond
the V4 already owned.

### 4. Continuous site characterisation

Rather than periodic RFI survey snapshots, the monitoring chain builds
a continuous RFI record across the full four-year programme. Temporal
patterns (time of day, day of week, seasonal) emerge naturally from
the continuous record without requiring dedicated survey sessions.
This is a significantly richer dataset than periodic snapshots.

### 5. Operational redundancy

If the Airspy R2 fails during a critical observing window, the V4 can
be switched to the dish feed (with bias tee enabled) to continue
observations. Performance is degraded but the session is not lost.
Conversely if the monitoring Pi fails, science observations continue
unaffected on Chain B.

### 6. SDR retention rather than replacement

The V4 is not superseded by the Airspy R2 — it is repurposed to a
role it is well suited for. The omnidirectional RFI monitoring role
does not require the dynamic range or sample rate of the Airspy. The
V4's 8-bit ADC and 3.2 Msps are entirely adequate for broadband RFI
logging. Retiring the V4 would discard a functional instrument and
eliminate the dual-chain capability.

---

## Computing Platform Assessment

### Chain B — Science (Raspberry Pi 3)

The Pi 3 handles the science chain: Airspy R2 via USB, EZRa data
acquisition, rotctl dish control via WiFi to Discovery Drive. The Pi 3
has adequate processing power for this role in Phase 1. GNU Radio
real-time processing in Phase 2 may require assessment — if the Pi 3
proves insufficient, a Pi 4 would be the upgrade path.

### Chain A — RFI Monitoring (Pi 2 or Pi 3 — TBC)

**If Pi 2:** The Raspberry Pi 2 has a 900 MHz quad-core ARM Cortex-A7
with 1GB RAM. This is significantly less capable than the Pi 3 but
adequate for the RFI monitoring role, which requires:

- Running RTL-SDR drivers
- Capturing wideband spectrum at moderate sample rates
- Writing power spectral density logs to disk
- WiFi data transfer to MacBook

The Pi 2 does **not** have built-in WiFi — it requires a USB WiFi
dongle, which consumes one of the two USB ports alongside the V4.
A powered USB hub may be needed. This is manageable but worth
confirming during commissioning.

The Pi 2 is **not** suitable for GNU Radio real-time processing or
EZRa science pipeline — it should be reserved for the monitoring role
only.

**If Pi 3:** Straightforward — same setup as the science Pi with
built-in WiFi. No USB hub required.

**Action:** Identify the second Pi model before commissioning.
Check the board revision printed on the PCB or run `cat /proc/cpuinfo`
and check the Hardware and Revision fields.

---

## Software Architecture

### Chain A — RFI Monitoring Software

| Software | Role |
|---|---|
| RTL-SDR drivers | V4 hardware interface |
| rtl_power | Wideband power sweep logging — lightweight, ideal for Pi 2 |
| Python post-processing | Convert rtl_power output to timestamped CSV logs |
| Cron job | Automated continuous logging — restarts on failure |

`rtl_power` is specifically recommended for the monitoring chain on a
Pi 2. It is extremely lightweight compared to GNU Radio, logs wideband
power sweeps continuously, and is well suited to long-term unattended
operation. Output is a CSV of frequency vs power vs time — directly
usable for RFI analysis.

Example rtl_power command for continuous 1420 MHz band monitoring:

```bash
rtl_power -f 1400M:1440M:12.5k -g 40 -i 10 -e 1h rfi_$(date +%Y%m%d_%H%M).csv
```

This sweeps 1400–1440 MHz in 12.5 kHz steps, 40dB gain, 10 second
integration, 1 hour per output file.

### Chain B — Science Software

| Software | Role |
|---|---|
| Airspy host library | R2 hardware interface |
| EZRa | Phase 1 HI data acquisition |
| GNU Radio | Phase 2 custom pipeline |
| rotctl / Hamlib | Dish pointing via Discovery Drive |
| Astropy | Doppler corrections |

---

## Data Management

Each chain produces independent data streams. File naming conventions
ensure unambiguous identification:

**Chain A (RFI):**
```
rfi/surveys/YYYY-MM-DD_HHMM_rfi.csv
```

**Chain B (Science):**
```
sessions/YYYY/YYYY-MM-DD_TARGET_NNN.[fits/csv]
```

Session logs reference both chains:

```
Science SDR: Airspy R2 (Chain B)
RFI monitor: RTL-SDR V4 (Chain A) — log file: rfi/surveys/2026-09-14_2100_rfi.csv
```

This cross-reference is the key to the correlated flagging methodology.

---

## Phase Timeline

| Phase | Chain A | Chain B |
|---|---|---|
| Phase 1a (pre-dish) | V4 + dipole, MacBook direct | — |
| Phase 1b (dish arrival) | V4 + dipole, monitoring Pi | V4 + dish (before Airspy arrives) |
| Phase 2 (Airspy) | V4 + dipole, monitoring Pi | Airspy R2 + dish, science Pi |
| Phase 3 (DDOEE) | V4 + dipole, monitoring Pi | Airspy R2 + dish in enclosure |

---

## Known Limitations

**Pi 2 WiFi** — requires USB WiFi dongle if confirmed as Pi 2. Monitor
for USB bandwidth contention between V4 and WiFi dongle on a 2-port Pi 2.
A powered USB hub resolves this if needed.

**Dipole RFI sensitivity** — the dipole is not calibrated for absolute
flux measurements. Chain A provides relative RFI monitoring and temporal
pattern identification, not calibrated flux density. Absolute RFI
characterisation requires the dish — see rfi/RFI_OVERVIEW.md.

**No simultaneous pointing** — the dish (Chain B) points at the science
target. The dipole (Chain A) is fixed and omnidirectional. The two chains
cannot simultaneously observe the same patch of sky with equivalent
sensitivity for direct comparison.

---

## References

- SDR_SELECTION.md — SDR hardware comparison and selection rationale
- rfi/RFI_OVERVIEW.md — RFI characterisation methodology
- INV003_rfi_flagging — RFI flagging algorithm development
- E001_2026-04-30.md — current equipment state
- setup/RASPBERRY_PI_SETUP.md — Pi configuration guide

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-30 | Initial document — dual chain architecture, Pi 2 assessment |
