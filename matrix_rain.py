#!/usr/bin/env python3
# ========================================================================
# matrix_rain.py
#
# Description: Simulate the digital rain drops effect from the Matrix.
#
# Author: Jim Ing
# Date: 2024-08-17
# ========================================================================

import time
import random
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# Set parameters for the rain effect
rain_speed = 0.1 # Speed of the rain falling
num_drops = 5    # Number of raindrops
trail_length = 3 # Length of the trailing effect

# Create a function to display the matrix rain effect
def matrix_rain():
    matrix_height = 8
    matrix_width = 8
    rain_intensity = 0.1 # Probability of rain in each column

    # Initialize raindrop positions and trails
    drops = []

    while True:
        # Randomly add new raindrops
        if len(drops) < num_drops and random.random() < rain_intensity:
            col = random.randint(0, matrix_width - 1)
            drops.append([col, 0, trail_length]) # [column, row, trail length]

        # Create an empty matrix
        matrix = [[(0, 0, 0) for _ in range(matrix_width)] for _ in range(matrix_height)]

        # Update raindrops
        new_drops = []
        for drop in drops:
            col, row, trail = drop
            # Draw the trail
            for t in range(trail):
                if row + t < matrix_height:
                    brightness = int(255 * (1 - t / trail))
                    matrix[row + t][col] = (0, brightness, 0) # Green with fading effect
            # Move the raindrop
            row += 1
            if row < matrix_height:
                new_drops.append([col, row, trail])

        drops = new_drops

        # Set the pixels on the Sense HAT
        for y in range(matrix_height):
            for x in range(matrix_width):
                r, g, b = matrix[y][x]
                sense.set_pixel(x, y, r, g, b)

        # Pause to create the falling effect
        time.sleep(rain_speed)

try:
    print("To quit, press Ctrl+C")
    matrix_rain()

except KeyboardInterrupt:
    sense.clear()
