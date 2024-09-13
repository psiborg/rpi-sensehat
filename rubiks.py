#!/usr/bin/env python3
# ========================================================================
# rubiks.py
#
# Description: A 2x2 Rubik's cube displayed in a 2D flat layout.
#
# https://rubiks-cube-solver.com/2x2/
#
# Author: Jim Ing
# Date: 2024-09-10
# ========================================================================

import argparse
import random
from time import sleep
from config import sense

# Define the colors
W = (102, 102, 102)  # White
R = (102, 0, 0)      # Red
G = (0, 102, 0)      # Green
B = (0, 0, 102)      # Blue
Y = (102, 102, 0)    # Yellow
O = (153, 51, 0)     # Orange
K = (0, 0, 0)        # Black (empty)

# Initial layout (2x2 cube faces)
layout = [
    K, K, K, K, K, K, K, K,
    K, K, Y, Y, K, K, K, K,
    K, K, Y, Y, K, K, K, K,
    G, G, O, O, B, B, R, R,
    G, G, O, O, B, B, R, R,
    K, K, W, W, K, K, K, K,
    K, K, W, W, K, K, K, K,
    K, K, K, K, K, K, K, K
]

# Faces and their indices on the 8x8 matrix
faces = {
    0: [(1, 2), (1, 3), (2, 2), (2, 3)],  # Yellow = Top
    1: [(3, 0), (3, 1), (4, 0), (4, 1)],  # Green = Left
    2: [(3, 2), (3, 3), (4, 2), (4, 3)],  # Orange = Front
    3: [(3, 4), (3, 5), (4, 4), (4, 5)],  # Blue = Right
    4: [(3, 6), (3, 7), (4, 6), (4, 7)],  # Red = Back
    5: [(5, 2), (5, 3), (6, 2), (6, 3)]   # White = Bottom
}

# Move counter and scramble
move_counter = 0
scramble_moves = []

# Selected face index
selected_face = 0

# Dictionary to store the current colors of the face before highlighting
original_face_colors = {}

# Debug flag
debug = False

# Argument parser for command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true', help='Enable debug output')
parser.add_argument('--scramble', type=int, default=0, help='Number of moves to scramble the cube')
args = parser.parse_args()
if args.debug:
    debug = True

def print_debug(message):
    if debug:
        print(message)

def print_instructions():
    """Print instructions for Rubik's Cube."""
    print("\nSense HAT Joystick:")
    print("Middle: Toggle cube faces, Left = Counter Clockwise, Right = Clockwise")
    print("\nCube Notation:")
    print("Clockwise: U = Up/Top, L = Left, F = Front, R = Right, B = Back, D = Down/Bottom")
    print("Counter Clockwise: U' = Up/Top, L' = Left, F' = Front, R' = Right, B' = Back, D' = Down/Bottom")

def draw_cube():
    """Display the current state of the cube."""
    sense.set_pixels(layout)

def brighten_color(color):
    """Increase the brightness of an RGB color by scaling each component."""
    factor = 1.5  # Brighten by 50%
    return tuple(min(int(c * factor), 255) for c in color)

def highlight_face(face_idx):
    """Highlight the selected face by brightening each pixel in the face and saving the current face colors."""
    face = faces[face_idx]

    # Save the current colors of the face before highlighting
    original_face_colors[face_idx] = [layout[x * 8 + y] for (x, y) in face]

    # Brighten each pixel in the face
    for (x, y) in face:
        current_color = layout[x * 8 + y]  # Get the current color
        layout[x * 8 + y] = brighten_color(current_color)  # Apply the brightened color

def dehighlight_face(face_idx):
    """Remove the highlight from the selected face by restoring its saved original colors."""
    face = faces[face_idx]

    # Restore the original colors if they were saved
    if face_idx in original_face_colors:
        for i, (x, y) in enumerate(face):
            layout[x * 8 + y] = original_face_colors[face_idx][i]

        # After restoring, clear the stored original colors for this face
        original_face_colors.pop(face_idx, None)

def rotate_face(face_idx, direction, record_move=True):
    # Define the side indices for each face
    face_sides = {
        0: [30, 31, 24, 25, 26, 27, 28, 29],  # Top face
        1: [18, 10, 31, 39, 50, 42, 34, 26],  # Left face
        2: [19, 18, 25, 33, 42, 43, 36, 28],  # Front face
        3: [11, 19, 27, 35, 43, 51, 38, 30],  # Right face
        4: [10, 11, 29, 37, 51, 50, 32, 24],  # Back face
        5: [35, 34, 33, 32, 39, 38, 37, 36],  # Bottom face
    }

    # Get the current face's sides
    sides = face_sides[face_idx]

    # Extract the RGB values for the current side
    current_values = [layout[i] for i in sides]

    # Rotate sides based on direction
    if direction == 'right':
        rotated_values = [current_values[-2], current_values[-1]] + current_values[:-2]
        move_notation = ['U', 'L', 'F', 'R', 'B', 'D'][face_idx] + "'"
    elif direction == 'left':
        rotated_values = current_values[2:] + [current_values[0], current_values[1]]
        move_notation = ['U', 'L', 'F', 'R', 'B', 'D'][face_idx]

    # Update layout with the rotated values
    for i in range(8):
        layout[sides[i]] = rotated_values[i]

    # Record move if it's not a scramble step
    if record_move:
        scramble_moves.append(move_notation)

    print(f"Move: {move_notation}")

def joystick_moved(event):
    global selected_face, move_counter
    print_debug(f'{event.action}: {event.direction}')

    if event.action == 'pressed':
        if event.direction == 'middle':
            # Dehighlight the previous face
            dehighlight_face(selected_face)

            # Move to the next face
            selected_face = (selected_face + 1) % 6
            print_debug(f'Selected face: {selected_face}')

            # Highlight the new face
            highlight_face(selected_face)
            draw_cube()

        elif event.direction == 'left':
            rotate_face(selected_face, 'left')
            move_counter += 1
            print_debug(f'Rotated face {selected_face} counterclockwise')

        elif event.direction == 'right':
            rotate_face(selected_face, 'right')
            move_counter += 1
            print_debug(f'Rotated face {selected_face} clockwise')

        print(f'Moves: {move_counter}')
        draw_cube()

def scramble_cube(n):
    """Scramble the cube with n random moves."""
    directions = ['left', 'right']
    for _ in range(n):
        face_idx = random.randint(0, 5)
        direction = random.choice(directions)
        rotate_face(face_idx, direction, record_move=False)
    print(f"Scrambled the cube with {n} moves.")

def is_solved():
    """Check if the cube is solved."""
    # Check if all colors on each face are uniform
    for face_idx, positions in faces.items():
        colors = [layout[x * 8 + y] for (x, y) in positions]
        if len(set(colors)) > 1:  # If there are different colors
            return False
    return True

try:
    # Scramble the cube if --scramble=n is passed
    if args.scramble > 0:
        scramble_cube(args.scramble)

        # Print instructions
        print_instructions()

    # Initial drawing
    draw_cube()

    # Highlight the first selected face (Yellow)
    highlight_face(selected_face)
    draw_cube()

    # Joystick event listener
    sense.stick.direction_any = joystick_moved

    # Keep the program running
    while True:
        sleep(0.1)
        if args.scramble > 0 and is_solved():
            print("Congratulations! The cube is solved!")
            break

except KeyboardInterrupt:
    sense.clear()
