#!/usr/bin/env python3

# Define color mappings
K = [0, 0, 0]   # Black
W = [255, 255, 255]   # White

fonts = {
    ' ': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K
    ],

    'A': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, W, W, W, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K
    ],
    'B': [
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, W, W, W, K, K, K
    ],
    'C': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, K, K, K
    ],
    'D': [
        K, K, K, K, K, K, K, K,
        K, W, W, W, K, K, K, K,
        K, W, K, K, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, W, K, K, K,
        K, W, W, W, K, K, K, K
    ],
    'E': [
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, W, W, W, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K
    ],
    'F': [
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, W, W, W, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K
    ],
    'G': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, W, W, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, W, K, K
    ],
    'H': [
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, W, W, W, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K
    ],
    'I': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, W, W, K, K, K
    ],
    'J': [
        K, K, K, K, K, K, K, K,
        K, K, K, W, W, W, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, W, K, K, K,
        K, W, K, K, W, K, K, K,
        K, K, W, W, K, K, K, K
    ],
    'K': [
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, W, K, K, K,
        K, W, K, W, K, K, K, K,
        K, W, W, K, K, K, K, K,
        K, W, K, W, K, K, K, K,
        K, W, K, K, W, K, K, K,
        K, W, K, K, K, W, K, K
    ],
    'L': [
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K
    ],
    'M': [
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, W, K, W, W, K, K,
        K, W, K, W, K, W, K, K,
        K, W, K, W, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K
    ],
    'N': [
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, W, K, K, W, K, K,
        K, W, K, W, K, W, K, K,
        K, W, K, K, W, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K
    ],
    'O': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, K, K, K
    ],
    'P': [
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, W, W, W, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K
    ],
    'Q': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, W, K, W, K, K,
        K, W, K, K, W, K, K, K,
        K, K, W, W, K, W, K, K
    ],
    'R': [
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, W, W, W, K, K, K,
        K, W, K, W, K, K, K, K,
        K, W, K, K, W, K, K, K,
        K, W, K, K, K, W, K, K
    ],
    'S': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, W, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, K, W, K, K,
        K, W, W, W, W, K, K, K
    ],
    'T': [
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K
    ],
    'U': [
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, K, K, K
    ],
    'V': [
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, K, W, K, K, K,
        K, K, K, W, K, K, K, K
    ],
    'W': [
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, W, K, W, K, K,
        K, W, K, W, K, W, K, K,
        K, W, W, K, W, W, K, K,
        K, W, K, K, K, W, K, K
    ],
    'X': [
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, K, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K
    ],
    'Y': [
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K
    ],
    'Z': [
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K
    ],

    'a': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, K, K, K, K, W, K, K,
        K, K, W, W, W, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, W, K, K
    ],
    'b': [
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, W, W, K, K, K,
        K, W, W, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, K, K, K
    ],
    'c': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, K, K, K
    ],
    'd': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, K, W, K, K,
        K, K, W, W, K, W, K, K,
        K, W, K, K, W, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, W, K, K
    ],
    'e': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, W, W, W, W, K, K,
        K, W, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K
    ],
    'f': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, K, W, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K
    ],
    'g': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, W, K, K,
        K, K, K, K, K, W, K, K,
        K, K, W, W, W, K, K, K
    ],
    'h': [
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, W, W, K, K, K,
        K, W, W, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K
    ],
    'i': [
        K, K, K, K, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, W, W, K, K, K
    ],
    'j': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, W, K, K, K,
        K, W, K, K, W, K, K, K,
        K, K, W, W, K, K, K, K
    ],
    'k': [
        K, K, K, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, W, K, K, W, K, K,
        K, K, W, K, W, K, K, K,
        K, K, W, W, K, K, K, K,
        K, K, W, K, W, K, K, K,
        K, K, W, K, K, W, K, K
    ],
    'l': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, W, W, K, K, K
    ],
    'm': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, W, W, K, W, K, K, K,
        K, W, K, W, K, W, K, K,
        K, W, K, W, K, W, K, K,
        K, W, K, W, K, W, K, K,
        K, W, K, W, K, W, K, K
    ],
    'n': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, W, K, W, W, K, K, K,
        K, W, W, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K
    ],
    'o': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, K, K, K
    ],
    'p': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, W, W, W, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K
    ],
    'q': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, W, K, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, K, W, K, K
    ],
    'r': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, K, W, W, K, K,
        K, K, W, W, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, W, K, K, K, K, K
    ],
    's': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, W, K, K,
        K, W, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, K, K, K, K, W, K, K,
        K, W, W, W, W, K, K, K
    ],
    't': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, W, K, K,
        K, K, K, K, W, K, K, K
    ],
    'u': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, W, W, K, K,
        K, K, W, W, K, W, K, K
    ],
    'v': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, K, W, K, K, K,
        K, K, K, W, K, K, K, K
    ],
    'w': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, W, K, W, K, K,
        K, W, K, W, K, W, K, K,
        K, K, W, K, W, K, K, K
    ],
    'x': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, W, W, K, K, W, K, K,
        K, K, K, W, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, W, K, K, W, W, K, K
    ],
    'y': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, K, K, W, K, K,
        K, K, K, W, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, W, W, K, K, K, K, K
    ],
    'z': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, W, W, W, W, W, K, K
    ],

    '0': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, W, W, K, K,
        K, W, K, W, K, W, K, K,
        K, W, W, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, K, K, K
    ],
    '1': [
        K, K, K, K, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, W, W, K, K, K
    ],
    '2': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, W, W, W, W, W, K, K
    ],
    '3': [
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, K, K, K
    ],
    '4': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, W, K, K, K,
        K, K, W, K, W, K, K, K,
        K, W, K, K, W, K, K, K,
        K, W, W, W, W, W, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, W, K, K, K
    ],
    '5': [
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K,
        K, W, K, K, K, K, K, K,
        K, W, W, W, W, K, K, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, K, K, K
    ],
    '6': [
        K, K, K, K, K, K, K, K,
        K, K, K, W, W, K, K, K,
        K, K, W, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, W, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, K, K, K
    ],
    '7': [
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K
    ],
    '8': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, K, K, K
    ],
    '9': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, W, K, K, K, W, K, K,
        K, K, W, W, W, W, K, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, W, K, K, K,
        K, K, W, W, K, K, K, K
    ],

    '!': [
        K, K, K, K, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, W, K, K, K, K
    ],
    '#': [
        K, K, K, K, K, K, K, K,
        K, K, W, K, W, K, K, K,
        K, K, W, K, W, K, K, K,
        K, W, W, W, W, W, K, K,
        K, K, W, K, W, K, K, K,
        K, W, W, W, W, W, K, K,
        K, K, W, K, W, K, K, K,
        K, K, W, K, W, K, K, K
    ],
    '$': [
        K, K, K, K, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, W, W, W, K, K,
        K, W, K, W, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, K, K, W, K, W, K, K,
        K, W, W, W, W, K, K, K,
        K, K, K, W, K, K, K, K
    ],
    '%': [
        K, K, K, K, K, K, K, K,
        K, W, W, K, K, K, K, K,
        K, W, W, K, K, W, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, W, K, K, W, W, K, K,
        K, K, K, K, W, W, K, K
    ],
    '&': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, W, K, K, W, K, K, K,
        K, W, K, W, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, W, K, W, K, W, K, K,
        K, W, K, K, W, K, K, K,
        K, K, W, W, K, W, K, K
    ],
    '(': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, K, W, K, K, K
    ],
    ')': [
        K, K, K, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, K, K, K, K, K
    ],
    '*': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, W, K, W, K, W, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, W, K, W, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, K, K, K, K, K
    ],
    '+': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, W, W, W, W, W, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, K, K, K, K, K
    ],
    ',': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, K, K, K, K, K
    ],
    '-': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K
    ],
    '.': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, K, W, W, K, K, K, K
    ],
    '/': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K
    ],
    ':': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, K, K, K, K, K, K, K
    ],
    ';': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, K, K, K, K, K
    ],
    '<': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, K, W, K, K, K
    ],
    '=': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K,
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K
    ],
    '>': [
        K, K, K, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, W, K, K, K, K, K
    ],
    '?': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, W, K, K, K, K
    ],
    '@': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, W, K, K, K, W, K, K,
        K, K, K, K, K, W, K, K,
        K, K, W, W, K, W, K, K,
        K, W, K, W, K, W, K, K,
        K, W, K, W, K, W, K, K,
        K, K, W, W, W, K, K, K
    ],
    '[': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, W, W, W, K, K, K
    ],
    '\\': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, W, K, K, K, K, K, K,
        K, K, W, K, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, K, W, K, K,
        K, K, K, K, K, K, K, K
    ],
    ']': [
        K, K, K, K, K, K, K, K,
        K, K, W, W, W, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, K, K, W, K, K, K,
        K, K, W, W, W, K, K, K
    ],
    '_': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, W, W, W, W, W, K, K
    ],
    '|': [
        K, K, K, K, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K,
        K, K, K, W, K, K, K, K
    ],
    '~': [
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, W, W, K, W, K, K,
        K, W, K, W, W, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K,
        K, K, K, K, K, K, K, K
    ]
}

# text = "Hello, World!"

# for index, char in enumerate(text):
#     print(f"Character at index {index}: {char}")
#     print(fonts[char])
