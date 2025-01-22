#!/usr/bin/env python3
# ========================================================================
# wopr_launch_codes.py
#
# Description: Simulates the animated LEDs resembling the WOPR's display
#              from WarGames while trying to hack launch codes. The
#              animation includes random flashing patterns and waves of
#              light, simulating a chaotic, computational look.
#
# Author: Jim Ing
# Date: 2025-01-21
# ========================================================================

import math
import random
import time

from config import sense
sense.clear()

# Define colors
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# Create a list of colors for variety
colors = [red, orange, yellow]

def random_flashes(duration=5):
    """Generate random flashes across the LED matrix for a given duration."""
    start_time = time.time()
    while time.time() - start_time < duration:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        color = random.choice(colors)
        sense.set_pixel(x, y, color)
        time.sleep(random.uniform(0.05, 0.2))
        sense.set_pixel(x, y, black)

def sinusoidal_wave(duration=5):
    """Animate a sinusoidal wave pattern across the LED matrix with random width and speed."""
    start_time = time.time()
    phase = 0  # Start phase for the sine wave

    while time.time() - start_time < duration:
        # Randomize frequency (wave width) and speed
        frequency = random.uniform(2, 4)  # Controls the number of waves across the width
        speed = random.uniform(0.1, 0.5)  # Controls the speed of the wave

        for x in range(8):
            # Calculate the y-position of the wave for this x
            y = int(3.5 + 3.5 * math.sin(frequency * (x / 7.0) + phase))

            # Set the pixel color based on the wave
            for row in range(8):
                if row == y:
                    color = random.choice(colors)
                    sense.set_pixel(x, row, color)
                else:
                    sense.set_pixel(x, row, black)

        # Advance the wave phase for animation
        phase += random.uniform(0.2, 0.5)  # Randomize phase increment for variable speed
        time.sleep(speed)
        sense.clear()

def grid_pattern(duration=5):
    """Display 2-4 groups of random flashing pixels."""
    start_time = time.time()

    while time.time() - start_time < duration:
        # Clear the grid before each new group
        sense.clear()

        # Randomize the number of groups (2 to 4)
        num_groups = random.randint(2, 4)

        # Generate random flashing groups
        for _ in range(num_groups):
            group_color = random.choice(colors)
            group_size = random.randint(2, 6)  # Each group has 2 to 6 pixels
            for _ in range(group_size):
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                sense.set_pixel(x, y, group_color)

        # Hold the group pattern briefly before flashing again
        time.sleep(0.5)
        sense.clear()
        time.sleep(0.3)

def main():
    try:
        while True:
            random_flashes(duration=3)
            sinusoidal_wave(duration=3)
            grid_pattern(duration=3)
    except KeyboardInterrupt:
        sense.clear()

if __name__ == "__main__":
    main()
