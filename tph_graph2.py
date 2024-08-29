#!/usr/bin/env python3
# ========================================================================
# tph_graph2.py
#
# Description: Display temperature, pressure, and humidity in real-time,
#              visualized as an animated line graph.
#
# Author: Jim Ing
# Date: 2024-08-20
# ========================================================================

import time
from config import sense

# Temperature adjustment factor
temp_adjustment = 13

# Define max values for comparison
max_temp = 65       # Max temperature value
max_humidity = 100  # Max humidity value
max_pressure = 1260 # Max pressure value

def get_color_for_humidity(humidity):
    if humidity >= 60:
        return (0, 0, 255)   # Blue for wet
    elif 50 <= humidity <= 59:
        return (0, 255, 255) # Cyan
    elif 30 <= humidity <= 49:
        return (0, 255, 0)   # Green
    elif 20 <= humidity <= 29:
        return (255, 255, 0) # Yellow for dry
    else:
        return (255, 0, 0)   # Red for very dry

def get_color_for_temperature(temperature):
    if temperature >= 28:
        return (255, 0, 0)   # Red for too hot
    elif 24 <= temperature <= 27:
        return (255, 165, 0) # Red-Orange
    elif 18 <= temperature <= 23:
        return (255, 140, 0) # Orange for comfortable
    elif 13 <= temperature <= 17:
        return (0, 255, 0)   # Green for cool
    elif 8 <= temperature <= 12:
        return (0, 255, 255) # Cyan for cold
    else:
        return (0, 0, 255)   # Blue for very cold

def get_color_for_pressure(pressure):
    if pressure >= 1050:
        return (255, 0, 0) # Red for high
    elif 980 <= pressure < 1050:
        return (0, 255, 0) # Green for normal
    else:
        return (0, 0, 255) # Blue for low

def display_bar_graph(value, max_value, color, max_color, column, comparison_column):
    num_pixels = int((value / max_value) * 8)
    for i in range(8):
        if i < num_pixels:
            sense.set_pixel(column, 7 - i, color)
        else:
            sense.set_pixel(column, 7 - i, 0, 0, 0) # Clear remaining pixels

        # Draw the max value bar in the comparison column, using the max_color
        sense.set_pixel(comparison_column, 7 - i, max_color)

        # Add a slight delay to animate the bar drawing
        time.sleep(0.075)

try:
    print("To quit, press Ctrl+C")
    while True:
        # Read sensor values
        raw_temp = sense.get_temperature_from_pressure() # Use pressure sensor for temperature
        temperature = raw_temp - temp_adjustment
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()

        # Print values to console
        print(f"Temp (0-65): {temperature:.2f}°C, Pres (260-1260): {pressure:.2f} hPa, Hum (0-100): {humidity:.2f}%")

        # Get colors for the readings and max values
        temp_color = get_color_for_temperature(temperature)
        pressure_color = get_color_for_pressure(pressure)
        humidity_color = get_color_for_humidity(humidity)

        # Get colors for the max values
        max_temp_color = get_color_for_temperature(max_temp)
        max_pressure_color = get_color_for_pressure(max_pressure)
        max_humidity_color = get_color_for_humidity(max_humidity)

        # Display bar graphs on LED matrix with colorized max value comparison
        display_bar_graph(temperature, max_temp, temp_color, max_temp_color, 0, 1)        # Columns 0-1 for temperature
        display_bar_graph(pressure, max_pressure, pressure_color, max_pressure_color, 3, 4) # Columns 3-4 for pressure
        display_bar_graph(humidity, max_humidity, humidity_color, max_humidity_color, 6, 7) # Columns 6-7 for humidity

        # Refresh display
        time.sleep(30) # Update every 30 seconds
        sense.clear()
        time.sleep(3)

except KeyboardInterrupt:
    sense.clear()
