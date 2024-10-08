#!/usr/bin/env python3
# ========================================================================
# rainbow0.py
#
# Description: Display solid rainbow colors.
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

import sys
from time import sleep
from config import sense

r = (255, 0, 0)     # red
o = (255, 128, 0)   # orange
y = (255, 255, 0)   # yellow
g = (0, 255, 0)     # green
c = (0, 255, 255)   # cyan
b = (0, 0, 255)     # blue
p = (255, 0, 255)   # purple
n = (255, 128, 128) # pink
w = (255, 255, 255) # white
k = (0, 0, 0)       # blank

rainbow = [r, o, y, g, c, b, p, n]

try:
    print ("To quit, press Ctrl+C")

    while True:
        sense.clear()

        for y in range(8):
            colour = rainbow[y]
            for x in range(8):
                sense.set_pixel(x, y, colour)

            sleep(1)
        sleep(3)

        sense.show_message("Hello!", text_colour = w, back_colour = b)
        sleep(3)

# Exit cleanly
except KeyboardInterrupt:
    print("\n" + "Stopped")

finally:
    sense.clear()
    sys.exit(0)
