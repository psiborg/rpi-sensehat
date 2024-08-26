# ========================================================================
# morse.py
#
# Description: Morse Code class for the Sense HAT.
#
# Author: Jim Ing
# Date: 2024-08-26
# ========================================================================

from sense_hat import SenseHat
import time

class Morse:
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

    dot_color = [0, 255, 0]  # Green for dots
    dash_color = [255, 0, 0]  # Red for dashes
    bg_color = [0, 0, 0]  # Background color (black)

    def __init__(self):
        self.sense = SenseHat()

    def text_to_morse(self, message):
        morse_code = ""
        for char in message.upper():
            if char in self.MORSE_CODE_DICT:
                morse_code += self.MORSE_CODE_DICT[char] + " "
        return morse_code.strip()

    # Flash

    def flash_dot(self):
        center_x, center_y = 3, 3
        for x in range(center_x, center_x + 2):
            for y in range(center_y, center_y + 2):
                self.sense.set_pixel(x, y, self.dot_color)
        time.sleep(0.3)
        self.sense.clear()

    def flash_dash(self):
        start_x, start_y = 1, 3
        for x in range(start_x, start_x + 6):
            for y in range(start_y, start_y + 2):
                self.sense.set_pixel(x, y, self.dash_color)
        time.sleep(0.9)
        self.sense.clear()

    def flash_morse_code(self, message):
        morse_code = self.text_to_morse(message)
        print(f"Message: {message}")
        print(f"Morse Code: {morse_code}\n")
        for symbol in morse_code:
            if symbol == '.':
                self.flash_dot()
            elif symbol == '-':
                self.flash_dash()
            elif symbol == ' ':
                time.sleep(0.6)
            self.sense.clear()
            time.sleep(0.3)

    # Scroll

    def scroll_dot(self):
        for start_x in range(-2, 8):
            self.sense.clear()
            for x in range(start_x, start_x + 2):
                for y in range(3, 5):
                    if 0 <= x < 8 and 0 <= y < 8:
                        self.sense.set_pixel(x, y, self.dot_color)
            time.sleep(0.1)

    def scroll_dash(self):
        for start_x in range(-6, 8):
            self.sense.clear()
            for x in range(start_x, start_x + 6):
                for y in range(3, 5):
                    if 0 <= x < 8 and 0 <= y < 8:
                        self.sense.set_pixel(x, y, self.dash_color)
            time.sleep(0.1)

    def scroll_morse_code(self, message):
        morse_code = self.text_to_morse(message)
        print(f"Message: {message}")
        print(f"Morse Code: {morse_code}\n")
        for symbol in morse_code:
            if symbol == '.':
                self.scroll_dot()
            elif symbol == '-':
                self.scroll_dash()
            elif symbol == ' ':
                time.sleep(0.6)
            self.sense.clear()
            time.sleep(0.3)

    # Stack

    def stack_dot(self, row):
        for x in range(3, 5):
            self.sense.set_pixel(x, row, self.dot_color)

    def stack_dash(self, row):
        for x in range(1, 7):
            self.sense.set_pixel(x, row, self.dash_color)

    def stack_morse_code(self, message):
        morse_code = self.text_to_morse(message)
        print(f"Message: {message}")
        print(f"Morse Code: {morse_code}\n")
        row = 0
        for symbol in morse_code:
            if row == 8:
                self.sense.clear()
                row = 0
            if symbol == '.':
                self.stack_dot(row)
            elif symbol == '-':
                self.stack_dash(row)
            row += 1
            time.sleep(0.5)
        time.sleep(0.75)
        self.sense.clear()
