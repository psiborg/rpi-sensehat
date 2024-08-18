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
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
from sprites import Sprites

sense = SenseHat()
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

# Bind joystick directions to functions
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
#sense.stick.direction_any = show_sprite

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
