#!/usr/bin/env python3
# ========================================================================
# rainbow10.py
#
# Description: Display rainbow colors in a spiral pattern then animates
#              each pixel to the next color using hues.
#
# Author: Jim Ing
# Date: 2024-08-17
# ========================================================================

import colorsys
import time
from sense_hat import SenseHat

sense = SenseHat()
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

# Initialize the hue for each pixel
hues = [(i / 64.0) for i in range(64)]

try:
    print("To quit, press Ctrl+C")

    # Loop indefinitely to continuously update the colors
    while True:
        # Iterate through the spiral order to update the pixels
        for i, (x, y) in enumerate(spiral_order):
            # Get the current hue
            hue = hues[i]

            # Convert HSV to RGB
            r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0) # Full saturation and value

            # Convert RGB values to 0-255 range
            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)

            # Set the pixel on the Sense HAT
            sense.set_pixel(x, y, r, g, b)

        # Shift each hue to the next color in the rainbow sequence
        hues = [(hue + 0.015625) % 1.0 for hue in hues]

        # Add a delay to control the speed of the animation
        time.sleep(0.1)

except KeyboardInterrupt:
    sense.clear()
