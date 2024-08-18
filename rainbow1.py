#!/usr/bin/env python3
# ========================================================================
# rainbow1.py
#
# Description: Display rainbow colors in a linear sequence.
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

import colorsys
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

for x in range(8):
    for y in range(8):
        # Calculate the hue based on the position (x, y)
        hue = (x * 8 + y) / 64.0  # Range from 0 to 1

        # Convert HSV to RGB
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0) # Full saturation and value

        # Convert RGB values to 0-255 range
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        # Print the coordinates and RGB values
        print(f"({x}, {y}) -> RGB: ({r}, {g}, {b})")
        sense.set_pixel(x, y, r, g, b)

        # Add a delay
        time.sleep(0.1)
