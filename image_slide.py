#!/usr/bin/env python3
# ========================================================================
# image_slide.py
#
# Description: Slide image.
#
# Author: Jim Ing
# Date: 2024-08-24
# ========================================================================

import random
import time
from sense_hat import SenseHat
from packages.sprites import Sprites

def image_slide(image, speed=None, direction=None, steps=None, timing=None):
    """
    Slides an 8x8 LED image on the Sense HAT.

    Parameters:
    - image: A list of 64 tuples representing the LED image.
    - speed: Base delay between steps in seconds (0.05 - 1.0).
    - direction: 'up', 'down', 'left', 'right'.
    - steps: Number of pixels to slide (1 - 8).
    - timing: 'linear' or 'ease' for animation timing.
    """

    # Validate inputs
    if len(image) != 64:
        raise ValueError("Image must be a list of 64 tuples representing an 8x8 matrix.")

    # Randomize parameters if not provided
    speed = speed if speed is not None else random.uniform(0.05, 1.0)
    direction = direction if direction is not None else random.choice(['up', 'down', 'left', 'right'])
    steps = steps if steps is not None else random.randint(4, 12)
    timing = timing if timing is not None else random.choice(['linear', 'ease'])
    print(f"speed = {speed}, direction = {direction}, steps = {steps}, timing = {timing}")

    # Convert flat list to 8x8 matrix
    matrix = [image[i:i+8] for i in range(0, 64, 8)]

    # Define slide function
    def slide(matrix, direction):
        if direction == 'up':
            return matrix[1:] + [[(0, 0, 0)] * 8]
        elif direction == 'down':
            return [[(0, 0, 0)] * 8] + matrix[:-1]
        elif direction == 'left':
            return [row[1:] + [(0, 0, 0)] for row in matrix]
        elif direction == 'right':
            return [[(0, 0, 0)] + row[:-1] for row in matrix]

    # Define timing functions
    def ease_timing(total_steps):
        return [speed * (1 + (i / total_steps)) for i in range(total_steps)]

    def linear_timing(total_steps):
        return [speed] * total_steps

    # Choose timing function
    delays = ease_timing(steps) if timing == 'ease' else linear_timing(steps)

    # Perform slides with delays
    for i in range(steps):
        matrix = slide(matrix, direction)
        flat_image = sum(matrix, [])
        sense.set_pixels(flat_image)
        time.sleep(delays[i])

    # Return the final slid image
    return sum(matrix, [])

# Example usage
if __name__ == "__main__":
    sense = SenseHat()
    sprite = Sprites()

    # Call the function with all parameters randomized
    image_slide(sprite.arrowUp, steps=8)
