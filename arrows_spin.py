#!/usr/bin/env python3
# ========================================================================
# arrows_spin.py
#
# Description:
#
# Author: Jim Ing
# Date: 2024-08-13
# ========================================================================

from sense_hat import SenseHat
import time

# Initialize Sense HAT
sense = SenseHat()

W = (255, 255, 255) # White
K = (0, 0, 0)       # Black

# Define the arrow sprites
arrow_north = [
    K, K, K, W, W, K, K, K,
    K, K, W, W, W, W, K, K,
    K, W, W, W, W, W, W, K,
    W, K, K, K, K, K, K, W,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K
]

arrow_northeast = [
    K, K, W, W, W, W, W, W,
    K, K, K, K, W, W, W, W,
    K, K, K, K, K, W, W, W,
    K, K, K, K, K, K, W, W,
    K, K, K, K, K, K, K, W,
    K, K, K, K, K, K, K, W,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K
]

arrow_east = [
    K, K, K, K, W, K, K, K,
    K, K, K, K, K, W, K, K,
    K, K, K, K, K, W, W, K,
    K, K, K, K, K, W, W, W,
    K, K, K, K, K, W, W, W,
    K, K, K, K, K, W, W, K,
    K, K, K, K, K, W, K, K,
    K, K, K, K, W, K, K, K
]

arrow_southeast = [
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, W,
    K, K, K, K, K, K, K, W,
    K, K, K, K, K, K, W, W,
    K, K, K, K, K, W, W, W,
    K, K, K, K, W, W, W, W,
    K, K, W, W, W, W, W, W
]

arrow_south = [
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    W, K, K, K, K, K, K, W,
    K, W, W, W, W, W, W, K,
    K, K, W, W, W, W, K, K,
    K, K, K, W, W, K, K, K
]

arrow_southwest = [
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    W, K, K, K, K, K, K, K,
    W, K, K, K, K, K, K, K,
    W, W, K, K, K, K, K, K,
    W, W, W, K, K, K, K, K,
    W, W, W, W, K, K, K, K,
    W, W, W, W, W, W, K, K
]

arrow_west = [
    K, K, K, W, K, K, K, K,
    K, K, W, K, K, K, K, K,
    K, W, W, K, K, K, K, K,
    W, W, W, K, K, K, K, K,
    W, W, W, K, K, K, K, K,
    K, W, W, K, K, K, K, K,
    K, K, W, K, K, K, K, K,
    K, K, K, W, K, K, K, K
]

arrow_northwest = [
    W, W, W, W, W, W, K, K,
    W, W, W, W, K, K, K, K,
    W, W, W, K, K, K, K, K,
    W, W, K, K, K, K, K, K,
    W, K, K, K, K, K, K, K,
    W, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K
]

# List of arrows for spinning animation
arrows = [
    arrow_north,
    arrow_northeast,
    arrow_east,
    arrow_southeast,
    arrow_south,
    arrow_southwest,
    arrow_west,
    arrow_northwest
]

def display_animation(sense, arrows, delay=1):
    while True:
        for arrow in arrows:
            sense.set_pixels(arrow)
            time.sleep(delay)

# Run the animation
try:
    print ("To quit, press Ctrl+C")
    display_animation(sense, arrows)

except KeyboardInterrupt:
    sense.clear()
