import unittest

from mkart.models.driver import Driver
from mkart.models.lap import Lap


class TestLap(unittest.TestCase):

    def setUp(self):
        self.load_fixtures()

    def load_fixtures(self):
        self.driver = Driver(1, 'F.MASSA')

    def test_create_lap(self):
        hour = 3661001
        number = 1
        duration = 60001
        average_speed = 44.275

        lap = Lap(
            hour,
            number,
            duration,
            average_speed,
            self.driver)

        self.assertEqual(type(lap), Lap)
        self.assertEqual(lap.driver.id, self.driver.id)
        self.assertEqual(lap.driver.name, self.driver.name)
        self.assertEqual(lap.hour, hour)
        self.assertEqual(lap.number, number)
        self.assertEqual(lap.duration, duration)
        self.assertEqual(lap.average_speed, average_speed)
