from mkart.exceptions.helper import HelperException
from mkart.exceptions.manager import ManagerException
from mkart.exceptions.service import ServiceException
from mkart.helpers.converter import convert_text_to_lap
from mkart.services.file import FileService
from mkart.services.lap import LapService
from mkart.services.position import PositionService
from mkart.utils.date import milliseconds_to_text


class RaceManager:

    def __init__(self, file):
        self._file = file
        self._get_lap_service()

    def _get_lines_file(self):
        file_service = FileService(self._file)
        return file_service.get_lines()

    def _get_laps(self, lines):
        try:
            laps = list(map(convert_text_to_lap, lines))
            if len(laps) == 0:
                raise ManagerException("File not match with pattern")
        except HelperException as e:
            raise ManagerException(e)
        return laps

    def _get_lap_service(self):
        try:
            lines = self._get_lines_file()
            laps = self._get_laps(lines)
        except ServiceException as e:
            raise ManagerException(e)
        return LapService(laps)

    def _get_last_laps_duration(self):
        lap_service = self._get_lap_service()
        return lap_service.get_last_laps_duration()

    def _get_positions(self, laps):
        position_service = PositionService(laps)
        return position_service.get_positions()

    def _get_best_drivers_lap(self):
        lap_service = self._get_lap_service()
        return lap_service.get_best_drivers_lap()

    def _get_best_lap_of_race(self):
        lap_service = self._get_lap_service()
        return lap_service.get_best_lap_of_race()

    def _get_drivers_average_speed(self):
        lap_service = self._get_lap_service()
        return lap_service.get_drivers_average_speed()

    def _get_drivers_lap_after_winner(self, laps):
        position_service = PositionService(laps)
        return position_service.get_time_drivers_after_winner()

    def show_result(self):
        last_laps = self._get_last_laps_duration()
        positions = self._get_positions(last_laps)

        for position in positions:
            print('{} {}-{} {} {}'.format(
                position.number,
                position.driver.id,
                position.driver.name,
                position.finished_laps,
                milliseconds_to_text(position.duration)
            ))

    def show_best_drivers_lap(self):
        best_drivers_lap = self._get_best_drivers_lap()
        for lap in best_drivers_lap:
            print('{}-{} {} {}'.format(
                lap.driver.id,
                lap.driver.name,
                lap.number,
                milliseconds_to_text(lap.duration)
            ))

    def show_best_lap_of_race(self):
        best_lap = self._get_best_lap_of_race()
        print('{}-{} {}'.format(
            best_lap.driver.id,
            best_lap.driver.name,
            milliseconds_to_text(best_lap.duration)
        ))

    def show_drivers_average_speed(self):
        average_speed_drivers = self._get_drivers_average_speed()
        for drive in average_speed_drivers:
            print('{}-{} {}'.format(
                drive.id,
                drive.name,
                "{0:.3f}".format(round(drive.average_speed, 3))
            ))

    def show_time_drivers_after_winner(self):
        last_laps = self._get_last_laps_duration()
        drivers_position_after_winner = self._get_drivers_lap_after_winner(last_laps)  # noqa
        for position in drivers_position_after_winner:
            print('{}-{} {} {}'.format(
                position.driver.id,
                position.driver.name,
                position.finished_laps,
                milliseconds_to_text(position.delay_after_winner)
            ))
