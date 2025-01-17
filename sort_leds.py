#!/usr/bin/env python3
# ========================================================================
# sort_leds.py
#
# Description: Generates a random list of 8 values (1-8) representing
#              colors and sorts them using the specified algorithm. Each
#              step of the sorting process is displayed on the LED
#              matrix, and colors are printed to the console.
#
# pip3 install termcolor
#
# Author: Jim Ing
# Date: 2025-01-16
# ========================================================================

import argparse
import random
import time

from termcolor import colored
from config import sense
sense.clear()

# Standard 8 colors
COLOR_NAMES = ["Gry", "Red", "Grn", "Yel", "Blu", "Mag", "Cyn", "Wht"]
COLORS = [
    (102, 102, 102), # Grey
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    (255, 255, 0),   # Yellow
    (0, 0, 255),     # Blue
    (255, 0, 255),   # Magenta
    (0, 255, 255),   # Cyan
    (255, 255, 255)  # White
]

COLOR_TERMCODES = {
    "Gry": "dark_grey",
    "Red": "red",
    "Grn": "green",
    "Yel": "yellow",
    "Blu": "blue",
    "Mag": "magenta",
    "Cyn": "cyan",
    "Wht": "white"
}

def partition(values, low, high):
    """
    Partition is a helper function used in the Quick Sort algorithm.
    Its purpose is to rearrange elements in a sublist so that all elements
    less than a chosen pivot value come before the pivot, and all elements
    greater than or equal to the pivot come after it.
    """
    pivot = values[high]  # Select the pivot (typically the last element)
    i = low - 1  # Pointer for the smaller element
    moves = 0  # Track the number of swaps/moves

    for j in range(low, high):
        if values[j] < pivot:  # If current element is smaller than pivot
            i += 1
            values[i], values[j] = values[j], values[i]  # Swap elements
            moves += 1

    values[i + 1], values[high] = values[high], values[i + 1]  # Place pivot in correct position
    moves += 1
    return i + 1, moves  # Return pivot index and moves count

def bubble_sort(values):
    """Bubble Sort Algorithm."""
    moves = 0
    for i in range(len(values) - 1):
        for j in range(len(values) - 1 - i):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                moves += 1
                yield values, moves

def selection_sort(values):
    """Selection Sort Algorithm."""
    moves = 0
    for i in range(len(values)):
        min_idx = i
        for j in range(i + 1, len(values)):
            if values[j] < values[min_idx]:
                min_idx = j
        values[i], values[min_idx] = values[min_idx], values[i]
        moves += 1
        yield values, moves

def insertion_sort(values):
    """Insertion Sort Algorithm."""
    moves = 0
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and key < values[j]:
            values[j + 1] = values[j]
            j -= 1
            moves += 1
            yield values, moves
        values[j + 1] = key
        yield values, moves

def quick_sort(values, low=0, high=None, moves=[0]):
    """Quick Sort Algorithm."""
    if high is None:
        high = len(values) - 1
    if low < high:
        pivot, m = partition(values, low, high)
        moves[0] += m
        yield values, moves[0]
        yield from quick_sort(values, low, pivot - 1, moves)
        yield from quick_sort(values, pivot + 1, high, moves)

def cocktail_shaker_sort(values):
    """Cocktail Shaker Sort Algorithm."""
    moves = 0
    n = len(values)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swapped = True
                moves += 1
                yield values, moves
        end -= 1
        for i in range(end, start, -1):
            if values[i] < values[i - 1]:
                values[i], values[i - 1] = values[i - 1], values[i]
                swapped = True
                moves += 1
                yield values, moves
        start += 1

def draw_bars(matrix):
    """Draws the entire matrix on the Sense HAT LED display."""
    sense.clear()
    for y in range(8):
        for x in range(8):
            sense.set_pixel(x, y, matrix[y][x])
    time.sleep(0.5)

def display_colors(label, values):
    """Displays colors as colored circles in the console."""
    print(f"{label:03}:", end=" ")
    for v in values:
        print(colored("●", COLOR_TERMCODES[COLOR_NAMES[v - 1]]), end=" ")
    print()

def sorting_visualizer(algorithm):
    """Runs a visual sorting demonstration on the 8x8 LED matrix."""
    while True:
        print(f"{algorithm.capitalize()} sort:")
        values = [random.randint(1, 8) for _ in range(8)]
        matrix = [[(0, 0, 0) for _ in range(8)] for _ in range(8)]

        # Initialize first row with randomly selected colors
        for x in range(8):
            matrix[0][x] = COLORS[values[x] - 1]

        draw_bars(matrix)
        display_colors(0, values)

        row = 1
        sort_function = globals()[algorithm + "_sort"]

        for sorted_values, moves in sort_function(values):
            if row % 8 == 0:  # Before wrapping back to the top row
                sense.clear()  # Clear the LED matrix
                matrix = [[(0, 0, 0) for _ in range(8)] for _ in range(8)]  # Reset matrix to black

            for x in range(8):
                matrix[row % 8][x] = COLORS[sorted_values[x] - 1]

            draw_bars(matrix)
            display_colors(row, sorted_values)
            row += 1

        draw_bars(matrix)
        print()
        time.sleep(20)
        sense.clear()  # Ensure the screen is cleared before restarting

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--algorithm", choices=["bubble", "selection", "insertion", "quick", "cocktail_shaker"], default="bubble")
        args = parser.parse_args()
        sorting_visualizer(args.algorithm)

    except KeyboardInterrupt:
        # Clear the LED matrix when exiting
        sense.clear()
