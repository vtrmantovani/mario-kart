import unittest

from mkart.models.driver import Driver
from mkart.models.lap import Lap
from mkart.models.position import Position
from mkart.services.position import PositionService


class TestServicePosition(unittest.TestCase):

    def setUp(self):
        self.load_fixtures()

    def load_fixtures(self):
        self.driver = Driver(38, 'F.MASSA')
        self.driver_2 = Driver(33, 'R.BARRICHELLO')
        self.driver_3 = Driver(2, 'R.K.RAIKKONEN')

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

        self.lap_3 = Lap(
            3661000,
            1,
            60003,
            44.265,
            self.driver_3)

        self.last_laps = [
            {'duration': self.lap_1.duration, 'lap': self.lap_1},  # noqa
            {'duration': self.lap_2.duration,  'lap': self.lap_2},  # noqa
            {'duration': self.lap_3.duration, 'lap': self.lap_3}  # noqa
        ]

        self.position_1 = Position(
            1,
            self.driver,
            2,
            3661001
        )

        self.position_2 = Position(
            2,
            self.driver,
            2,
            3661002
        )

        self.position_3 = Position(
            3,
            self.driver,
            1,
            3661002
        )

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

    def test_get_delay_after_winner(self):
        position_service = PositionService(self.last_laps)
        winer = self.position_1
        loser = self.position_2
        result = position_service._get_delay_after_winner(winer, loser)
        self.assertEquals(result, 1)

    def test_get_delay_after_winner_with_not_finish_the_race(self):
        position_service = PositionService(self.last_laps)
        winer = self.position_1
        loser = self.position_3
        result = position_service._get_delay_after_winner(winer, loser)
        self.assertEquals(result, 3661002)

    def test_et_time_drivers_after_winner(self):
        position_service = PositionService(self.last_laps)
        result = position_service.get_time_drivers_after_winner()
        self.assertEquals(result[0].driver, self.driver_2)
        self.assertEquals(result[0].delay_after_winner, 1)
        self.assertEquals(result[1].driver, self.driver_3)
        self.assertEquals(result[1].delay_after_winner, 2)
