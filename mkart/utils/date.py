from datetime import timedelta

HOURS_IN_MILLISECONDS = 3600000
MINUTES_IN_MILLISECONDS = 60000
SECONDS_IN_MILLISECONDS = 1000


def text_hour_to_milliseconds(value):
    value = value.replace('.', ':')
    hours, minutes, seconds, milliseconds = value.split(':')

    return ((HOURS_IN_MILLISECONDS * int(hours)) +
            (MINUTES_IN_MILLISECONDS * int(minutes)) +
            (SECONDS_IN_MILLISECONDS * int(minutes)) +
            int(milliseconds))


def text_minutes_to_milliseconds(value):
    value = value.replace('.', ':')
    minutes, seconds, milliseconds = value.split(':')

    return (((MINUTES_IN_MILLISECONDS * int(minutes)) +
             (SECONDS_IN_MILLISECONDS * int(seconds)) +
             int(milliseconds)))


def milliseconds_to_text(value):
    return str(timedelta(milliseconds=value))
