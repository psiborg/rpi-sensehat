#!/usr/bin/env python3
# ========================================================================
# tetris.py
#
# Description: Tetris on the Sense HAT.
#
# Author: Jim Ing
# Date: 2024-09-23
# ========================================================================

import time
import random
from copy import deepcopy
from config import sense

# Define Tetromino shapes (4x4 matrix for each)
TETROMINOS = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1], [1, 1]],
    'T': [[0, 1, 0], [1, 1, 1]],
    'L': [[1, 0], [1, 0], [1, 1]],
    'J': [[0, 1], [0, 1], [1, 1]],
    'S': [[0, 1, 1], [1, 1, 0]],
    'Z': [[1, 1, 0], [0, 1, 1]]
}

# Board size (8x8 grid)
WIDTH, HEIGHT = 8, 8

# Tetromino colors
COLORS = {
    'I': (0, 255, 255),  # Cyan
    'O': (255, 255, 0),  # Yellow
    'T': (128, 0, 128),  # Purple
    'L': (255, 165, 0),  # Orange
    'J': (0, 0, 255),    # Blue
    'S': (0, 255, 0),    # Green
    'Z': (255, 0, 0),    # Red
}

# Initialize game board
board = [[None] * WIDTH for _ in range(HEIGHT)]

# Initialize score
score = 0

# Check if tetromino fits in the grid
def check_collision(shape, offset):
    x_off, y_off = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if (x + x_off >= WIDTH or x + x_off < 0 or
                        y + y_off >= HEIGHT or board[y + y_off][x + x_off]):
                    return True
    return False

# Add tetromino to the board
def merge_tetromino(shape, offset, tetromino_type):
    x_off, y_off = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[y + y_off][x + x_off] = tetromino_type

# Remove tetromino from board (before moving)
def remove_tetromino(shape, offset):
    x_off, y_off = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[y + y_off][x + x_off] = None

# Rotate tetromino (90 degrees clockwise)
def rotate_tetromino(shape):
    return [list(reversed(col)) for col in zip(*shape)]

# Draw only changes in the board
def draw_board():
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                sense.set_pixel(x, y, COLORS[cell])  # Use tetromino name for color
            else:
                sense.set_pixel(x, y, (0, 0, 0))  # Empty space

# Clear full lines
def clear_lines():
    global score
    lines_cleared = 0
    new_board = [row for row in board if any(cell is None for cell in row)]  # Keep only rows with empty cells
    lines_cleared = HEIGHT - len(new_board)

    # If any lines were cleared, add empty rows on top
    if lines_cleared > 0:
        new_board = [[None] * WIDTH for _ in range(lines_cleared)] + new_board
        for y in range(HEIGHT):
            board[y] = new_board[y]

        # Update the score based on lines cleared
        if lines_cleared == 1:
            score += 100
        elif lines_cleared == 2:
            score += 300
        elif lines_cleared == 3:
            score += 500
        elif lines_cleared == 4:
            score += 800

    print(f"Score: {score}")  # Print the updated score

# Game over check
def check_game_over():
    return any(board[0])

# Main game loop
def tetris_game():
    current_tetromino = random.choice(list(TETROMINOS.keys()))
    current_shape = deepcopy(TETROMINOS[current_tetromino])
    current_offset = [3, 0]  # Start near the top-middle of the grid

    speed = 2.0  # Falling speed (adjustable)
    drop_time = time.time()

    while True:
        # Check if it's time to drop the tetromino
        if time.time() - drop_time > speed:
            remove_tetromino(current_shape, current_offset)
            current_offset[1] += 1  # Move down
            if check_collision(current_shape, current_offset):
                current_offset[1] -= 1  # Revert move if collision
                merge_tetromino(current_shape, current_offset, current_tetromino)
                clear_lines()  # Check for cleared lines
                if check_game_over():
                    sense.show_message("Game Over", text_colour=(255, 0, 0))
                    break
                # Spawn new tetromino
                current_tetromino = random.choice(list(TETROMINOS.keys()))
                current_shape = deepcopy(TETROMINOS[current_tetromino])
                current_offset = [3, 0]
            else:
                merge_tetromino(current_shape, current_offset, current_tetromino)
            drop_time = time.time()

        # Joystick controls
        for event in sense.stick.get_events():
            if event.action == "pressed":
                remove_tetromino(current_shape, current_offset)
                if event.direction == "left":
                    current_offset[0] -= 1  # Move left
                    if check_collision(current_shape, current_offset):
                        current_offset[0] += 1  # Revert if collision
                elif event.direction == "right":
                    current_offset[0] += 1  # Move right
                    if check_collision(current_shape, current_offset):
                        current_offset[0] -= 1  # Revert if collision
                elif event.direction == "down":
                    current_offset[1] += 1  # Move down faster
                    if check_collision(current_shape, current_offset):
                        current_offset[1] -= 1  # Revert if collision
                elif event.direction == "up":
                    rotated_shape = rotate_tetromino(current_shape)
                    if not check_collision(rotated_shape, current_offset):
                        current_shape = rotated_shape  # Rotate if no collision
                merge_tetromino(current_shape, current_offset, current_tetromino)

        draw_board()  # Only update the board if there's a change

# Run the game
tetris_game()
