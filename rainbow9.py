#!/usr/bin/env python3
# ========================================================================
# rainbow9.py
#
# Description: Display rainbow colors in a spiral pattern then animates
#              each pixel to the next color.
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

# Draw the initial rainbow colors on the matrix
colors = []
for i, (x, y) in enumerate(spiral_order):
    hue = i / 64.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    sense.set_pixel(x, y, r, g, b)
    colors.append((r, g, b)) # Save the color for later

# Pause to display the initial pattern
time.sleep(2)

# Continuous animation
try:
    print("To quit, press Ctrl+C")

    while True:
        # Change each pixel to the next color in the sequence
        new_colors = [colors[(i + 1) % len(colors)] for i in range(len(colors))]

        for i, (x, y) in enumerate(spiral_order):
            sense.set_pixel(x, y, new_colors[i])

        # Update the colors list to the new colors
        colors = new_colors

        # Short delay to control the speed of the animation
        time.sleep(0.2)

except KeyboardInterrupt:
    sense.clear()
