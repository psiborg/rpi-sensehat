#!/usr/bin/env python3
# ========================================================================
# kitt_voice_live.py
#
# Description: KITT's voice box for mic input
#
# Author: Jim Ing
# Date: 2024-08-13
# ========================================================================

# Install Required Libraries:
# pip install pyaudio numpy

import numpy as np
import pyaudio
from sense_hat import SenseHat
from time import sleep

# Initialize Sense HAT
sense = SenseHat()

# Define colors with varying brightness
red_high = [255, 0, 0]
red_medium = [150, 0, 0]
red_low = [75, 0, 0]
off = [0, 0, 0]

# PyAudio configuration
CHUNK = 1024  # Number of audio samples per frame
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Mono audio
RATE = 44100  # Sampling rate (samples per second)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open microphone stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

def get_audio_level():
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    peak = np.abs(data).max()
    return peak

def draw_voice_box(height):
    # Initialize all LEDs to off
    pixels = [off] * 64

    if height > 0:
        for col in [3, 4]:
            for row in range(3 - height//2, 4 + height//2):
                pixels[row*8 + col] = red_high if row in [3, 4] else red_medium

        for col in [1, 2, 5, 6]:
            for row in range(4 - height//2, 3 + height//2):
                pixels[row*8 + col] = red_low

    # Update the LED matrix
    sense.set_pixels(pixels)

try:
    while True:
        # Get the audio level from the microphone
        level = get_audio_level()

        # Normalize the level to a height between 0 and 6
        height = min(6, max(0, int(level / 5000)))  # Adjust the divisor based on sensitivity

        draw_voice_box(height)

        # Short delay to control the update rate
        sleep(0.05)

except KeyboardInterrupt:
    # Clean up on exit
    stream.stop_stream()
    stream.close()
    p.terminate()
    sense.clear()
