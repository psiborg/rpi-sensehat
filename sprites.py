# ========================================================================
# sprites.py
#
# Description: Sprites class.
#
# Author: Jim Ing
# Date: 2024-08-15
# ========================================================================

class Sprites:
    def __init__(self):
        # Basic color palette
        W = (255, 255, 255) # White
        R = (255, 0, 0)     # Red
        G = (0, 255, 0)     # Green
        B = (0, 0, 255)     # Blue
        C = (0, 255, 255)   # Cyan
        M = (255, 0, 255)   # Magenta
        Y = (255, 255, 0)   # Yellow
        O = (255, 127, 0)   # Orange
        P = (255, 192, 203) # Pink
        K = (0, 0, 0)       # Black

        self.blank = [
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K
        ]

        # Animals

        self.chicken = [
            K, K, K, Y, Y, Y, K, K,
            K, K, O, Y, B, Y, K, K,
            K, K, K, Y, Y, Y, K, K,
            K, P, P, P, P, P, P, K,
            K, P, W, W, W, W, P, K,
            K, P, W, W, W, W, P, K,
            K, K, P, W, W, P, K, K,
            K, K, K, P, P, K, K, K
        ]

        self.crab = [
            K, W, W, K, W, W, K, K,
            K, W, K, K, W, K, K, K,
            K, R, K, K, R, K, K, K,
            K, R, K, K, R, K, K, K,
            R, R, R, R, R, K, R, R,
            R, R, K, K, R, R, R, K,
            R, R, R, R, R, K, R, R,
            R, K, R, K, R, K, K, K
        ]

        self.crocodile = [
            G, G, G, G, G, K, K, K,
            G, B, G, B, G, G, G, G,
            G, G, G, G, G, G, G, G,
            G, G, K, W, K, K, K, W,
            G, G, K, K, K ,K ,K ,K,
            G, G, K, K, K, W, K, K,
            G, G, G, G, G, G, G, G,
            G, G, G, G, G, G, G, G
        ]

        self.frog = [
            K, G, G, G, K, G, G, G,
            K, G, Y, G, K, G, Y, G,
            G, G, G, G, G, G, G, G,
            G, R, R, R, R, R, R, R,
            G, G, G, G, G, G, G, G,
            G, G, G, G, G, G, G, G,
            G, G, G, G, G, G, G, G,
            G, G, K, G, G, G, K, G
        ]

        self.snake = [
            K, K, K, K, K, K, K, G,
            K, G, G, G, G, G, G, G,
            K, G, K, K, K, K, K, K,
            K, G, G, G, G, G, K, K,
            K, K, K, K, K, G, K, K,
            Y, G, Y, G, G, G, K, K,
            G, G, G, K, K, K, K, K,
            R, K, K, K, K, K, K, K
        ]

        self.animals = [
            self.chicken,
            self.crab,
            self.crocodile,
            self.frog,
            self.snake
        ]

        # Arrows

        self.arrowUp = [
            K, K, K, W, W, K, K, K,
            K, K, W, W, W, W, K, K,
            K, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            K, K, W, W, W, W, K, K,
            K, K, W, W, W, W, K, K,
            K, K, W, W, W, W, K, K,
            K, K, W, W, W, W, K, K
        ]

        self.arrowDown = [
            K, K, W, W, W, W, K, K,
            K, K, W, W, W, W, K, K,
            K, K, W, W, W, W, K, K,
            K, K, W, W, W, W, K, K,
            W, W, W, W, W, W, W, W,
            K, W, W, W, W, W, W, K,
            K, K, W, W, W, W, K, K,
            K, K, K, W, W, K, K, K
        ]

        self.arrowLeft = [
            K, K, K, W, K, K, K, K,
            K, K, W, W, K, K, K, K,
            K, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            K, W, W, W, W, W, W, W,
            K, K, W, W, K, K, K, K,
            K, K, K, W, K, K, K, K
        ]

        self.arrowRight = [
            K, K, K, K, W, K, K, K,
            K, K, K, K, W, W, K, K,
            W, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, K,
            K, K, K, K, W, W, K, K,
            K, K, K, K, W, K, K, K
        ]

        self.arrows = [
            self.arrowUp,
            self.arrowDown,
            self.arrowLeft,
            self.arrowRight
        ]

        # Dice

        self.dice1 = [
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, R, R, K, K, K,
            K, K, K, R, R, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K
        ]

        self.dice2 = [
            R, R, K, K, K, K, K, K,
            R, R, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, R, R,
            K, K, K, K, K, K, R, R
        ]

        self.dice3 = [
            R, R, K, K, K, K, K, K,
            R, R, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, R, R, K, K, K,
            K, K, K, R, R, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, R, R,
            K, K, K, K, K, K, R, R
        ]

        self.dice4 = [
            R, R, K, K, K, K, R, R,
            R, R, K, K, K, K, R, R,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            R, R, K, K, K, K, R, R,
            R, R, K, K, K, K, R, R
        ]

        self.dice5 = [
            R, R, K, K, K, K, R, R,
            R, R, K, K, K, K, R, R,
            K, K, K, K, K, K, K, K,
            K, K, K, R, R, K, K, K,
            K, K, K, R, R, K, K, K,
            K, K, K, K, K, K, K, K,
            R, R, K, K, K, K, R, R,
            R, R, K, K, K, K, R, R
        ]

        self.dice6 = [
            R, R, K, K, K, K, R, R,
            R, R, K, K, K, K, R, R,
            K, K, K, K, K, K, K, K,
            R, R, K, K, K, K, R, R,
            R, R, K, K, K, K, R, R,
            K, K, K, K, K, K, K, K,
            R, R, K, K, K, K, R, R,
            R, R, K, K, K, K, R, R
        ]

        self.dices = [
            self.dice1,
            self.dice2,
            self.dice3,
            self.dice4,
            self.dice5,
            self.dice6
        ]

        # Pacman Ghosts

        self.blinky = [
            K, K, K, R, R, K, K, K,
            K, R, R, R, R, R, R, K,
            R, W, W, R, W, W, R, R,
            R, W, K, R, W, K, R, R,
            R, R, R, R, R, R, R, R,
            R, R, R, R, R, R, R, R,
            R, R, R, R, R, R, R, R,
            K, R, K, R, K, R, K, R
        ]

        self.clyde = [
            K, K, K, Y, Y, K, K, K,
            K, Y, Y, Y, Y, Y, Y, K,
            Y, W, W, Y, W, W, Y, Y,
            Y, W, K, Y, W, K, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            K, Y, K, Y, K, Y, K, Y
        ]

        self.inky = [
            K, K, K, C, C, K, K, K,
            K, C, C, C, C, C, C, K,
            C, W, W, C, W, W, C, C,
            C, W, K, C, W, K, C, C,
            C, C, C, C, C, C, C, C,
            C, C, C, C, C, C, C, C,
            C, C, C, C, C, C, C, C,
            K, C, K, C, K, C, K, C
        ]

        self.pinky = [
            K, K, K, M, M, K, K, K,
            K, M, M, M, M, M, M, K,
            M, W, W, M, W, W, M, M,
            M, W, K, M, W, K, M, M,
            M, M, M, M, M, M, M, M,
            M, M, M, M, M, M, M, M,
            M, M, M, M, M, M, M, M,
            K, M, K, M, K, M, K, M
        ]

        self.ghosts = [
            self.blinky,
            self.clyde,
            self.inky,
            self.pinky
        ]

        # Misc

        self.flower = [
            K, K, P, P, P, P, K, K,
            K, P, P, O, O, P, P, K,
            P, P, O, Y, Y, O, P, P,
            K, P, P, O, O, P, P, K,
            K, K, P, P, P, P, K, K,
            G, K, K, G, G, K, K, G,
            K, G, G, G, G, G, G, K,
            K, K, K, G, G, K, K, K
        ]

        self.heart = [
            K, K, K, K, K, K, K, K,
            K, R, R, K, R, R, K, K,
            R, R, R, R, R, R, R, K,
            R, R, R, R, R, R, R, K,
            K, R, R, R, R, R, K, K,
            K, K, R, R, R, K, K, K,
            K, K, K, R, K, K, K, K,
            K, K, K, K, K, K, K, K
        ]

        self.noentry = [
            K, K, R, R, R, R, K, K,
            K, R, R, R, R, R, R, K,
            R, R, R, R, R, R, R, R,
            R, W, W, W, W, W, W, R,
            R, W, W, W, W, W, W, R,
            R, R, R, R, R, R, R, R,
            K, R, R, R, R, R, R, K,
            K, K, R, R, R, R, K, K
        ]

        self.plus = [
            K, K, K, K, K, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, W, W, W, W, W, W, K,
            K, W, W, W, W, W, W, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, K, K, K, K, K
        ]

        self.raspberry = [
            K, G, G, K, K, G, G, K,
            K, K, G, G, G, G, K, K,
            K, K, R, R, R, R, K, K,
            K, R, R, R, R, R, R, K,
            R, R, R, R, R, R, R, R,
            R, R, R, R, R, R, R, R,
            K, R, R, R, R, R, R, K,
            K, K, R, R, R, R, K, K
        ]

        self.smiley = [
            K, K, Y, Y, Y, Y, K, K,
            K, Y, Y, Y, Y, Y, Y, K,
            Y, Y, K, Y, Y, K, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, K, Y, Y, K, Y, Y,
            K, Y, Y, K, K, Y, Y, K,
            K, K, Y, Y, Y, Y, K, K
        ]

        self.misc = [
            self.flower,
            self.heart,
            self.noentry,
            self.plus,
            self.raspberry,
            self.smiley
        ]

        self.all = [
            self.chicken,
            self.crab,
            self.crocodile,
            self.frog,
            self.snake,

            self.arrowUp,
            self.arrowDown,
            self.arrowLeft,
            self.arrowRight,

            self.dice1,
            self.dice2,
            self.dice3,
            self.dice4,
            self.dice5,
            self.dice6,

            self.blinky,
            self.clyde,
            self.inky,
            self.pinky,

            self.flower,
            self.heart,
            self.noentry,
            self.plus,
            self.raspberry,
            self.smiley
        ]
