# Rubik's Cube

This Python script simulates a Rubik's Cube using the Sense HAT LED matrix on a Raspberry Pi. The program allows you to scramble, manipulate, and solve a virtual 2x2 version of a Rubik's Cube using the Sense HAT joystick.

## Features

- Interactive Cube Manipulation: Control cube rotations using the Sense HAT joystick.
- Scrambling: Automatically scramble the cube by a specified number of moves.
- Highlighting: The currently selected face of the cube is highlighted to help with orientation.
- Debug Mode: Enables debug output to track actions and cube movements.
- Win Condition: Detects when the cube is solved.

## Requirements

- Python 3.x
- Sense HAT (Raspberry Pi)
- Required external config.py file with a sense object initialized for the Sense HAT (e.g., sense = SenseHat()).

Install the necessary dependencies using the following command:

```bash
pip install sense-hat
```

## Setup

1. Ensure that you have a Raspberry Pi with the Sense HAT attached.

2. Make sure you have the config.py file that contains the following:

```python
from sense_hat import SenseHat
sense = SenseHat()
```

3. Download the provided Python code to your Raspberry Pi.

## Usage

The script can be run from the command line with optional arguments for scrambling the cube and enabling debug mode.

```bash
python rubiks.py --scramble <number_of_moves> --debug
```

### Arguments

- --scramble: Scrambles the cube by the specified number of moves (e.g., --scramble 20).
- --debug: Enables debug output to view joystick inputs and move tracking.

### Example

To scramble the cube with 15 random moves and enable debug mode, run:

```bash
python rubiks.py --scramble 15 --debug
```

## Controls

The Sense HAT joystick is used to control the cube:

- Joystick Directions:
  - Middle: Switch between cube faces.
  - Left: Rotate the selected face counter-clockwise.
  - Right: Rotate the selected face clockwise.

## Cube Notation

- U: Up/Top face
- L: Left face
- F: Front face
- R: Right face
- B: Back face
- D: Down/Bottom face

Adding a prime (') after the letter denotes a counter-clockwise move, e.g., U' means turning the top face counter-clockwise.

## Cube Layout

The cube layout is represented by an 8x8 LED matrix. Each face of the cube occupies a portion of this grid as follows:

- Yellow: Top
- Green: Left
- Orange: Front
- Blue: Right
- Red: Back
- White: Bottom

### Highlighting

The current face is highlighted by brightening its colors on the LED matrix, making it easier to identify.

## Functions Overview

- draw_cube(): Displays the current state of the cube on the Sense HAT LED matrix.
- rotate_face(face_idx, direction): Rotates a selected face clockwise or counter-clockwise.
- scramble_cube(n): Randomly scrambles the cube with n moves.
- is_solved(): Checks if the cube is solved (all faces have uniform colors).
- highlight_face(face_idx): Highlights a face by increasing the brightness of its pixels.
- dehighlight_face(face_idx): Removes the highlight from a face by restoring its original colors.
- joystick_moved(event): Handles joystick movement and maps joystick actions to cube rotations.

## Debugging

The --debug flag enables debug mode, which outputs joystick actions and move details to the terminal. This can be useful for tracking the cube's state and understanding how joystick inputs are processed.

## Future Improvements
- Expand the cube to a 3x3 Rubik's Cube.
- Add an algorithm to solve the cube automatically.
- Implement different difficulty levels for scrambling.
