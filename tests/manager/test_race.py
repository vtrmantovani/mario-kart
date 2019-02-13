import io
import os
import unittest

import mock

from mkart.exceptions.manager import ManagerException
from mkart.manager.race import RaceManager
from mkart.models.driver import Driver
from mkart.models.lap import Lap
from mkart.models.position import Position
from mkart.services.lap import LapService


class TestManagerRace(unittest.TestCase):

    def setUp(self):
        self.fixtures_path = os.path.join(os.path.dirname(__file__), '../fixtures')  # noqa
        self.load_fixtures()

    def load_fixtures(self):
        self.driver = Driver(1, 'F.MASSA')
        self.driver_2 = Driver(2, 'K.RAIKKONEN')

        self.lap = Lap(
            3661001,
            1,
            60001,
            44.275,
            self.driver)

    @mock.patch('mkart.services.file.FileService._check_file_exists')
    @mock.patch('mkart.services.file.FileService.get_lines')
    def test_get_lines_file(self, mock_s_file, mock_s_check):
        mock_s_file.return_value = ['23:49:08.277']
        race_manager = RaceManager('a.log')
        result = race_manager._get_lines_file()
        self.assertEquals(result, ['23:49:08.277'])

    def test_get_laps(self):
        lines = ["23:49:08.277      038 – MARIO                           1		1:02.852                        44,275"]  # noqa

        race_manager = RaceManager('a.log')
        result = race_manager._get_laps(lines)
        self.assertEqual(type(result[0]), Lap)

    def get_lap_service(self):
        race_manager = RaceManager(self.fixtures_path + '/file_with_laps.log')
        result = race_manager._get_lap_service()
        self.assertEqual(type(result), LapService)

    @mock.patch('mkart.services.position.PositionService.get_positions')
    def test_get_positions(self, mock_s_position):
        position = Position(1, self.driver, 1, 60001)
        mock_s_position.return_value = [position]

        race_manager = RaceManager('a.log')
        result = race_manager._get_positions([])
        self.assertEqual(type(result[0]), Position)

    def test_get_best_drivers_lap(self):
        race_manager = RaceManager(self.fixtures_path + '/file_with_laps.log')
        result = race_manager._get_best_drivers_lap()
        self.assertEqual(type(result[0]), Lap)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result(self, mock_stdout):
        race_manager = RaceManager(self.fixtures_path + '/file_with_laps.log')
        race_manager.show_result()
        self.assertEqual(mock_stdout.getvalue(), '1 038 MARIO 1 1:02.852\n2 033 R.BARRICHELLO 1 1:04.352\n')  # noqa

    def test_show_result_with_expection(self):
        with self.assertRaises(ManagerException) as error:
            race_manager = RaceManager(self.fixtures_path + '/file_empty.log')
            race_manager.show_result()

        self.assertEqual(str(error.exception), 'File is empty')

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_show_best_drivers_lap(self, mock_stdout):
        race_manager = RaceManager(self.fixtures_path + '/file_with_laps.log')
        race_manager.show_best_drivers_lap()
        self.assertEqual(mock_stdout.getvalue(), '038 MARIO 1 1:02.852\n033 R.BARRICHELLO 1 1:04.352\n')  # noqa

    def test_show_best_drivers_lap_with_expection(self):
        with self.assertRaises(ManagerException) as error:
            race_manager = RaceManager(self.fixtures_path + '/file_empty.log')
            race_manager.show_best_drivers_lap()

        self.assertEqual(str(error.exception), 'File is empty')

    def test_get_best_lap_of_race(self):
        race_manager = RaceManager(self.fixtures_path + '/file_with_laps.log')
        result = race_manager._get_best_lap_of_race()
        self.assertEqual(type(result), Lap)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_show_best_lap_of_race(self, mock_stdout):
        race_manager = RaceManager(self.fixtures_path + '/file_with_laps.log')
        race_manager.show_best_lap_of_race()
        self.assertEqual(mock_stdout.getvalue(), '038 MARIO 1:02.852\n')  # noqa

    def test_show_best_lap_of_race_with_expection(self):
        with self.assertRaises(ManagerException) as error:
            race_manager = RaceManager(self.fixtures_path + '/file_empty.log')
            race_manager.show_best_lap_of_race()

        self.assertEqual(str(error.exception), 'File is empty')

    def test_get_drivers_average_speed(self):
        race_manager = RaceManager(self.fixtures_path + '/file_with_laps.log')
        result = race_manager._get_drivers_average_speed()
        self.assertEqual(type(result[0]), Driver)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_show_drivers_average_speed(self, mock_stdout):
        race_manager = RaceManager(self.fixtures_path + '/file_with_laps.log')
        race_manager.show_drivers_average_speed()
        self.assertEqual(mock_stdout.getvalue(), '038 MARIO 44.275\n033 R.BARRICHELLO 43.243\n')  # noqa

    def test_show_drivers_average_speed_with_expection(self):
        with self.assertRaises(ManagerException) as error:
            race_manager = RaceManager(self.fixtures_path + '/file_empty.log')
            race_manager.show_drivers_average_speed()

        self.assertEqual(str(error.exception), 'File is empty')

    @mock.patch('mkart.services.position.PositionService.get_positions')
    def test_get_drivers_lap_after_winner(self, mock_s_position):
        position = Position(1, self.driver, 1, 60001)
        position_2 = Position(2, self.driver_2, 1, 60002)
        mock_s_position.return_value = [position, position_2]

        race_manager = RaceManager('a.log')
        result = race_manager._get_drivers_lap_after_winner([])
        self.assertEqual(type(result[0]), Position)
        self.assertEqual(result[0].delay_after_winner, 1)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_show_time_drivers_after_winner(self, mock_stdout):
        race_manager = RaceManager(self.fixtures_path + '/file_with_laps.log')
        race_manager.show_time_drivers_after_winner()
        self.assertEqual(mock_stdout.getvalue(), '033 R.BARRICHELLO 1 0:01.500\n')  # noqa

    def test_show_time_drivers_after_winner_with_expection(self):
        with self.assertRaises(ManagerException) as error:
            race_manager = RaceManager(self.fixtures_path + '/file_empty.log')
            race_manager.show_time_drivers_after_winner()

        self.assertEqual(str(error.exception), 'File is empty')
