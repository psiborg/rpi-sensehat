#!/usr/bin/env python3
# ========================================================================
# joystick.py
#
# Description: Use the joystick to move a white dot on the LED screen.
#
# https://sense-hat.readthedocs.io/en/latest/api/#direction_up-direction_left-direction_right-direction_down-direction_middle-direction_any
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

from signal import pause
from config import sense

x = 3
y = 3

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def move_pixel(dx, dy):
    """Move the pixel, adjusted for rotation."""
    global x, y
    rotation = sense.rotation

    # Adjust movement based on the current rotation
    if rotation == 90:
        dx, dy = dy, -dx
    elif rotation == 180:
        dx, dy = -dx, -dy
    elif rotation == 270:
        dx, dy = -dy, dx

    print(f"move_pixel: ({dx}, {dy}), rotation: {rotation}")

    new_x, new_y = clamp(x + dx), clamp(y + dy)

    # Update the position
    x, y = new_x, new_y

def pushed_up(event):
    if event.action == "pressed":
        print("pushed_up")
        move_pixel(0, -1)
        refresh()

def pushed_down(event):
    if event.action == "pressed":
        print("pushed_down")
        move_pixel(0, 1)
        refresh()

def pushed_left(event):
    if event.action == "pressed":
        print("pushed_left")
        move_pixel(-1, 0)
        refresh()

def pushed_right(event):
    if event.action == "pressed":
        print("pushed_right")
        move_pixel(1, 0)
        refresh()

def refresh(event=None):
    print(f"refresh: {x}, {y}")
    sense.clear()  # comment out this line to leave a trail
    sense.set_pixel(x, y, 255, 255, 255)

print("Instructions:")
print("  - Use the mini joystick to move the white dot on the LED screen.")
print("  - To quit, press Ctrl+C")

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
#sense.stick.direction_any = refresh

try:
    refresh()
    pause()

except SystemExit:
    print("SystemExit")

except KeyboardInterrupt:
    print("KeyboardInterrupt")

finally:
    sense.clear()
