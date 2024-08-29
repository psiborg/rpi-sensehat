#!/usr/bin/env python3
# ========================================================================
# surface_level.py
#
# Description: A bubble level for checking flat surfaces.
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

import time
from config import sense

sense.clear()

# Define colors
MIDDLE_COLOR = (0, 255, 0)   # Green for middle
CLOSE_COLOR = (255, 255, 0)  # Yellow for close to the middle
FAR_COLOR = (255, 0, 0)      # Red for far from the middle
BACKGROUND_COLOR = (0, 0, 0) # Black for background

# Function to map pitch and roll to x and y positions on the LED matrix
def get_bubble_position(pitch, roll):
    sensitivity = 4.0  # Use 1 to 4, where higher = more responsive

    x = 3.5 + (pitch / 90) * sensitivity
    x = max(0, min(7, x))  # Ensure x is within [0,7]
    x = int(round(x))

    y = 3.5 - (roll / 90) * sensitivity
    y = max(0, min(7, y))  # Ensure y is within [0,7]
    y = int(round(y))

    return x, y

# Rotation mapping based on rotation degrees
ROTATION_MAP = {
    0: lambda x, y: (x, y),
    90: lambda x, y: (7-y, x),
    180: lambda x, y: (7-x, 7-y),
    270: lambda x, y: (y, 7-x)
}

try:
    print("To quit, press Ctrl+C")

    while True:
        # Get orientation in degrees
        orientation = sense.get_orientation_degrees()
        pitch = orientation['pitch']
        roll = orientation['roll']

        # Adjust pitch and roll to be in the range [-180, 180]
        if pitch > 180:
            pitch -= 360
        if roll > 180:
            roll -= 360

        # Get bubble position
        x, y = get_bubble_position(pitch, roll)

        # Get the current rotation of the Sense HAT
        rotation = sense.rotation

        # Apply rotation mapping to the bubble position
        x, y = ROTATION_MAP[rotation](x, y)

        # Determine color based on distance from center
        if (x == 3 or x == 4) and (y == 3 or y == 4):
            bubble_color = MIDDLE_COLOR  # Green if in the center
        elif (2 <= x <= 5) and (2 <= y <= 5):
            bubble_color = CLOSE_COLOR  # Yellow if close to the center
        else:
            bubble_color = FAR_COLOR  # Red if farther from the center

        # Prepare the pixel list
        pixels = [BACKGROUND_COLOR for _ in range(64)]
        # Set the bubble pixel with the appropriate color
        pixels[y * 8 + x] = bubble_color
        # Update the LED matrix
        sense.set_pixels(pixels)

        # Optional: Print debug information
        print(f"Pitch: {pitch:.2f}°, Roll: {roll:.2f}°, Bubble Position: (x={x}, y={y}), Color: {bubble_color}")

        # Delay for a smoother update
        time.sleep(0.25)

except KeyboardInterrupt:
    sense.clear()
