#!/usr/bin/env python3
# ========================================================================
# sprites_joystick.py
#
# Description: Display image sprites using the joystick to navigate.
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

import random
import time
from signal import pause

from sense_hat import SenseHat, ACTION_RELEASED
sense = SenseHat()
sense.rotation = 180
sense.low_light = True

from packages.sprites import Sprites
sprite = Sprites()

# Track current group and image indices
current_group_index = 0
current_image_index = 0

# List of groups
groups = [
    sprite.animals,
    sprite.arrows,
    sprite.dices,
    sprite.ghosts,
    sprite.misc
]

def show_sprite():
    print(current_group_index, current_image_index)
    group = groups[current_group_index]
    image = group[current_image_index]
    sense.clear()
    sense.set_pixels(image)

def pushed_up(event):
    if event.action != ACTION_RELEASED:
        print("Up")
        global current_group_index, current_image_index
        current_group_index = (current_group_index - 1) % len(groups)
        current_image_index = 0 # Reset to the first image in the new group
        show_sprite()

def pushed_down(event):
    if event.action != ACTION_RELEASED:
        print("Down")
        global current_group_index, current_image_index
        current_group_index = (current_group_index + 1) % len(groups)
        current_image_index = 0 # Reset to the first image in the new group
        show_sprite()

def pushed_left(event):
    if event.action != ACTION_RELEASED:
        print("Left")
        global current_image_index
        current_image_index = (current_image_index - 1) % len(groups[current_group_index])
        show_sprite()

def pushed_right(event):
    if event.action != ACTION_RELEASED:
        print("Right")
        global current_image_index
        current_image_index = (current_image_index + 1) % len(groups[current_group_index])
        show_sprite()

# Rotation mapping based on rotation degrees
ROTATION_MAP = {
    0: {
        'up': pushed_up,
        'down': pushed_down,
        'left': pushed_left,
        'right': pushed_right
    },
    90: {
        'up': pushed_right,
        'down': pushed_left,
        'left': pushed_up,
        'right': pushed_down
    },
    180: {
        'up': pushed_down,
        'down': pushed_up,
        'left': pushed_right,
        'right': pushed_left
    },
    270: {
        'up': pushed_left,
        'down': pushed_right,
        'left': pushed_down,
        'right': pushed_up
    }
}

# Apply the appropriate mappings based on current rotation
rotation_mapping = ROTATION_MAP[sense.rotation]

# Bind joystick directions to functions based on rotation
sense.stick.direction_up = rotation_mapping['up']
sense.stick.direction_down = rotation_mapping['down']
sense.stick.direction_left = rotation_mapping['left']
sense.stick.direction_right = rotation_mapping['right']

# Clear the screen when the middle button is pressed
sense.stick.direction_middle = sense.clear

print ("Joystick Instructions:")
print ("┌───────────┬──────────────────┐")
print ("│ Direction │ Description      │")
print ("├───────────┼──────────────────┤")
print ("│ Up        │ Prev image group │")
print ("├───────────┼──────────────────┤")
print ("│ Down      │ Next image group │")
print ("├───────────┼──────────────────┤")
print ("│ Left      │ Prev image       │")
print ("├───────────┼──────────────────┤")
print ("│ Right     │ Next image       │")
print ("├───────────┼──────────────────┤")
print ("│ Middle    │ Clear image      │")
print ("└───────────┴──────────────────┘")
print ("To quit, press Ctrl+C")

try:
    # Display the initial sprite
    show_sprite()
    pause()

except SystemExit:
    print("SystemExit")

except KeyboardInterrupt:
    print("KeyboardInterrupt")

finally:
    sense.clear()
