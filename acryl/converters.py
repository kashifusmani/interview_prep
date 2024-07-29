from pytz import timezone
from datetime import datetime
import pytz

"""
This utility is responsible to provide conversion methods.
"""


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)


def kmh_to_mph(kmh):
    conversion_factor = 0.621371
    mph = kmh * conversion_factor
    return round(mph, 2)


def get_current_time_pst():
    date_format = "%Y-%m-%d %I:%M %p"
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone("US/Pacific"))
    return date.strftime(date_format)


def str_to_date(date_string):
    date_format = "%Y-%m-%dT%H:%M"
    datetime_object = datetime.strptime(date_string, date_format)
    return datetime_object


def convert_utc_to_pst(utc_time):
    utc_zone = pytz.utc
    pst_zone = pytz.timezone("America/Los_Angeles")
    utc_time = utc_zone.localize(utc_time)
    pst_time = utc_time.astimezone(pst_zone)
    return pst_time.strftime("%Y-%m-%d %I:%M %p")
