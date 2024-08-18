#!/usr/bin/env python3
# ========================================================================
# beat_clock.py
#
# Description: Display Swatch Internet Time (.beat).
#
# https://www.swatch.com/en-us/internet-time.html
#
# Author: Jim Ing
# Date: 2024-08-16
# ========================================================================

from sense_hat import SenseHat
from datetime import datetime, timezone, timedelta

sense = SenseHat()
sense.low_light = True

def calculate_beat_time():
    # Central European Time (CET) is UTC+1
    cet = timezone(timedelta(hours=1))
    now_cet = datetime.now(cet)

    # Calculate the total seconds since midnight CET
    seconds_since_midnight = (
        now_cet.hour * 3600 +
        now_cet.minute * 60 +
        now_cet.second
    )

    # Convert seconds into Swatch Beats
    beats = seconds_since_midnight / 86.4 # Round to the nearest whole number and return it

    return int(round(beats))

def display_time():
    while True:
        # Get the current time in regular format
        now = datetime.now()
        regular_time = now.strftime("%H:%M:%S")

        # Get the current Beat Time
        beat_time = calculate_beat_time()
        beat_time_str = f"@{beat_time:03d}" # Format as @XXX

        # Display times
        sense.show_message(f"{beat_time_str} {regular_time}", scroll_speed=0.1, text_colour=[255, 255, 255])

try:
    print ("To quit, press Ctrl+C")
    display_time()

except KeyboardInterrupt:
    sense.clear()
