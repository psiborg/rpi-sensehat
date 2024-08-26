# Conway's Game of Life on the Sense HAT

This Python script simulates Conway's Game of Life on an 8x8 LED matrix using the Raspberry Pi's Sense HAT. The game is a zero-player game, meaning its evolution is determined by its initial state, requiring no further input from the user. The script runs continuously, generating new generations of cells until it reaches stability, all cells die, or a maximum number of generations is reached.

## Overview of the Game

Conway's Game of Life is a cellular automaton devised by mathematician John Conway. The game consists of a grid of cells, each of which can be either alive or dead. The game evolves in discrete steps, with the state of each cell in the next generation determined by the number of live neighbors it has:

- Survival: A living cell with 2 or 3 live neighbors survives to the next generation.
- Birth: A dead cell with exactly 3 live neighbors becomes a live cell in the next generation.
- Death: All other cells die or remain dead in the next generation.

The game continues to evolve through generations until it either stabilizes (no change between generations), all cells die, or it reaches the maximum number of generations allowed by the script.

## Features

- Random Initialization: The grid is initialized with a random distribution of live and dead cells.
- Random Color: The live cells are displayed in a randomly chosen color on the Sense HAT LED matrix.
- Stability Detection: The script checks for stability (repeated grids) or if all cells are dead, and will stop the simulation when one of these conditions is met.
- Generational Limit: The simulation will run for up to 1000 generations unless stability or extinction occurs first.
- Continuous Play: After reaching the end of a game, the simulation restarts with a new random grid.

## Requirements

- Raspberry Pi with Sense HAT
- Python 3
- Sense HAT library

## Installation

1. Install the Sense HAT library if you haven't already:

    ```sh
    sudo apt-get update
    sudo apt-get install sense-hat
    ```

2. Clone or download this repository to your Raspberry Pi.

3. Navigate to the directory containing the script.

## Usage

Run the script with Python:

```sh
python3 conway.py
```

The game will begin immediately, displaying the evolving generations of Conway's Game of Life on the 8x8 LED matrix. You can quit the game by pressing Ctrl+C.

## Customization

- MAX_GENERATIONS: You can adjust the maximum number of generations by changing the MAX_GENERATIONS constant in the script.
- Speed: The speed of the game can be adjusted by modifying the time.sleep(0.5) value in the main game loop. A smaller value will speed up the simulation, while a larger value will slow it down.
- Grid Size: The script is designed for an 8x8 grid, but you can adapt it for larger grids if using a different display. Note that this will require changes to the WIDTH and HEIGHT constants.


## License

This project is open-source and available under the MIT License.
