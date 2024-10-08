#!/usr/bin/env python3
# ========================================================================
# stardate_clock.py
#
# Description: Stardate is a fictional timekeeping system from Star Trek.
#
# Author: Jim Ing
# Date: 2024-08-16
# ========================================================================

from datetime import datetime
from config import sense

def calculate_stardate():
    now = datetime.now()
    year = now.year
    day_of_year = now.timetuple().tm_yday

    # Calculate Stardate
    stardate = year * 1000 + (day_of_year / 365) * 1000 # Format Stardate with 2 decimal places
    return f"{stardate:.2f}"

def display_time():
    while True:
        # Get the current time in regular format
        now = datetime.now()
        regular_time = now.strftime("%H:%M:%S")

        # Get the current Stardate
        stardate = calculate_stardate()

        # Display the regular time
        #sense.show_message(f"Time: {regular_time}", scroll_speed=0.1, text_colour=[255, 255, 255])

        # Display the Stardate
        print(f"Stardate: {stardate}")
        sense.show_message(f"Stardate: {stardate}", scroll_speed=0.15, text_colour=[0, 255, 0])

try:
    print ("To quit, press Ctrl+C")
    display_time()

except KeyboardInterrupt:
    sense.clear()
