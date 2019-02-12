import unittest

from mkart.models.driver import Driver
from mkart.models.lap import Lap
from mkart.services.position import PositionService


class TestServicePosition(unittest.TestCase):

    def setUp(self):
        self.load_fixtures()

    def load_fixtures(self):
        self.driver = Driver(38, 'F.MASSA')
        self.driver_2 = Driver(33, 'R.BARRICHELLO')

        self.lap_1 = Lap(
            3661001,
            1,
            60001,
            44.275,
            self.driver)

        self.lap_2 = Lap(
            3661002,
            1,
            60002,
            44.275,
            self.driver_2)

        self.last_laps = [
            {'duration':self.lap_1.duration, 'lap': self.lap_1},  # noqa
            {'duration': self.lap_2.duration,  'lap': self.lap_2}  # noqa
        ]

    def test_get_positions(self):
        position_service = PositionService(self.last_laps)
        result = position_service.get_positions()
        self.assertEquals(result[0].number, 1)
        self.assertEquals(result[0].driver, self.driver)
        self.assertEquals(result[0].finished_laps, 1)
        self.assertEquals(result[0].duration, 60001)
        self.assertEquals(result[1].number, 2)
        self.assertEquals(result[1].driver, self.driver_2)
        self.assertEquals(result[1].finished_laps, 1)
        self.assertEquals(result[1].duration, 60002)
