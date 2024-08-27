# Morse Code Visualization on Sense HAT

This Python script allows you to visualize Morse code on the Raspberry Pi Sense HAT's LED matrix in three different modes: flash, scroll, and stack. The script converts a user-provided message into Morse code and displays it using colored dots and dashes on the LED matrix.

## Background

Morse code is a method of encoding text characters as sequences of dots and dashes (or short and long signals). It was developed in the early 1830s and 1840s by Samuel Morse and Alfred Vail as a means of long-distance communication using telegraph systems. Morse code can be transmitted in various forms, such as sound (beeps), light (flashes), or visual signals (dots and dashes), making it versatile and effective for different communication mediums.

### Importance

Morse code played a crucial role in the development of long-distance communication before modern technology. It is valued for its simplicity and reliability, particularly in situations where other communication methods might fail. Even with today's advanced communication systems, Morse code remains a vital skill for certain specialized fields, including emergency signaling and aviation.

### Components of Morse Code

1. Dots and Dashes:

    - Dot (.): Represents a short signal, often referred to as a "dit."
    - Dash (-): Represents a longer signal, often referred to as a "dah."

2. Letter Spacing:

    - A gap equivalent to three dots is used between letters within a word.

3. Word Spacing:

    - A gap equivalent to seven dots is used between words.

### Structure of Morse Code

- Alphabet: Each letter in the alphabet is represented by a unique sequence of dots and dashes. For example:

    - A: .-
    - B: -...
    - C: -.-.
    - Z: --..

- Numbers: Numbers are also represented in Morse code:

    - 1: .----
    - 2: ..---
    - 0: -----

- Punctuation: Common punctuation marks have corresponding Morse code representations:

    - Period (.): .-.-.-
    - Comma (,): --..--
    - Question Mark (?): ..--..

## Features

- Flash Mode: Morse code is displayed by flashing the dots and dashes in place on the LED matrix.
- Scroll Mode: Morse code is displayed by scrolling the dots and dashes across the LED matrix from left to right.
- Stack Mode: Morse code is displayed by stacking the dots and dashes from top to bottom on the LED matrix.

## Morse Code Representation

- Dots: Represented by a green 2x2 square of pixels.
- Dashes: Represented by a red 6x2 rectangle of pixels.
- Background: Black (unlit pixels).

## Requirements

- Raspberry Pi with Sense HAT
- Python 3.x
- sense_hat library (can be installed via pip: pip install sense-hat)


## Installation

1. Ensure that the Sense HAT is correctly connected to your Raspberry Pi.
2. Install the sense_hat library:

    ```sh
    pip install sense-hat
    ```

3. Clone or download this script to your Raspberry Pi.

## Usage

Run the script from the command line, providing the desired mode and message as arguments.

### Command Line Arguments

- mode: The mode of visualization (flash, scroll, stack).
- user_input: The message you want to convert to Morse code.

### Example Commands

- Flash Mode:

    ```sh
    python morse_code.py flash "Hello World"
    ```

- Scroll Mode:

    ```sh
    python morse_code.py scroll "SOS"
    ```

- Stack Mode:

    ```sh
    python morse_code.py stack "123"
    ```

### Script Output

The script will print the original message and its corresponding Morse code in the console before visualizing it on the LED matrix.

## Notes

- The timing for dots, dashes, and pauses between symbols follows the standard Morse code timing.
- The Sense HAT LED matrix is 8x8, so the script adapts the visualization to fit within this constraint.
- Ensure the message is concise, as longer messages may result in overlapping or truncated visualizations in stack mode.

## License

This project is open-source and available for use under the MIT License.
