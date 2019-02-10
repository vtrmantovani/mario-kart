import unittest

from mkart.utils.date import (milliseconds_to_text, text_hour_to_milliseconds,
                              text_minutes_to_milliseconds)


class TestUtilsDate(unittest.TestCase):

    def test_text_hour_to_milliseconds(self):
        result = text_hour_to_milliseconds('01:01:00.1')
        self.assertEquals(result, 3661001)

    def test_text_minutes_to_milliseconds(self):
        result = text_minutes_to_milliseconds('1:00.1')
        self.assertEquals(result, 60001)

    def test_milliseconds_to_texte(self):
        result = milliseconds_to_text(60001)
        self.assertEquals(result, '0:01:00.001000')
