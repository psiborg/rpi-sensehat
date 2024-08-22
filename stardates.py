#!/usr/bin/env python3
# ========================================================================
# stardates.py
#
# Description: Convert from common date to Stardate.
#
# https://www.wikihow.com/Calculate-Stardates
#
# Author: Jim Ing
# Date: 2024-08-21
# ========================================================================

import sys
import time
from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()

def is_leap_year(year):
    """Check if a given year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_stardate(year, month, day, base_system):
    """Calculate the stardate based on the given year, month, day, and system."""
    if base_system == "tng":
        b = 2005     # base date for TNG
        c = 58000.00 # stardate year for TNG
    elif base_system == "tos":
        b = 2323     # base date for TOS
        c = 00000.00 # stardate year for TOS
    else:
        raise ValueError("Invalid base system. Use 'tng' or 'tos'.")

    m_values = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334] # month start days
    n = 366 if is_leap_year(year) else 365
    m = m_values[month - 1]
    if is_leap_year(year) and month > 2:
        m += 1

    stardate = c + (1000 * (year - b)) + ((1000 / n) * (m + day - 1))
    return stardate

def warp_effect():
    """Create a warp effect on the Sense HAT."""
    white = (255, 255, 255)
    black = (0, 0, 0)

    for i in range(4):
        # Simulate stars shooting by
        sense.clear(black)
        sense.set_pixel(3, 3, white)
        sense.set_pixel(4, 3, white)
        sense.set_pixel(3, 4, white)
        sense.set_pixel(4, 4, white)
        time.sleep(0.1)

        sense.clear(black)
        sense.set_pixel(2, 2, white)
        sense.set_pixel(5, 2, white)
        sense.set_pixel(2, 5, white)
        sense.set_pixel(5, 5, white)
        time.sleep(0.1)

        sense.clear(black)
        sense.set_pixel(1, 1, white)
        sense.set_pixel(6, 1, white)
        sense.set_pixel(1, 6, white)
        sense.set_pixel(6, 6, white)
        time.sleep(0.1)

        sense.clear(black)
        sense.set_pixel(0, 0, white)
        sense.set_pixel(7, 0, white)
        sense.set_pixel(0, 7, white)
        sense.set_pixel(7, 7, white)
        time.sleep(0.1)

    sense.clear(black)

def display_stardate(stardate):
    """Display the stardate on the Sense HAT with a slower scroll speed."""
    sense.show_message(f"Stardate: {stardate:.2f}", scroll_speed=0.08, text_colour=[255, 255, 255])

def main():
    base_system = "tng" # Default to TNG system
    if len(sys.argv) == 2:
        base_system = sys.argv[1].lower()

    print ("To quit, press Ctrl+C")

    while True:
        today = datetime.today()
        year = today.year
        month = today.month
        day = today.day
        stardate = calculate_stardate(year, month, day, base_system)

        warp_effect() # Show warp effect
        display_stardate(stardate) # Display the updated stardate

        time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sense.clear()
