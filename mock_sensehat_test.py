#!/usr/bin/env python3

from mock_sensehat import SenseHat
import random
import time

sense = SenseHat()
sense.clear()

# Test by setting the entire display
pixels = [(255, 0, 0)] * 64  # all red
sense.set_pixels(pixels)
time.sleep(5)
sense.clear()

# Test by pixel
for y in range(8):
    for x in range(8):
        sense.set_pixel(x, y, (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255)))
        #sense.set_pixel(x, y, (random.randint(10, 255), 0, 0))
        time.sleep(0.1)
time.sleep(5)
sense.clear()

# Test by random pixels
off = [0, 0, 0]
red = [255, 0, 0]
amber = [255, 165, 0]
colors = [red, amber]

while True:
    pixels = [off] * 64
    for _ in range(random.randint(5, 15)):
        idx = random.randint(0, 63)
        pixels[idx] = random.choice(colors)
    sense.set_pixels(pixels)
    time.sleep(0.5 / 1)
sense.clear()
