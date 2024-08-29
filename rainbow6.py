#!/usr/bin/env python3
# ========================================================================
# rainbow6.py
#
# Description: Display rainbow colors in a spiral pattern then clear them
#              in reverse order.
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

import colorsys
import time
from config import sense

sense.clear()

# Define the spiral order for an 8x8 matrix
spiral_order = [
    (3, 3), (3, 4), (4, 4), (4, 3),
    (4, 2), (3, 2), (2, 2), (2, 3),
    (2, 4), (2, 5), (3, 5), (4, 5),
    (5, 5), (5, 4), (5, 3), (5, 2),
    (5, 1), (4, 1), (3, 1), (2, 1),
    (1, 1), (1, 2), (1, 3), (1, 4),
    (1, 5), (1, 6), (2, 6), (3, 6),
    (4, 6), (5, 6), (6, 6), (6, 5),
    (6, 4), (6, 3), (6, 2), (6, 1),
    (6, 0), (5, 0), (4, 0), (3, 0),
    (2, 0), (1, 0), (0, 0), (0, 1),
    (0, 2), (0, 3), (0, 4), (0, 5),
    (0, 6), (0, 7), (1, 7), (2, 7),
    (3, 7), (4, 7), (5, 7), (6, 7),
    (7, 7), (7, 6), (7, 5), (7, 4),
    (7, 3), (7, 2), (7, 1), (7, 0)
]

# Iterate through the spiral order to light up the pixels
for i, (x, y) in enumerate(spiral_order):
    # Calculate the hue based on the index
    hue = i / 64.0 # Range from 0 to 1

    # Convert HSV to RGB
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0) # Full saturation and value

    # Convert RGB values to 0-255 range
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)

    # Set the pixel on the Sense HAT
    sense.set_pixel(x, y, r, g, b)

    # Add a delay
    time.sleep(0.1)

# Add a delay before starting to unlight the pixels
time.sleep(5)

# Iterate through the spiral order in reverse to unlight the pixels
for x, y in reversed(spiral_order):
    # Turn off the pixel by setting it to black (0, 0, 0)
    sense.set_pixel(x, y, 0, 0, 0)

    # Add a delay
    time.sleep(0.1)
