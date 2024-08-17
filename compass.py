#!/usr/bin/env python3
# ========================================================================
# compass.py
#
# Description:
#
# Author: Jim Ing
# Date: 2024-08-13
# ========================================================================

from sense_hat import SenseHat
import time

sense = SenseHat()

# Define colors
W = (255, 255, 255)  # White
K = (0, 0, 0)        # Black

# Define the arrow sprites
arrow_sprites = {
    'N': [
        K, K, K, W, W, K, K, K,
        K, K, W, W, W, W, K, K,
        K, W, W, W, W, W, W, K,
        W, K, K, K, K, K, K, W,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K
    ],
    'NE': [
        K, K, W, W, W, W, W, W,
        K, K, K, K, W, W, W, W,
        K, K, K, K, K, W, W, W,
        K, K, K, K, K, K, W, W,
        K, K, K, K, K, K, K, W,
        K, K, K, K, K, K, K, W,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K
    ],
    'E': [
        K, K, K, K, W, K, K, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, K, W, W, K,
        K, K, K, K, K, W, W, W,
        K, K, K, K, K, W, W, W,
        K, K, K, K, K, W, W, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, W, K, K, K
    ],
    'SE': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, W,
        K, K, K, K, K, K, K, W,
        K, K, K, K, K, K, W, W,
        K, K, K, K, K, W, W, W,
        K, K, K, K, W, W, W, W,
        K, K, W, W, W, W, W, W
    ],
    'S': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        W, K, K, K, K, K, K, W,
        K, W, W, W, W, W, W, K,
        K, K, W, W, W, W, K, K,
        K, K, K, W, W, K, K, K
    ],
    'SW': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        W, K, K, K, K, K, K, K,
        W, K, K, K, K, K, K, K,
        W, W, K, K, K, K, K, K,
        W, W, W, K, K, K, K, K,
        W, W, W, W, K, K, K, K,
        W, W, W, W, W, W, K, K
    ],
    'W': [
        K, K, K, W, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, W, W, K, K, K, K, K,
        W, W, W, K, K, K, K, K,
        W, W, W, K, K, K, K, K,
        K, W, W, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, K, W, K, K, K, K
    ],
    'NW': [
        W, W, W, W, W, W, K, K,
        W, W, W, W, K, K, K, K,
        W, W, W, K, K, K, K, K,
        W, W, K, K, K, K, K, K,
        W, K, K, K, K, K, K, K,
        W, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K
    ]
}

def display_arrow(arrow):
    matrix = [arrow[i:i+8] for i in range(0, 64, 8)]
    sense.set_pixels([pixel for row in matrix for pixel in row])

def get_direction():
    heading = sense.get_compass()
    print(heading)

    if heading >= 337.5 or heading < 22.5:
        return 'N'
    elif 22.5 <= heading < 67.5:
        return 'NE'
    elif 67.5 <= heading < 112.5:
        return 'E'
    elif 112.5 <= heading < 157.5:
        return 'SE'
    elif 157.5 <= heading < 202.5:
        return 'S'
    elif 202.5 <= heading < 247.5:
        return 'SW'
    elif 247.5 <= heading < 292.5:
        return 'W'
    elif 292.5 <= heading < 337.5:
        return 'NW'

def main():
    while True:
        direction = get_direction()
        display_arrow(arrow_sprites[direction])
        time.sleep(1)  # Update display every 1 second

if __name__ == "__main__":
    try:
        print ("To quit, press Ctrl+C")
        main()

    except KeyboardInterrupt:
        sense.clear()
