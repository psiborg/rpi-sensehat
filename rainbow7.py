#!/usr/bin/env python3
# ========================================================================
# rainbow7.py
#
# Description: Display rainbow colors in a diagonal pattern.
#
# Author: Jim Ing
# Date: 2024-08-16
# ========================================================================

import colorsys
import time
from config import sense

sense.clear()

for x in range(8):
    for y in range(8):
        # Calculate the hue based on the sum of the x and y coordinates
        hue = ((x + y) % 8) / 8.0 # Adjusted to create a diagonal gradient

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
