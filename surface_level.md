# Surface Level

## Mapping Roll to y (Vertical Axis):

- Roll represents the tilt to the left or right. When you tilt the device to the right, you expect the bubble to move to the left (decrease in y value). Conversely, tilting to the left should increase the y value.
- In the formula y = 3.5 - (roll / 90) * sensitivity, tilting to the right (roll > 0) subtracts from 3.5, moving the bubble up on the grid (decreasing y).
- Tilting to the left (roll < 0) adds to 3.5, moving the bubble down on the grid (increasing y).

## Mapping Pitch to x (Horizontal Axis):

- Pitch represents the tilt forward or backward. When you tilt the device forward, the bubble should move up the grid (increase in x value), and when you tilt backward, it should move down the grid (decrease in x value).
- In the formula x = 3.5 + (pitch / 90) * sensitivity, tilting forward (pitch > 0) adds to 3.5, moving the bubble to the right (increasing x).
- Tilting backward (pitch < 0) subtracts from 3.5, moving the bubble to the left (decreasing x).

## Coordinate System:

- The Sense HAT’s 8x8 LED matrix uses (0, 0) as the top-left corner and (7, 7) as the bottom-right corner.
- The use of 3.5 as the center allows the code to calculate positions relative to the middle of the matrix.

## Summary:

- Roll affects y: A positive roll (tilt right) decreases y, moving the bubble up, while a negative roll (tilt left) increases y, moving the bubble down.
- Pitch affects x: A positive pitch (tilt forward) increases x, moving the bubble right, while a negative pitch (tilt backward) decreases x, moving the bubble left.

This matches the expected movement of a bubble in a physical level.
