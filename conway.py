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
from sense_hat import SenseHat

sense = SenseHat()

# Constants
WIDTH, HEIGHT = 8, 8
MAX_GENERATIONS = 1000

# Directions for checking neighbors
NEIGHBOR_DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),         (0, 1),
    (1, -1), (1, 0), (1, 1)
]

# Random color
def random_color():
    return [random.randint(0, 255) for _ in range(3)]

# Initialize grid
def init_grid():
    return [[random.choice([0, 1]) for _ in range(WIDTH)] for _ in range(HEIGHT)]

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

# Display grid
def display_grid(grid, color):
    pixels = []
    for row in grid:
        for cell in row:
            pixels.append(color if cell else [0, 0, 0])
    sense.set_pixels(pixels)

# Check for stability or dead cells
def check_stability(current_grid, previous_grids):
    if current_grid in previous_grids:
        return "Stable"
    if sum(map(sum, current_grid)) == 0:
        return "All Dead"
    return None

# Main game loop
def game_of_life():
    generation = 0
    color = random_color()
    grid = init_grid()
    previous_grids = []

    while generation < MAX_GENERATIONS:
        display_grid(grid, color)
        time.sleep(0.5)

        new_grid = next_generation(grid)
        state = check_stability(new_grid, previous_grids)

        population = sum(map(sum, new_grid))
        print(f"Generation: {generation}, Population: {population}, State: {state if state else 'Active'}")

        if state or population == 0:
            break

        previous_grids.append(grid)
        if len(previous_grids) > 10:
            previous_grids.pop(0)

        grid = new_grid
        generation += 1

    if generation >= MAX_GENERATIONS:
        print(f"Reached {MAX_GENERATIONS} generations.")

    time.sleep(3) # Pause before resetting
    sense.clear()

try:
    print("To quit, press Ctrl+C")
    while True:
        game_of_life()

except KeyboardInterrupt:
    sense.clear()
