#!/usr/bin/env python3
# ========================================================================
# wopr.py
#
# Description: Simulates WOPR activity by lighting up random patterns on
#              the LED matrix in pulses.
#
# Author: Jim Ing
# Date: 2024-12-29
# ========================================================================

import time
import random
from config import sense

def generate_random_led_color():
    """Generate a random RGB color."""
    red = [255, 0, 0]
    amber = [255, 191, 0]
    yellow = [255, 255, 0]
    green = [0, 255, 0]
    return random.choice([red, amber])

def wopr_simulation():
    """Simulate WOPR LED activity with colors."""
    try:
        while True:
            led_matrix = [[0, 0, 0] for _ in range(64)]

            # Simulate activity by lighting up random patterns
            for _ in range(random.randint(5, 15)):
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                led_matrix[y * 8 + x] = generate_random_led_color()

            # Update the Sense HAT LED matrix
            sense.set_pixels(led_matrix)

            # Add a random delay to simulate activity pulses
            time.sleep(random.uniform(0.25, 1.0))
    except KeyboardInterrupt:
        # Clear the LED matrix when exiting
        sense.clear()

if __name__ == "__main__":
    wopr_simulation()
