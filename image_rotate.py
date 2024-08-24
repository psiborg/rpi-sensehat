#!/usr/bin/env python3
# ========================================================================
# image_rotate.py
#
# Description: Rotate image.
#
# Author: Jim Ing
# Date: 2024-08-24
# ========================================================================

import random
import time
from sense_hat import SenseHat
from packages.sprites import Sprites

def image_rotate(image, speed=None, direction=None, steps=None, timing=None):
    """
    Rotates an 8x8 LED image on the Sense HAT.

    Parameters:
    - image: A list of 64 tuples representing the LED image.
    - speed: Base delay between steps in seconds (0.05 - 1.0).
    - direction: 'clockwise' or 'counter-clockwise'.
    - steps: Number of 90-degree rotations to perform (4 - 40).
    - timing: 'linear' or 'ease' for animation timing.
    """

    # Validate inputs
    if len(image) != 64:
        raise ValueError("Image must be a list of 64 tuples representing an 8x8 matrix.")

    # Randomize parameters if not provided
    speed = speed if speed is not None else random.uniform(0.05, 1.0)
    direction = direction if direction is not None else random.choice(['clockwise', 'counter-clockwise'])
    steps = steps if steps is not None else random.randint(4, 40)
    timing = timing if timing is not None else random.choice(['linear', 'ease'])
    print(f"speed = {speed}, direction = {direction}, steps = {steps}, timing = {timing}")

    # Convert flat list to 8x8 matrix
    matrix = [image[i:i+8] for i in range(0, 64, 8)]

    # Define rotation function
    def rotate_90(matrix, direction):
        if direction == 'clockwise':
            return [list(row) for row in zip(*matrix[::-1])]
        else:  # counter-clockwise
            return [list(row) for row in zip(*matrix)][::-1]

    # Define timing functions
    def ease_timing(total_steps):
        return [speed * (1 + (i / total_steps)) for i in range(total_steps)]

    def linear_timing(total_steps):
        return [speed] * total_steps

    # Choose timing function
    delays = ease_timing(steps) if timing == 'ease' else linear_timing(steps)

    # Perform rotations with delays
    for i in range(steps):
        matrix = rotate_90(matrix, direction)
        flat_image = sum(matrix, [])
        sense.set_pixels(flat_image)
        time.sleep(delays[i])

    # Return the final rotated image
    return sum(matrix, [])

if __name__ == "__main__":
    sense = SenseHat()
    sprite = Sprites()

    image_rotate(sprite.arrowUp)

    #pick = random.randint(0, len(sprite.all) - 1)
    #image_rotate(sprite.all[pick])
