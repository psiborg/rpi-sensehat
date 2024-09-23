# Conway's Game of Life on the Sense HAT

This Python script implements **Conway's Game of Life** using the Sense HAT LED matrix. It includes predefined patterns and displays the game in real-time with color-coded cells representing different stages of life (alive, newly born, dying, or dead).

## Overview of Conway's Game of Life

Conway's Game of Life is a cellular automaton devised by British mathematician John Horton Conway in 1970. It's a zero-player game that simulates the birth, survival, and death of cells on a grid, following simple rules that lead to complex and often unpredictable behavior.

### Rules:

1. **Survival**: Any live cell with 2 or 3 live neighbors stays alive.
2. **Death**: Any live cell with fewer than 2 or more than 3 live neighbors dies (underpopulation/overpopulation).
3. **Birth**: Any dead cell with exactly 3 live neighbors becomes a live cell.

Despite these simple rules, Conway's Game of Life can produce infinitely complex and varied behaviors.

### Patterns

The game is particularly famous for its predefined patterns, such as oscillators (patterns that repeat over time), still lifes (patterns that remain unchanged), and spaceships (patterns that move across the grid).

## Features

- **8x8 Grid**: The game is played on an 8x8 grid, mapped to the Sense HAT's LED matrix.
- **Color-coded Cells**:
  - **Green (G)**: Stable cells (alive for multiple generations).
  - **Blue (B)**: Newly born cells.
  - **Red (R)**: Dying cells (alive in the previous generation, but now dead).
  - **Black**: Dead cells.
- **Predefined Patterns**: Start with common patterns such as Block, Blinker, Glider, Toad, Beacon, etc.
- **Console Output**: Displays a simplified version of the grid to the console, using characters `G`, `B`, `R`, and spaces for different states of cells.

## Technical Overview

The game proceeds by updating the grid in discrete steps (or generations). Each step is computed based on the previous state of the grid and the number of neighboring cells.

### Key Components of the Code:

1. **Grid Initialization** (`init_grid`):
   The grid is initialized as a two-dimensional list. If a predefined pattern is chosen, the corresponding cells are set to alive (`1`), otherwise, the grid is populated randomly.

2. **Neighbor Count** (`count_neighbors`):
   For each cell, the number of live neighbors is counted using the eight possible adjacent directions (up, down, left, right, and diagonals). The grid uses modulo arithmetic to wrap around the edges (allowing the game to behave as a toroidal grid).

3. **Next Generation Calculation** (`next_generation`):
   The script applies Conway's rules to determine whether each cell will be alive or dead in the next generation. If the number of neighbors meets the survival or birth conditions, the cell's state is updated.

4. **Grid Display** (`display_grid`):
   The state of the grid is translated into an array of pixel colors corresponding to the Sense HAT's LED display. Newly born cells are blue, stable cells are green, and dying cells (those that were alive but are now dead) are red.

5. **Grid Print to Console** (`print_grid`):
   This function prints a text-based version of the grid to the console, showing red cells as `R`, green cells as `G`, blue cells as `B`, and dead cells as blank spaces.

6. **Pattern Stability**:
   The game checks for stability by keeping track of previous generations. If a grid configuration repeats (indicating a stable or oscillating pattern) or all cells die, the game ends.

## Prerequisites

- Sense HAT installed on a Raspberry Pi.
- Python 3.x.
- Sense HAT Python library installed.

## Installation

1. Clone the repository or copy the script to your Raspberry Pi.
2. Ensure the Sense HAT is connected to the Raspberry Pi.
3. Install the necessary dependencies using the following command:

```bash
sudo apt install sense-hat
```

4. Place the config.py file (which initializes the sense object) in the same directory as the script.


## Usage

Run the script using Python and optionally specify a pattern to start the game with.

```bash
python game_of_life.py [--pattern PATTERN]
```

### Available Patterns

You can start the game with one of the following predefined patterns that fit within the 8x8 grid:

- block: Stable 2x2 block.
- blinker: Oscillating line of 3 cells.
- toad: 6-cell oscillator.
- glider: A pattern that "glides" across the grid.
- beacon: Oscillating 2x2 blocks.
- pulsar: Larger oscillator pattern.
- diehard: A pattern that eventually dies out.
- acorn: Small pattern that grows into a complex structure.
- r_pentomino: A small, chaotic pattern.
- pentadecathlon: Oscillator with a period of 15 generations.

For example, to start with a glider:

```bash
python game_of_life.py --pattern glider
```

If no pattern is specified, the grid will be randomly populated.

## Game Mechanics

The game proceeds through generations based on the following rules:

1. Any live cell with two or three neighbors survives.
2. Any dead cell with exactly three live neighbors becomes a live cell (birth).
3. All other live cells die, and all other dead cells stay dead.

The game will terminate if:

- All cells die (the grid becomes empty).
- A stable or oscillating pattern is reached (detected by checking previous generations).

## Console Output

During each generation, the grid is printed to the console in a simplified format:

- G: Stable (green) cells.
- B: Newly born (blue) cells.
- R: Dying (red) cells.
- Empty space: Dead cells.

For example, a grid with a pattern might appear like this:

```txt
........
........
........
...R....
..BGB...
...R....
........
........
```

## License

This project is licensed under the MIT License.
