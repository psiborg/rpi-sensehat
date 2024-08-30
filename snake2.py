#!/usr/bin/env python3
# ========================================================================
# snake2.py
#
# Description: Simulate a snake that zigzags across the LED until it
#              reaches the bottom corner. This version includes obstacle
#              generation and detection
#
# Author: Jim Ing
# Date: 2024-08-30
# ========================================================================

from config import sense
#from sense_hat import SenseHat
import time
import random

def clear_matrix(sense):
    sense.clear()

def display_snake(sense, snake_positions, obstacles):
    # Create an empty matrix
    matrix = [[(0, 0, 0)] * 8 for _ in range(8)]

    # Define colors
    snake_color = (255, 255, 255)  # Full brightness green
    obstacle_color = (255, 0, 0)   # Red for obstacles
    fade_step = 16  # Increased value to fade the tail more quickly

    # Display the current snake positions
    for i, pos in enumerate(snake_positions):
        if 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
            # Fade the tail based on its length
            if i < 5:
                fade_value = max(0, 255 - (i * fade_step))  # Tail fades from bright to dark
                matrix[pos[1]][pos[0]] = (fade_value, fade_value, 0)  # Yellow fading tail
            else:
                matrix[pos[1]][pos[0]] = snake_color

    # Display the obstacles
    for obs in obstacles:
        matrix[obs[1]][obs[0]] = obstacle_color

    # Flatten the matrix into a list of pixels
    pixels = [matrix[y][x] for y in range(8) for x in range(8)]

    # Display the matrix
    sense.set_pixels(pixels)

def move_snake(sense):
    x, y = 0, 0
    direction = 1  # 1 for right, -1 for left
    snake_positions = []
    obstacles = []

    # Generate random obstacles
    num_obstacles = random.randint(2, 5)
    for _ in range(num_obstacles):
        obs_x = random.randint(1, 6)  # Avoiding the edges
        obs_y = random.randint(0, 7)
        obstacles.append((obs_x, obs_y))

    while True:
        # Add the current position to the snake's positions
        snake_positions.append((x, y))

        # Keep the tail length to 5
        if len(snake_positions) > 5:
            snake_positions.pop(0)

        # Display the snake with the tail and obstacles
        display_snake(sense, snake_positions, obstacles)

        # Move the snake
        if direction == 1:
            x += 1
            if (x, y) in obstacles:
                y += 1  # Drop down a row if an obstacle is encountered
            if x == 8:
                x = 7
                y += 1
                direction = -1
        else:
            x -= 1
            if (x, y) in obstacles:
                y += 1  # Drop down a row if an obstacle is encountered
            if x < 0:
                x = 0
                y += 1
                direction = 1

        # Check if the snake has reached the bottom-right corner
        if y >= 8:
            # Update the final position before breaking the loop
            display_snake(sense, snake_positions, obstacles)
            break

        time.sleep(0.2)

    # Clear the matrix when finished
    clear_matrix(sense)

def main():
    #sense = SenseHat()

    try:
        move_snake(sense)
    except KeyboardInterrupt:
        sense.clear()

if __name__ == "__main__":
    main()
