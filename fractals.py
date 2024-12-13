#!/usr/bin/env python3
# ========================================================================
# fractals.py
#
# Description: A fractal-like animation based on the Mandelbrot set. The
#              animation cycles through different gradient color schemes
#              and zoom levels.
#
# Author: Jim Ing
# Date: 2024-12-11
# ========================================================================

import time
import random
from config import sense

# Function to calculate Mandelbrot set value for a point
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n

# Generate random color gradient
def generate_gradient():
    base_color = [random.randint(0, 255) for _ in range(3)]
    gradient = []
    for i in range(64):
        color = [min(255, int(base_color[j] * (i / 63))) for j in range(3)]
        gradient.append(color)
    return gradient

# Map Mandelbrot iterations to a color from the gradient
def map_to_color(iterations, max_iter, gradient):
    if iterations == max_iter:
        return [0, 0, 0]  # Black for points inside the set
    index = int((iterations / max_iter) * (len(gradient) - 1))
    return gradient[index]

# Main animation loop
try:
    while True:
        # Generate random zoom and center for the fractal
        zoom = random.uniform(0.5, 2.0)
        center_x = random.uniform(-1.5, 0.5)
        center_y = random.uniform(-1.0, 1.0)

        # Generate a random color gradient
        gradient = generate_gradient()

        # Fractal bounds
        width, height = 8, 8
        x_min, x_max = center_x - (1.5 / zoom), center_x + (1.5 / zoom)
        y_min, y_max = center_y - (1.0 / zoom), center_y + (1.0 / zoom)

        # Debugging information
        print(f"Zoom: {zoom}")
        print(f"Center: ({center_x}, {center_y})")
        print(f"X range: ({x_min}, {x_max})")
        print(f"Y range: ({y_min}, {y_max})")
        print(f"Gradient: {gradient}")

        # Generate fractal image
        for y in range(height):
            for x in range(width):
                # Map pixel to fractal coordinates
                real = x_min + (x / width) * (x_max - x_min)
                imag = y_min + (y / height) * (y_max - y_min)
                c = complex(real, imag)

                # Calculate iterations
                iterations = mandelbrot(c, max_iter=32)

                # Map to color and set pixel
                color = map_to_color(iterations, 32, gradient)
                sense.set_pixel(x, y, color)

        # Pause before the next frame
        time.sleep(2)

except KeyboardInterrupt:
    sense.clear()
