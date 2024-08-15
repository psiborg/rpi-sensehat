#!/usr/bin/env python3
# ========================================================================
# kitt_scanner1.py
#
# Description: Simulate LEDs from KITT's scanner
#
# Author: Jim Ing
# Date: 2024-08-13
# ========================================================================

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

red = (255, 0, 0)
off = (0, 0, 0)

def kitt_scanner():
    while True:
        # Move from left to right
        for x in range(8):
            sense.clear()
            sense.set_pixel(x, 3, red)
            time.sleep(0.1)

        # Move from right to left
        for x in range(6, -1, -1):
            sense.clear()
            sense.set_pixel(x, 3, red)
            time.sleep(0.1)

try:
    print ("To quit, press Ctrl+C")

    kitt_scanner()

except KeyboardInterrupt:
    sense.clear()
