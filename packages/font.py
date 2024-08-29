# ========================================================================
# packages/font.py
#
# Description: Custom font class for the Sense HAT.
#
# https://www.pixilart.com/art/8x8-pixel-font-sr247895d16d2aws3
#
# Author: Jim Ing
# Date: 2024-08-26
# ========================================================================

class Font:
    def __init__(self):
        # Basic color palette
        W = (255, 255, 255) # White
        K = (0, 0, 0)       # Black

        self.charA = [
            K, K, W, W, W, W, W, W,
            K, W, W, W, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W
        ]

        self.charB = [
            W, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, W, W, W, W, K
        ]

        self.charC = [
            K, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W
        ]

        self.charD = [
            W, W, W, W, W, W, K, K,
            W, W, W, W, W, W, W, K,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, K
        ]

        self.charE = [
            K, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, W, W, W, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W
        ]

        self.charF = [
            K, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, W, W, W, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K
        ]

'''
        self.white = [
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W
        ]
'''
