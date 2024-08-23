#!/usr/bin/env python3
# ========================================================================
# rainbow8.py
#
# Description: Display rainbow colors in a diagonal pattern that rotates
#              360 degrees and then rotates back.
#
# Author: Jim Ing
# Date: 2024-08-16
# ========================================================================

import colorsys
import math
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

def rotate_around_center(x, y, angle):
    # Translate the coordinates to center (3.5, 3.5)
    cx, cy = 3.5, 3.5
    x -= cx
    y -= cy

    # Rotate the coordinates
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)

    # Translate back to original position
    new_x += cx
    new_y += cy

    return int(round(new_x)), int(round(new_y))

def display_rotating_pattern(angle):
    for x in range(8):
        for y in range(8):
            # Calculate the rotated coordinates
            rotated_x, rotated_y = rotate_around_center(x, y, angle)

            # Calculate the hue based on the original position (for consistent color pattern)
            hue = ((rotated_x + rotated_y) % 8) / 8.0

            # Convert HSV to RGB
            r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0) # Full saturation and value

            # Convert RGB values to 0-255 range
            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)

            # Set the pixel color
            sense.set_pixel(x, y, r, g, b)

def pause_if_corner(angle):
    # Check if the angle is close to a corner (0°, 90°, 180°, 270°)
    if angle % 90 == 0:
        time.sleep(2) # Pause for 2 seconds

try:
    print("To quit, press Ctrl+C")

    while True:
        # Rotate pattern forward
        for i in range(0, 360, 5): # Rotate in 5-degree increments
            angle = math.radians(i)
            display_rotating_pattern(angle)
            pause_if_corner(i)
            time.sleep(0.1) # Control the speed of rotation

        # 5-second pause before rotating back
        time.sleep(5)

        # Rotate pattern backward
        for i in range(360, 0, -5): # Rotate back in 5-degree increments
            angle = math.radians(i)
            display_rotating_pattern(angle)
            pause_if_corner(i)
            time.sleep(0.1) # Control the speed of rotation

        # 5-second pause before starting again
        time.sleep(5)

except KeyboardInterrupt:
    sense.clear()
