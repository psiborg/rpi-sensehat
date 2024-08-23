#!/usr/bin/env python3
# ========================================================================
# kitt_scanner2.py
#
# Description: KITT's scanner with trailing LEDs.
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

# Define colors
red = (255, 0, 0)
dim_red1 = (128, 0, 0) # Less bright red
dim_red2 = (64, 0, 0)  # Even dimmer red
off = (0, 0, 0)        # Turn off pixel

def kitt_scanner_with_trail():
    while True:
        # Move from left to right
        for x in range(8):
            sense.clear()
            sense.set_pixel(x, 3, red)
            sense.set_pixel(x, 4, red)
            if x > 0:
                sense.set_pixel(x-1, 3, dim_red1)
                sense.set_pixel(x-1, 4, dim_red1)
            if x > 1:
                sense.set_pixel(x-2, 3, dim_red2)
                sense.set_pixel(x-2, 4, dim_red2)
            time.sleep(0.1)

        # Move from right to left
        for x in range(6, -1, -1):
            sense.clear()
            sense.set_pixel(x, 3, red)
            sense.set_pixel(x, 4, red)
            if x < 7:
                sense.set_pixel(x+1, 3, dim_red1)
                sense.set_pixel(x+1, 4, dim_red1)
            if x < 6:
                sense.set_pixel(x+2, 3, dim_red2)
                sense.set_pixel(x+2, 4, dim_red2)
            time.sleep(0.1)

try:
    print ("To quit, press Ctrl+C")
    kitt_scanner_with_trail()

except KeyboardInterrupt:
    sense.clear()
