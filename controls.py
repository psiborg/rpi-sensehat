#!/usr/bin/env python3
# ========================================================================
# controls2.py
#
# Description:
#
# pip3 install pygame
#
# Author: Jim Ing
# Date: 2024-09-03
# ========================================================================

import os
import pygame
import time
from config import sense

pygame.init()

# Initialize the joystick
pygame.joystick.init()

# Check for a connected joystick
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    raise Exception("No joystick found!")

def print_at(x, y, text):
    # Move the cursor to the specified position, clear the line, and print the text
    print(f"\033[{y};{x}H\033[2K{text}")

def move_pixel(joystick, pos, rotation):
    x, y = pos
    axis_x = joystick.get_axis(0)
    axis_y = joystick.get_axis(1)

    # Deadzone to prevent unwanted movements
    if abs(axis_x) < 0.1:
        axis_x = 0
    if abs(axis_y) < 0.1:
        axis_y = 0

    # Movement based on joystick input
    dx = int(round(axis_x))
    dy = int(round(axis_y))
    print_at(1, 3, f"(dx, dy) = ({dx}, {dy})")

    # Update the position
    x = (x + dx) % 8
    y = (y + dy) % 8
    print_at(1, 4, f"(x, y) = ({x}, {y})")

    return x, y

# Starting position of the pixel
pos = [4, 4]

# Initial color of the pixel
color = [255, 0, 0]

try:
    # Clear the screen
    os.system('clear')

    # Get the current rotation
    rotation = sense.rotation
    print_at(1, 1, f"Current rotation: {rotation}°")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise KeyboardInterrupt

        # Move the pixel based on joystick input
        pos = move_pixel(joystick, pos, rotation)

        # Clear the LED matrix
        sense.clear()

        # Draw the pixel at the new position
        sense.set_pixel(pos[0], pos[1], color)

        # Delay to make the movement smoother
        time.sleep(0.1)

except KeyboardInterrupt:
    pygame.quit()
    sense.clear()
