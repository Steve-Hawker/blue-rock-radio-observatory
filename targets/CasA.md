# Target Reference — Cassiopeia A (Cas A)

## Identity

| Parameter | Value |
|---|---|
| Common name | Cassiopeia A |
| Catalogue | Cas A, 3C 461, G111.7-2.1 |
| Type | Supernova remnant |
| RA (J2000) | 23h 23m 27.9s |
| Dec (J2000) | +58° 48' 42" |
| Distance | ~3.4 kpc |
| Age (approx) | ~340 years (SN ~1680 AD) |

## Radio Properties at 1420 MHz

| Parameter | Value | Reference |
|---|---|---|
| Flux density (J2000 epoch) | ~2723 Jy | Baars et al. 1977 |
| Secular decrease rate | ~0.77% per year | |
| Angular diameter | ~5 arcmin | |
| Spectral index | ~-0.77 | |

**Flux at any epoch:**
F(year) = 2723 × (1 - 0.0077)^(year - 2000) Jy

Expected values:
- 2026: ~2567 Jy
- 2027: ~2547 Jy
- 2028: ~2528 Jy
- 2029: ~2508 Jy

## Observability from San Jose (37.3°N)

| Parameter | Value |
|---|---|
| Max elevation | ~74° |
| Circumpolar | No (sets briefly) |
| Best season | Year-round, highest in autumn/winter |
| Hours above 30° | ~14 hrs/day (autumn) |

## Role in observing program

**Primary calibration standard.** Cas A should be observed:
- At the start of every new equipment configuration
- At least monthly during active observing seasons
- Whenever system behaviour seems anomalous

Each Cas A observation yields an independent estimate of Tsys and SEFD,
allowing tracking of system performance over time and detection of any
degradation (connector corrosion, LNA ageing, feed misalignment etc).

## Secondary science goal

The secular flux decrease of ~0.77%/yr means over 3 years of monitoring,
the total change is ~2.3%. This is potentially measurable with careful
absolute calibration. Requires:
- Consistent gain settings across all sessions
- Well-characterised receiver linearity
- Careful treatment of atmospheric opacity (minor at 1420 MHz)

## HI absorption science

Foreground HI clouds along the line of sight to Cas A produce absorption
features at specific LSR velocities. These are well-catalogued and provide
a check on your velocity calibration and spectral resolution.

Key absorption components (approximate LSR velocities):
- Perseus arm: ~ -47 km/s
- Local arm: ~ -5 km/s
- Outer arm: ~ +5 km/s (weak)

Detecting these absorption features confirms your Doppler pipeline is working.

## Session history

| Date | Session ID | Derived Tsys (K) | Derived SEFD (Jy) | Notes |
|---|---|---|---|---|
| (none yet) | | | | |

## Notes

Cas A is unresolved by a 70cm dish at 1420 MHz (beam ~17°, source ~5').
Treat as a point source for all flux calculations.
