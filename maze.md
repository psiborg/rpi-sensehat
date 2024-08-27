# Maze Game for Sense HAT

This is a simple maze game designed for the Raspberry Pi Sense HAT. The game generates a random maze that the player can navigate using either the Sense HAT's mini joystick, a USB gamepad, or the keyboard. The objective is to reach the green goal.

## Features

- Random Maze Generation: A new maze is generated each time the game starts.
- Player Movement: Control the player using the Sense HAT joystick, a USB gamepad, or the keyboard (W, A, S, D).
- Reachable Goal: The goal is always placed at a reachable position within the maze.
- Winning Condition: When the player reaches the goal, a winning message is displayed.

## Installation

### Prerequisites

- Raspberry Pi with Sense HAT installed.
- Python 3.x.
- Required Python libraries:
  - sense_hat
  - curses
  - pygame

You can install the necessary libraries using:

```sh
sudo apt-get install sense-hat

pip3 install pygame
```

Run the game:

```sh
python3 maze.py
```

### How to Play

- Joystick Controls:
  - Up: Move up
  - Down: Move down
  - Left: Move left
  - Right: Move right

- Gamepad Controls:
  - Left Stick Up: Move up
  - Left Stick Down: Move down
  - Left Stick Left: Move left
  - Left Stick Right: Move right

- Keyboard Controls:
  - W: Move up
  - A: Move left
  - S: Move down
  - D: Move right

- Objective: Navigate the yellow player character through the maze to reach the green goal.

## Customization

## Maze Size

The default maze size is 8x8, matching the Sense HAT's LED matrix. You can change the maze size by adjusting the maze_size variable in the script, although the Sense HAT's LED matrix limits this to 8x8.

## Colors

You can customize the colors of the walls, paths, player, and goal by modifying the respective variables:

- wall_color: Color of the maze walls (default: blue).
- path_color: Color of the maze paths (default: black).
- player_color: Color of the player (default: yellow).
- goal_color: Color of the goal (default: green).

## Gamepad Input

The game uses the pygame library to handle gamepad input. The left stick of the gamepad is used to navigate the maze. You can customize button actions or use different controls by modifying the gamepad_movement() function in the script.

## Known Issues

- The game must be run in a terminal with access to the keyboard.
- If the terminal window is resized or if focus is lost, the curses interface may not work properly.
- Ensure the USB gamepad is connected before running the game for the script to detect it.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
