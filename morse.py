#!/usr/bin/env python3
# ========================================================================
# morse.py
#
# Description: Morse Code Generator.
#
# Author: Jim Ing
# Date: 2024-08-26
# ========================================================================

from sense_hat import SenseHat
import time

sense = SenseHat()

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': ' '
}

# Define colors
dot_color = [0, 255, 0]  # Green for dots
dash_color = [255, 0, 0]  # Red for dashes
bg_color = [0, 0, 0]  # Background color (black)

# Convert text to Morse code
def text_to_morse(message):
    morse_code = ""
    for char in message.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
    return morse_code.strip()

# Flash Morse code on Sense HAT
def flash_morse_code(message):
    morse_code = text_to_morse(message)

    # Output the Morse code to the console
    print(f"Message: {message}")
    print(f"Morse Code: {morse_code}\n")

    # Flash each symbol on the LED matrix
    for symbol in morse_code:
        if symbol == '.':
            flash_dot()
        elif symbol == '-':
            flash_dash()
        elif symbol == ' ':
            time.sleep(0.6)  # Longer pause between letters
        sense.clear()
        time.sleep(0.3)  # Short pause between symbols

def flash_dot():
    # Light up a 2x2 pixel square centered on the matrix
    center_x, center_y = 3, 3
    for x in range(center_x, center_x + 2):
        for y in range(center_y, center_y + 2):
            sense.set_pixel(x, y, dot_color)
    time.sleep(0.3)  # Duration of the dot flash
    sense.clear()

def flash_dash():
    # Light up a 2-pixel high and 6-pixel wide horizontal line, shifted down and right
    start_x = 1
    start_y = 3
    for x in range(start_x, start_x + 6):
        for y in range(start_y, start_y + 2):  # 2 pixels high
            sense.set_pixel(x, y, dash_color)
    time.sleep(0.9)  # Duration of the dash flash
    sense.clear()

# Main function
def main():
    try:
        while True:
            user_input = input("Enter a message to convert to Morse code: ")
            flash_morse_code(user_input)
    except KeyboardInterrupt:
        sense.clear()

if __name__ == "__main__":
    main()
