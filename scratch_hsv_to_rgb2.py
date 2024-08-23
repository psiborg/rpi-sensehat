#!/usr/bin/env python3
# ========================================================================
# scratch_hsv_to_rgb2.py
#
# Description: Convert Scratch's HSV values to RGB color.
#
# Author: Jim Ing
# Date: 2024-08-21
# ========================================================================

from math import sqrt

# List of common HTML color names with their RGB values
html_colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "lime": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "silver": (192, 192, 192),
    "gray": (128, 128, 128),
    "maroon": (128, 0, 0),
    "olive": (128, 128, 0),
    "green": (0, 128, 0),
    "purple": (128, 0, 128),
    "teal": (0, 128, 128),
    "navy": (0, 0, 128),
    # Add more colors as needed
}

def scratch_hsv_to_rgb(h, s, v):
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

    r = int((r + m) * 255)
    g = int((g + m) * 255)
    b = int((b + m) * 255)

    return r, g, b

def closest_html_color_name(rgb):
    r, g, b = rgb
    closest_color = None
    min_distance = float('inf')

    for color_name, color_rgb in html_colors.items():
        cr, cg, cb = color_rgb
        distance = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        if distance < min_distance:
            min_distance = distance
            closest_color = color_name

    return closest_color

# Example: Convert Scratch HSV (50, 100, 100) to RGB and find the HTML color name
scratch_hue = 50
scratch_saturation = 100
scratch_value = 100

rgb = scratch_hsv_to_rgb(scratch_hue, scratch_saturation, scratch_value)
html_color_name = closest_html_color_name(rgb)

print(f"HSV: (50, 100, 100)")
print(f"RGB: {rgb}")
print(f"Closest HTML Color Name: {html_color_name}")
