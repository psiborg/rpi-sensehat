#!/usr/bin/env python3
# ========================================================================
# scratch_hsv_to_rgb1.py
#
# Description: Convert Scratch's HSV values to RGB color.
#
# Author: Jim Ing
# Date: 2024-08-21
# ========================================================================

def scratch_hsv_to_rgb(h, s, v):
    # Convert Scratch HSV to standard HSV
    h = h * 3.6
    s /= 100.0
    v /= 100.0

    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    elif 300 <= h < 360:
        r, g, b = c, 0, x

    r = (r + m) * 255
    g = (g + m) * 255
    b = (b + m) * 255

    return int(r), int(g), int(b)

# Example: Convert Scratch HSV (50, 100, 100) to RGB
rgb = scratch_hsv_to_rgb(50, 100, 100)
print(f"HSV: (50, 100, 100)")
print(f"RGB: {rgb}")  # Output: (0, 255, 255)
