# Stardate Calculator and Display using Sense HAT

This Python script calculates and displays the current stardate on the Sense HAT LED matrix. The stardate is continuously updated, with an animated warp effect displayed before each update. The script supports two different stardate calculation systems: TNG (The Next Generation) and TOS (The Original Series).

## Background

### Stardate Systems

In the Star Trek universe, stardates are a way of expressing the current date in a futuristic and non-standard format. Over time, different series used different methods to calculate stardates, leading to some confusion. This script uses two common systems:

1. TNG (The Next Generation):

- Base Date (b): 2005
- Stardate Year (c): 58000.00
- This system is used in "Star Trek: The Next Generation" and subsequent series. The base date of 2005 was chosen arbitrarily to match the timeline established in the series. The stardate starts at 58000.00 in the year 2005 and increases as time progresses.

2. TOS (The Original Series):

- Base Date (b): 2323
- Stardate Year (c): 00000.00
- This system is used in "Star Trek: The Original Series." The base date of 2323 corresponds to an earlier point in the Star Trek timeline, where stardates start at 00000.00.

### Stardate Conversion Formula

The stardate is calculated using the following formula:

$
Stardate = c + (1000 × (y − b)) + ((1000 / n) × (m + d − 1))
$

Where:

- b: Base date (2005 for TNG, 2323 for TOS)
- c: Stardate year (58000.00 for TNG, 00000.00 for TOS)
- y: Current year
- m: Number of days from the start of the year to the start of the current month (adjusted for leap years)
- d: Current day of the month
- n: Number of days in the current year (365 for a regular year, 366 for a leap year)

## Features

- Stardate Calculation: Calculates stardates based on either the TNG or TOS system.
- Warp Effect: Before each stardate update, a warp effect simulates stars shooting by on the LED matrix.
- Continuous Display: The stardate is displayed on the Sense HAT's LED matrix and updated.
- Command Line Arguments: Choose between TNG or TOS system using command line arguments.

## Usage

### Command Line Arguments

You can specify which stardate system to use by passing either tng or tos as a command line argument:

```sh
python stardate.py tng
python stardate.py tos
```

If no argument is provided, the script defaults to the TNG system.

The script can be executed with or without date arguments.

- Example with date arguments:

    ```sh
    python stardate.py tng 2024 8 21
    ```

If no date arguments are supplied, it defaults to the current date.

### Displaying the Stardate

The stardate is displayed on the Sense HAT LED matrix with a slow scroll speed for readability. The display is refreshed with the current date converted to stardate format.

### Warp Effect

Before each stardate update, a warp effect is displayed. This animation simulates stars shooting by.

### Interrupting the Script

To stop the script, press Ctrl+C. The Sense HAT display will be cleared before exiting.

## Installation

To run this script, you will need:

- A Raspberry Pi with Sense HAT
- Python 3 installed
- The sense-hat Python library (can be installed via pip):

```sh
pip install sense-hat
```

## Example Output

```sh
$ python stardate.py tng
To quit, press Ctrl+C
# Warp effect displayed
# Stardate: 69034.85 displayed on Sense HAT
```

## License

This code is open-source and free to use under the MIT License.
