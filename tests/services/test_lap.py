import unittest

from mkart.models.driver import Driver
from mkart.models.lap import Lap
from mkart.services.lap import LapService


class TestServiceLap(unittest.TestCase):

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

        self.lap_3 = Lap(
            3661012,
            2,
            60002,
            44.275,
            self.driver_2)

        self.lap_4 = Lap(
            3661021,
            2,
            60001,
            44.275,
            self.driver)

        self.laps = [self.lap_1, self.lap_2, self.lap_4, self.lap_3]
        self.drive_1_laps = [self.lap_1, self.lap_4]
        self.drive_1_laps_sorted = [self.lap_4, self.lap_1]

    def test_get_drivers_id(self):
        lap_service = LapService(self.laps)
        result = lap_service._get_drivers_id()
        self.assertEquals(result, [33, 38])

    def test_get_driver_laps(self):
        lap_service = LapService(self.laps)
        result = lap_service._get_driver_laps(self.driver.id)
        self.assertEquals(result, self.drive_1_laps)

    def test_get_last_driver_laps(self):
        lap_service = LapService(self.laps)
        result = lap_service._get_last_driver_laps(self.drive_1_laps_sorted)
        self.assertEquals(result, self.lap_4)

    def test_get_race_duration_of_driver(self):
        lap_service = LapService(self.laps)
        result = lap_service._get_race_duration_of_driver(self.drive_1_laps_sorted)  # noqa
        self.assertEquals(result, self.lap_4.duration + self.lap_1.duration)

    def test_get_last_laps_duration(self):
        lap_service = LapService(self.laps)
        result = lap_service.get_last_laps_duration()

        duration_1 = self.lap_1.duration + self.lap_4.duration
        duration_2 = self.lap_2.duration + self.lap_3.duration

        self.assertEquals(result[0]['duration'], duration_1)
        self.assertEquals(result[0]['lap'], self.lap_4)
        self.assertEquals(result[1]['duration'], duration_2)
        self.assertEquals(result[1]['lap'], self.lap_3)

    def test_get_best_lap(self):
        lap_service = LapService(self.laps)
        result = lap_service._get_best_lap(self.drive_1_laps)  # noqa
        self.assertEquals(result.driver.id, self.lap_1.driver.id)
        self.assertEquals(result.driver.name, self.lap_1.driver.name)
        self.assertEquals(result.number, self.lap_1.number)
        self.assertEquals(result.duration, self.lap_1.duration)

    def test_get_best_drivers_lap(self):
        lap_service = LapService(self.laps)
        result = lap_service.get_best_drivers_lap()
        self.assertEquals(result[0].driver.id, self.lap_1.driver.id)
        self.assertEquals(result[0].driver.name, self.lap_1.driver.name)
        self.assertEquals(result[0].number, self.lap_1.number)
        self.assertEquals(result[0].duration, self.lap_1.duration)
        self.assertEquals(result[1].driver.id, self.lap_2.driver.id)
        self.assertEquals(result[1].driver.name, self.lap_2.driver.name)
        self.assertEquals(result[1].number, self.lap_2.number)
        self.assertEquals(result[1].duration, self.lap_2.duration)

    def test_get_best_lap_of_race(self):
        lap_service = LapService(self.laps)
        result = lap_service.get_best_lap_of_race()
        self.assertEquals(result.driver.id, self.lap_1.driver.id)
        self.assertEquals(result.driver.name, self.lap_1.driver.name)
        self.assertEquals(result.number, self.lap_1.number)
        self.assertEquals(result.duration, self.lap_1.duration)
