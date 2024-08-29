#!/usr/bin/env python3
# ========================================================================
# config.py
#
# Description: Global configuration.
#
# Author: Jim Ing
# Date: 2024-08-29
# ========================================================================

from sense_hat import SenseHat
#from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED

sense = SenseHat()

sense.rotation = 180
sense.low_light = True
