#!/usr/bin/env python3
# ========================================================================
# image_slide.py
#
# Description: Slide image.
#
# Author: Jim Ing
# Date: 2024-08-24
# ========================================================================

from packages.image_transformers import ImageSlider
from packages.sprites import Sprites

if __name__ == "__main__":
    sprite = Sprites()

    # Sliding an image
    slider = ImageSlider(sprite.arrowUp, steps=8, debug=True)
    slider.slide()
