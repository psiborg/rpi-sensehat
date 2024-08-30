#!/usr/bin/env python3
# ========================================================================
# snake1.py
#
# Description: Simulate a snake that zigzags across the LED until it
#              reaches the bottom corner.
#
# Author: Jim Ing
# Date: 2024-08-30
# ========================================================================

from config import sense
#from sense_hat import SenseHat
import time

def clear_matrix(sense):
    sense.clear()

def display_snake(sense, snake_positions):
    # Create an empty matrix
    matrix = [[(0, 0, 0)] * 8 for _ in range(8)]

    # Define colors
    snake_color = (255, 255, 255)  # Full brightness green
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

    # Flatten the matrix into a list of pixels
    pixels = [matrix[y][x] for y in range(8) for x in range(8)]

    # Display the matrix
    sense.set_pixels(pixels)

def move_snake(sense):
    x, y = 0, 0
    direction = 1  # 1 for right, -1 for left
    snake_positions = []

    while True:
        # Add the current position to the snake's positions
        snake_positions.append((x, y))

        # Keep the tail length to 5
        if len(snake_positions) > 5:
            snake_positions.pop(0)

        # Display the snake with the tail
        display_snake(sense, snake_positions)

        # Move the snake
        if direction == 1:
            x += 1
            if x == 8:
                x = 7
                y += 1
                direction = -1
        else:
            x -= 1
            if x < 0:
                x = 0
                y += 1
                direction = 1

        # Check if the snake has reached the bottom-right corner
        if y >= 8:
            break

        time.sleep(0.1)

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
