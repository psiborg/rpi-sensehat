#!/usr/bin/env python3
# ========================================================================
# rainbow2.py
#
# Description: Display random rainbow colors in a linear sequence.
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

import colorsys
import random
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# Generate 64 rainbow colors
colors = []
for i in range(64):
    hue = i / 64.0 # Range from 0 to 1
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0) # Full saturation and value
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    colors.append((r, g, b))

# Shuffle the colors to randomize the order
random.shuffle(colors)

# Print colors in (x, y, r, g, b) format
for i, (r, g, b) in enumerate(colors):
    x = i // 8 # Row index
    y = i % 8  # Column index
    print(f"({x}, {y}, {r}, {g}, {b})")
    sense.set_pixel(x, y, r, g, b)

    # Add a delay
    time.sleep(0.1)
