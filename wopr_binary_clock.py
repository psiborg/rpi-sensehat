#!/usr/bin/env python3
# ========================================================================
# wopr_binary_clock.py
#
# Description: This project simulates a binary clock in the style of the
#              WOPR supercomputer on a Raspberry Pi Sense HAT. The LED
#              matrix dynamically updates to display the current time
#              using binary-coded columns for hours, minutes, and seconds.
# Features:
#
#   - Binary Clock Representation: Uses red LEDs for binary 1 and amber
#     LEDs for binary 0.
#   - Ambient Glow: A dim red background mimics the aesthetic of WOPR.
#   - Flashing Effect: The seconds column flashes briefly every second to
#     simulate activity.
#   - Flickering Effect: Some LEDs randomly flicker to create a more
#     dynamic and realistic display.
#   - Smooth Animation: Updates happen with subtle fading transitions.
#
# Author: Jim Ing
# Date: 2025-01-02
# ========================================================================

import time
import random
from config import sense

# Define colors
OFF = [0, 0, 0]       # LED off
RED = [255, 0, 0]     # Red for binary 1
AMBER = [255, 191, 0] # Amber for binary 0
DIM_RED = [50, 0, 0]  # Dim red background glow
FLASH = [255, 100, 0] # Flashing effect for seconds

# Convert number to a 6-bit binary list
def number_to_binary_list(number, length=6):
    return [int(bit) for bit in f"{number:0{length}b}"]

# Generate the binary clock LED matrix
def generate_binary_clock_matrix(flash=False, flicker=False, print_time=False):
    current_time = time.localtime()
    hours, minutes, seconds = current_time.tm_hour, current_time.tm_min, current_time.tm_sec

    # Convert time to binary
    hours_bin = number_to_binary_list(hours, 6)
    minutes_bin = number_to_binary_list(minutes, 6)
    seconds_bin = number_to_binary_list(seconds, 6)

    # Print time to console every 15 minutes
    if print_time:
        print(f"Time: {hours:02}:{minutes:02}:{seconds:02} | "
              f"Binary: {''.join(map(str, hours_bin))} : {''.join(map(str, minutes_bin))} : {''.join(map(str, seconds_bin))}")

    # Start with ambient glow
    matrix = [[DIM_RED for _ in range(8)] for _ in range(8)]

    # Function to set two rows for each time component
    def place_binary(start_row, binary_list):
        for i in range(6):
            color = RED if binary_list[i] else (FLASH if (flash and start_row == 6) else AMBER)
            matrix[start_row][i + 1] = color  # Shifted right by 1 column
            matrix[start_row + 1][i + 1] = color  # Duplicate for double height

    # Apply binary values to the matrix
    place_binary(0, hours_bin)   # Hours: rows 0-1
    place_binary(3, minutes_bin) # Minutes: rows 3-4
    place_binary(6, seconds_bin) # Seconds: rows 6-7

    # Flickering effect on random pixels
    if flicker and random.random() < 0.2:
        x, y = random.randint(1, 7), random.randint(0, 7)  # Adjusted x range to avoid column 0
        matrix[y][x] = OFF if matrix[y][x] != OFF else DIM_RED

    return [pixel for row in matrix for pixel in row]

# Main loop for updating the display
def binary_clock():
    last_console_print = -1  # Initialize with an invalid minute value
    try:
        while True:
            current_minute = time.localtime().tm_min

            # Print time every 15 minutes
            print_time = current_minute % 15 == 0 and current_minute != last_console_print
            if print_time:
                last_console_print = current_minute

            for _ in range(3):  # Fading effect loop
                sense.set_pixels(generate_binary_clock_matrix(flash=True, flicker=True, print_time=print_time))
                time.sleep(0.1)
            sense.set_pixels(generate_binary_clock_matrix(flash=False, flicker=True))
            time.sleep(1)  # Standard update interval
    except KeyboardInterrupt:
        sense.clear()

if __name__ == "__main__":
    binary_clock()
