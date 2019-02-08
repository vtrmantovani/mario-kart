class Lap:

    def __init__(self, hour, number, duration, average_speed, driver):

        self._hour = hour
        self._number = number
        self._duration = duration
        self._average_speed = average_speed
        self._driver = driver

    @property
    def hour(self):
        return self._hour

    @property
    def number(self):
        return self._number

    @property
    def duration(self):
        return self._duration

    @property
    def average_speed(self):
        return self._average_speed

    @property
    def driver(self):
        return self._driver
