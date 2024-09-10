#!/usr/bin/env python3
# ========================================================================
# markov_pixelart1.py
#
# Description: Create random pixel animations that evolve over time based
#              on state transitions.
#
# Author: Jim Ing
# Date: 2024-09-09
# ========================================================================

import random
import time
from config import sense

# Define states (Red, Green, Blue, Off)
R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)
K = (0, 0, 0)

states = [R, G, B, K]  # RGB values

# Define transition probabilities for each state
transition_probs = {
    R: [(0.5, R), (0.2, G), (0.2, B), (0.1, K)],
    G: [(0.4, R), (0.4, G), (0.1, B), (0.1, K)],
    B: [(0.3, R), (0.3, G), (0.3, B), (0.1, K)],
    K: [(0.2, R), (0.2, G), (0.2, B), (0.4, K)]
}

# Function to randomly choose next state based on probabilities
def next_state(current_color):
    rand = random.random()
    cumulative_prob = 0
    for prob, state in transition_probs[current_color]:
        cumulative_prob += prob
        if rand < cumulative_prob:
            return state
    return current_color

# Initialize random starting colors
matrix = [random.choice(states) for _ in range(64)]

# Function to update the matrix colors based on the Markov chain
def update_matrix():
    global matrix
    for i in range(64):
        matrix[i] = next_state(matrix[i])
    sense.set_pixels(matrix)

try:
    # Main loop: Continuously update the display
    while True:
        update_matrix()
        time.sleep(0.5)

except KeyboardInterrupt:
    sense.clear()
