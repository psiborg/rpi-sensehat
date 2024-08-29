# ========================================================================
# packages/warp.py
#
# Description: WarpEffects class.
#
# Author: Jim Ing
# Date: 2024-08-23
# ========================================================================

import random
import time
from packages.color_names import HTML_COLORS

class WarpEffects:
    def __init__(self, sense, speed=1, colors=None):
        self.sense = sense
        self.speed = speed
        self.delay = 1.0 / (speed * 10)
        self.colors = colors or {
            'tl': HTML_COLORS.get('red'),
            'tr': HTML_COLORS.get('green'),
            'bl': HTML_COLORS.get('blue'),
            'br': HTML_COLORS.get('yellow')
        }
        self.directions = {
            'tl': (-1, -1),
            'tr': (1, -1),
            'bl': (-1, 1),
            'br': (1, 1)
        }
        self.centers = {
            'tl': (3, 3),
            'tr': (4, 3),
            'bl': (3, 4),
            'br': (4, 4)
        }

        # tpv
        self.max_length = 3 # Maximum length of star tails
        self.base_delay = 0.2 # Initial delay for the warp effect

    def move_positions(self, positions, directions, step):
        """Calculate the new positions of the pixels."""
        return [
            (x + dx * step, y + dy * step)
            for (x, y), (dx, dy) in zip(positions, directions)
        ]

    def show_trails(self, steps):
        """Display the moving star trails."""
        for i in range(steps):
            positions = self.move_positions(
                self.centers.values(),
                self.directions.values(),
                i + 1
            )
            for pos, color in zip(positions, self.colors.values()):
                self.sense.set_pixel(pos[0], pos[1], color)
            time.sleep(self.delay)

    def clear_trails(self, steps):
        """Clear the star trails."""
        for i in range(steps):
            positions = self.move_positions(
                self.centers.values(),
                self.directions.values(),
                i + 1
            )
            for pos in positions:
                self.sense.set_pixel(pos[0], pos[1], (0, 0, 0))
            time.sleep(self.delay)

    def fpv(self):
        """Run the warp effect in first person view."""
        self.sense.clear()
        self.show_trails(steps=3)
        self.clear_trails(steps=3)

    def tpv(self, duration=5):
        """Run the warp effect in third person view with growing tails."""
        white = (255, 255, 255)
        black = (0, 0, 0)

        start_time = time.time()
        delay = self.base_delay
        stars = [] # List to keep track of stars and their positions

        while time.time() - start_time < duration:
            self.sense.clear()

            # Create new stars at random positions on the left side
            if random.random() < 0.5: # 50% chance to create a star in each row
                row = random.randint(0, 7)
                stars.append({'row': row, 'col': 0, 'tail': 1}) # Start with tail length of 1

            # Move stars and update their tails
            new_stars = []
            for star in stars:
                if star['col'] < 7: # Move the star only if it's still on the matrix
                    # Clear the tail
                    for i in range(star['tail']):
                        if star['col'] - i >= 0:
                            self.sense.set_pixel(star['col'] - i, star['row'], black)

                    # Move the star
                    star['col'] += 1
                    if star['tail'] < self.max_length:
                        star['tail'] += 1 # Increase tail length as the star moves

                    # Draw the star and its tail
                    for i in range(star['tail']):
                        if star['col'] - i >= 0:
                            self.sense.set_pixel(star['col'] - i, star['row'], white)

                    new_stars.append(star)

            stars = new_stars

            time.sleep(delay)
            delay = max(0.01, delay * 0.9) # Gradually decrease the delay to speed up

        self.sense.clear()
