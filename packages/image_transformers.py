# ========================================================================
# packages/image_transformers.py
#
# Description: ImageTransformers classes.
#
# Author: Jim Ing
# Date: 2024-08-24
# ========================================================================

import random
import time
from config import sense

class ImageTransformer:
    def __init__(self, image, speed=None, direction=None, steps=None, timing=None, debug=False):
        if len(image) != 64:
            raise ValueError("Image must be a list of 64 tuples representing an 8x8 matrix.")

        self.sense = sense
        self.image = image
        self.speed = speed if speed is not None else random.uniform(0.025, 0.75)
        self.direction = direction
        self.steps = steps
        self.timing = timing if timing is not None else random.choice(['linear', 'ease'])
        self.matrix = [image[i:i+8] for i in range(0, 64, 8)]
        self.debug = debug

    def ease_timing(self):
        return [self.speed * (1 + (i / self.steps)) for i in range(self.steps)]

    def linear_timing(self):
        return [self.speed] * self.steps

    def get_delays(self):
        return self.ease_timing() if self.timing == 'ease' else self.linear_timing()

    def set_pixels(self):
        flat_image = sum(self.matrix, [])
        self.sense.set_pixels(flat_image)

    def print_debug_info(self):
        print(f"Image: {self.image}")
        print(f"Speed: {self.speed}")
        print(f"Direction: {self.direction}")
        print(f"Steps: {self.steps}")
        print(f"Timing: {self.timing}")

class ImageRotator(ImageTransformer):
    def __init__(self, image, speed=None, direction=None, steps=None, timing=None, debug=False):
        super().__init__(image, speed, direction, steps, timing, debug)
        self.direction = direction if direction else random.choice(['clockwise', 'counter-clockwise'])
        self.steps = steps if steps else random.randint(4, 40)

        if self.debug:
            self.print_debug_info()  # Moved here to reflect the final values

    def rotate_90(self):
        if self.direction == 'clockwise':
            self.matrix = [list(row) for row in zip(*self.matrix[::-1])]
        else:  # counter-clockwise
            self.matrix = [list(row) for row in zip(*self.matrix)][::-1]

    def rotate(self):
        delays = self.get_delays()
        for i in range(self.steps):
            self.rotate_90()
            self.set_pixels()
            time.sleep(delays[i])

        return sum(self.matrix, [])

    def clear(self):
        sense.clear()

class ImageSlider(ImageTransformer):
    def __init__(self, image, speed=None, direction=None, steps=None, timing=None, debug=False):
        super().__init__(image, speed, direction, steps, timing, debug)
        self.direction = direction if direction else random.choice(['up', 'down', 'left', 'right'])
        self.steps = steps if steps else random.randint(4, 12)

        if self.debug:
            self.print_debug_info()  # Moved here to reflect the final values

    def slide(self):
        def slide_matrix(matrix, direction):
            if direction == 'up':
                return matrix[1:] + [[(0, 0, 0)] * 8]
            elif direction == 'down':
                return [[(0, 0, 0)] * 8] + matrix[:-1]
            elif direction == 'left':
                return [row[1:] + [(0, 0, 0)] for row in matrix]
            elif direction == 'right':
                return [[(0, 0, 0)] + row[:-1] for row in matrix]

        delays = self.get_delays()
        for i in range(self.steps):
            self.matrix = slide_matrix(self.matrix, self.direction)
            self.set_pixels()
            time.sleep(delays[i])

        return sum(self.matrix, [])

    def clear(self):
        sense.clear()
