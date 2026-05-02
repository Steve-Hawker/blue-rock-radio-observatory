#!/usr/bin/env python3
"""
generate_calendar.py — Blue Rock Radio Observatory
====================================================
Generates an iCalendar (.ics) file of observable windows for all
non-circumpolar programme targets. The resulting file can be imported
directly into Google Calendar, Apple Calendar, or any calendar
application supporting the iCalendar standard.

Circumpolar targets (Cas A, Complex C, M81) are omitted — they are
always available and adding them would clutter the calendar.

Observable window = time each day when target is above 30° elevation.
At 1420 MHz observations are valid at any time of day provided solar
separation >20-30° is maintained.

Usage:
    # Default — M31 season 2026/27 (Sep 2026 to Jan 2027)
    python3 generate_calendar.py

    # Custom date range
    python3 generate_calendar.py --start 2027-09-01 --end 2028-01-31

    # Custom output file
    python3 generate_calendar.py --output my_calendar.ics

    # Custom minimum elevation
    python3 generate_calendar.py --min-el 45

Output:
    BRRO_observing_windows_YYYY_YY.ics  (in current directory)
    Import into Google Calendar: Settings → Import & Export → Import

Author: Steve Hawker BEng MBA FRAS
Observatory: Blue Rock Radio Observatory, San Jose CA
Repository: https://github.com/Steve-Hawker/blue-rock-radio-observatory
"""

import math
import uuid
import argparse
from datetime import datetime, timedelta, timezone


# ── Observatory location ───────────────────────────────────────────────────────

LATITUDE  =  37.3382   # degrees North
LONGITUDE = -121.8863  # degrees West (negative = west)
SITE_NAME = "Blue Rock Radio Observatory, San Jose CA"

# ── Target catalogue — non-circumpolar targets only ───────────────────────────
# Circumpolar from San Jose: dec > 90 - 37.3 = 52.7°
# Cas A (+58.8°), Complex C (+55.0°), M81 (+69.1°) are circumpolar — omitted.

TARGETS = {
    'M31': {
        'dec':   41.27,
        'ra_h':   0.712,
        'emoji': '🌌',
        'desc':  'Andromeda Galaxy — primary science target',
    },
    'M33': {
        'dec':   30.66,
        'ra_h':   1.564,
        'emoji': '🌀',
        'desc':  'Triangulum Galaxy — secondary science target',
    },
    'M1': {
        'dec':   22.01,
        'ra_h':   5.575,
        'emoji': '💫',
        'desc':  'Crab Nebula — secondary calibrator',
    },
}

# ── Core calculations ──────────────────────────────────────────────────────────

def hours_above(dec, lat=LATITUDE, min_el=30.0):
    """Hours per day target is above min_el elevation."""
    lat_r = math.radians(lat)
    dec_r = math.radians(dec)
    min_r = math.radians(min_el)
    cos_H = ((math.sin(min_r) - math.sin(lat_r) * math.sin(dec_r))
             / (math.cos(lat_r) * math.cos(dec_r)))
    if cos_H > 1:  return 0.0
    if cos_H < -1: return 24.0
    H = math.degrees(math.acos(cos_H))
    return 2.0 * H / 15.0


def transit_utc(ra_h, date, lon=LONGITUDE):
    """
    Calculate UTC hour of meridian transit for given RA on given date.
    Uses simplified sidereal time formula — accurate to ~1 minute.
    """
    j2000 = datetime(2000, 1, 1, 12, 0, 0)
    d = (datetime(date.year, date.month, date.day) - j2000).total_seconds() / 86400.0
    gmst_0h = (6.697374558 + 2400.0513369 * (d / 36525.0)) % 24
    ut_transit = (ra_h - gmst_0h - lon / 15.0) % 24
    return ut_transit


def window_utc(ra_h, dec, date, min_el=30.0):
    """
    Returns (rise_utc, set_utc) as decimal hours UTC when target
    is above min_el elevation on the given date.
    """
    half = hours_above(dec, min_el=min_el) / 2.0
    transit = transit_utc(ra_h, date)
    rise = (transit - half) % 24
    set_ = (transit + half) % 24
    return rise, set_


def to_datetime_utc(date, decimal_hours):
    """Convert date + decimal UTC hours to a timezone-aware datetime."""
    hh = int(decimal_hours % 24)
    remainder = (decimal_hours % 24 - hh) * 60
    mm = int(remainder)
    ss = int((remainder - mm) * 60)
    return datetime(date.year, date.month, date.day, hh, mm, ss,
                    tzinfo=timezone.utc)


# ── iCalendar generation ───────────────────────────────────────────────────────

def generate_ics(start_date, end_date, min_el=30.0, targets=None):
    """
    Generate iCalendar content as a string.

    Parameters:
        start_date: datetime — first day of calendar
        end_date:   datetime — last day of calendar
        min_el:     float — minimum elevation in degrees (default 30)
        targets:    dict — target catalogue (default TARGETS)

    Returns:
        str — iCalendar formatted string
    """
    if targets is None:
        targets = TARGETS

    lines = [
        'BEGIN:VCALENDAR',
        'VERSION:2.0',
        'PRODID:-//Blue Rock Radio Observatory//Observing Windows//EN',
        'CALSCALE:GREGORIAN',
        'METHOD:PUBLISH',
        'X-WR-CALNAME:Blue Rock Observatory — Observing Windows',
        f'X-WR-CALDESC:Observable windows {start_date.strftime("%b %Y")} to '
        f'{end_date.strftime("%b %Y")} — {SITE_NAME}',
        'X-WR-TIMEZONE:America/Los_Angeles',
    ]

    current = start_date
    event_count = 0

    while current <= end_date:
        for name, t in targets.items():
            hrs = hours_above(t['dec'], min_el=min_el)
            if hrs == 0:
                continue  # target never rises on this day

            rise_h, set_h = window_utc(t['ra_h'], t['dec'], current, min_el)

            rise_dt = to_datetime_utc(current, rise_h)

            # Handle window crossing midnight
            if set_h < rise_h:
                set_dt = to_datetime_utc(current + timedelta(days=1), set_h)
            else:
                set_dt = to_datetime_utc(current, set_h)

            summary = f"{t['emoji']} {name} observable ({hrs:.1f}h)"
            description = (
                f"{name} — {t['desc']}\\n"
                f"Observable for {hrs:.1f} hours above {min_el:.0f}°\\n"
                f"{SITE_NAME}\\n"
                f"Lat: {LATITUDE}°N  Lon: {LONGITUDE}°W\\n"
                f"Times in UTC — Google Calendar converts to local time\\n"
                f"Solar separation must be checked before observing"
            )

            lines += [
                'BEGIN:VEVENT',
                f'UID:{uuid.uuid4()}',
                f'SUMMARY:{summary}',
                f'DESCRIPTION:{description}',
                f'DTSTART:{rise_dt.strftime("%Y%m%dT%H%M%SZ")}',
                f'DTEND:{set_dt.strftime("%Y%m%dT%H%M%SZ")}',
                'STATUS:CONFIRMED',
                'TRANSP:TRANSPARENT',  # shows as free — not blocking
                'END:VEVENT',
            ]
            event_count += 1

        current += timedelta(days=1)

    lines.append('END:VCALENDAR')
    print(f"Generated {event_count} events across "
          f"{(end_date - start_date).days + 1} days")

    return '\r\n'.join(lines)


# ── Entry point ────────────────────────────────────────────────────────────────

def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate observing window calendar for Blue Rock Radio Observatory'
    )
    parser.add_argument(
        '--start', default='2026-09-01',
        help='Start date YYYY-MM-DD (default: 2026-09-01)'
    )
    parser.add_argument(
        '--end', default='2027-01-31',
        help='End date YYYY-MM-DD (default: 2027-01-31)'
    )
    parser.add_argument(
        '--min-el', type=float, default=30.0,
        help='Minimum elevation in degrees (default: 30)'
    )
    parser.add_argument(
        '--output', default=None,
        help='Output filename (default: auto-generated from dates)'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    start = datetime.strptime(args.start, '%Y-%m-%d')
    end   = datetime.strptime(args.end,   '%Y-%m-%d')

    if args.output:
        filename = args.output
    else:
        filename = (f"BRRO_observing_windows_"
                    f"{start.strftime('%Y%m')}_"
                    f"{end.strftime('%Y%m')}.ics")

    print(f"Blue Rock Radio Observatory — Calendar Generator")
    print(f"Site: {SITE_NAME}")
    print(f"Date range: {start.strftime('%d %b %Y')} to {end.strftime('%d %b %Y')}")
    print(f"Minimum elevation: {args.min_el}°")
    print(f"Targets: {', '.join(TARGETS.keys())} (circumpolar targets omitted)")
    print(f"Output: {filename}")
    print()

    ics = generate_ics(start, end, min_el=args.min_el)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(ics)

    print(f"\nDone. Import {filename} into Google Calendar:")
    print("  Settings (gear icon) → Import & Export → Import")
    print("  Select 'Blue Rock Observatory' as the destination calendar")
    print("  (create this calendar first if it doesn't exist)")
