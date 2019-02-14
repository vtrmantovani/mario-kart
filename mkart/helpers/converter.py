import re

from mkart.exceptions.helper import HelperException
from mkart.models.driver import Driver
from mkart.models.lap import Lap
from mkart.utils.date import (text_hour_to_milliseconds,
                              text_minutes_to_milliseconds)

SPACE_PATTERN = "\\s+"
HOUR_PATTERN = "(\\d{2}:\\d{2}:\\d{2}.\\d{3})"
DRIVER_PATTERN = "(\\d{3}) – ([A-Za-z\\.]+)"
LAP_NUMBER_PATTERN = "(\\d)"
LAP_DURATION_PATTERN = "(\\d+:?\\d+\\.\\d{3})"
LAP_AVG_SPEED_PATTERN = "(\\d+,\\d+)"

LINE_PATTERN = \
    HOUR_PATTERN +\
    SPACE_PATTERN + \
    DRIVER_PATTERN + \
    SPACE_PATTERN + \
    LAP_NUMBER_PATTERN +\
    SPACE_PATTERN + \
    LAP_DURATION_PATTERN + \
    SPACE_PATTERN + \
    LAP_AVG_SPEED_PATTERN

HOUR_GROUP = 1
DRIVER_ID_GROUP = 2
DRIVER_NAME_GROUP = 3
LAP_NUMBER_GROUP = 4
LAP_DURATION_PATTERN = 5
LAP_AVG_SPEED_GROUP = 6


def _create_driver(id, name):

    if not id:
        raise HelperException('Id is required')
    if not name:
        raise HelperException('Name is required')

    return Driver(id, name)


def convert_text_to_lap(line):
    line_match = re.match(LINE_PATTERN, line)
    if not line_match:
        raise HelperException("Line '{}' not match with pattern".format(line))

    driver = _create_driver(
        line_match.group(DRIVER_ID_GROUP),
        line_match.group(DRIVER_NAME_GROUP)
    )

    lap_hour = line_match.group(HOUR_GROUP)
    lap_number = line_match.group(LAP_NUMBER_GROUP)
    lap_duration = line_match.group(LAP_DURATION_PATTERN)
    lap_average_speed = float(
        line_match.group(LAP_AVG_SPEED_GROUP).replace(',', '.')
    )

    lap = Lap(
        text_hour_to_milliseconds(lap_hour),
        lap_number,
        text_minutes_to_milliseconds(lap_duration),
        lap_average_speed,
        driver)

    return lap
