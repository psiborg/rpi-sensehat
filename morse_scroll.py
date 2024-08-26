#!/usr/bin/env python3
# ========================================================================
# morse_scroll.py
#
# Description: Morse Code Scroller.
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

# Scroll Morse code on Sense HAT
def scroll_morse_code(message):
    morse_code = text_to_morse(message)

    # Output the Morse code to the console
    print(f"Message: {message}")
    print(f"Morse Code: {morse_code}\n")

    # Scroll each symbol on the LED matrix
    for symbol in morse_code:
        if symbol == '.':
            scroll_dot()
        elif symbol == '-':
            scroll_dash()
        elif symbol == ' ':
            time.sleep(0.6)  # Longer pause between letters
        sense.clear()
        time.sleep(0.3)  # Short pause between symbols

def scroll_dot():
    # Scroll a 2x2 pixel square dot across the matrix
    for start_x in range(-2, 8):
        sense.clear()
        for x in range(start_x, start_x + 2):
            for y in range(3, 5):
                if 0 <= x < 8 and 0 <= y < 8:
                    sense.set_pixel(x, y, dot_color)
        time.sleep(0.1)

def scroll_dash():
    # Scroll a 2-pixel high and 6-pixel wide horizontal line across the matrix
    for start_x in range(-6, 8):
        sense.clear()
        for x in range(start_x, start_x + 6):
            for y in range(3, 5):  # 2 pixels high
                if 0 <= x < 8 and 0 <= y < 8:
                    sense.set_pixel(x, y, dash_color)
        time.sleep(0.1)

# Main function
def main():
    try:
        while True:
            user_input = input("Enter a message to convert to Morse code: ")
            scroll_morse_code(user_input)
    except KeyboardInterrupt:
        sense.clear()

if __name__ == "__main__":
    main()
