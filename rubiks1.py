#!/usr/bin/env python3
# ========================================================================
# rubiks1.py
#
# Description:
#
# Author: Jim Ing
# Date: 2024-09-09
# ========================================================================

import time
from config import sense

# Define colors for each face (RGB values)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)

# Initial state of the cube (each face is 2x2)
cube = {
    'front': [[WHITE, WHITE], [WHITE, WHITE]],
    'back': [[YELLOW, YELLOW], [YELLOW, YELLOW]],
    'left': [[RED, RED], [RED, RED]],
    'right': [[ORANGE, ORANGE], [ORANGE, ORANGE]],
    'top': [[BLUE, BLUE], [BLUE, BLUE]],
    'bottom': [[GREEN, GREEN], [GREEN, GREEN]],
}

# Current view shows these 5 faces
view = ['top', 'left', 'front', 'right', 'bottom']

def display_face(face, x_offset, y_offset):
    """Display a 2x2 face on the Sense HAT LED matrix starting at the offset."""
    for y in range(2):
        for x in range(2):
            sense.set_pixel(x + x_offset, y + y_offset, cube[face][y][x])

def display_cube():
    """Display all visible faces of the cube with a black border around the front face."""
    sense.clear()

    # Black border around the front face (3x3 area in the center)
    for y in range(1, 4):
        for x in range(1, 4):
            sense.set_pixel(x + 2, y + 2, BLACK)

    # Display top, front, left, right, and bottom faces with offsets
    display_face(view[0], 3, 0)  # Top face (centered on top)
    display_face(view[1], 0, 3)  # Left face (left of front)
    display_face(view[2], 3, 3)  # Front face (centered with black border)
    display_face(view[3], 6, 3)  # Right face (right of front)
    display_face(view[4], 3, 6)  # Bottom face (centered below front)

def rotate_view(direction):
    """Rotate the view to show different cube faces."""
    global view
    if direction == 'left':
        # Rotate the cube view left (front -> left, left -> back, etc.)
        view = [view[0], view[2], view[3], view[4], view[1]]  # Rotate visible sides left
    elif direction == 'right':
        # Rotate the cube view right (front -> right, right -> back, etc.)
        view = [view[0], view[4], view[1], view[2], view[3]]  # Rotate visible sides right
    elif direction == 'up':
        # Rotate up (showing the top as front, etc.)
        view = ['back', 'left', 'top', 'right', 'front']
    elif direction == 'down':
        # Rotate down (showing the bottom as front, etc.)
        view = ['front', 'left', 'bottom', 'right', 'back']

    display_cube()

def rotate_face(face, direction):
    """Rotate a 2x2 face of the cube 90 degrees clockwise or counterclockwise."""
    if direction == 'clockwise':
        cube[face] = [list(row) for row in zip(*cube[face][::-1])]
    elif direction == 'counterclockwise':
        cube[face] = [list(row) for row in zip(*cube[face])][::-1]

def joystick_event(event):
    """Handle joystick events to rotate cube faces or switch views."""
    print(f"{event.action}: {event.direction}")
    if event.action == 'pressed':
        if event.direction == 'up':
            rotate_view('up')
        elif event.direction == 'down':
            rotate_view('down')
        elif event.direction == 'left':
            rotate_view('left')
        elif event.direction == 'right':
            rotate_view('right')
        elif event.direction == 'middle':
            # Rotate front face by default (could change this to rotate any face)
            rotate_face(view[2], 'clockwise')
        display_cube()

# Main loop to capture joystick input and update the display
sense.clear()
display_cube()

sense.stick.direction_any = joystick_event

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    sense.clear()
