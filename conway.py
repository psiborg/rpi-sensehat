#!/usr/bin/env python3
# ========================================================================
# conway.py
#
# Description: Conway's game of life.
#
# Author: Jim Ing
# Date: 2024-08-24
# ========================================================================

import random
import time
import argparse
from config import sense

# Constants
WIDTH, HEIGHT = 8, 8
MAX_GENERATIONS = 1000

# Directions for checking neighbors
NEIGHBOR_DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

# Color definitions
RED = [255, 0, 0]    # Dying cells
GREEN = [0, 255, 0]  # Stable (alive) cells
BLUE = [0, 0, 255]   # Newly born cells
BLACK = [0, 0, 0]    # Dead cells

# Predefined patterns that fit within an 8x8 grid
PATTERNS = {
    "block": [(3, 3), (3, 4), (4, 3), (4, 4)],
    "blinker": [(3, 3), (3, 4), (3, 5)],
    "toad": [(2, 4), (3, 4), (4, 4), (3, 3), (4, 3), (5, 3)],
    "glider": [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)],
    "beacon": [(2, 2), (2, 3), (3, 2), (3, 3), (4, 4), (4, 5), (5, 4), (5, 5)],
    "pulsar": [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2),
               (4, 3), (1, 2), (1, 4), (5, 2), (5, 4), (6, 2), (6, 4)],
    "diehard": [(1, 0), (1, 1), (2, 1), (2, 2), (3, 0), (3, 2), (4, 1),
                (4, 2)],
    "acorn": [(1, 2), (2, 1), (2, 2), (3, 0), (3, 2), (3, 3), (4, 1), (4, 3)],
    "r_pentomino": [(3, 4), (4, 3), (4, 4), (4, 5), (5, 3)],
    "pentadecathlon": [(2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (3, 5), (4, 5),
                       (5, 5)]
}

# Initialize grid
def init_grid(pattern=None):
    grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    if pattern:
        for x, y in PATTERNS[pattern]:
            grid[y][x] = 1
    else:
        grid = [[random.choice([0, 1]) for _ in range(WIDTH)]
                for _ in range(HEIGHT)]
    return grid

# Count neighbors
def count_neighbors(grid, x, y):
    count = 0
    for dx, dy in NEIGHBOR_DIRECTIONS:
        nx, ny = (x + dx) % WIDTH, (y + dy) % HEIGHT
        count += grid[ny][nx]
    return count

# Next generation
def next_generation(grid):
    new_grid = [[0] * WIDTH for _ in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = count_neighbors(grid, x, y)
            if grid[y][x] == 1:
                if neighbors in (2, 3):
                    new_grid[y][x] = 1
            elif neighbors == 3:
                new_grid[y][x] = 1
    return new_grid

# Display grid with color coding
def display_grid(grid, previous_grid):
    pixels = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x] == 1:  # Alive cell
                if previous_grid and previous_grid[y][x] == 1:
                    # Stable cell (was alive last generation and still alive)
                    pixels.append(GREEN)
                else:
                    # Newly born cell
                    pixels.append(BLUE)
            elif previous_grid and previous_grid[y][x] == 1:
                # Dying cell (was alive last generation, now dead)
                pixels.append(RED)
            else:
                # Dead cell
                pixels.append(BLACK)
    sense.set_pixels(pixels)

# Print grid to console
def print_grid(grid, previous_grid):
    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            if grid[y][x] == 1:  # Alive cell
                if previous_grid and previous_grid[y][x] == 1:
                    line += "G"  # Green (stable)
                else:
                    line += "B"  # Blue (newly born)
            elif previous_grid and previous_grid[y][x] == 1:
                line += "R"  # Red (dying)
            else:
                line += "."  # Blank for dead cells
        print(line)

# Main game loop
def game_of_life(pattern=None):
    generation = 0
    grid = init_grid(pattern)
    previous_grids = []
    previous_color_grid = None  # To track the color state for each cell

    print("Initial grid:")
    print_grid(grid, previous_color_grid)

    while generation < MAX_GENERATIONS:
        display_grid(grid, previous_color_grid)
        time.sleep(1)

        new_grid = next_generation(grid)

        # Check stability
        if new_grid in previous_grids:
            print(f"Stable pattern reached at generation {generation}:")
            print_grid(grid, previous_color_grid)
            break
        if sum(map(sum, new_grid)) == 0:
            print(f"All cells dead at generation {generation}:")
            print_grid(grid, previous_color_grid)
            break

        # Keep track of previous grids (limit to the last 10 generations)
        previous_grids.append(grid)
        if len(previous_grids) > 10:
            previous_grids.pop(0)  # Keep history of 10 generations

        previous_color_grid = grid
        grid = new_grid
        generation += 1

    if generation >= MAX_GENERATIONS:
        print(f"Reached {MAX_GENERATIONS} generations:")
        print_grid(grid, previous_color_grid)

    time.sleep(20)  # Pause before resetting
    sense.clear()


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            description="Conway's Game of Life with patterns")
        parser.add_argument('--pattern', type=str, choices=PATTERNS.keys(),
                            help='Start with a common pattern')
        args = parser.parse_args()

        print("To quit, press Ctrl+C")
        while True:
            game_of_life(pattern=args.pattern)

    except KeyboardInterrupt:
        sense.clear()
