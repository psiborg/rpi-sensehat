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

        self.charG = [
            K, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, K, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W
        ]

        self.charH = [
            K, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W
        ]

        self.charI = [
            K, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, K
        ]

        self.charJ = [
            K, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            K, K, K, K, W, W, K, K,
            K, K, K, K, W, W, K, K,
            K, K, K, K, W, W, K, K,
            W, W, K, K, W, W, K, K,
            W, W, W, W, W, W, K, K,
            K, W, W, W, W, K, K, K
        ]

        self.charK = [
            K, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, W, W, W, K,
            W, W, W, W, W, W, K, K,
            W, W, W, W, W, W, K, K,
            W, W, W, W, W, W, W, K,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W
        ]

        self.charL = [
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W
        ]

        self.charM = [
            W, W, K, K, K, K, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, K, W, W, K, W, W,
            W, W, K, W, W, K, W, W,
            W, W, K, K, K, K, W, W
        ]

        self.charN = [
            W, W, K, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, W, K, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, K, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, K, W, W
        ]

        self.charO = [
            K, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, W, W, W, W, W,
            K, W, W, W, W, W, W, K
        ]

        self.charP = [
            W, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, K,
            W, W, W, K, K, K, K, K,
            W, W, W, K, K, K, K, K
        ]

        self.charQ = [
            K, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, W, W, W, K,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W
        ]

        self.charR = [
            W, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, K,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W
        ]

        self.charS = [
            K, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, K, K, K, K,
            W, W, W, W, W, K, K, K,
            K, W, W, W, W, W, W, K,
            K, K, K, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, K
        ]

        self.charT = [
            K, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K
        ]

        self.charU = [
            K, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            K, W, W, W, W, W, W, K
        ]

        self.charV = [
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, W, K, W, W, W,
            K, W, W, W, W, W, W, K,
            K, K, W, W, W, W, K, K,
            K, K, K, W, W, K, K, K
        ]

        self.charW = [
            W, W, K, K, K, K, W, W,
            W, W, K, K, K, K, W, W,
            W, W, K, K, K, K, W, W,
            W, W, K, W, W, K, W, W,
            W, W, K, W, W, K, W, W,
            W, W, W, W, W, W, W, W,
            K, W, W, W, W, W, W, K,
            K, K, W, K, K, W, K, K
        ]

        self.charX = [
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            K, W, W, W, W, W, W, K,
            K, K, W, W, W, W, K, K,
            K, K, W, W, W, W, K, K,
            K, W, W, W, W, W, W, K,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W
        ]

        self.charY = [
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            K, W, W, W, W, W, W, K,
            K, K, W, W, W, W, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K
        ]

        self.charZ = [
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            K, K, K, K, W, W, W, K,
            K, K, K, W, W, W, K, K,
            K, K, W, W, W, K, K, K,
            K, W, W, W, K, K, K, K,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W
        ]

        self.char1 = [
            K, K, K, W, W, W, K, K,
            K, W, W, W, W, W, K, K,
            K, K, K, W, W, W, K, K,
            K, K, K, W, W, W, K, K,
            K, K, K, W, W, W, K, K,
            K, K, K, W, W, W, K, K,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W
        ]

        self.char2 = [
            K, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            K, K, K, K, K, W, W, W,
            K, K, K, K, W, W, W, W,
            K, K, W, W, W, W, W, K,
            K, W, W, W, W, K, K, K,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W
        ]

        self.char3 = [
            K, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            K, K, K, K, K, W, W, W,
            K, K, K, W, W, W, W, K,
            K, K, K, W, W, W, W, K,
            K, K, K, K, K, W, W, W,
            W, W, W, W, W, W, W, W,
            K, W, W, W, W, W, W, W
        ]

        self.char4 = [
            K, K, K, K, W, W, W, K,
            K, K, K, W, W, W, W, K,
            K, K, W, W, W, W, W, K,
            K, W, W, K, W, W, W, K,
            W, W, K, K, W, W, W, K,
            W, W, W, W, W, W, W, W,
            K, K, K, K, W, W, W, K,
            K, K, K, K, W, W, W, K
        ]

        self.char5 = [
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, K, K, K,
            W, W, W, W, W, W, W, K,
            K, W, W, W, W, W, W, W,
            K, K, K, K, K, W, W, W,
            W, W, W, W, W, W, W, W,
            K, W, W, W, W, W, W, K
        ]

        self.char6 = [
            K, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, K, K, K,
            W, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, W, W, W, W, W,
            K, W, W, W, W, W, W, K
        ]

        self.char7 = [
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, K, K, K, K, K, W, W,
            K, K, K, K, K, W, W, W,
            K, K, K, K, W, W, W, K,
            K, K, K, W, W, W, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K
        ]

        self.char8 = [
            K, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            K, W, W, W, W, W, W, K,
            W, W, W, K, K, W, W, W,
            W, W, W, W, W, W, W, W,
            K, W, W, W, W, W, W, K
        ]

        self.char9 = [
            K, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, K, W, W, W,
            K, W, W, W, W, W, W, W,
            K, K, K, K, K, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, W, W, W, K
        ]

        self.char0 = [
            K, W, W, W, W, W, W, K,
            W, W, W, W, W, W, W, W,
            W, W, W, K, K, W, W, W,
            W, W, W, K, W, W, W, W,
            W, W, W, W, W, W, W, W,
            W, W, W, W, K, W, W, W,
            W, W, W, W, W, W, W, W,
            K, W, W, W, W, W, W, K
        ]

        self.charExclamation = [
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K
        ]

        self.charQuestion = [
            K, K, W, W, W, W, K, K,
            K, W, W, W, W, W, W, K,
            K, W, W, K, K, W, W, K,
            K, K, K, K, W, W, W, K,
            K, K, K, W, W, W, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K
        ]

        self.charPeriod = [
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K
        ]

        self.charColon = [
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, K, K, K, K, K,
            K, K, K, W, W, K, K, K,
            K, K, K, W, W, K, K, K
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

        # Character mapping
        self.char_map = {
            'A': self.charA,
            'B': self.charB,
            'C': self.charC,
            'D': self.charD,
            'E': self.charE,
            'F': self.charF,
            'G': self.charG,
            'H': self.charH,
            'I': self.charI,
            'J': self.charJ,
            'K': self.charK,
            'L': self.charL,
            'M': self.charM,
            'N': self.charN,
            'O': self.charO,
            'P': self.charP,
            'Q': self.charQ,
            'R': self.charR,
            'S': self.charS,
            'T': self.charT,
            'U': self.charU,
            'V': self.charV,
            'W': self.charW,
            'X': self.charX,
            'Y': self.charY,
            'Z': self.charZ,
            '1': self.char1,
            '2': self.char2,
            '3': self.char3,
            '4': self.char4,
            '5': self.char5,
            '6': self.char6,
            '7': self.char7,
            '8': self.char8,
            '9': self.char9,
            '0': self.char0,
            '!': self.charExclamation,
            '?': self.charQuestion,
            '.': self.charPeriod,
            ':': self.charColon
        }
