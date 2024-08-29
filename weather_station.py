#!/usr/bin/env python3
# ========================================================================
# weather_station.py
#
# Description: Python version of the Scratch 3 version.
#
# https://learn.littlebirdelectronics.com.au/raspberry-pi/raspberry-pi-weather-station-with-the-sense-hat
#
# Author: Jim Ing
# Date: 2024-08-21
# ========================================================================

from time import sleep
from config import sense

sense.clear()

R = [229, 0, 0]     # red
O = [229, 123, 0]   # darkorange
Y = [204, 195, 0]   # goldenrod
G = [28, 204, 0]    # limegreen
T = [0, 191, 204]   # darkturquoise
B = [4, 0, 204]     # mediumblue
W = [255, 255, 255] # white
K = [0, 0, 0]       # black

try:
    print ("To quit, press Ctrl+C")
    while True:
        temp = sense.get_temperature()
        temp_color = K

        if temp > 40:
            temp_color = R
        elif temp > 35:
            temp_color = O
        elif temp > 30:
            temp_color = Y
        elif temp > 25:
            temp_color = G
        elif temp > 20:
            temp_color = T
        else:
            temp_color = B

        print(temp, temp_color)

        sense.show_message(str(temp), text_colour=W, back_colour=temp_color)
        sleep(5)

except KeyboardInterrupt:
    sense.clear()
