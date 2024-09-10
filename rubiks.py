#!/usr/bin/env python3
# ========================================================================
# rubiks.py
#
# Description:
#
# Author: Jim Ing
# Date: 2024-09-10
# ========================================================================

import argparse
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

# Brighter versions for highlighting
bright_W = (255, 255, 255)  # White
bright_R = (255, 0, 0)      # Red
bright_G = (0, 255, 0)      # Green
bright_B = (0, 0, 255)      # Blue
bright_Y = (255, 255, 0)    # Yellow
bright_O = (255, 102, 0)    # Orange

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

# Move counter
move_counter = 0

# Selected face index (0 = Yellow, 1 = Green, 2 = Orange, 3 = Blue, 4 = Red, 5 = White)
selected_face = 0

# Debug flag
debug = False

# Argument parser for command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true', help='Enable debug output')
args = parser.parse_args()
if args.debug:
    debug = True

def print_debug(message):
    if debug:
        print(message)

# Faces and their indices on the 8x8 matrix
faces = {
    0: [(1, 2), (1, 3), (2, 2), (2, 3)],  # Yellow
    1: [(3, 0), (3, 1), (4, 0), (4, 1)],  # Green
    2: [(3, 2), (3, 3), (4, 2), (4, 3)],  # Orange
    3: [(3, 4), (3, 5), (4, 4), (4, 5)],  # Blue
    4: [(3, 6), (3, 7), (4, 6), (4, 7)],  # Red
    5: [(5, 2), (5, 3), (6, 2), (6, 3)]   # White
}

# Color mapping for faces
face_colors = [Y, G, O, B, R, W]

# Brighter colors for highlighting
bright_face_colors = [bright_Y, bright_G, bright_O, bright_B, bright_R, bright_W]

def draw_cube():
    """Display the current state of the cube."""
    sense.set_pixels(layout)

def highlight_face(face_idx):
    """Highlight the selected face."""
    face = faces[face_idx]
    for (x, y) in face:
        layout[x * 8 + y] = bright_face_colors[face_idx]

def dehighlight_face(face_idx):
    """Remove the highlight from the selected face."""
    face = faces[face_idx]
    for (x, y) in face:
        layout[x * 8 + y] = face_colors[face_idx]

def rotate_face(face_idx, direction):
    """Rotate the selected face clockwise or counterclockwise."""
    face = faces[face_idx]
    face_data = [layout[x * 8 + y] for (x, y) in face]

    if direction == 'right':
        # Rotate clockwise
        layout[face[0][0] * 8 + face[0][1]] = face_data[2]
        layout[face[1][0] * 8 + face[1][1]] = face_data[0]
        layout[face[2][0] * 8 + face[2][1]] = face_data[3]
        layout[face[3][0] * 8 + face[3][1]] = face_data[1]
    elif direction == 'left':
        # Rotate counterclockwise
        layout[face[0][0] * 8 + face[0][1]] = face_data[1]
        layout[face[1][0] * 8 + face[1][1]] = face_data[3]
        layout[face[2][0] * 8 + face[2][1]] = face_data[0]
        layout[face[3][0] * 8 + face[3][1]] = face_data[2]

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

try:
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

except KeyboardInterrupt:
    sense.clear()
