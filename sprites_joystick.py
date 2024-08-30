#!/usr/bin/env python3
# ========================================================================
# sprites_joystick.py
#
# Description: Display image sprites using the joystick to navigate.
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

from time import sleep
from config import sense
from packages.sprites import Sprites

def display_sprite(sprite):
    sense.set_pixels(sprite)

class JoystickController:
    def __init__(self, sprites):
        self.sprites = sprites
        self.current_group = 0
        self.current_index = 0

    def handle_joystick_event(self, event):
        if event.action == "pressed":
            if event.direction == "up":
                self.current_index = (self.current_index - 1) % len(self.sprites.groups[self.current_group])
            elif event.direction == "down":
                self.current_index = (self.current_index + 1) % len(self.sprites.groups[self.current_group])
            elif event.direction == "left":
                self.current_group = (self.current_group - 1) % len(self.sprites.groups)
                self.current_index = 0
            elif event.direction == "right":
                self.current_group = (self.current_group + 1) % len(self.sprites.groups)
                self.current_index = 0
            elif event.direction == "middle":
                sense.show_message(self.sprites.group_names[self.current_group])

            self.update_display()

    def update_display(self):
        sprite = self.sprites.groups[self.current_group][self.current_index]
        display_sprite(sprite)

def main():
    sprites = Sprites()
    joystick_controller = JoystickController(sprites)

    # Display initial sprite
    joystick_controller.update_display()

    try:
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

        while True:
            for event in sense.stick.get_events():
                joystick_controller.handle_joystick_event(event)
            sleep(0.1)

    except KeyboardInterrupt:
        sense.clear()

if __name__ == "__main__":
    main()
