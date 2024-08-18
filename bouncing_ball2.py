#!/usr/bin/env python3
# ========================================================================
# bouncing_ball2.py
#
# Description: A bouncing ball that resets after so many bounces.
#
# Author: Jim Ing
# Date: 2024-08-17
# ========================================================================

import time
import random
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# Set parameters for the ball animation
ball_color = (255, 255, 255) # White color
ball_size = 1                # Size of the ball (1x1 pixel)
ball_speed = 0.1             # Speed of the ball movement
bounce_limit = 16            # Number of bounces before resetting
disappearance_time = 1       # Time for ball to disappear (in seconds)

# Initialize ball position, direction, and bounce counter
def initialize_ball():
    return (random.randint(0, 7), random.randint(0, 7), random.choice([-1, 1]), random.choice([-1, 1]), 0)

ball_x, ball_y, dx, dy, bounce_count = initialize_ball()

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

        # Check for collision with the edges
        collision = False
        if new_x < 0 or new_x >= 8:
            dx = -dx
            collision = True
        if new_y < 0 or new_y >= 8:
            dy = -dy
            collision = True

        # Update ball position
        ball_x += dx
        ball_y += dy

        # If there was a collision, increase bounce count and check if it reached the limit
        if collision:
            ball_color = get_random_color() # Change color on collision
            bounce_count += 1

            if bounce_count >= bounce_limit:
                sense.clear()  # Clear the matrix to make the ball disappear
                time.sleep(disappearance_time) # Wait for the ball to disappear
                ball_x, ball_y, dx, dy, bounce_count = initialize_ball() # Reset ball
                ball_color = get_random_color() # Change color on reset

        # Wait before the next frame
        time.sleep(ball_speed)

except KeyboardInterrupt:
    sense.clear()
