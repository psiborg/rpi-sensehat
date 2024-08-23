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

import random
import sys
import time
from datetime import datetime
from sense_hat import SenseHat
from effects.warp import WarpEffect
from utils.color_names import HTML_COLORS

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

def warp_effect2b(duration=5):
    """Create a warp effect with stars flying from left to right with growing tails on the Sense HAT."""
    white = (255, 255, 255)
    black = (0, 0, 0)

    start_time = time.time()
    max_length = 3  # Maximum length of star tails
    delay = 0.2
    stars = []  # List to keep track of stars and their positions

    while time.time() - start_time < duration:
        sense.clear()

        # Create new stars at random positions on the left side
        if random.random() < 0.5: # 50% chance to create a star in each row
            row = random.randint(0, 7)
            stars.append({'row': row, 'col': 0, 'tail': 1}) # Start with tail length of 1

        # Move stars and update their tails
        new_stars = []
        for star in stars:
            if star['col'] < 7: # Move the star only if it's still on the matrix
                # Clear the tail
                for i in range(star['tail']):
                    if star['col'] - i >= 0:
                        sense.set_pixel(star['col'] - i, star['row'], black)

                # Move the star
                star['col'] += 1
                if star['tail'] < max_length:
                    star['tail'] += 1 # Increase tail length as the star moves

                # Draw the star and its tail
                for i in range(star['tail']):
                    if star['col'] - i >= 0:
                        sense.set_pixel(star['col'] - i, star['row'], white)

                new_stars.append(star)

        stars = new_stars

        time.sleep(delay)
        delay = max(0.01, delay * 0.9) # Gradually decrease the delay to speed up

    sense.clear()

def display_stardate(stardate):
    """Display the stardate on the Sense HAT with a slower scroll speed."""
    sense.show_message(f"Stardate: {stardate:.2f}", scroll_speed=0.08, text_colour=[255, 255, 255])

def main():
    base_system = "tng" # Default to TNG system
    if len(sys.argv) == 2:
        base_system = sys.argv[1].lower()

    warp_effect = WarpEffect(sense, speed=1, colors={
        'tl': HTML_COLORS.get('white'),
        'tr': HTML_COLORS.get('magenta'),
        'bl': HTML_COLORS.get('cyan'),
        'br': HTML_COLORS.get('orange')
    })

    print ("To quit, press Ctrl+C")

    try:
        while True:
            today = datetime.today()
            year = today.year
            month = today.month
            day = today.day
            stardate = calculate_stardate(year, month, day, base_system)
            print(stardate)

            warp_effect.fpv()
            display_stardate(stardate) # Display the updated stardate
            #warp_effect2b() # Show warp effect
            warp_effect.tpv()

            time.sleep(5)

    except KeyboardInterrupt:
        sense.clear()

if __name__ == "__main__":
    main()
