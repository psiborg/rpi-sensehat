#!/usr/bin/env python3
# ========================================================================
# kitt_voice.py
#
# Description: Simulate LEDs from KITT's voice box
#
# Author: Jim Ing
# Date: 2024-08-13
# ========================================================================

from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

# Define colors (from bright to dim)
colors = [
    (255, 0, 0),   # Full brightness red
    (192, 0, 0),   # Slightly dimmer red
    (128, 0, 0),   # Dim red
    (64, 0, 0),    # Very dim red
    (32, 0, 0),    # Almost off red
    (16, 0, 0),    # Barely visible red
    (8, 0, 0),     # Very faint red
    (0, 0, 0)      # Off
]

def draw_bar(column, height, max_height, is_main=True):
    mid = 3  # Middle row index (y=3 and y=4 are the center rows)

    # Clear the column
    for y in range(8):
        sense.set_pixel(column, y, colors[-1])

    # Draw the bar with decreasing brightness
    half_height = height // 2
    for i in range(half_height + 1):
        if mid - i >= 0:
            sense.set_pixel(column, mid - i, colors[i])
        if mid + i < 8:
            sense.set_pixel(column, mid + i, colors[i])

    # Fill extra height for odd heights
    if is_main and height % 2 != 0:
        if mid + half_height + 1 < 8:
            sense.set_pixel(column, mid + half_height + 1, colors[half_height])

def kitt_voice_box():
    main_columns = [3, 4]  # Main bars in the center
    side_columns = [1, 2, 5, 6]  # Side bars

    while True:
        # Generate random height for main bars
        main_height = random.randint(3, 8)  # Random height between 3 and 8

        # Calculate corresponding height for side bars
        side_height = max(1, main_height // 2)  # Side bars are half the height of main bars

        # Draw the main bars
        for column in main_columns:
            draw_bar(column, main_height, main_height, is_main=True)

        # Draw the side bars
        for column in side_columns:
            draw_bar(column, side_height, main_height, is_main=False)

        time.sleep(0.2)  # Adjust speed as needed

try:
    print ("To quit, press Ctrl+C")

    kitt_voice_box()

except KeyboardInterrupt:
    sense.clear()
