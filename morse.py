#!/usr/bin/env python3
# ========================================================================
# morse.py
#
# Description: Morse Code converter and visualizer for the Sense HAT.
#
# Author: Jim Ing
# Date: 2024-08-26
# ========================================================================

import argparse
from packages.morse import Morse

# Main function
def main():
    parser = argparse.ArgumentParser(description="Morse code visualization on Sense HAT")
    parser.add_argument("mode", choices=["flash", "scroll", "stack"], help="Choose the mode: flash, scroll, or stack")
    parser.add_argument("user_input", help="The message to convert to Morse code")
    args = parser.parse_args()

    morse = Morse()

    if args.mode == "flash":
        morse.flash_morse_code(args.user_input)
    elif args.mode == "scroll":
        morse.scroll_morse_code(args.user_input)
    elif args.mode == "stack":
        morse.stack_morse_code(args.user_input)

if __name__ == "__main__":
    main()
