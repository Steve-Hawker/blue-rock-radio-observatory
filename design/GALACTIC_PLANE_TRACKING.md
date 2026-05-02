# Galactic Plane Tracking — Coordinate Transformations

**Author:** Steve Hawker BEng MBA FRAS  
**Observatory:** Blue Rock Radio Observatory  
**Date:** 2026-05-02  
**Version:** 1.0  

---

## Overview

This document records the coordinate transformation equations needed
to track the Galactic plane with an AZ/EL mount, extracted and
analysed from a field report by Dr. Kamal Jabbour (Pompey Observatory,
New York) published on CrowdSupply February 2026.

Galactic plane tracking is not a primary Blue Rock programme goal —
M31, Complex C, and HVC monitoring are the primary science targets.
However the equations are non-trivial and having them documented means
Galactic plane surveys are available as a future programme extension
without having to rederive the mathematics.

---

## Background — The Pompey Observatory Implementation

Dr. Jabbour mounted a Discovery Dish on a Skywatcher AZ-GTi mount
and wrote ASCOM Javascript code to track the Galactic plane from
RA = 17h (Sagittarius A*) to RA = 9h (Orion arm) over a 16-hour
session, producing a colourful HI intensity map of the Milky Way
at 21cm.

The code drove the mount through Stellarium using Windows batch
automation and RTL-SDR Blog V4 for data acquisition.

**Blue Rock advantage:** The Discovery Drive + rotctl + Stellarium
integration provides native tracking capability that Dr. Jabbour
had to build from scratch in ASCOM Javascript. The coordinate
transformation mathematics remain identical regardless of mount
hardware.

---

## Coordinate Systems

### Galactic coordinates (l, b)

The Galactic coordinate system is centred on the Sun with:
- **l** = Galactic longitude (0° at Galactic centre, Sgr A*)
- **b** = Galactic latitude (0° = Galactic plane, +90° = north pole)

The Galactic plane is defined by b = 0°.

### Equatorial coordinates (RA, Dec)

The standard astronomical coordinate system:
- **RA** = Right Ascension (hours, 0–24h)
- **Dec** = Declination (degrees, -90° to +90°)

The mount points in RA/Dec. Science is described in Galactic
coordinates. Transformation between the two is required.

### The Galactic north pole in equatorial coordinates (B1950)

The Galactic coordinate system is defined relative to:
- Galactic north pole: RA = 192.8598° (12h 51.4m), Dec = +27.128°
- Galactic centre (l=0°, b=0°): RA = 17h 42.4m, Dec = -28° 55'

These are the B1950 epoch values used in the standard transformation.
For J2000 epoch the values are slightly different but the difference
is small for this application.

---

## The Transformation Equations

### Galactic longitude from RA (along the Galactic plane, b=0)

From the Pompey Observatory code, the Galactic longitude l for a
point on the Galactic plane at Right Ascension RA is:

$$l = 32.9319 - \frac{180}{\pi} \arctan\left(\frac{1}{\sin(\delta_{NGP}) \cdot \tan\left(\frac{(RA - \alpha_{NGP}) \cdot \pi}{12}\right)}\right)$$

Where:
- δ_NGP = 27.128027° — declination of Galactic north pole (radians in calculation)
- α_NGP = 192.8598/15 = 12.8573h — RA of Galactic north pole
- 32.9319° — position angle correction

**Branch correction:** For RA > 248/10 = 24.8h (i.e. the western
portion of the Galactic plane): l = l + 180°

This handles the ambiguity in the arctan function.

### Declination from Galactic longitude (b=0)

For points on the Galactic plane (b = 0°):

$$Dec = \frac{180}{\pi} \arcsin\left(\cos(\delta_{NGP}) \cdot \sin(l - 32.9319°)\right)$$

Where:
- δ_NGP = 27.128027° (Galactic north pole declination)
- l = Galactic longitude calculated above
- 32.9319° = position angle of Galactic centre from north pole

### Combined: RA → (l, Dec) for b=0

Given a Right Ascension RA (in hours), the corresponding point
on the Galactic plane has:

1. Calculate radL = π(l - 32.9319)/180 where l is from equation above
2. Dec = (180/π) × arcsin(cos(δ_NGP) × sin(radL))

---

## Python Implementation

The equations above translated to Python using Astropy for
coordinate handling. This is cleaner and more robust than the
original Javascript implementation:

```python
#!/usr/bin/env python3
"""
galactic_plane_track.py
Calculates RA/Dec coordinates along the Galactic plane (b=0)
for use with Discovery Drive rotctl tracking.

Usage:
    python3 galactic_plane_track.py --ra-start 17 --ra-end 9 --steps 100
"""

import numpy as np
from astropy.coordinates import SkyCoord, Galactic
import astropy.units as u


def galactic_plane_coords(ra_start_h, ra_end_h, n_steps=100):
    """
    Generate RA/Dec coordinates along the Galactic plane.

    Uses Astropy's coordinate transformation — more robust than
    manual trigonometry for edge cases.

    Parameters:
        ra_start_h: float — starting RA in decimal hours
        ra_end_h:   float — ending RA in decimal hours
        n_steps:    int   — number of coordinate steps

    Returns:
        list of (ra_hours, dec_deg) tuples
    """
    # Generate Galactic longitudes corresponding to RA range
    # First find Galactic longitudes that correspond to the RA range
    # by sampling and using Astropy transformation

    # Sample RA values
    ra_values = np.linspace(ra_start_h, ra_end_h, n_steps) * 15  # convert to degrees

    coords = []
    for ra_deg in ra_values:
        # Convert equatorial to Galactic to find l
        eq_coord = SkyCoord(ra=ra_deg*u.degree, dec=0*u.degree, frame='icrs')
        gal = eq_coord.galactic
        l = gal.l.degree

        # Now create coordinate on Galactic plane at this longitude
        gal_plane = SkyCoord(l=l*u.degree, b=0*u.degree, frame='galactic')
        eq = gal_plane.icrs

        coords.append((eq.ra.hour, eq.dec.degree))

    return coords


def generate_tracking_sequence(ra_start_h=17.0, ra_end_h=9.0,
                                 step_minutes=5, output_file=None):
    """
    Generate a time-sequenced list of (RA, Dec) pointing coordinates
    for tracking the Galactic plane.

    Parameters:
        ra_start_h:   float — starting RA (hours) — default Sgr A* region
        ra_end_h:     float — ending RA (hours) — default Orion arm
        step_minutes: float — time between pointing updates (minutes)
        output_file:  str   — optional CSV output file path

    Returns:
        list of dicts with keys: step, ra_h, dec_deg, ra_str, dec_str
    """
    # Calculate number of steps based on RA range and sidereal rate
    # Galactic plane crosses meridian at sidereal rate ~15°/hour
    ra_range_h = abs(ra_start_h - ra_end_h)
    if ra_start_h > ra_end_h:
        ra_range_h = ra_start_h - ra_end_h
    else:
        ra_range_h = 24 - ra_end_h + ra_start_h

    total_minutes = ra_range_h * 60  # sidereal hours to minutes
    n_steps = int(total_minutes / step_minutes)

    coords = galactic_plane_coords(ra_start_h, ra_end_h, n_steps)

    sequence = []
    for i, (ra_h, dec_deg) in enumerate(coords):
        # Format RA as HH:MM:SS
        ra_h_int = int(ra_h)
        ra_m = (ra_h - ra_h_int) * 60
        ra_m_int = int(ra_m)
        ra_s = (ra_m - ra_m_int) * 60
        ra_str = f"{ra_h_int:02d}h{ra_m_int:02d}m{ra_s:04.1f}s"

        # Format Dec as ±DD:MM:SS
        sign = '+' if dec_deg >= 0 else '-'
        dec_abs = abs(dec_deg)
        dec_d = int(dec_abs)
        dec_m = (dec_abs - dec_d) * 60
        dec_m_int = int(dec_m)
        dec_s = (dec_m - dec_m_int) * 60
        dec_str = f"{sign}{dec_d:02d}°{dec_m_int:02d}'{dec_s:04.1f}\""

        sequence.append({
            'step': i,
            'time_offset_min': i * step_minutes,
            'ra_h': ra_h,
            'dec_deg': dec_deg,
            'ra_str': ra_str,
            'dec_str': dec_str,
        })

    if output_file:
        with open(output_file, 'w') as f:
            f.write("step,time_min,ra_hours,dec_deg,ra_str,dec_str\n")
            for s in sequence:
                f.write(f"{s['step']},{s['time_offset_min']:.1f},"
                        f"{s['ra_h']:.6f},{s['dec_deg']:.6f},"
                        f"{s['ra_str']},{s['dec_str']}\n")
        print(f"Sequence written to {output_file}")

    return sequence


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Generate Galactic plane tracking coordinates'
    )
    parser.add_argument('--ra-start', type=float, default=17.0,
                        help='Starting RA in hours (default: 17h = Sgr A* region)')
    parser.add_argument('--ra-end', type=float, default=9.0,
                        help='Ending RA in hours (default: 9h = Orion arm)')
    parser.add_argument('--step-minutes', type=float, default=5.0,
                        help='Minutes between pointing updates (default: 5)')
    parser.add_argument('--output', default='galactic_plane_track.csv',
                        help='Output CSV file (default: galactic_plane_track.csv)')
    args = parser.parse_args()

    print(f"Galactic plane tracking sequence")
    print(f"RA: {args.ra_start}h to {args.ra_end}h")
    print(f"Step: {args.step_minutes} minutes")
    print()

    seq = generate_tracking_sequence(
        ra_start_h=args.ra_start,
        ra_end_h=args.ra_end,
        step_minutes=args.step_minutes,
        output_file=args.output
    )

    print(f"Generated {len(seq)} pointing steps")
    print(f"Total duration: {seq[-1]['time_offset_min']:.0f} minutes "
          f"({seq[-1]['time_offset_min']/60:.1f} hours)")
    print()
    print("First 5 pointings:")
    for s in seq[:5]:
        print(f"  Step {s['step']:3d} (+{s['time_offset_min']:5.1f} min): "
              f"RA {s['ra_str']}  Dec {s['dec_str']}")
    print()
    print("Last 5 pointings:")
    for s in seq[-5:]:
        print(f"  Step {s['step']:3d} (+{s['time_offset_min']:5.1f} min): "
              f"RA {s['ra_str']}  Dec {s['dec_str']}")
```

---

## Discovery Drive Integration

The tracking sequence CSV output feeds directly into the rotctl
control pipeline. Each row specifies a pointing position and time
offset — the control software slews to each position at the
appropriate time.

Integration with the Phase 2 GNU Radio pipeline would allow
simultaneous HI data acquisition and mount control — a fully
automated Galactic plane survey session.

---

## Comparison with Pompey Observatory Implementation

| Aspect | Pompey Observatory | Blue Rock (this document) |
|---|---|---|
| Language | ASCOM Javascript | Python + Astropy |
| Coordinate transform | Manual trigonometry | Astropy (validated library) |
| Mount interface | ASCOM/Stellarium | rotctl / Discovery Drive |
| Platform | Windows | Linux / macOS |
| Edge case handling | Branch correction needed | Handled by Astropy |
| Reproducibility | Single implementation | Open source, documented |
| Calibration | Not documented | Cas A flux calibration standard |

The Astropy implementation is more robust for edge cases (e.g.
coordinates near the Galactic poles or crossing RA = 0h/24h boundary)
and benefits from a validated, widely-used coordinate library.

---

## Science Context

A Galactic plane survey at 1420 MHz maps the distribution of neutral
hydrogen in the Milky Way disk. The double-peaked velocity profiles
at each Galactic longitude reveal the spiral arm structure — different
arms appear at different LSR velocities due to Galactic differential
rotation.

This is fundamentally different from the extragalactic HI observations
(M31, M33) that form the primary Blue Rock programme. The Galactic
HI is much brighter (easier to detect) but scientifically the result
is well-established — professional surveys (HI4PI, CGPS, SGPS) have
mapped it comprehensively. A Blue Rock Galactic plane survey would
be a capability demonstration and pipeline validation exercise
rather than a new scientific result.

**Appropriate programme role:** Commissioning and pipeline validation
in Phase 1. A Galactic plane drift scan or tracked scan confirms the
system is working correctly and provides a visually compelling
demonstration of HI detection before the more challenging
extragalactic targets.

---

## References

- Jabbour, K. 2026 — "Field Report: Imaging the Hydrogen Line of
  the Milky Way" — CrowdSupply Discovery Dish project update 12
  (source of Javascript equations)
- Astropy Collaboration 2022 — *AJ* 935, 167 — Astropy coordinate
  transformation framework
- HI4PI Collaboration (Ben Bekhti et al. 2016) — professional
  Galactic HI survey for comparison
- Binney & Merrifield — *Galactic Astronomy* — Galactic coordinate
  system definition

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-02 | Initial document — equations from Pompey Observatory, Python implementation, Discovery Drive integration notes |
