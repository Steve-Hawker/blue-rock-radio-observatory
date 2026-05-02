#!/usr/bin/env python3
"""
galactic_plane_track.py — Blue Rock Radio Observatory
======================================================
Generates RA/Dec coordinate sequences for tracking the Galactic plane
(b=0°) with the Discovery Drive AZ/EL mount.

Uses Astropy for coordinate transformation — more robust than manual
trigonometry for edge cases near RA=0h/24h boundary.

Inspired by ASCOM Javascript implementation by Dr. Kamal Jabbour,
Pompey Observatory (CrowdSupply Discovery Dish field report, Feb 2026).
This implementation uses Astropy for validated coordinate transforms
and outputs to CSV for rotctl / Discovery Drive integration.

Usage:
    # Default: Sgr A* region to Orion arm (17h to 9h)
    python3 galactic_plane_track.py

    # Custom range
    python3 galactic_plane_track.py --ra-start 17 --ra-end 9

    # Finer steps
    python3 galactic_plane_track.py --step-minutes 2

Author: Steve Hawker BEng MBA FRAS
Observatory: Blue Rock Radio Observatory, San Jose CA
Repository: https://github.com/Steve-Hawker/blue-rock-radio-observatory
"""

import numpy as np
import argparse

try:
    from astropy.coordinates import SkyCoord, Galactic
    import astropy.units as u
    ASTROPY_AVAILABLE = True
except ImportError:
    ASTROPY_AVAILABLE = False
    print("WARNING: Astropy not installed. Using manual trigonometry fallback.")
    print("Install with: pip3 install astropy")


# ── Astropy implementation (preferred) ────────────────────────────────────────

def galactic_plane_coords_astropy(ra_start_h, ra_end_h, n_steps=100):
    """
    Generate RA/Dec coordinates along the Galactic plane using Astropy.
    Handles all edge cases correctly including RA=0h/24h crossing.
    """
    ra_values = np.linspace(ra_start_h * 15, ra_end_h * 15, n_steps)
    coords = []
    for ra_deg in ra_values:
        eq = SkyCoord(ra=ra_deg*u.degree, dec=0*u.degree, frame='icrs')
        gal = eq.galactic
        gal_plane = SkyCoord(l=gal.l, b=0*u.degree, frame='galactic')
        eq_plane = gal_plane.icrs
        coords.append((eq_plane.ra.hour, eq_plane.dec.degree))
    return coords


# ── Manual trigonometry fallback (from Pompey Observatory equations) ──────────

def galactic_plane_coords_manual(ra_start_h, ra_end_h, n_steps=100):
    """
    Generate RA/Dec coordinates along the Galactic plane.
    Manual trigonometry implementation from Pompey Observatory equations.
    Use Astropy implementation if available.

    Galactic north pole: RA = 192.8598°, Dec = 27.128027° (B1950)
    """
    import math

    NGP_DEC_RAD = math.radians(27.128027)
    NGP_RA_H = 192.8598 / 15.0   # hours
    PA = 32.9319                   # position angle degrees

    ra_values = np.linspace(ra_start_h, ra_end_h, n_steps)
    coords = []

    for i, ra_h in enumerate(ra_values):
        # Galactic longitude
        arg = 1.0 / (math.sin(NGP_DEC_RAD) *
                     math.tan((ra_h - NGP_RA_H) * math.pi / 12.0))
        l = PA - (180.0 / math.pi) * math.atan(arg)

        # Branch correction for western galactic plane
        idx = i * (len(ra_values) - 1) / max(n_steps - 1, 1)
        if ra_h * 10 > 248:
            l = l + 180.0

        # Declination on Galactic plane
        rad_l = math.radians(l - PA)
        dec = (180.0 / math.pi) * math.asin(
            math.cos(NGP_DEC_RAD) * math.sin(rad_l))

        coords.append((ra_h, dec))

    return coords


# ── Main sequence generator ────────────────────────────────────────────────────

def generate_tracking_sequence(ra_start_h=17.0, ra_end_h=9.0,
                                step_minutes=5.0, output_file=None):
    """
    Generate time-sequenced Galactic plane pointing coordinates.

    Parameters:
        ra_start_h:   float — starting RA (hours)
        ra_end_h:     float — ending RA (hours)
        step_minutes: float — minutes between pointing updates
        output_file:  str   — optional CSV output path

    Returns:
        list of dicts with pointing data
    """
    # Calculate number of steps
    if ra_start_h > ra_end_h:
        ra_range_h = ra_start_h - ra_end_h
    else:
        ra_range_h = 24.0 - ra_end_h + ra_start_h

    total_minutes = ra_range_h * 60.0
    n_steps = max(2, int(total_minutes / step_minutes))

    # Get coordinates
    if ASTROPY_AVAILABLE:
        coords = galactic_plane_coords_astropy(ra_start_h, ra_end_h, n_steps)
        method = "Astropy"
    else:
        coords = galactic_plane_coords_manual(ra_start_h, ra_end_h, n_steps)
        method = "Manual trigonometry (Pompey Observatory equations)"

    # Build sequence
    sequence = []
    for i, (ra_h, dec_deg) in enumerate(coords):
        ra_h = ra_h % 24.0

        # Format RA
        ra_h_int = int(ra_h)
        ra_m = (ra_h - ra_h_int) * 60
        ra_m_int = int(ra_m)
        ra_s = (ra_m - ra_m_int) * 60
        ra_str = f"{ra_h_int:02d}h{ra_m_int:02d}m{ra_s:04.1f}s"

        # Format Dec
        sign = '+' if dec_deg >= 0 else '-'
        dec_abs = abs(dec_deg)
        dec_d = int(dec_abs)
        dec_m_f = (dec_abs - dec_d) * 60
        dec_m_int = int(dec_m_f)
        dec_s = (dec_m_f - dec_m_int) * 60
        dec_str = f"{sign}{dec_d:02d}d{dec_m_int:02d}m{dec_s:04.1f}s"

        sequence.append({
            'step':            i,
            'time_offset_min': i * step_minutes,
            'ra_h':            ra_h,
            'dec_deg':         dec_deg,
            'ra_str':          ra_str,
            'dec_str':         dec_str,
        })

    # Write CSV
    if output_file:
        with open(output_file, 'w') as f:
            f.write("step,time_min,ra_hours,dec_deg,ra_str,dec_str\n")
            for s in sequence:
                f.write(f"{s['step']},{s['time_offset_min']:.1f},"
                        f"{s['ra_h']:.6f},{s['dec_deg']:.6f},"
                        f"{s['ra_str']},{s['dec_str']}\n")
        print(f"Sequence written to {output_file} ({len(sequence)} steps)")

    return sequence, method


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate Galactic plane tracking coordinates for Discovery Drive'
    )
    parser.add_argument('--ra-start', type=float, default=17.0,
                        help='Starting RA in hours (default: 17 = Sgr A* region)')
    parser.add_argument('--ra-end', type=float, default=9.0,
                        help='Ending RA in hours (default: 9 = Orion arm)')
    parser.add_argument('--step-minutes', type=float, default=5.0,
                        help='Minutes between pointing updates (default: 5)')
    parser.add_argument('--output', default='galactic_plane_track.csv',
                        help='Output CSV filename')
    args = parser.parse_args()

    print("Blue Rock Radio Observatory — Galactic Plane Tracker")
    print(f"RA range: {args.ra_start}h → {args.ra_end}h")
    print(f"Step interval: {args.step_minutes} minutes")
    print()

    seq, method = generate_tracking_sequence(
        ra_start_h=args.ra_start,
        ra_end_h=args.ra_end,
        step_minutes=args.step_minutes,
        output_file=args.output
    )

    print(f"Coordinate method: {method}")
    print(f"Steps generated: {len(seq)}")
    print(f"Total duration: {seq[-1]['time_offset_min']:.0f} min "
          f"({seq[-1]['time_offset_min']/60:.1f} hrs)")
    print()
    print("First 3 pointings:")
    for s in seq[:3]:
        print(f"  +{s['time_offset_min']:5.1f} min: "
              f"RA {s['ra_str']}  Dec {s['dec_str']}")
    print("  ...")
    print("Last 3 pointings:")
    for s in seq[-3:]:
        print(f"  +{s['time_offset_min']:5.1f} min: "
              f"RA {s['ra_str']}  Dec {s['dec_str']}")
