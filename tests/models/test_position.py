import unittest

from mkart.models.driver import Driver
from mkart.models.position import Position


class TestPosition(unittest.TestCase):

    def setUp(self):
        self.load_fixtures()

    def load_fixtures(self):
        driver = Driver(1, 'F.MASSA')
        driver.laps = 1
        driver.laps = 2

        self.driver = driver

    def test_create_position(self):
        number = 1
        finished_laps = 2
        duration = 60001
        position = Position(number, self.driver, finished_laps, duration)

        self.assertEqual(type(position), Position)
        self.assertEqual(type(position.driver), Driver)
        self.assertEqual(position.driver.id, self.driver.id)
        self.assertEqual(position.driver.name, self.driver.name)
        self.assertEqual(position.number, number)
        self.assertEqual(position.finished_laps, finished_laps)
        self.assertEqual(position.duration, duration)

    def test_create_position_with_delay_after_winner(self):
        number = 1
        finished_laps = 2
        duration = 60001
        position = Position(number, self.driver, finished_laps, duration)
        position.delay_after_winner = 60001
        self.assertEqual(type(position), Position)
        self.assertEqual(type(position.driver), Driver)
        self.assertEqual(position.driver.id, self.driver.id)
        self.assertEqual(position.driver.name, self.driver.name)
        self.assertEqual(position.number, number)
        self.assertEqual(position.finished_laps, finished_laps)
        self.assertEqual(position.duration, duration)
        self.assertEqual(position.delay_after_winner, 60001)
