#!/usr/bin/env python3
# ========================================================================
# ecg.py
#
# Description:
#
# Author: Jim Ing
# Date: 2024-09-06
# ========================================================================

import time
from config import sense

sense.clear()

# Define colors
wave_color = (0, 255, 0)  # Green wave color
background_color = (0, 0, 0)  # Black background (off)

# ECG wave pattern data (P wave, QRS complex, T wave, flat line)
# Using a simplified version of the ECG wave in an 8x8 grid:
# Each number corresponds to the Y-coordinate for each point in the wave
ecg_wave = [4, 4, 3, 4, 6, 1, 4, 4]  # P, flat, QRS, flat, T, flat

def draw_ecg_wave(offset):
    """Draw the ECG wave on the LED matrix, offset for scrolling effect."""
    sense.clear()
    for x in range(8):
        # Calculate the corresponding Y position for each point in the wave pattern
        y = ecg_wave[(x + offset) % len(ecg_wave)]  # Loop through the wave pattern
        sense.set_pixel(x, y, wave_color)  # Set the wave pixel to green

try:
    offset = 0
    while True:
        draw_ecg_wave(offset)  # Draw the wave pattern with the current offset
        offset += 1  # Move the wave to the left by shifting the pattern
        time.sleep(0.2)  # Control the speed of the animation

except KeyboardInterrupt:
    sense.clear()  # Clear the LED matrix on exit
