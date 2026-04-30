# Target Reference — Complex C (High-Velocity Cloud)

## Identity

| Parameter | Value |
|---|---|
| Name | Complex C |
| Type | High-Velocity Cloud (HVC) |
| Central RA (approx) | ~15h 30m |
| Central Dec (approx) | ~+55° |
| Angular extent | ~30° × 15° (very extended) |
| Distance | ~10 kpc (estimated) |

## HI Properties

| Parameter | Value |
|---|---|
| LSR velocity | -90 to -170 km/s |
| Peak brightness temperature | ~0.5 — 2 K |
| HI column density (peak) | ~2 × 10²⁰ cm⁻² |
| Kinematically separated from Galactic emission | Yes — clearly offset in velocity |

## Why Complex C is a good target

The large angular extent means a 17° beam sees a significant fraction of
the cloud simultaneously — the large beam is an advantage rather than a
liability. The anomalous velocity (-90 to -170 km/s) clearly separates
the HVC signal from Galactic plane emission, making detection and
identification unambiguous. No pointing precision is required.

## Observability from San Jose (37.3°N)

Complex C spans a large area of sky centred roughly at high northern
declination (~+55°). Well placed from San Jose for much of the year,
reaching elevations of ~70°+ at transit. Essentially year-round target.

## Science context

Complex C is believed to be infalling gas from the Galactic halo,
potentially of extragalactic origin (low metallicity observed).
It is one of the most studied HVCs and serves as an excellent
benchmark for comparison with professional data.

## Role in the calibration web

Complex C serves a dual role in the Blue Rock programme — it is both
a primary science target and an independent calibration check. This
is distinct from Cas A which provides flux calibration only.

### Velocity calibration
Complex C's well-known LSR velocity range (-90 to -170 km/s) provides
an independent check on the Doppler correction pipeline. If the measured
peak velocity disagrees with HI4PI by a systematic offset, this indicates
an error in the Doppler pipeline that affects all observations including M31.
Complex C therefore validates the velocity scale independently of Cas A.

### Beam efficiency check
HI4PI measures Complex C flux in a well-characterised beam. Comparing
Blue Rock integrated flux against HI4PI reveals any systematic beam
efficiency error — for example from feed misalignment or incorrect
aperture efficiency assumption. The derived correction factor applies
directly to M31 flux measurements.

### Baseline subtraction quality
Complex C's anomalous velocity places its signal in a clean spectral
region away from Galactic emission. Baseline ripple or curvature introduced
by the receiver will show up as discrepancies in the wings of the Complex C
profile relative to HI4PI. Identifying and correcting these baseline errors
improves M31 spectral quality, which is much more sensitive to baseline
problems than Complex C.

### RFI flagging validation
Discrepancies between Blue Rock and HI4PI at specific velocity channels
that correlate with known RFI frequencies identify gaps in the flagging
algorithm. Improvements propagate to all datasets.

### The calibration web

The three primary targets form a self-consistent calibration framework:

```
Cas A ──────────────→ Flux scale (Y-factor method)
                             ↓
Complex C vs HI4PI ─→ Beam efficiency + Velocity calibration
                             ↓
M31 ─────────────────→ Science result with fully characterised uncertainties
```

Each node checks the others. Discrepancies are informative rather than
merely problematic — they reveal systematic effects that can be quantified,
corrected, and documented. This triangulated approach is more rigorous than
relying on a single calibration source and is worth making explicit in the
thesis methodology chapter.

## Fixed pointing policy

For the calibration cross-check role to function correctly, Complex C
must be observed at a **consistent fixed pointing** across all sessions.
Casual variation in pointing position invalidates the HI4PI comparison.

**Primary monitoring pointing:**
- RA: (to be chosen and fixed at first detection)
- Dec: (to be chosen and fixed at first detection)

If deliberate offset pointing to map the cloud is undertaken, this is
recorded as a separate programme with its own pointing log, distinct
from the primary monitoring position.

## Professional data for comparison

- **HI4PI survey** provides full coverage — primary comparison dataset
- **HIPASS** (southern sky complement)
- Wakker et al. 2007, 2008 — detailed studies of Complex C distance and metallicity

## Monitoring strategy

Because Complex C is extended and kinematically isolated, repeated
observations at a fixed pointing allow long-term signal averaging.
A 3-year monitoring programme could:
1. Build very high SNR integrated spectrum
2. Search for any brightness variations (unlikely but scientifically interesting)
3. Map the velocity gradient across the cloud by varying pointing
4. Provide ongoing velocity and beam efficiency calibration checks throughout
   the programme lifetime

## Session history

| Date | Session ID | Pointing (RA, Dec) | Peak Tb (K) | Peak velocity (km/s) | Notes |
|---|---|---|---|---|---|
| (none yet) | | | | | |

## Notes

LSR velocity correction is essential — the velocity of Complex C relative
to the observer changes significantly with Earth's orbital phase.
Always apply full Doppler correction to LSR before recording velocities.
