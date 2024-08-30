#!/usr/bin/env python3
# ========================================================================
# font_scroller.py
#
# Description: Custom font scroller that scrolls vertically.
#
# ./font_scroller.py "DECAF" "0,0,255" "255,255,0" 0.05 2
#
# Author: Jim Ing
# Date: 2024-08-30
# ========================================================================

import sys
import time
from config import sense
from packages.font import Font

# Initialize Sense HAT and Font class
font = Font()

# Function to parse command line arguments
def parse_args():
    text = "ABCDEF"
    bg_color = (0, 0, 0)  # Black
    text_color = (255, 255, 255)  # White
    scroll_speed = 0.1
    gap = 1

    if len(sys.argv) > 1:
        text = sys.argv[1]
    if len(sys.argv) > 2:
        bg_color = tuple(map(int, sys.argv[2].split(',')))
    if len(sys.argv) > 3:
        text_color = tuple(map(int, sys.argv[3].split(',')))
    if len(sys.argv) > 4:
        scroll_speed = float(sys.argv[4])
    if len(sys.argv) > 5:
        gap = int(sys.argv[5])

    return text, bg_color, text_color, scroll_speed, gap

# Function to combine characters into one long image
def create_message_image(text, text_color, bg_color, gap):
    message_image = []
    for char in text:
        char_image = font.char_map.get(char.upper(), [bg_color] * 64)
        colored_char_image = [text_color if pixel == (255, 255, 255) else bg_color for pixel in char_image]
        message_image.extend(colored_char_image)
        # Add gap between characters
        message_image.extend([bg_color] * 8 * gap)
    return message_image

# Function to scroll the message across the LED matrix
def scroll_message(message_image, scroll_speed):
    for i in range(len(message_image) // 8 - 7):
        frame = message_image[i * 8:(i + 8) * 8]
        sense.set_pixels(frame)
        time.sleep(scroll_speed)
    sense.clear()

# Main function
def main():
    text, bg_color, text_color, scroll_speed, gap = parse_args()
    message_image = create_message_image(text, text_color, bg_color, gap)
    scroll_message(message_image, scroll_speed)

if __name__ == "__main__":
    main()
