#!/usr/bin/env python3
# ========================================================================
# sprites_show.py
#
# Description: Display image sprites in a slideshow.
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

import random
import time
from sense_hat import SenseHat
from packages.sprites import Sprites

def show_sprite(sid):
    if getattr(sprite, sid):
        sense.clear()
        sense.set_pixels(getattr(sprite, sid))
    return

def show_animals():
    # Show a random animal
    pick = random.randint(0, len(sprite.animals) - 1)
    #print(pick)
    if sprite.animals[pick]:
        animal = sprite.animals[pick]
        sense.clear()
        sense.set_pixels(animal)
    return

def show_arrows():
    # Show a random ghost
    pick = random.randint(0, len(sprite.arrows) - 1)
    #print(pick)
    if sprite.arrows[pick]:
        arrow = sprite.arrows[pick]
        sense.clear()
        sense.set_pixels(arrow)
    return

def show_dices():
    # Show a random dice
    pick = random.randint(0, len(sprite.dices) - 1)
    #print(pick)
    if sprite.dices[pick]:
        dice = sprite.dices[pick]
        sense.clear()
        sense.set_pixels(dice)
    return

def show_ghosts():
    # Show a random ghost
    pick = random.randint(0, len(sprite.ghosts) - 1)
    #print(pick)
    if sprite.ghosts[pick]:
        ghost = sprite.ghosts[pick]
        sense.clear()
        sense.set_pixels(ghost)
    return

def show_misc():
    # Show a random sprite
    pick = random.randint(0, len(sprite.misc) - 1)
    #print(pick)
    if sprite.misc[pick]:
        sp = sprite.misc[pick]
        sense.clear()
        sense.set_pixels(sp)
    return

def show_all():
    # Show a random sprite
    pick = random.randint(0, len(sprite.all) - 1)
    #print(pick)
    if sprite.all[pick]:
        sp = sprite.all[pick]
        sense.clear()
        sense.set_pixels(sp)
    return

# ------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------

sense = SenseHat()
#sense.low_light = True
#sense.set_rotation(180)
#sense.clear()

sprite = Sprites()

try:
    print ("To quit, press Ctrl+C")

    while True:
        #show_sprite('raspberry')
        #show_animals()
        #show_arrows()
        #show_dices()
        #show_ghosts()
        #show_misc()
        show_all()
        time.sleep(3)

except SystemExit:
    print("SystemExit")

except KeyboardInterrupt:
    print("KeyboardInterrupt")

finally:
    sense.clear()
