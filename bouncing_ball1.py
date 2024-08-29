#!/usr/bin/env python3
# ========================================================================
# bouncing_ball1.py
#
# Description: Display a simple ball that bounces off the edges.
#
# Author: Jim Ing
# Date: 2024-08-17
# ========================================================================

import random
import time
from config import sense

sense.clear()

# Set parameters for the ball animation
ball_color = (255, 255, 255) # White color
ball_size = 1                # Size of the ball (1x1 pixel)
ball_speed = 0.1             # Speed of the ball movement

# Initialize ball position and direction
ball_x = random.randint(0, 7)
ball_y = random.randint(0, 7)
dx = random.choice([-1, 1])
dy = random.choice([-1, 1])

# Generate a random color
def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

try:
    print("To quit, press Ctrl+C")

    while True:
        sense.clear()

        # Draw the ball
        sense.set_pixel(ball_x, ball_y, ball_color)

        # Move the ball
        new_x = ball_x + dx
        new_y = ball_y + dy

        # Check for collision with the edges and change direction and color if necessary
        if new_x < 0 or new_x >= 8:
            dx = -dx
            ball_color = get_random_color() # Change color on collision
        if new_y < 0 or new_y >= 8:
            dy = -dy
            ball_color = get_random_color() # Change color on collision

        # Update ball position
        ball_x += dx
        ball_y += dy

        # Wait before the next frame
        time.sleep(ball_speed)

except KeyboardInterrupt:
    sense.clear()
