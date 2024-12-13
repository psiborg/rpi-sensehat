#!/usr/bin/env python3
# ========================================================================
# spectrum_analyzer.py
#
# Description: A real-time spectrum analyzer that displays audio
#              frequency bands as vibrant, color-coded bars on the LED
#              matrix. It plays a specified MP3 file while dynamically
#              visualizing the song's frequency spectrum using Fast
#              Fourier Transform (FFT).
#
# sudo apt-get install ffmpeg
# pip install pydub numpy
#
# Author: Jim Ing
# Date: 2024-12-13
# ========================================================================

import argparse
import numpy as np
import os
import threading
import time
from pydub import AudioSegment
from pydub.playback import play
from config import sense

# Define colors
colors = [
    (255, 0, 0),   # Red
    (255, 128, 0), # Orange
    (255, 255, 0), # Yellow
    (0, 255, 0),   # Green
    (0, 255, 255), # Cyan
    (0, 0, 255),   # Blue
    (128, 0, 255), # Purple
    (255, 0, 255)  # Magenta
]

# Playback control flag
is_playing = True

# Function to play audio
def play_audio(file):
    global is_playing
    song = AudioSegment.from_file(file)
    play(song)
    is_playing = False  # Set flag to False when playback finishes

# Function to map amplitude to LED bar height
def amplitude_to_height(amplitudes, max_height=8):
    max_amp = max(amplitudes) if max(amplitudes) > 0 else 1
    return [int((amp / max_amp) * max_height) for amp in amplitudes]

# Function to update the LED matrix
def update_display(heights):
    sense.clear()
    for x, height in enumerate(heights):
        for y in range(8):
            if y < height:
                sense.set_pixel(x, 7 - y, colors[x])
            else:
                sense.set_pixel(x, 7 - y, (0, 0, 0))

# Main animation loop
def spectrum_analyzer(audio_file):
    global is_playing
    # Load audio file
    song = AudioSegment.from_file(audio_file)
    samples = np.array(song.get_array_of_samples())
    sample_rate = song.frame_rate
    chunk_size = int(sample_rate / 30)  # ~30 updates per second

    # Split into chunks and analyze
    for start in range(0, len(samples), chunk_size):
        if not is_playing:  # Stop if playback has ended
            sense.clear()
            break
        chunk = samples[start:start + chunk_size]
        if len(chunk) < chunk_size:
            break
        # Perform FFT to get frequency data
        fft_data = np.fft.fft(chunk)
        amplitudes = np.abs(fft_data[:len(fft_data) // 2])
        freq_bands = np.array_split(amplitudes, 8)
        avg_amplitudes = [np.mean(band) for band in freq_bands]

        # Convert amplitudes to LED heights
        heights = amplitude_to_height(avg_amplitudes)
        update_display(heights)
        time.sleep(1 / 30)  # Maintain ~30 FPS

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Spectrum Analyzer for Sense HAT.")
parser.add_argument(
    "audio_file",
    type=str,
    help="Path to the MP3 file to analyze."
)
args = parser.parse_args()

try:
    # Run the audio playback and analyzer in parallel
    threading.Thread(target=play_audio, args=(args.audio_file,)).start()
    spectrum_analyzer(args.audio_file)
finally:
    # Cleanup terminal
    os.system('stty sane')
    sense.clear()  # Clear the LED matrix
