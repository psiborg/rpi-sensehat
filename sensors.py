#!/usr/bin/env python3
# ========================================================================
# sensors.py
#
# Description: Select temperature, pressure, or humidity with the
#              joystick to visualize the current sensor values on the LED.
#
# https://trinket.io/python/ee99673139
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

import time
from config import sense

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

def show_t():
    sense.show_letter("T", back_colour=red)
    time.sleep(.5)

def show_p():
    sense.show_letter("P", back_colour=green)
    time.sleep(.5)

def show_h():
    sense.show_letter("H", back_colour=blue)
    time.sleep(.5)

def update_screen(mode, show_letter=False):
    if mode == "temp":
        if show_letter:
            show_t()
        temp = sense.temp
        temp_value = temp / 2.5 + 16
        pixels = [red if i < temp_value else white for i in range(64)]

    elif mode == "pressure":
        if show_letter:
            show_p()
        pressure = sense.pressure
        pressure_value = pressure / 20
        pixels = [green if i < pressure_value else white for i in range(64)]

    elif mode == "humidity":
        if show_letter:
            show_h()
        humidity = sense.humidity
        humidity_value = 64 * humidity / 100
        pixels = [blue if i < humidity_value else white for i in range(64)]

    sense.set_pixels(pixels)

# Rotation mapping based on rotation degrees
ROTATION_MAP = {
    0: {
        'left': 'left',
        'right': 'right',
        'up': 'up',
        'down': 'down'
    },
    90: {
        'left': 'up',
        'right': 'down',
        'up': 'right',
        'down': 'left'
    },
    180: {
        'left': 'right',
        'right': 'left',
        'up': 'down',
        'down': 'up'
    },
    270: {
        'left': 'down',
        'right': 'up',
        'up': 'left',
        'down': 'right'
    }
}

show_t()
show_p()
show_h()

update_screen("temp")

index = 0
sensors = ["temp", "pressure", "humidity"]

try:
    print("Instructions:")
    print("  - To switch between sensors, move the joystick left or right.")
    print("  - To quit, press Ctrl+C")

    while True:
        selection = False
        events = sense.stick.get_events()

        # Get the current rotation of the Sense HAT
        rotation = sense.rotation

        # Apply the appropriate mappings based on current rotation
        rotation_mapping = ROTATION_MAP[rotation]

        for event in events:
            # Skip releases
            if event.action != "released":
                # Use mapped direction based on rotation
                mapped_direction = rotation_mapping[event.direction]

                if mapped_direction == "left":
                    index -= 1
                    selection = True
                elif mapped_direction == "right":
                    index += 1
                    selection = True

                if selection:
                    current_mode = sensors[index % 3]
                    update_screen(current_mode, show_letter=True)

        if not selection:
            current_mode = sensors[index % 3]
            update_screen(current_mode)

finally:
    sense.clear()
