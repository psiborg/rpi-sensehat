#!/usr/bin/env python3
# ========================================================================
# markov_pixelart2.py
#
# Description: Create a Markov Chain pixel art animation with gradients.
#
# Author: Jim Ing
# Date: 2024-09-09
# ========================================================================

import random
import time
from config import sense

# Define gradient states as RGB values (ranging from dark to light)
gradient_red = [(50, 0, 0), (100, 0, 0), (150, 0, 0), (200, 0, 0), (255, 0, 0)]
gradient_green = [(0, 50, 0), (0, 100, 0), (0, 150, 0), (0, 200, 0), (0, 255, 0)]
gradient_blue = [(0, 0, 50), (0, 0, 100), (0, 0, 150), (0, 0, 200), (0, 0, 255)]

# Combine all gradient states
states = gradient_red + gradient_green + gradient_blue

# Define transition probabilities for each state
def transition_probs(current_color):
    idx = states.index(current_color)
    # Increase probability of transitioning to neighboring colors for smoothness
    if idx == 0:
        return [(0.7, states[0]), (0.3, states[1])]  # Edge case for the darkest color
    elif idx == len(states) - 1:
        return [(0.7, states[-1]), (0.3, states[-2])]  # Edge case for the lightest color
    else:
        return [(0.5, states[idx]), (0.25, states[idx - 1]), (0.25, states[idx + 1])]

# Function to randomly choose next state based on probabilities
def next_state(current_color):
    probs = transition_probs(current_color)
    rand = random.random()
    cumulative_prob = 0
    for prob, state in probs:
        cumulative_prob += prob
        if rand < cumulative_prob:
            return state
    return current_color

# Initialize random starting colors
matrix = [random.choice(states) for _ in range(64)]

# Function to update the matrix colors based on the Markov chain with gradients
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
