# ========================================================================
# stardate.py
#
# Description: Stardate class.
#
# https://stardatecalculator.com/
#
# Author: Jim Ing
# Date: 2024-08-16
# ========================================================================

from datetime import datetime, timedelta

class Stardate:
    TOS_ROOT = 2265.1893
    TOS_INCREMENT = 1496.2162
    TMP_ROOT = 2224.155
    TMP_INCREMENT = 133.07789
    FILMS_ROOT = 2242.08
    FILMS_INCREMENT = 188.116
    TNG_ROOT = 2323.3981
    TNG_INCREMENT = 1000

    def __init__(self):
        self.earth_date = None
        self.tos_metric = None
        self.tmp_metric = None
        self.films_metric = None
        self.tng_metric = None

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    def format_stardate(self, stardate):
        if isinstance(stardate, datetime):
            return stardate.strftime("%d/%m/%Y %H:%M")
        elif isinstance(stardate, float):
            return f"{stardate:.2f}"
        else:
            return "Error"

    def earth_date(self):
        return self.earth_date

    def tos(self):
        return self.tos_metric

    def tmp(self):
        return self.tmp_metric

    def films(self):
        return self.films_metric

    def tng(self):
        return self.tng_metric

    def primary(self, force_stardate=False):
        if self.earth_date is None:
            return None
        if self.tos_metric < 0 and not force_stardate:
            return self.earth_date
        if self.tos_metric < 22160:  # ~year 2080
            return min(self.tos_metric, self.tmp_metric)
        if self.tos_metric < 52084:  # ~year 2300
            return max(self.tmp_metric, self.films_metric)
        return max(self.films_metric, self.tng_metric)

    def calculate(self, stardate):
        if isinstance(stardate, (int, float)):
            stardate += 0.0000001
            if stardate < 7000:
                real_tos = (stardate / self.TOS_INCREMENT) + self.TOS_ROOT
                real_tmp = (stardate / self.TMP_INCREMENT) + self.TMP_ROOT
                stardate = max(real_tos, real_tmp)
            elif stardate < 10000:
                real_tmp = (stardate / self.TMP_INCREMENT) + self.TMP_ROOT
                real_films = (stardate / self.FILMS_INCREMENT) + self.FILMS_ROOT
                stardate = min(real_tmp, real_films)
            else:
                real_films = (stardate / self.FILMS_INCREMENT) + self.FILMS_ROOT
                real_tng = (stardate / self.TNG_INCREMENT) + self.TNG_ROOT
                stardate = min(real_films, real_tng)

            year = int(stardate)
            days_in_year = 366 if self.is_leap_year(year) else 365
            date = datetime(year, 1, 1) + timedelta(days=(stardate % 1) * days_in_year)
            self.apply(stardate, date)

        elif isinstance(stardate, datetime):
            start_of_year = datetime(stardate.year, 1, 1)
            seconds_along_year = (stardate - start_of_year).total_seconds()
            year_fraction = seconds_along_year / (366 * 86400 if self.is_leap_year(stardate.year) else 365 * 86400)
            self.apply(stardate.year + year_fraction, stardate)
        else:
            print("Error: Invalid input")

    def apply(self, date_real, date_time):
        if not isinstance(date_real, (int, float)) or not isinstance(date_time, datetime):
            print("Error: Invalid input")
        else:
            self.earth_date = date_time
            self.tos_metric = (date_real - self.TOS_ROOT) * self.TOS_INCREMENT
            self.tmp_metric = (date_real - self.TMP_ROOT) * self.TMP_INCREMENT
            self.films_metric = (date_real - self.FILMS_ROOT) * self.FILMS_INCREMENT
            self.tng_metric = (date_real - self.TNG_ROOT) * self.TNG_INCREMENT
