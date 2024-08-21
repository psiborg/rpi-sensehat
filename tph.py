#!/usr/bin/env python3
# ========================================================================
# tph.py
#
# Description: A compact approach to visualize three distinct sensor
#              readings in real-time using the small 8x8 matrix.
#
# Author: Jim Ing
# Date: 2024-08-18
# ========================================================================

from sense_hat import SenseHat
import time

sense = SenseHat()

# Function to map sensor value to a color gradient
def get_color(value, min_val, max_val, color_range):
    # Handle edge case where min_val equals max_val
    if min_val == max_val:
        normalized = 0.5  # Set to middle of the range
    else:
        # Normalize the value between 0 and 1
        normalized = (value - min_val) / (max_val - min_val)
        # Clamp the normalized value to [0, 1] to avoid index errors
        normalized = max(0, min(1, normalized))

    # Map to color in range
    index = int(normalized * (len(color_range) - 1))
    return color_range[index]

# Color gradients
temperature_colors = [(0, 0, 255), (255, 0, 0)]  # Blue to Red
pressure_colors = [(173, 216, 230), (0, 0, 139)] # Light blue to Dark blue
humidity_colors = [(255, 255, 255), (0, 255, 0)] # White to Green

def visualize_data():
    while True:
        # Read sensor data
        temp = sense.get_temperature()
        pressure = sense.get_pressure()
        humidity = sense.get_humidity()
        print(temp, pressure, humidity)

        # Map temperature and pressure to color
        temp_color = get_color(temp, 0, 40, temperature_colors)
        pressure_color = get_color(pressure, 900, 1100, pressure_colors)
        humidity_color = get_color(humidity, 0, 100, humidity_colors)

        # Temperature and Pressure Bars: The left half shows temperature
        # with a gradient from blue (cold) to red (hot). The right half
        # shows pressure with a gradient from light blue (low) to dark
        # blue (high).
        #
        # Humidity Visualization: The top row shows humidity as a binary
        # number, where each bit is represented by an LED (white for 0,
        # green for 1). Alternatively, the entire matrix can change to a
        # gradient color based on humidity.

        # Visualize temperature (left 4 columns)
        for x in range(4):
            for y in range(8):
                sense.set_pixel(x, y, temp_color)

        # Visualize pressure (right 4 columns)
        for x in range(4, 8):
            for y in range(8):
                sense.set_pixel(x, y, pressure_color)

        # Visualize humidity (use top row as binary indicator or matrix-wide color)
        humidity_binary = int(humidity)
        for x in range(8):
            bit = (humidity_binary >> (7 - x)) & 1
            color = humidity_colors[1] if bit else humidity_colors[0]
            sense.set_pixel(x, 0, color)

        time.sleep(1)

try:
    print("To quit, press Ctrl+C")
    visualize_data()

except KeyboardInterrupt:
    sense.clear()
