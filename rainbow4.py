#!/usr/bin/env python3
# ========================================================================
# rainbow4.py
#
# Description: Randomly display a matrix of rainbow colors, and randomly
#              clear the colors.
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

# Create a list of all positions
positions = [(x, y) for x in range(8) for y in range(8)]

# Shuffle the positions to randomize the order
random.shuffle(positions)

# List to keep track of lit pixels
lit_pixels = []

# Set pixels in random order and record the lit pixels
for x, y in positions:
    # Calculate the hue based on the position (x, y)
    hue = (x * 8 + y) / 64.0 # Range from 0 to 1

    # Convert HSV to RGB
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0) # Full saturation and value

    # Convert RGB values to 0-255 range
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)

    # Print the coordinates and RGB values
    print(f"({x}, {y}) -> RGB: ({r}, {g}, {b})")
    sense.set_pixel(x, y, r, g, b)

    # Add the position to the list of lit pixels
    lit_pixels.append((x, y))

    # Add a delay
    time.sleep(0.1)

# Add a delay before starting to unlight the pixels
time.sleep(5)

# Shuffle the list of lit pixels to randomize the order of unlighting
random.shuffle(lit_pixels)

# Unlight the pixels in the randomized order
for x, y in lit_pixels:
    sense.set_pixel(x, y, 0, 0, 0) # Set the pixel to black (off)

    # Add a delay
    time.sleep(0.1)
