#!/usr/bin/env python3
# ========================================================================
# image_rotate.py
#
# Description: Rotate image.
#
# Author: Jim Ing
# Date: 2024-08-24
# ========================================================================

from packages.image_transformers import ImageRotator
from packages.sprites import Sprites

if __name__ == "__main__":
    try:
        sprite = Sprites()

        # Rotating an image
        rotator = ImageRotator(sprite.arrowUp, debug=True)
        rotator.rotate()

    except KeyboardInterrupt:
        rotator.clear()
