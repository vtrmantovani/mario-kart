class Position:

    def __init__(self, position, driver, finished_laps, duration):
        self._number = position
        self._driver = driver
        self._finished_laps = finished_laps
        self._duration = duration
        self._delay_after_winner = 0

    @property
    def number(self):
        return self._number

    @property
    def driver(self):
        return self._driver

    @property
    def finished_laps(self):
        return self._finished_laps

    @property
    def duration(self):
        return self._duration

    @property
    def delay_after_winner(self):
        return self._delay_after_winner

    @delay_after_winner.setter
    def delay_after_winner(self, value):
        self._delay_after_winner = value
