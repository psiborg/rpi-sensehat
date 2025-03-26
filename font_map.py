#!/usr/bin/env python3

# Run the following code at https://trinket.io/sense-hat to generate the font map dictionary.

from sense_hat import SenseHat
import string
import time
from collections import OrderedDict

# Initialize SenseHat
s = SenseHat()
s.set_rotation(90)

# Define color mappings
K = [0, 0, 0]   # Black
W = [255, 255, 255]   # White

# Characters to map (printable, ascii_letters, digits, punctuation)
#characters = sorted(string.ascii_letters)
characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+,-./:;<=>?@[\]_|~"

# Font map dictionary (ordered)
font_map = OrderedDict()

for char in characters:
    print(char)
    s.show_letter(char)
    time.sleep(0.25)  # Short delay to ensure display update
    pixel_list = s.get_pixels()

    # Check if all pixels are black (i.e., character is not displayed)
    if all(pixel == [0, 0, 0] for pixel in pixel_list):
        print("Skipping", char)
        continue  # Skip this character

    # Convert pixel RGB values to W or K
    mapped_pixels = ['W' if pixel == [255, 255, 255] else 'K' for pixel in pixel_list]

    # Store in dictionary
    font_map[char] = mapped_pixels

# Print the font map dictionary
print(font_map)
