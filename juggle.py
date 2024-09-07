#!/usr/bin/env python3
# ========================================================================
# juggle.py
#
# Description: 3-ball cascade
#
# Author: Jim Ing
# Date: 2024-09-06
# ========================================================================

import time
from config import sense

class Sprites:
    def __init__(self):
        # Basic color palette
        K = (0, 0, 0)       # Black
        W = (255, 255, 255) # White

        R = (255, 0, 0)     # Red
        S = (99, 0, 0)      # Dark Faded Red
        T = (33, 0, 0)      # Obscure Weak Red

        G = (0, 255, 0)     # Green
        H = (0, 99, 0)      # Dark Faded Green
        I = (0, 33, 0)      # Obscure Weak Green

        B = (0, 0, 255)     # Blue
        C = (0, 0, 99)      # Dark Faded Blue
        D = (0, 0, 33)      # Obscure Weak Blue

        # Frame definitions:
        '''
            W|R|S|T|G|H|I|B|C|D
            [
                K, K, K, W, W, K, K, K,
                K, K, W, W, W, W, K, K,
                K, K, W, K, K, W, K, K,
                K, W, K, W, W, K, W, K,
                K, W, K, W, W, K, W, K,
                W, K, W, K, K, W, K, W,
                W, K, W, K, K, W, K, W,
                K, W, K, K, K, K, W, K
            ]
        '''

        self.frames = [
            [
                K, K, K, K, K, K, K, K,
                K, K, K, K, K, K, K, K,
                K, K, R, K, K, K, K, K,
                K, K, K, K, K, K, K, K,
                K, K, K, K, K, K, K, K,
                K, K, G, K, K, K, K, K,
                K, K, K, K, K, K, K, B,
                K, K, K, K, K, K, K, K
            ], [
                K, K, K, K, K, K, K, K,
                K, K, K, K, K, K, K, K,
                K, K, S, K, K, K, K, K,
                K, R, K, K, K, K, K, K,
                K, K, K, G, K, K, K, K,
                K, K, H, K, K, K, K, K,
                K, K, K, K, K, K, K, C,
                K, K, K, K, K, K, B, K
            ], [
                K, K, K, K, K, K, K, K,
                K, K, K, K, K, K, K, K,
                K, K, T, K, K, K, K, K,
                K, S, K, G, K, K, K, K,
                K, R, K, H, K, K, K, K,
                K, K, I, K, K, K, K, K,
                K, K, K, K, K, B, K, D,
                K, K, K, K, K, K, C, K
            ], [
                K, K, K, K, K, K, K, K,
                K, K, K, K, G, K, K, K,
                K, K, K, K, K, K, K, K,
                K, T, K, H, K, K, K, K,
                K, S, K, I, K, K, K, K,
                R, K, K, K, K, B, K, K,
                K, K, K, K, K, C, K, K,
                K, K, K, K, K, K, D, K
            ], [
                K, K, K, K, G, K, K, K,
                K, K, K, K, H, K, K, K,
                K, K, K, K, K, K, K, K,
                K, K, K, I, K, K, K, K,
                K, T, K, K, B, K, K, K,
                S, K, K, K, K, C, K, K,
                R, K, K, K, K, D, K, K,
                K, K, K, K, K, K, K, K
            ], [
                K, K, K, K, H, K, K, K,
                K, K, K, K, I, G, K, K,
                K, K, K, K, K, K, K, K,
                K, K, K, K, B, K, K, K,
                K, K, K, K, C, K, K, K,
                T, K, K, K, K, D, K, K,
                S, K, K, K, K, K, K, K,
                K, R, K, K, K, K, K, K
            ], [
                K, K, K, K, I, K, K, K,
                K, K, K, B, K, H, K, K,
                K, K, K, K, K, G, K, K,
                K, K, K, K, C, K, K, K,
                K, K, K, K, D, K, K, K,
                K, K, K, K, K, K, K, K,
                T, K, R, K, K, K, K, K,
                K, S, K, K, K, K, K, K
            ], [
                K, K, K, B, K, K, K, K,
                K, K, K, C, K, I, K, K,
                K, K, K, K, K, H, K, K,
                K, K, K, K, D, K, G, K,
                K, K, K, K, K, K, K, K,
                K, K, R, K, K, K, K, K,
                K, K, S, K, K, K, K, K,
                K, T, K, K, K, K, K, K
            ], [
                K, K, K, C, K, K, K, K,
                K, K, B, D, K, K, K, K,
                K, K, K, K, K, I, K, K,
                K, K, K, K, K, K, H, K,
                K, K, K, R, K, K, G, K,
                K, K, S, K, K, K, K, K,
                K, K, T, K, K, K, K, K,
                K, K, K, K, K, K, K, K
            ], [
                K, K, K, D, K, K, K, K,
                K, K, C, K, K, K, K, K,
                K, K, B, K, K, K, K, K,
                K, K, K, R, K, K, I, K,
                K, K, K, S, K, K, H, K,
                K, K, T, K, K, K, K, G,
                K, K, K, K, K, K, K, K,
                K, K, K, K, K, K, K, K
            ], [
                K, K, K, K, K, K, K, K,
                K, K, D, K, R, K, K, K,
                K, K, C, K, K, K, K, K,
                K, B, K, S, K, K, K, K,
                K, K, K, T, K, K, I, K,
                K, K, K, K, K, K, K, H,
                K, K, K, K, K, K, K, G,
                K, K, K, K, K, K, K, K
            ], [
                K, K, K, K, R, K, K, K,
                K, K, K, K, S, K, K, K,
                K, K, D, K, K, K, K, K,
                K, C, K, T, K, K, K, K,
                K, B, K, K, K, K, K, K,
                K, K, K, K, K, K, K, I,
                K, K, K, K, K, K, K, H,
                K, K, K, K, K, K, G, K
            ], [
                K, K, K, K, S, K, K, K,
                K, K, K, K, T, R, K, K,
                K, K, K, K, K, K, K, K,
                K, D, K, K, K, K, K, K,
                K, C, K, K, K, K, K, K,
                B, K, K, K, K, K, K, K,
                K, K, K, K, K, G, K, I,
                K, K, K, K, K, K, H, K
            ], [
                K, K, K, K, T, K, K, K,
                K, K, K, K, K, S, K, K,
                K, K, K, K, K, R, K, K,
                K, K, K, K, K, K, K, K,
                K, D, K, K, K, K, K, K,
                C, K, K, K, K, G, K, K,
                B, K, K, K, K, H, K, K,
                K, K, K, K, K, K, I, K
            ], [
                K, K, K, K, K, K, K, K,
                K, K, K, K, K, T, K, K,
                K, K, K, K, K, S, K, K,
                K, K, K, K, K, K, R, K,
                K, K, K, K, G, K, K, K,
                D, K, K, K, K, H, K, K,
                C, K, K, K, K, I, K, K,
                K, B, K, K, K, K, K, K
            ], [
                K, K, K, K, K, K, K, K,
                K, K, K, K, K, K, K, K,
                K, K, K, K, K, T, K, K,
                K, K, K, K, G, K, S, K,
                K, K, K, K, H, K, R, K,
                K, K, K, K, K, I, K, K,
                D, K, B, K, K, K, K, K,
                K, C, K, K, K, K, K, K
            ], [
                K, K, K, K, K, K, K, K,
                K, K, K, G, K, K, K, K,
                K, K, K, K, K, K, K, K,
                K, K, K, K, H, K, T, K,
                K, K, K, K, I, K, S, K,
                K, K, B, K, K, K, K, R,
                K, K, C, K, K, K, K, K,
                K, D, K, K, K, K, K, K
            ], [
                K, K, K, G, K, K, K, K,
                K, K, K, H, K, K, K, K,
                K, K, K, K, K, K, K, K,
                K, K, K, K, I, K, K, K,
                K, K, K, B, K, K, T, K,
                K, K, C, K, K, K, K, S,
                K, K, D, K, K, K, K, R,
                K, K, K, K, K, K, K, K
            ], [
                K, K, K, H, K, K, K, K,
                K, K, G, I, K, K, K, K,
                K, K, K, K, K, K, K, K,
                K, K, K, B, K, K, K, K,
                K, K, K, C, K, K, K, K,
                K, K, D, K, K, K, K, T,
                K, K, K, K, K, K, K, S,
                K, K, K, K, K, K, R, K
            ], [
                K, K, K, I, K, K, K, K,
                K, K, H, K, B, K, K, K,
                K, K, G, K, K, K, K, K,
                K, K, K, C, K, K, K, K,
                K, K, K, D, K, K, K, K,
                K, K, K, K, K, K, K, K,
                K, K, K, K, K, R, K, T,
                K, K, K, K, K, K, S, K
            ], [
                K, K, K, K, B, K, K, K,
                K, K, I, K, C, K, K, K,
                K, K, H, K, K, K, K, K,
                K, G, K, D, K, K, K, K,
                K, K, K, K, K, K, K, K,
                K, K, K, K, K, R, K, K,
                K, K, K, K, K, S, K, K,
                K, K, K, K, K, K, T, K
            ], [
                K, K, K, K, C, K, K, K,
                K, K, K, K, D, B, K, K,
                K, K, I, K, K, K, K, K,
                K, H, K, K, K, K, K, K,
                K, G, K, K, R, K, K, K,
                K, K, K, K, K, S, K, K,
                K, K, K, K, K, T, K, K,
                K, K, K, K, K, K, K, K
            ], [
                K, K, K, K, D, K, K, K,
                K, K, K, K, K, C, K, K,
                K, K, K, K, K, B, K, K,
                K, I, K, K, R, K, K, K,
                K, H, K, K, S, K, K, K,
                G, K, K, K, K, T, K, K,
                K, K, K, K, K, K, K, K,
                K, K, K, K, K, K, K, K
            ], [
                K, K, K, K, K, K, K, K,
                K, K, K, R, K, D, K, K,
                K, K, K, K, K, C, K, K,
                K, K, K, K, S, K, B, K,
                K, I, K, K, T, K, K, K,
                H, K, K, K, K, K, K, K,
                G, K, K, K, K, K, K, K,
                K, K, K, K, K, K, K, K
            ], [
                K, K, K, R, K, K, K, K,
                K, K, K, S, K, K, K, K,
                K, K, K, K, K, D, K, K,
                K, K, K, K, T, K, C, K,
                K, K, K, K, K, K, B, K,
                I, K, K, K, K, K, K, K,
                H, K, K, K, K, K, K, K,
                K, G, K, K, K, K, K, K
            ], [
                K, K, K, S, K, K, K, K,
                K, K, R, T, K, K, K, K,
                K, K, K, K, K, K, K, K,
                K, K, K, K, K, K, D, K,
                K, K, K, K, K, K, C, K,
                K, K, K, K, K, K, K, B,
                I, K, G, K, K, K, K, K,
                K, H, K, K, K, K, K, K
            ]
        ]

# Function to continuously animate through the frames
def animate(sprites, delay=0.1):
    while True:
        for frame in sprites.frames:
            sense.set_pixels(frame)  # Set the current frame to the LED matrix
            time.sleep(delay)        # Delay before showing the next frame

# Create an instance of Sprites class
sprites = Sprites()

# Start the animation
try:
    animate(sprites, delay=0.2)  # Adjust delay for animation speed
except KeyboardInterrupt:
    sense.clear()
