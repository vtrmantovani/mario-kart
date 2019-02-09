import unittest

from mkart.utils.date import (text_hour_to_milliseconds,
                              text_minutes_to_milliseconds)


class TestUtilsDate(unittest.TestCase):

    def test_text_hour_to_milliseconds(self):
        result = text_hour_to_milliseconds('01:01:00.1')
        self.assertEquals(result, 3661001)

    def test_text_minutes_to_milliseconds(self):
        result = text_minutes_to_milliseconds('1:00.1')
        self.assertEquals(result, 60001)
