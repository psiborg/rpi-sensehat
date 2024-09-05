#!/usr/bin/env python3

import os
import pygame
import time

pygame.init()

def print_at(x, y, text):
    # Move the cursor to the specified position, clear the line, and print the text
    print(f"\033[{y};{x}H\033[2K{text}")

def main():
    # This dict can be left as-is, since pygame will generate a
    # pygame.JOYDEVICEADDED event for every joystick connected
    # at the start of the program.
    joysticks = {}

    os.system('clear')  # Clear the screen

    done = False
    while not done:
        # Event processing step.
        # Possible joystick events: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN:
                print_at(1, 3, "Joystick button: pressed")
                if event.button == 0:
                    joystick = joysticks[event.instance_id]
                    if joystick.rumble(0, 0.7, 500):
                        print_at(1, 1, f"Rumble effect played on joystick {event.instance_id}")

            if event.type == pygame.JOYBUTTONUP:
                print_at(1, 3, "Joystick button: released")

            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print_at(1, 2, f"Joystick {joy.get_instance_id()} connencted")

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print_at(1, 2, f"Joystick {event.instance_id} disconnected")

        # Get count of joysticks.
        joystick_count = pygame.joystick.get_count()

        print_at(1, 4, f"Number of joysticks: {joystick_count}")

        # For each joystick:
        for joystick in joysticks.values():
            jid = joystick.get_instance_id()

            print_at(1, 5, f"  Joystick {jid}")

            # Get the name from the OS for the controller/joystick.
            name = joystick.get_name()
            print_at(1, 6, f"    Joystick name: {name}")

            guid = joystick.get_guid()
            print_at(1, 7, f"    GUID: {guid}")

            power_level = joystick.get_power_level()
            print_at(1, 8, f"    Joystick's power level: {power_level}")

            # Usually axis run in pairs, up/down for one, and left/right for
            # the other. Triggers count as axes.
            axes = joystick.get_numaxes()
            print_at(1, 9, f"    Number of axes: {axes}")

            ctr_axes = 0
            for i in range(axes):
                axis = joystick.get_axis(i)
                print_at(1, 10 + ctr_axes, f"      Axis {i} value: {axis:>6.3f}")
                ctr_axes += 1

            buttons = joystick.get_numbuttons()
            print_at(1, 12, f"    Number of buttons: {buttons}")

            ctr_buttons = 0
            for i in range(buttons):
                button = joystick.get_button(i)
                print_at(1, 13 + ctr_buttons, f"      Button {i:>2} value: {button}")
                ctr_buttons += 1

            hats = joystick.get_numhats()
            print_at(1, 23, f"    Number of hats: {hats}")

            # Hat position. All or nothing for direction, not a float like
            # get_axis(). Position is a tuple of int values (x, y).
            ctr_hats = 0
            for i in range(hats):
                hat = joystick.get_hat(i)
                print_at(1, 24 + ctr_hats, f"      Hat {i} value: {str(hat)}")
                ctr_hats += 1

        time.sleep(0.1)

if __name__ == "__main__":
    try:
        print("To quit, press Ctrl+C")

        main()

    except KeyboardInterrupt:
        #sense.clear()

        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
        pygame.quit()

'''
Joystick button: pressed/released

Number of joysticks: 1
  Joystick 0
    Joystick name: USB Gamepad
    GUID: 030...
    Joystick's power level: unknown
    Number of axes: 2
      Axis 0 value: 0.000
      Axis 1 value: 0.000
    Number of buttons: 10
      Button 0 value: 0
      Button 1 value: 0
      Button 2 value: 0
      Button 3 value: 0
      Button 4 value: 0
      Button 5 value: 0
      Button 6 value: 0
      Button 7 value: 0
      Button 8 value: 0
      Button 9 value: 0
    Number of hats: 0
'''
