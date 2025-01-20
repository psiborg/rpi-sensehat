#!/usr/bin/env python3
# ========================================================================
# sort_leds.py --algorithm bubble --palette wopr
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

# Color palettes
PALETTES = {
    "default": {
        "names": ["Gry", "Red", "Grn", "Yel", "Blu", "Mag", "Cyn", "Wht"],
        "colors": [
            (102, 102, 102),  # Grey
            (255, 0, 0),      # Red
            (0, 255, 0),      # Green
            (255, 255, 0),    # Yellow
            (0, 0, 255),      # Blue
            (255, 0, 255),    # Magenta
            (0, 255, 255),    # Cyan
            (255, 255, 255)   # White
        ],
        "termcodes": {
            "Gry": "dark_grey",
            "Red": "red",
            "Grn": "green",
            "Yel": "yellow",
            "Blu": "blue",
            "Mag": "magenta",
            "Cyn": "cyan",
            "Wht": "white"
        }
    },
    "wopr": {
        "names": ["Red", "Org", "Yel", "Grn", "Cyn", "Blu", "Pur", "Wht"],
        "colors": [
            (255, 0, 0),      # Red
            (255, 165, 0),    # Orange
            (255, 255, 0),    # Yellow
            (0, 255, 0),      # Green
            (0, 255, 255),    # Cyan
            (0, 0, 255),      # Blue
            (128, 0, 128),    # Purple
            (255, 255, 255)   # White
        ],
        "termcodes": {
            "Red": "red",
            "Org": "yellow",  # Closest match for terminal
            "Yel": "yellow",
            "Grn": "green",
            "Cyn": "cyan",
            "Blu": "blue",
            "Pur": "magenta",  # Closest match for terminal
            "Wht": "white"
        }
    }
}

def partition(values, low, high):
    """
    Partition is a helper function used in the Quick Sort algorithm.
    Its purpose is to rearrange elements in a sublist so that all elements
    less than a chosen pivot value come before the pivot, and all elements
    greater than or equal to the pivot come after it.
    """
    pivot = values[high]
    i = low - 1
    moves = 0
    for j in range(low, high):
        if values[j] < pivot:
            i += 1
            values[i], values[j] = values[j], values[i]
            moves += 1
    values[i + 1], values[high] = values[high], values[i + 1]
    moves += 1
    return i + 1, moves

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

def display_colors(label, values, palette):
    """Displays colors as colored circles in the console."""
    print(f"{label:03}:", end=" ")
    for v in values:
        print(colored("●", palette["termcodes"][palette["names"][v - 1]]), end=" ")
    print()

def sorting_visualizer(algorithm, palette_name):
    """Runs a visual sorting demonstration on the 8x8 LED matrix."""
    palette = PALETTES[palette_name]
    while True:
        print(f"{algorithm.capitalize()} sort:")
        values = [random.randint(1, 8) for _ in range(8)]
        matrix = [[(0, 0, 0) for _ in range(8)] for _ in range(8)]

        # Initialize first row with randomly selected colors
        for x in range(8):
            matrix[0][x] = palette["colors"][values[x] - 1]

        draw_bars(matrix)
        display_colors(0, values, palette)

        row = 1
        sort_function = globals()[algorithm + "_sort"]

        for sorted_values, moves in sort_function(values):
            if row % 8 == 0:
                sense.clear()
                matrix = [[(0, 0, 0) for _ in range(8)] for _ in range(8)]

            for x in range(8):
                matrix[row % 8][x] = palette["colors"][sorted_values[x] - 1]

            draw_bars(matrix)
            display_colors(row, sorted_values, palette)
            row += 1

        draw_bars(matrix)
        print()
        time.sleep(20)
        sense.clear()

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--algorithm", choices=["bubble", "selection", "insertion", "quick", "cocktail_shaker"], default="bubble")
        parser.add_argument("--palette", choices=PALETTES.keys(), default="default", help="Choose a color palette (default or wopr).")
        args = parser.parse_args()
        sorting_visualizer(args.algorithm, args.palette)

    except KeyboardInterrupt:
        sense.clear()
