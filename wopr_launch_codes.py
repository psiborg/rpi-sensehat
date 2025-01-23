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

def expanding_rings(duration=5):
    """Animate expanding and contracting rings."""
    start_time = time.time()
    while time.time() - start_time < duration:
        for radius in range(4):  # Expanding rings (0 to 3)
            color = random.choice(colors)
            for x in range(-radius, radius + 1):
                for y in [-radius, radius]:
                    if 0 <= 3 + x < 8 and 0 <= 3 + y < 8:
                        sense.set_pixel(3 + x, 3 + y, color)
                    if 0 <= 3 + y < 8 and 0 <= 3 + x < 8:
                        sense.set_pixel(3 + y, 3 + x, color)
            time.sleep(0.2)
            sense.clear()
        for radius in range(3, -1, -1):  # Contracting rings (3 to 0)
            color = random.choice(colors)
            for x in range(-radius, radius + 1):
                for y in [-radius, radius]:
                    if 0 <= 3 + x < 8 and 0 <= 3 + y < 8:
                        sense.set_pixel(3 + x, 3 + y, color)
                    if 0 <= 3 + y < 8 and 0 <= 3 + x < 8:
                        sense.set_pixel(3 + y, 3 + x, color)
            time.sleep(0.2)
            sense.clear()

def diagonal_sweep(duration=5):
    """Animate diagonal sweeps across the matrix."""
    start_time = time.time()
    while time.time() - start_time < duration:
        for d in range(-7, 8):  # Diagonal index
            color = random.choice(colors)
            for x in range(8):
                y = x + d
                if 0 <= y < 8:
                    sense.set_pixel(x, y, color)
            time.sleep(0.1)
            sense.clear()

def pixel_explosion(duration=5):
    """Simulate a pixel explosion effect."""
    start_time = time.time()
    while time.time() - start_time < duration:
        center = (3, 3)  # Starting pixel
        color = random.choice(colors)
        for radius in range(5):  # Increase radius outward
            for dx in range(-radius, radius + 1):
                for dy in range(-radius, radius + 1):
                    if abs(dx) == radius or abs(dy) == radius:
                        x, y = center[0] + dx, center[1] + dy
                        if 0 <= x < 8 and 0 <= y < 8:
                            sense.set_pixel(x, y, color)
            time.sleep(0.1)
            sense.clear()

def random_walk(duration=5):
    """Animate a random walk with a fading trail."""
    start_time = time.time()
    x, y = 3, 3  # Start in the center
    while time.time() - start_time < duration:
        color = random.choice(colors)
        sense.set_pixel(x, y, color)
        time.sleep(0.1)
        sense.set_pixel(x, y, [int(c / 2) for c in color])  # Dim the trail
        # Move randomly to a neighboring pixel
        x = max(0, min(7, x + random.choice([-1, 0, 1])))
        y = max(0, min(7, y + random.choice([-1, 0, 1])))
    sense.clear()

def snake_animation(duration=5):
    """Simulate a snake that moves across the matrix."""
    start_time = time.time()
    snake = [(0, 0)]  # Initial snake position
    direction = (1, 0)  # Moving right
    while time.time() - start_time < duration:
        # Add a new head based on direction
        new_head = (snake[-1][0] + direction[0], snake[-1][1] + direction[1])
        new_head = (new_head[0] % 8, new_head[1] % 8)  # Wrap around edges
        snake.append(new_head)

        # Randomize direction occasionally
        if random.random() < 0.2:
            direction = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])

        # Draw the snake
        for segment in snake:
            sense.set_pixel(segment[0], segment[1], random.choice(colors))

        # Remove the tail
        if len(snake) > 8:
            tail = snake.pop(0)
            sense.set_pixel(tail[0], tail[1], black)

        time.sleep(0.2)
        sense.clear()

def meteor_shower(duration=5):
    """Simulate a meteor shower effect."""
    start_time = time.time()
    while time.time() - start_time < duration:
        x = random.randint(0, 7)  # Random starting column
        color = random.choice(colors)
        for y in range(8):
            sense.set_pixel(x, y, color)
            time.sleep(0.1)
            sense.set_pixel(x, y, [int(c / 2) for c in color])  # Dim trail
    sense.clear()

def main():
    try:
        while True:
            random_flashes(duration=3)
            sinusoidal_wave(duration=3)
            grid_pattern(duration=3)
            expanding_rings(duration=3)
            diagonal_sweep(duration=3)
            pixel_explosion(duration=3)
            random_walk(duration=3)
            snake_animation(duration=3)
            meteor_shower(duration=3)
    except KeyboardInterrupt:
        sense.clear()

if __name__ == "__main__":
    main()
