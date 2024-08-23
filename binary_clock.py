#!/usr/bin/env python3
# ========================================================================
# binary_clock.py
#
# Description: Display a binary clock.
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

from sense_hat import SenseHat
from datetime import datetime
import time

sense = SenseHat()

# Define colors
red = (255, 0, 0)    # Red for hours
green = (0, 255, 0)  # Green for minutes
blue = (0, 0, 255)   # Blue for seconds
inactive = (0, 0, 0) # Off for binary 0

def display_binary(value, col_start, bits, color):
    # Display a binary value on the LED matrix with a specific color.
    binary_str = f'{value:0{bits}b}' # Convert to binary string with a fixed number of bits
    for i in range(bits):
        bit = int(binary_str[i])
        # Place the bit on the corresponding column with the specified color
        sense.set_pixel(col_start, 7 - i, color if bit else inactive)

def display_time():
    # Display the current time in binary on the Sense HAT 8x8 matrix.
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    sense.clear()

    # Display hours (5 bits) in red
    display_binary(hour, 0, 5, red)

    # Display minutes (6 bits) in green
    display_binary(minute, 3, 6, green)

    # Display seconds (6 bits) in blue
    display_binary(second, 6, 6, blue)

try:
    print ("To quit, press Ctrl+C")
    while True:
        display_time()
        time.sleep(1) # Update every second

except KeyboardInterrupt:
    sense.clear()
