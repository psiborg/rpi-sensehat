#!/usr/bin/env python3
# ========================================================================
# bouncing_ball3.py
#
# Description: A bouncing ball that grows in length after each bounce.
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
ball_speed = 0.1             # Speed of the ball movement
bounce_limit = 16            # Number of bounces before resetting
disappearance_time = 1       # Time for ball to disappear (in seconds)
initial_ball_size = 1        # Initial size of the ball

# Initialize ball position, direction, bounce count, and size
def initialize_ball():
    return (random.randint(0, 7), random.randint(0, 7), random.choice([-1, 1]), random.choice([-1, 1]), 0, initial_ball_size)

ball_x, ball_y, dx, dy, bounce_count, ball_size = initialize_ball()

# Generate a random color
def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_ball(x, y, size, color):
    # Draw the ball as a line of pixels
    for i in range(size):
        new_x = x + i * dx
        new_y = y + i * dy
        if 0 <= new_x < 8 and 0 <= new_y < 8:
            sense.set_pixel(new_x, new_y, color)

try:
    print("To quit, press Ctrl+C")
    while True:
        sense.clear()

        # Draw the ball
        draw_ball(ball_x, ball_y, ball_size, ball_color)

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
            ball_size += 1 # Increase length of the ball

            if bounce_count >= bounce_limit:
                sense.clear() # Clear the matrix to make the ball disappear
                time.sleep(disappearance_time) # Wait for the ball to disappear
                ball_x, ball_y, dx, dy, bounce_count, ball_size = initialize_ball() # Reset ball
                ball_color = get_random_color() # Change color on reset

        # Wait before the next frame
        time.sleep(ball_speed)

except KeyboardInterrupt:
    sense.clear()
