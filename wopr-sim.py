#!/usr/bin/env python3

"""
WOPR Simulation Script

This script simulates an 80s-themed terminal with LED effects (if Sense HAT is available)
and interactive responses (using YAML-defined commands or Ollama for AI-generated responses).

Requirements:
- Python 3
- `sense_hat` library for LED matrix functionality (optional)
- `ollama` library for AI-based responses (optional)
- `PyYAML` for YAML parsing

Setup:
- On a Raspberry Pi, use:
  pip install ollama --break-system-packages
"""

import argparse
import random
import time
import math
import yaml
import shutil
import textwrap
import threading
from itertools import cycle

# ASCII art for 80s vibes
# https://patorjk.com/software/taag/#p=testall&f=Graffiti&t=WOPR

ascii_art = [
    r"""
   ________  _______  ________   _______
  /  /  /  \/       \/        \//       \
 /         /        //         //        /
//        /         //      __/        _/
\\_______/\________/\\_____/  \____/___/ # babyface-lame
    """,

    r"""
 __      __________ ____________________
/  \    /  \_____  \\______   \______   \
\   \/\/   //   |   \|     ___/|       _/
 \        //    |    \    |    |    |   \
  \__/\  / \_______  /____|    |____|_  /
       \/          \/                 \/ # Graffiti
    """,

    r"""
 _ _ _ _____ _____ _____
| | | |     |  _  | __  |
| | | |  |  |   __|    -|
|_____|_____|__|  |__|__| # Rectangles
    """,

    r"""
         ___ ._______  ._______ .______
.___    |   |: .___  \ : ____  |: __   \
:   | /\|   || :   |  ||    :  ||  \____|
|   |/  :   ||     :  ||   |___||   :  \
|   /       | \_. ___/ |___|    |   |___\
|______/|___|   :/              |___|
        :       :
        : # Stronger Than All
    """
]

try:
    from sense_hat import SenseHat
    sense = SenseHat()
    sense.rotation = 180
    sense.low_light = True
    sense_hat_available = True
except ImportError:
    sense_hat_available = False

try:
    from ollama import chat
    ollama_available = True
except ImportError:
    ollama_available = False

# Load YAML responses
def load_responses(file_path="wopr-sim_responses.yaml"):
    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Failed to parse YAML file. {e}")
        exit(1)

def led_wopr_activity(stop_event, speed_multiplier):
    """WOPR LED activity with red and amber colors."""
    if not sense_hat_available:
        return

    off = [0, 0, 0]
    red = [255, 0, 0]
    #amber = [255, 191, 0]
    amber = [255, 165, 0]
    colors = [red, amber]

    while not stop_event.is_set():
        pixels = [off] * 64
        for _ in range(random.randint(5, 15)):
            idx = random.randint(0, 63)
            pixels[idx] = random.choice(colors)

        sense.set_pixels(pixels)
        time.sleep(0.5 / speed_multiplier[0])

    sense.clear()

def led_sine_wave(stop_event, speed_multiplier):
    """Sine wave effect with red and amber."""
    if not sense_hat_available:
        return

    red = [255, 0, 0]
    amber = [255, 165, 0]
    colors = [red, amber]

    t = 0
    while not stop_event.is_set():
        pixels = [[0, 0, 0] for _ in range(64)]
        for x in range(8):
            y = int((math.sin((t + x) / 2) + 1) * 3.5)  # Sine wave mapped to LED rows
            pixels[y * 8 + x] = random.choice(colors)
        sense.set_pixels(pixels)
        t += 0.2
        time.sleep(0.1 / speed_multiplier[0])

    sense.clear()

def led_kitt_scanner(stop_event, speed_multiplier):
    """KITT scanner effect with red moving lights."""
    if not sense_hat_available:
        return

    red = [255, 0, 0]
    black = [0, 0, 0]
    position = 0
    direction = 1

    while not stop_event.is_set():
        pixels = [black for _ in range(64)]
        pixels[position] = red
        sense.set_pixels(pixels)

        position += direction
        if position == 7 or position == 0:
            direction *= -1

        time.sleep(0.1 / speed_multiplier[0])

    sense.clear()

# Process a command
def process_command(command, responses, width):
    command = command.lower()
    resp_found = False
    for entry in responses["responses"]:
        if entry["COMMAND"].lower() == command:
            resp_found = True
            return entry["RESPONSE"], entry.get("SPEED", "medium")

    if resp_found is False and ollama_available:
        oresp = chat(
            model="tinyllama",
            messages=[
                {
                    "role": "user",
                    "content": command
                }
            ]
        )
        formatted_text = textwrap.fill(oresp.message.content, width=width)
        return formatted_text, "fast"

    return "COMMAND NOT RECOGNIZED.\n", "medium"

# Simulate typing effect
def type_out(text, speed="medium"):
    speeds = {"slow": 0.1, "medium": 0.05, "fast": 0.01}
    delay = speeds.get(speed, 0.05)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# Flash backdoor screens
def flash_screens(screens):
    for screen in screens:
        lines = screens[screen].split("\n")
        for line in lines:
            print(line)
            time.sleep(0.075)
        time.sleep(0.2)
        print("\033c", end="")  # Clear screen

# Loading bar simulation
def loading_bar(text, duration=5, bar_length=30):
    print(text + ": [" + " " * bar_length + "]", end="\r")
    for i in range(1, bar_length + 1):
        time.sleep(duration / bar_length)
        print(text + f": [{'#' * i}{' ' * (bar_length - i)}]", end="\r")
    print(text + ": [" + "#" * bar_length + "] Done!\n")

# Main function
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="WOPR Simulation")
    parser.add_argument(
        "--led",
        choices=["wopr_activity", "sine_wave", "kitt_scanner"],
        default="wopr_activity",
        help="Specify the LED animation to use."
    )
    args = parser.parse_args()

    # Select the LED function based on the argument
    led_functions = {
        "wopr_activity": led_wopr_activity,
        "sine_wave": led_sine_wave,
        "kitt_scanner": led_kitt_scanner
    }
    selected_led_function = led_functions[args.led]

    responses = load_responses()
    auth = responses.get("auth", {})

    backdoor_screens = responses.get("backdoor", {})

    correct_user = auth.get("USER", "admin")
    invalid_msg = auth.get("INVALID", "ACCESS DENIED.")
    valid_msg = auth.get("VALID", "ACCESS GRANTED.")

    terminal_width = shutil.get_terminal_size().columns

    print("WOPR SIMULATION STARTED. TYPE 'quit' OR 'exit' TO TERMINATE.\n")

    print(f"Ollama: {ollama_available} | SenseHAT: {sense_hat_available} | LED: {args.led} | Width: {terminal_width}")

    print(random.choice(ascii_art))

    type_out("Initializing terminal...", "medium")
    type_out("Booting system...", "medium")
    loading_bar("Connecting")

    logged_in = False

    # LED activity thread setup
    stop_event = threading.Event()
    speed_multiplier = [1]  # Shared variable for controlling LED speed

    if sense_hat_available:
        led_thread = threading.Thread(target=selected_led_function, args=(stop_event, speed_multiplier))
        led_thread.start()

    while not logged_in:
        user_input = input("LOGON: ").strip()
        if user_input == correct_user:
            logged_in = True

            # Increase LED activity speed during command processing
            speed_multiplier[0] = 5

            flash_screens(backdoor_screens)
            type_out(valid_msg, "medium")

            # Restore idle speed after command processing
            speed_multiplier[0] = 1
        else:
            type_out(invalid_msg, "medium")

    try:
        while True:
            command = input("> ").strip()
            if command.lower() in ["q", "quit", "x", "exit"]:
                print("WOPR SIMULATION TERMINATED.\n")
                break

            # Increase LED activity speed during command processing
            speed_multiplier[0] = 3

            response, speed = process_command(command, responses, terminal_width)
            type_out(response, speed)

            # Restore idle speed after command processing
            speed_multiplier[0] = 1

    except KeyboardInterrupt:
        print("\nWOPR SIMULATION TERMINATED.\n")

    finally:
        if sense_hat_available:
            stop_event.set()
            led_thread.join()
            sense.clear()

if __name__ == "__main__":
    main()
