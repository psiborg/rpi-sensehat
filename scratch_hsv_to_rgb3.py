#!/usr/bin/env python3
# ========================================================================
# scratch_hsv_to_rgb3.py
#
# Description: Convert Scratch's HSV values to RGB color.
#
# Author: Jim Ing
# Date: 2024-08-21
# ========================================================================

import argparse
from math import sqrt
from utils.color_names import HTML_COLORS

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

    for color_name, color_rgb in HTML_COLORS.items():
        cr, cg, cb = color_rgb
        distance = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        if distance < min_distance:
            min_distance = distance
            closest_color = color_name

    return closest_color

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Scratch HSV to RGB and find the closest HTML color name.")
    parser.add_argument("hue", type=float, help="Hue value (0-100 in Scratch)")
    parser.add_argument("saturation", type=float, help="Saturation value (0-100 in Scratch)")
    parser.add_argument("value", type=float, help="Value (Brightness) value (0-100 in Scratch)")

    args = parser.parse_args()

    scratch_hue = args.hue
    scratch_saturation = args.saturation
    scratch_value = args.value

    rgb = scratch_hsv_to_rgb(scratch_hue, scratch_saturation, scratch_value)
    html_color_name = closest_html_color_name(rgb)

    print(f"Scratch HSV: ({scratch_hue}, {scratch_saturation}, {scratch_value})")
    print(f"RGB: {rgb}")
    print(f"Closest HTML Color Name: {html_color_name}")
