#!/usr/bin/env python3
# ========================================================================
# warp_effect.py
#
# Description: Warp effect.
#
# Author: Jim Ing
# Date: 2024-08-23
# ========================================================================

import time
import argparse
from config import sense
from packages.warp_effects import WarpEffects
from packages.color_names import HTML_COLORS

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Warp Effect on Sense HAT')
    parser.add_argument('--speed', type=int, default=1, help='Warp speed (1-9)')
    parser.add_argument('--colors', nargs=4, default=['red', 'green', 'blue', 'yellow'],
                        help='Four colors for quadrants (names of HTML colors)')
    return parser.parse_args()

def main():
    args = parse_args()

    # Convert color names to tuples
    colors = {
        'tl': HTML_COLORS.get(args.colors[0], (255, 0, 0)),  # Default to red
        'tr': HTML_COLORS.get(args.colors[1], (0, 255, 0)),  # Default to green
        'bl': HTML_COLORS.get(args.colors[2], (0, 0, 255)),  # Default to blue
        'br': HTML_COLORS.get(args.colors[3], (255, 255, 0)) # Default to yellow
    }

    warp_effect = WarpEffects(sense, speed=args.speed, colors=colors)

    print("To quit, press Ctrl+C")

    try:
        while True:
            warp_effect.fpv()
            time.sleep(0.25)

    except KeyboardInterrupt:
        sense.clear()

if __name__ == "__main__":
    main()
