#!/usr/bin/env python3
# ========================================================================
# kitt_voice.py
#
# Description: Simulate the voice module from Knight Rider's KITT.
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

import random
from time import sleep
from config import sense

# Define colors with varying brightness
red_high = [255, 0, 0]
red_medium = [150, 0, 0]
red_low = [75, 0, 0]
off = [0, 0, 0]

def draw_voice_box(height, speed):
    # Initialize all LEDs to off
    pixels = [off] * 64

    if height > 0:
        # Draw expanding bars based on the height
        for col in [3, 4]:
            for row in range(3 - height//2, 4 + height//2):
                pixels[row*8 + col] = red_high if row in [3, 4] else red_medium

        for col in [1, 2, 5, 6]:
            for row in range(4 - height//2, 3 + height//2):
                pixels[row*8 + col] = red_low

    # Update the LED matrix
    sense.set_pixels(pixels)
    sleep(speed)

try:
    print("To quit, press Ctrl+C")

    while True:
        # Randomize height (0, 2, 4, or 6 pixels) and speed (0.05 to 0.3 seconds)
        height = random.choice([0, 2, 4, 6])
        speed = random.uniform(0.05, 0.3)

        draw_voice_box(height, speed)

except KeyboardInterrupt:
    sense.clear()
