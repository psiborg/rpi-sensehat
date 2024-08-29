#!/usr/bin/env python3
# ========================================================================
# temperature_monitor.py
#
# Description: A temperature monitor that shows severity by color.
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

import time
from config import sense

# Define the color ranges with hex codes and names
colors = [
    (-20, -10.01, (1, 144, 240), "#0190F0", "Extreme cold"),
    (-10, 0.99, (0, 190, 252), "#00BEFC", "Very cold"),
    (0, 9.99, (80, 205, 160), "#50CDA0", "Cold"),
    (10, 19.99, (169, 231, 81), "#A9E751", "Cool"),
    (20, 29.99, (254, 253, 0), "#FEFD00", "Brisk"),
    (30, 34.99, (247, 124, 1), "#F77C01", "Warm"),
    (35, 39.99, (250, 125, 0), "#FA7D00", "Hot"),
    (40, 49.99, (248, 0, 0), "#F80000", "Very hot"),
    (50, 100, (185, 0, 0), "#B90000", "Extreme heat")
]

def get_color(temperature):
    for temp_range in colors:
        if temp_range[0] <= temperature <= temp_range[1]:
            return temp_range[2], temp_range[3], temp_range[4]
    return (0, 0, 0), "#000000", "Out of range" # default to black if out of range

try:
    print("To quit, press Ctrl+C")

    while True:
        temp = sense.get_temperature()
        #print(temp)
        color, hex_color, color_name = get_color(temp)
        print(f"Temperature: {temp:.2f}°C, RGB: {color}, Hex: {hex_color}, Color: {color_name}")
        #print(f"Temperature: {temp:.2f}°C, {color_name}")

        if temp >= 50:
            # Flashing effect
            for _ in range(3): # Flash 3 times
                sense.clear(color)
                time.sleep(0.5)
                sense.clear(0, 0, 0) # Turn off LEDs
                time.sleep(0.5)
        else:
            sense.clear(color)

        time.sleep(1) # Update every second

except KeyboardInterrupt:
    sense.clear()
