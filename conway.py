#!/usr/bin/env python3
# ========================================================================
# conway.py
#
# Description: Conway's game of life.
#
# Rules:
#   - Underpopulation: Any live cell with fewer than two live neighbors dies.
#   - Overcrowding: Any live cell with more than three live neighbors dies.
#   - Survival: Any live cell with two or three live neighbors lives to the next generation.
#   - Reproduction: Any dead cell with exactly three live neighbors becomes a live cell.
#
# Author: Jim Ing
# Date: 2024-08-24
# ========================================================================

from sense_hat import SenseHat
import time
import random

sense = SenseHat()

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Initialize colors
alive_color = random_color()  # Random color for alive cells
dead_color = (0, 0, 0)       # Black for dead cells
stable_color = (255, 0, 0)   # Red for stable cells

# Initialize the grid (8x8) with random 0s and 1s
grid = [[random.choice([0, 1]) for _ in range(8)] for _ in range(8)]
iteration_count = 0  # Initialize the iteration counter

# To track the last few grid states for detecting alternating patterns
previous_grids = []

def count_neighbors(x, y):
    """Count the number of alive neighbors around a given cell (x, y)."""
    neighbor_coords = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in neighbor_coords:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8:
            count += grid[nx][ny]
    return count

def update_grid():
    """Update the grid according to the Game of Life rules."""
    new_grid = [[0 for _ in range(8)] for _ in range(8)]
    for x in range(8):
        for y in range(8):
            neighbors = count_neighbors(x, y)
            if grid[x][y] == 1:  # Alive cell
                if neighbors < 2 or neighbors > 3:
                    new_grid[x][y] = 0  # Dies
                else:
                    new_grid[x][y] = 1  # Lives
            else:  # Dead cell
                if neighbors == 3:
                    new_grid[x][y] = 1  # Becomes alive
    return new_grid

def display_grid(color):
    """Display the grid on the Sense HAT LED matrix."""
    pixels = []
    for x in range(8):
        for y in range(8):
            if grid[x][y] == 1:
                pixels.append(color)
            else:
                pixels.append(dead_color)
    sense.set_pixels(pixels)

def grids_are_equal(grid1, grid2):
    """Check if two grids are the same."""
    for x in range(8):
        for y in range(8):
            if grid1[x][y] != grid2[x][y]:
                return False
    return True

def detect_stable_pattern(grid):
    """Detect and describe common stable patterns."""
    # Simple detection for common patterns
    patterns = {
        "Block (Still Life)": [
            [1, 1],
            [1, 1]
        ],
        "Blinker (Oscillator)": [
            [1, 1, 1]
        ],
        "Glider (Spaceship)": [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ]
    }

    for name, pattern in patterns.items():
        p_height = len(pattern)
        p_width = len(pattern[0])
        for x in range(8 - p_height + 1):
            for y in range(8 - p_width + 1):
                match = True
                for px in range(p_height):
                    for py in range(p_width):
                        if grid[x + px][y + py] != pattern[px][py]:
                            match = False
                            break
                    if not match:
                        break
                if match:
                    return name

    return "Unknown Pattern"

def all_cells_dead(grid):
    """Check if all cells in the grid are dead."""
    return all(cell == 0 for row in grid for cell in row)

def check_for_alternation():
    """Check if the grid is alternating between two patterns more than three times."""
    if len(previous_grids) >= 4:
        if (grids_are_equal(previous_grids[-1], previous_grids[-3]) and
            grids_are_equal(previous_grids[-2], previous_grids[-4])):
            return True
    return False

# Track the time since the last change in the grid
last_change_time = time.time()
time_limit = 10
stable_display_time = 30
pause_time = 20  # seconds before resetting the grid

try:
    while True:
        # Store the previous state of the grid
        previous_grid = [row[:] for row in grid]
        previous_grids.append(previous_grid)
        if len(previous_grids) > 4:
            previous_grids.pop(0)  # Keep the last four grids

        # Update and display the grid
        display_grid(alive_color)
        time.sleep(0.5)
        grid = update_grid()
        iteration_count += 1  # Increment the iteration counter

        # Check if the grid has changed
        if not grids_are_equal(grid, previous_grid):
            last_change_time = time.time()

        # Check if the system has become stable
        if time.time() - last_change_time > time_limit:
            pattern_name = detect_stable_pattern(grid)
            print(f"System has become stable after {iteration_count} iterations.")
            print(f"Stability pattern: {pattern_name}")
            print(f"Summary: The grid reached a stable configuration resembling a '{pattern_name}' after {iteration_count} iterations.\n")
            # Display the grid in red to indicate stability
            display_grid(stable_color)
            time.sleep(stable_display_time)  # Show the stable pattern in red for 1 minute

            '''
            # Pause before resetting the grid
            print("Pausing before resetting the grid...")
            time.sleep(pause_time)  # 30-second pause
            '''

            # Reset the grid for a new round
            print("Resetting the grid...")
            grid = [[random.choice([0, 1]) for _ in range(8)] for _ in range(8)]
            alive_color = random_color()  # Randomize the color for alive cells
            stable_color = (255, 0, 0)   # Set stable color to red
            last_change_time = time.time()  # Reset the timer
            iteration_count = 0  # Reset the iteration counter
            previous_grids.clear()  # Clear previous grids
            continue

        # Check if all cells are dead
        if all_cells_dead(grid):
            print(f"All cells are dead after {iteration_count} iterations. Resetting grid.")
            grid = [[random.choice([0, 1]) for _ in range(8)] for _ in range(8)]
            alive_color = random_color()  # Randomize the color for alive cells
            stable_color = (255, 0, 0)   # Set stable color to red
            last_change_time = time.time()  # Reset the timer
            iteration_count = 0  # Reset the iteration counter
            previous_grids.clear()  # Clear previous grids
            continue
        '''
        # Check if the grid is alternating between two patterns
        if check_for_alternation():
            print(f"System is alternating between two patterns after {iteration_count} iterations. Resetting grid.")
            grid = [[random.choice([0, 1]) for _ in range(8)] for _ in range(8)]
            alive_color = random_color()  # Randomize the color for alive cells
            stable_color = (255, 0, 0)   # Set stable color to red
            last_change_time = time.time()  # Reset the timer
            iteration_count = 0  # Reset the iteration counter
            previous_grids.clear()  # Clear previous grids
            continue
        '''

except KeyboardInterrupt:
    sense.clear()
