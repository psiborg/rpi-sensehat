# Binary Clock

Let's break down how to read the binary time based on the layout where:

- Columns 0-1: Represent the hours using 5 bits.
- Columns 3-5: Represent the minutes using 6 bits.
- Columns 6-7: Represent the seconds using 6 bits.

## Understanding Binary Time Representation:

1. Columns 0-1: Hours (5 bits)

- Bits 4, 3, 2, 1, 0: From top (row 0) to bottom (row 4), these bits represent the binary value for the hour.
- Since there are 5 bits, the possible values range from 0 (00000) to 23 (10111) in a 24-hour clock format.

### Example:

- Suppose the LEDs in columns 0-1 are lit as follows:

    ```
    Row 0: 1 0
    Row 1: 0 1
    Row 2: 1 0
    Row 3: 0 0
    Row 4: 1 1
    ```

- Reading top to bottom, you get 10101 in binary, which is 21 in decimal. So the hour is 21 (or 9 PM in 12-hour format).

2. Columns 3-5: Minutes (6 bits)

- Bits 5, 4, 3, 2, 1, 0: From top (row 0) to bottom (row 5), these bits represent the binary value for the minutes.
- Since there are 6 bits, the possible values range from 0 (000000) to 59 (111011).

### Example:

- Suppose the LEDs in columns 3-5 are lit as follows:

    ```
    Row 0: 0 1 1
    Row 1: 1 0 0
    Row 2: 1 1 1
    Row 3: 0 0 1
    Row 4: 1 0 0
    Row 5: 0 1 0
    ```

- Reading top to bottom, you get 011101 in binary, which is 29 in decimal. So the minutes are 29.

3. Columns 6-7: Seconds (6 bits)

- Bits 5, 4, 3, 2, 1, 0: From top (row 0) to bottom (row 5), these bits represent the binary value for the seconds.
- Just like minutes, the range is from 0 to 59.

### Example:

- Suppose the LEDs in columns 6-7 are lit as follows:

    ```
    Row 0: 1 0
    Row 1: 0 1
    Row 2: 0 1
    Row 3: 1 0
    Row 4: 1 1
    Row 5: 0 0
    ```

- Reading top to bottom, you get 100110 in binary, which is 38 in decimal. So the seconds are 38.

## Summary:
- Hours (columns 0-1): Read the top 5 rows of columns 0-1 as a 5-bit binary number.
- Minutes (columns 3-5): Read the top 6 rows of columns 3-5 as a 6-bit binary number.
- Seconds (columns 6-7): Read the top 6 rows of columns 6-7 as a 6-bit binary number.

To read the time:

1. Convert the binary numbers from each column group (hours, minutes, seconds) to their decimal equivalents.
2. These decimal numbers represent the current time in hours, minutes, and seconds, respectively.

If you see:

- Columns 0-1: 10101 → 21 (hours)
- Columns 3-5: 011101 → 29 (minutes)
- Columns 6-7: 100110 → 38 (seconds)

The time displayed would be 21:29:38.
