#!/usr/bin/env python3
# ========================================================================
# sinusoidal.py
#
# Description:
#
# Author: Jim Ing
# Date: 2024-09-06
# ========================================================================

import time
import math
from config import sense

sense.clear()

# Define colors based on height
colors = [
    (255, 0, 0),    # Red for heights 0-1
    (255, 255, 0),  # Yellow for heights 2-3
    (0, 255, 0),    # Green for heights 4-5
    (0, 0, 255)     # Blue for heights 6-7
]

# Animation parameters
speed = 0.1
wave_amplitude = 3  # Amplitude of the wave (vertical height)
wave_frequency = 0.5  # Controls the frequency of the wave
offset = 0  # Starting phase offset

def get_color_for_height(y):
    """Return the appropriate color based on the pixel height."""
    if y <= 1:
        return colors[0]  # Red
    elif y <= 3:
        return colors[1]  # Yellow
    elif y <= 5:
        return colors[2]  # Green
    else:
        return colors[3]  # Blue

def draw_wave():
    """Draw a sinusoidal wave on the Sense HAT matrix with colors based on height."""
    sense.clear()  # Clear the display
    for x in range(8):
        # Calculate the y position using a sine wave formula
        y = int(3.5 + wave_amplitude * math.sin(x * wave_frequency + offset))
        # Get the color for the current y-coordinate
        color = get_color_for_height(y)
        # Set the pixel for the wave with the appropriate color
        sense.set_pixel(x, y, color)

try:
    while True:
        draw_wave()  # Draw the current frame of the wave
        offset += 0.3  # Move the wave to the left by shifting the phase
        time.sleep(speed)  # Control the speed of the animation

except KeyboardInterrupt:
    sense.clear()  # Clear the LED matrix on exit
