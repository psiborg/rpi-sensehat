#!/usr/bin/env python3
# ========================================================================
# color_wave.py
#
# Description: Animate a gradient pattern that shifts across the rows or
#              columns.
#
# Author: Jim Ing
# Date: 2024-08-18
# ========================================================================

from sense_hat import SenseHat
import time

sense = SenseHat()

# Define the gradient colors (RGB tuples)
colors = [
    (255, 0, 0),     # Red
    (255, 165, 0),   # Orange
    (255, 255, 0),   # Yellow
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (75, 0, 130),    # Indigo
    (238, 130, 238), # Violet
    (255, 0, 255)    # Magenta
]

def shift_gradient(colors, offset):
    # Shift colors by offset for a flowing gradient effect.
    return colors[-offset:] + colors[:-offset]

def display_wave():
    offset = 0
    while True:
        for y in range(8):
            gradient_row = shift_gradient(colors, (offset + y) % len(colors))
            for x in range(8):
                sense.set_pixel(x, y, gradient_row[x % len(gradient_row)])
        offset += 1
        time.sleep(0.1)

try:
    print("To quit, press Ctrl+C")
    display_wave()

except KeyboardInterrupt:
    sense.clear()
