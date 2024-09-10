#!/usr/bin/env python3
# ========================================================================
# mars_clock.py
#
# Description: Mars days (sols) are about 24 hours, 39 minutes, and
#              35.244 seconds. A Mars year is approximately 687 Earth
#              days or 669 sols.
#
# Author: Jim Ing
# Date: 2024-09-09
# ========================================================================

import datetime
import math
from config import sense

# Constants
SECONDS_IN_A_DAY = 86400  # Earth seconds in a day
MARS_SOL_IN_SECONDS = 88775.244  # Seconds in a Mars day (sol)
MARS_YEAR_IN_SOL = 668.5991  # Number of sols in a Mars year

# Function to calculate Mars time
def earth_to_mars_time(earth_datetime):
    """
    Convert Earth time to Mars Coordinated Time (MTC).
    Returns the Martian sol (day) and time of day on Mars.
    """
    # Earth start time (reference point: Jan 6, 2000, 00:00:00 UTC)
    epoch_start = datetime.datetime(2000, 1, 6, 0, 0, 0, tzinfo=datetime.timezone.utc)

    # Calculate the difference in seconds
    delta_seconds = (earth_datetime - epoch_start).total_seconds()

    # Convert Earth seconds to Mars sols
    mars_sols = delta_seconds / MARS_SOL_IN_SECONDS

    # Mars Sol date (starting from epoch)
    sol_day = math.floor(mars_sols)

    # Calculate MTC (Mars time of day in seconds)
    mars_time_of_day_seconds = (mars_sols - sol_day) * MARS_SOL_IN_SECONDS

    # Convert seconds to hours, minutes, and seconds
    hours = int(mars_time_of_day_seconds // 3600)
    minutes = int((mars_time_of_day_seconds % 3600) // 60)
    seconds = int(mars_time_of_day_seconds % 60)

    return sol_day, hours, minutes, seconds

# Function to get Mars year and sol in the Martian year
def get_martian_year_and_sol(earth_datetime):
    """
    Calculate the Martian year and the sol within that year.
    """
    epoch_start = datetime.datetime(2000, 1, 6, 0, 0, 0, tzinfo=datetime.timezone.utc)

    # Total sols since the epoch start
    delta_seconds = (earth_datetime - epoch_start).total_seconds()
    mars_sols = delta_seconds / MARS_SOL_IN_SECONDS

    # Martian year
    mars_year = math.floor(mars_sols / MARS_YEAR_IN_SOL) + 1

    # Sol within that Martian year
    sol_in_year = math.floor(mars_sols % MARS_YEAR_IN_SOL)

    return mars_year, sol_in_year

try:
    while True:
        # Get current Earth time (UTC and timezone aware)
        earth_time = datetime.datetime.now(datetime.timezone.utc)

        # Convert to Mars time
        sol_day, hours, minutes, seconds = earth_to_mars_time(earth_time)
        mars_year, sol_in_year = get_martian_year_and_sol(earth_time)

        # Display Mars date and time
        print(f"Mars Year: {mars_year}, Sol (year): {sol_in_year}")
        print(f"Sol (day): {sol_day}, Time: {hours:02}:{minutes:02}:{seconds:02} MTC")

        # Prepare the message
        message = f"Mars Year: {mars_year}, Sol: {sol_in_year} Time: {hours:02}:{minutes:02}:{seconds:02} MTC"
        #print(message)

        # Display the message on the Sense HAT LED matrix
        sense.show_message(message, scroll_speed=0.1, text_colour=[255, 255, 255], back_colour=[0, 0, 0])

except KeyboardInterrupt:
    sense.clear()
