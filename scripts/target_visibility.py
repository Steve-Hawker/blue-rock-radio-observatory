#!/usr/bin/env python3
"""
target_visibility.py — Blue Rock Radio Observatory
====================================================
Calculates transit elevations, daily hours above minimum elevation,
and monthly night-time availability for all programme targets.

Observer location: San Jose, California (37.3382°N, 121.8863°W)

Usage:
    python3 target_visibility.py

Output:
    - Target transit elevations and daily availability
    - Monthly availability table (night-time quality)

Author: Steve Hawker BEng MBA FRAS
Observatory: Blue Rock Radio Observatory
Date: 2026-04-30
"""

import math

# ── Observer location ──────────────────────────────────────────────────────────

LATITUDE  = 37.3382   # degrees North — San Jose CA
LONGITUDE = -121.8863 # degrees West

# ── Target catalogue ───────────────────────────────────────────────────────────

TARGETS = {
    'Cas A':        {'dec': 58.81,  'ra_h': 23.39},
    'M31':          {'dec': 41.27,  'ra_h': 0.712},
    'Complex C':    {'dec': 55.0,   'ra_h': 15.5},
    'M1':           {'dec': 22.01,  'ra_h': 5.575},
    'M33':          {'dec': 30.66,  'ra_h': 1.564},
    'M81':          {'dec': 69.07,  'ra_h': 9.926},
    'Gal Centre':   {'dec': -29.01, 'ra_h': 17.76},
}

# ── Approximate RA of midnight Sun by month ────────────────────────────────────
# (the RA that transits at local midnight each month)

MIDNIGHT_RA = {
    'Jan': 7,  'Feb': 9,  'Mar': 11, 'Apr': 13,
    'May': 15, 'Jun': 17, 'Jul': 19, 'Aug': 21,
    'Sep': 23, 'Oct': 1,  'Nov': 3,  'Dec': 5,
}

MONTHS = ['Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec']

# ── Core calculations ──────────────────────────────────────────────────────────

def transit_elevation(dec, lat=LATITUDE):
    """Maximum elevation at meridian transit (degrees)."""
    return 90.0 - abs(lat - dec)


def hours_above(dec, lat=LATITUDE, min_el=30.0):
    """
    Approximate hours per day the target is above min_el elevation.
    Returns 0 if never rises above min_el, 24 if always above.
    """
    lat_r = math.radians(lat)
    dec_r = math.radians(dec)
    min_r = math.radians(min_el)

    cos_H = ((math.sin(min_r) - math.sin(lat_r) * math.sin(dec_r))
             / (math.cos(lat_r) * math.cos(dec_r)))

    if cos_H > 1:
        return 0.0    # never rises above min_el
    if cos_H < -1:
        return 24.0   # always above min_el (circumpolar)

    H = math.degrees(math.acos(cos_H))
    return round(2.0 * H / 15.0, 1)


def night_quality(ra_h, dec, lat=LATITUDE, min_el=30.0):
    """
    Monthly night-time availability symbol.
    Based on angular distance of target RA from midnight RA.
    ● = best (transits near midnight)
    ◑ = moderate
    ○ = poor (daylight transit)
    ✗ = never rises above minimum elevation
    """
    if hours_above(dec, lat, min_el) == 0:
        return {m: '✗' for m in MONTHS}

    result = {}
    for month, mid_ra in MIDNIGHT_RA.items():
        diff = abs(ra_h - mid_ra)
        if diff > 12:
            diff = 24 - diff
        if diff <= 3:
            result[month] = '●'
        elif diff <= 6:
            result[month] = '◑'
        else:
            result[month] = '○'
    return result


# ── Output ─────────────────────────────────────────────────────────────────────

def print_summary():
    print("=" * 60)
    print("BLUE ROCK RADIO OBSERVATORY — Target Visibility")
    print(f"Site: San Jose CA  {LATITUDE}°N  {LONGITUDE}°W")
    print(f"Minimum useful elevation: 30°")
    print("=" * 60)

    print(f"\n{'Target':<14} {'Transit El':>10} {'Hrs/day >30°':>13}")
    print("-" * 42)
    for name, t in TARGETS.items():
        el  = transit_elevation(t['dec'])
        hrs = hours_above(t['dec'])
        flag = " ← never usable" if hrs == 0 else ""
        print(f"{name:<14} {el:>9.1f}°  {hrs:>10.1f} hrs{flag}")

    print("\n")
    print("Monthly observing quality — time of day when target transits")
    print("All symbols represent valid observing conditions at 1420 MHz")
    print("● transits at night   ◑ transits dawn/dusk   ○ transits daytime   ✗ never rises")
    print("● best  ◑ moderate  ○ poor/daytime  ✗ never rises")
    print()

    header = f"{'Target':<14}" + "".join(f" {m}" for m in MONTHS)
    print(header)
    print("-" * (14 + 4 * 12))

    for name, t in TARGETS.items():
        quality = night_quality(t['ra_h'], t['dec'])
        row = f"{name:<14}" + "".join(f"  {quality[m]}" for m in MONTHS)
        print(row)

    print()
    print("NOTE: ○ targets transit in daylight but ARE observable at")
    print("1420 MHz. Full schedule flexibility means daytime sessions")
    print("are viable — table shows night-time quality only.")


def elevation_at_time(dec, hour_angle_deg, lat=LATITUDE):
    """
    Elevation of target at a given hour angle (degrees).
    hour_angle_deg = 0 at transit, positive = west of meridian.
    """
    lat_r = math.radians(lat)
    dec_r = math.radians(dec)
    ha_r  = math.radians(hour_angle_deg)

    sin_el = (math.sin(lat_r) * math.sin(dec_r)
              + math.cos(lat_r) * math.cos(dec_r) * math.cos(ha_r))
    return math.degrees(math.asin(sin_el))


def print_elevation_arc(name, dec, steps=13):
    """Print elevation vs hour angle for a target."""
    print(f"\n{name} (dec {dec:+.1f}°) — elevation arc")
    print(f"{'Hour angle':>12}  {'Elevation':>10}")
    print("-" * 26)
    for i in range(steps):
        ha = -90 + i * 15   # -90° to +90° in 15° steps
        el = elevation_at_time(dec, ha)
        bar = '█' * max(0, int(el / 3))
        marker = " ← transit" if ha == 0 else ""
        print(f"{ha:>+11}°  {el:>9.1f}°  {bar}{marker}")


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print_summary()

    # Elevation arcs for primary targets
    print("\n" + "=" * 60)
    print("ELEVATION ARCS — primary targets")
    print("=" * 60)
    for name in ['M31', 'Cas A', 'Complex C']:
        print_elevation_arc(name, TARGETS[name]['dec'])

    print()
    print("To add a new target, add an entry to the TARGETS dictionary.")
    print("RA in decimal hours, Dec in decimal degrees (positive = North).")
