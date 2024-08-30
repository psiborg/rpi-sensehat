#!/usr/bin/env python3
# ========================================================================
# rainbow12.py
#
# Description: Diagonal rainbow with gradient effect.
#
# Author: Jim Ing
# Date: 2024-08-30
# ========================================================================

from config import sense
import time

def create_diagonal_rainbow(sense):
    width, height = 8, 8
    for t in range(width + height):  # Total time to create the diagonal effect
        # Create an empty matrix to store the colors
        matrix = [[(0, 0, 0)] * width for _ in range(height)]

        # Calculate the color gradient
        for y in range(height):
            for x in range(width):
                # Calculate distance from the diagonal (i.e., the diagonal line equation y = x)
                distance = abs(x - y + t) % (width + height)

                # Generate color based on the distance
                r = int(255 * (distance / (width + height)))
                g = int(255 * ((distance + (width + height) / 3) % (width + height)) / (width + height))
                b = int(255 * ((distance + 2 * (width + height) / 3) % (width + height)) / (width + height))

                # Assign color to the matrix
                matrix[y][x] = (r, g, b)

        # Flatten the matrix into a list of pixels
        pixels = [matrix[y][x] for y in range(height) for x in range(width)]

        # Display the matrix
        sense.set_pixels(pixels)
        time.sleep(0.1)

def main():
    try:
        while True:
            create_diagonal_rainbow(sense)

    except KeyboardInterrupt:
        sense.clear()

if __name__ == "__main__":
    main()
