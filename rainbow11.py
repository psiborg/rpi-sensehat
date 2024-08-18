#!/usr/bin/env python3
# ========================================================================
# rainbow11.py
#
# Description: Display rainbow colors in a spiral pattern followed by a
#              white dot "chaser".
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

# Store the original colors of the spiral pattern
original_colors = []

# Iterate through the spiral order to light up the pixels with their respective colors
for i, (x, y) in enumerate(spiral_order):
    # Calculate the hue based on the index
    hue = i / 64.0 # Range from 0 to 1

    # Convert HSV to RGB
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0) # Full saturation and value

    # Convert RGB values to 0-255 range
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)

    # Save the original color to restore later
    original_colors.append((r, g, b))

    # Set the pixel on the Sense HAT
    sense.set_pixel(x, y, r, g, b)

try:
    print("To quit, press Ctrl+C")

    # Animate the white dot following the spiral pattern
    while True:
        for i, (x, y) in enumerate(spiral_order):
            # Restore the previous pixel's color (except for the first iteration)
            if i > 0:
                prev_x, prev_y = spiral_order[i - 1]
                prev_color = original_colors[i - 1]
                sense.set_pixel(prev_x, prev_y, prev_color[0], prev_color[1], prev_color[2])

            # Set the current pixel to white
            sense.set_pixel(x, y, 255, 255, 255)

            # Add a delay
            time.sleep(0.1)

        # Restore the last pixel color after the loop
        last_x, last_y = spiral_order[-1]
        last_color = original_colors[-1]
        sense.set_pixel(last_x, last_y, last_color[0], last_color[1], last_color[2])

except KeyboardInterrupt:
    sense.clear()
