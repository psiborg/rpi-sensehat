#!/usr/bin/env python3
# ========================================================================
# stardate_tng_clock.py
#
# Description:
#
# Author: Jim Ing
# Date: 2024-08-13
# ========================================================================

import time
from datetime import datetime
from sense_hat import SenseHat
from stardate import Stardate

sense = SenseHat()

stardate = Stardate()

def display_stardate():
    # Get the current Earth date
    now = datetime.now()

    # Calculate the Stardate
    stardate.calculate(now)

    # Get the TNG Stardate
    tng_stardate = stardate.format_stardate(stardate.tng())

    # Display the Stardate on the Sense HAT
    print(tng_stardate)
    sense.show_message(f"TNG: {tng_stardate}", scroll_speed=0.15, text_colour=[255, 255, 255])

try:
    print ("To quit, press Ctrl+C")

    while True:
        display_stardate()
        time.sleep(60)  # Update every minute

except KeyboardInterrupt:
    sense.clear()
