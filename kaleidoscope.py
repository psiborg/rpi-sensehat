#!/usr/bin/env python3
# ========================================================================
# kaleidoscope.py
#
# Description: Simulate a kaleidoscope pattern.
#
# Author: Jim Ing
# Date: 2024-09-24
# ========================================================================

import argparse
import time
import random
from signal import pause
from config import sense

# Define color palettes
palettes = {
    'rainbow': [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238), (0, 0, 0)],  # Black included
    'cool': [(0, 255, 255), (0, 128, 255), (0, 0, 255), (0, 0, 128), (0, 0, 0)],  # Blue shades and black
    'warm': [(255, 0, 0), (255, 165, 0), (255, 255, 0), (255, 69, 0), (0, 0, 0)],  # Warm colors and black
    'pastel': [(255, 182, 193), (176, 224, 230), (255, 218, 185), (221, 160, 221), (0, 0, 0)],  # Pastel colors and black
    'grayscale': [(255, 255, 255), (192, 192, 192), (128, 128, 128), (64, 64, 64), (0, 0, 0)],  # Shades of gray and black
}

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Kaleidoscope for Sense HAT")
parser.add_argument("--mode", choices=["random", "smooth"], default="random", help="Control mode")
parser.add_argument("--palette", choices=palettes.keys(), default="rainbow", help="Choose color palette")
args = parser.parse_args()

# Load selected color palette
color_palette = palettes[args.palette]

# Rotate a pixel matrix (8x8 grid)
def rotate_pixels_90_clockwise(pixels):
    rotated = [None] * 64
    for y in range(8):
        for x in range(8):
            rotated[x * 8 + (7 - y)] = pixels[y * 8 + x]
    return rotated

# Draw a symmetrical kaleidoscope pattern
def draw_kaleidoscope(pixels):
    # Apply symmetry to an 8x8 grid
    for y in range(4):  # Work on the first 4 rows (top half)
        for x in range(4):  # Work on the first 4 columns (left half)
            mirror_x = 7 - x  # Symmetry along the vertical axis
            mirror_y = 7 - y  # Symmetry along the horizontal axis
            pixels[y * 8 + mirror_x] = pixels[y * 8 + x]  # Horizontal mirror
            pixels[mirror_y * 8 + x] = pixels[y * 8 + x]  # Vertical mirror
            pixels[mirror_y * 8 + mirror_x] = pixels[y * 8 + x]  # Both axes mirror

    sense.set_pixels(pixels)

# Initialize the pixel grid with random colors
def initialize_pixels():
    return [random.choice(color_palette) for _ in range(64)]

# Random mode
def random_mode():
    while True:
        pixels = initialize_pixels()
        draw_kaleidoscope(pixels)
        time.sleep(1)

# Smooth transition mode
def smooth_transition_mode():
    pixels = initialize_pixels()
    while True:
        draw_kaleidoscope(pixels)
        time.sleep(0.5)  # Control the speed of transitions
        # Apply a 90-degree clockwise rotation to the pixel grid
        pixels = rotate_pixels_90_clockwise(pixels)

try:
    # Run the script based on the selected mode
    if args.mode == "random":
        random_mode()
    elif args.mode == "smooth":
        smooth_transition_mode()

except KeyboardInterrupt:
    sense.clear()
