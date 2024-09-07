#!/usr/bin/env python3
# ========================================================================
# pygame_joystick.py
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

pygame.init()

def print_at(x, y, text):
    # Move the cursor to the specified position, clear the line, and print the text
    print(f"\033[{y};{x}H\033[2K{text}")

def print_two_column(info1, info2):
    # Display two columns side by side, info1 on the left and info2 on the right
    for i, (line1, line2) in enumerate(zip(info1.split('\n'), info2.split('\n'))):
        print_at(1, 2 + i, f"{line1:<40}{line2}")

def main():
    joysticks = {}

    done = False

    while not done:
        os.system('clear')  # Clear the screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.JOYBUTTONDOWN:
                #print_at(1, 3, "Joystick button: pressed")
                if event.button == 0:
                    joystick = joysticks[event.instance_id]
                    #if joystick.rumble(0, 0.7, 500):
                        #print_at(1, 1, f"Rumble effect played on joystick {event.instance_id}")

            #if event.type == pygame.JOYBUTTONUP:
                #print_at(1, 3, "Joystick button: released")

            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                #print_at(1, 2, f"Joystick {joy.get_instance_id()} connected")

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                #print_at(1, 2, f"Joystick {event.instance_id} disconnected")

        joystick_count = pygame.joystick.get_count()
        print_at(1, 1, f"Number of joysticks: {joystick_count}")

        # Create empty strings for joystick info
        info_left = ""
        info_right = ""

        # Collect joystick data for two-column display
        for index, joystick in enumerate(joysticks.values()):
            jid = joystick.get_instance_id()

            info = f"Joystick {jid}\n"
            name = joystick.get_name()
            info += f"    Joystick name: {name}\n"

            guid = joystick.get_guid()
            info += f"    GUID: {guid}\n"

            power_level = joystick.get_power_level()
            info += f"    Power level: {power_level}\n"

            axes = joystick.get_numaxes()
            info += f"    Number of axes: {axes}\n"
            for i in range(axes):
                axis = joystick.get_axis(i)
                info += f"      Axis {i} value: \033[32m{axis:>6.3f}\033[0m\n"

            buttons = joystick.get_numbuttons()
            info += f"    Number of buttons: {buttons}\n"
            for i in range(buttons):
                button = joystick.get_button(i)
                info += f"      Button {i:>2} value: \033[36m{button}\033[0m\n"

            hats = joystick.get_numhats()
            info += f"    Number of hats: {hats}\n"
            for i in range(hats):
                hat = joystick.get_hat(i)
                info += f"      Hat {i} value: {str(hat)}\n"

            # Distribute info into left and right columns
            if index == 0:
                info_left = info
            elif index == 1:
                info_right = info

        # Print both columns side by side
        print_two_column(info_left, info_right)

        time.sleep(0.1)

if __name__ == "__main__":
    try:
        print("To quit, press Ctrl+C")
        main()
    except KeyboardInterrupt:
        pygame.quit()

'''
Number of joysticks: 2
Joystick 0                              Joystick 1
    Joystick name: USB Gamepad              Joystick name: USB Gamepad
    GUID: 03000000790000001100000010010000    GUID: 03000000790000001100000010010000
    Power level: unknown                    Power level: unknown
    Number of axes: 2                       Number of axes: 2
      Axis 0 value:  0.000                    Axis 0 value:  0.000
      Axis 1 value:  0.000                    Axis 1 value:  0.000
    Number of buttons: 10                   Number of buttons: 10
      Button  0 value: 0                      Button  0 value: 0
      Button  1 value: 0                      Button  1 value: 0
      Button  2 value: 0                      Button  2 value: 0
      Button  3 value: 0                      Button  3 value: 0
      Button  4 value: 0                      Button  4 value: 0
      Button  5 value: 0                      Button  5 value: 0
      Button  6 value: 0                      Button  6 value: 0
      Button  7 value: 0                      Button  7 value: 0
      Button  8 value: 0                      Button  8 value: 0
      Button  9 value: 0                      Button  9 value: 0
    Number of hats: 0                       Number of hats: 0

Explanation:
  \033[{color_code}m: This ANSI escape sequence sets the text color. color_code is the code for the color you want (e.g., 31 for red, 32 for green, etc.).
  \033[0m: Resets the formatting to default after printing the text to prevent coloring the rest of the terminal output.

Common Color Codes:
  30: Black
  31: Red
  32: Green
  33: Yellow
  34: Blue
  35: Magenta
  36: Cyan
  37: White (default)
'''
