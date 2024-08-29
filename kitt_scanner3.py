#!/usr/bin/env python3
# ========================================================================
# kitt_scanner3.py
#
# Description: KITT's scanner in selectable colors.
#
# Author: Jim Ing
# Date: 2024-08-16
# ========================================================================

import time
from config import sense

sense.clear()

# Define colors
colors = {
    1: ("red", (255, 0, 0)),
    2: ("orange", (255, 165, 0)),
    3: ("yellow", (255, 255, 0)),
    4: ("green", (0, 255, 0)),
    5: ("blue", (0, 0, 255)),
    6: ("violet", (238, 130, 238)),
    7: ("pink", (255, 192, 203)),
    8: ("white", (255, 255, 255))
}

# Prompt user to select a color by number
print("Select a color for the scanner effect:")
for number, (color_name, _) in colors.items():
    print(f"{number}: {color_name}")

try:
    selected_number = int(input("Enter the number corresponding to your color choice: "))
except ValueError:
    selected_number = 0

# Ensure valid color choice
if selected_number in colors:
    selected_color_name, main_color = colors[selected_number]
else:
    print("Invalid selection. Defaulting to red.")
    selected_color_name, main_color = colors[1]

print(f"You selected {selected_color_name}.")

# Dimmed versions of the selected color
dim_color1 = tuple(int(c / 2) for c in main_color) # Less bright
dim_color2 = tuple(int(c / 4) for c in main_color) # Even dimmer
off = (0, 0, 0)  # Turn off pixel

def kitt_scanner_with_trail():
    while True:
        # Move from left to right
        for x in range(8):
            sense.clear()
            sense.set_pixel(x, 3, main_color)
            sense.set_pixel(x, 4, main_color)
            if x > 0:
                sense.set_pixel(x-1, 3, dim_color1)
                sense.set_pixel(x-1, 4, dim_color1)
            if x > 1:
                sense.set_pixel(x-2, 3, dim_color2)
                sense.set_pixel(x-2, 4, dim_color2)
            time.sleep(0.1)

        # Move from right to left
        for x in range(6, -1, -1):
            sense.clear()
            sense.set_pixel(x, 3, main_color)
            sense.set_pixel(x, 4, main_color)
            if x < 7:
                sense.set_pixel(x+1, 3, dim_color1)
                sense.set_pixel(x+1, 4, dim_color1)
            if x < 6:
                sense.set_pixel(x+2, 3, dim_color2)
                sense.set_pixel(x+2, 4, dim_color2)
            time.sleep(0.1)

try:
    print("To quit, press Ctrl+C")
    kitt_scanner_with_trail()

except KeyboardInterrupt:
    sense.clear()
