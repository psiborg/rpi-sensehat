#!/usr/bin/env python3
# ========================================================================
# temperature_monitor.py
#
# Description:
#
# Author: Jim Ing
# Date: 2024-08-13
# ========================================================================

from sense_hat import SenseHat
import time

sense = SenseHat()

# Define the color ranges with names and hex codes
colors = [
    (-20, -11, (1, 144, 240), "#0190F0", "Extreme cold"),
    (-10, 1, (0, 190, 252), "#00BEFC", "Very cold"),
    (0, 9, (80, 205, 160), "#50CDA0", "Cold"),
    (10, 19, (169, 231, 81), "#A9E751", "Cool"),
    (20, 29, (254, 253, 0), "#FEFD00", "Brisk"),
    (30, 34, (247, 124, 1), "#F77C01", "Warm"),
    (35, 39, (250, 125, 0), "#FA7D00", "Hot"),
    (40, 49, (248, 0, 0), "#F80000", "Very hot"),
    (50, 100, (185, 0, 0), "#B90000", "Extreme heat")
]

def get_color(temperature):
    for temp_range in colors:
        if temp_range[0] <= temperature <= temp_range[1]:
            return temp_range[2], temp_range[3], temp_range[4]
    return (0, 0, 0), "#000000", "Out of range"  # default to black if out of range

try:
    print("To quit, press Ctrl+C")

    while True:
        temp = sense.get_temperature()
        color, hex_color, color_name = get_color(temp)
        #print(f"Temperature: {temp:.2f}°C, RGB: {color}, Hex: {hex_color}, Color: {color_name}")
        print(f"Temperature: {temp:.2f}°C, {color_name}")

        if temp >= 50:
            # Flashing effect
            for _ in range(5):  # Flash 5 times
                sense.clear(color)
                time.sleep(0.5)
                sense.clear(0, 0, 0)  # Turn off LEDs
                time.sleep(0.5)
        else:
            sense.clear(color)

        time.sleep(1)  # Update every second

except KeyboardInterrupt:
    # Clear the LED matrix when the script is interrupted
    sense.clear()
