#!/usr/bin/env python3
# ========================================================================
# pacman.py
#
# Description: Pac-Man chomping on a dot.
#
# Author: Jim Ing
# Date: 2024-08-25
# ========================================================================

from time import sleep
from config import sense

# Define the colors
Y = (255, 255, 0)   # Yellow
F = (153, 153, 0)   # Dark Faded Yellow
D = (51, 51, 0)     # Obscure Weak Yellow
W = (255, 255, 255) # White
K = (0, 0, 0)       # Black

# Pac-Man with Mouth Open (facing right)
pacman_open = [
    K, D, F, Y, Y, Y, K, K,
    D, F, Y, Y, Y, F, K, K,
    F, Y, Y, Y, D, K, K, K,
    Y, Y, F, D, K, K, K, W,
    Y, Y, F, D, K, K, K, W,
    F, Y, Y, Y, D, K, K, K,
    D, F, Y, Y, Y, F, K, K,
    K, D, F, Y, Y, Y, K, K
]

# Pac-Man with Mouth Half-Open (facing right)
pacman_half_open = [
    K, D, F, Y, Y, Y, F, D,
    D, F, Y, Y, Y, Y, Y, F,
    F, Y, Y, Y, Y, Y, Y, F,
    Y, Y, Y, Y, Y, F, D, K,
    Y, Y, Y, F, D, K, K, W,
    Y, Y, Y, Y, Y, F, D, K,
    D, F, Y, Y, Y, Y, Y, F,
    K, D, F, Y, Y, Y, F, D,
]

# Pac-Man Closed (facing right)
pacman_closed = [
    K, D, F, Y, Y, F, D, K,
    D, Y, Y, Y, Y, Y, Y, D,
    F, Y, Y, Y, Y, Y, Y, F,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    F, Y, Y, Y, Y, Y, Y, F,
    D, Y, Y, Y, Y, Y, Y, D,
    K, D, F, Y, Y, F, D, K,
]

# Function to shift the frame to the left
def shift_left(frame):
    return frame[1:] + [K]  # Shift everything left and add black at the end

# Function to animate Pac-Man
def animate_pacman():
    frames = [pacman_open, pacman_half_open, pacman_closed, pacman_half_open]
    for _ in range(8):  # Move Pac-Man across the screen
        for frame in frames:
            sense.set_pixels(frame)
            sleep(0.2)
            frame = shift_left(frame)

# Run the animation
try:
    print ("To quit, press Ctrl+C")
    while True:
        animate_pacman()

except KeyboardInterrupt:
    sense.clear()
