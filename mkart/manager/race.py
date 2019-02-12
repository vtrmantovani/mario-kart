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

    def _get_lines_file(self):
        file_service = FileService(self._file)
        return file_service.get_lines()

    def _get_laps(self, lines):
        return list(map(convert_text_to_lap, lines))

    def _get_last_laps_duration(self):
        lines = self._get_lines_file()
        laps = self._get_laps(lines)
        lap_service = LapService(laps)
        return lap_service.get_last_laps_duration()

    def _get_positions(self, laps):
        position_service = PositionService(laps)
        return position_service.get_positions()

    def _get_best_drivers_lap(self):
        lines = self._get_lines_file()
        laps = self._get_laps(lines)
        lap_service = LapService(laps)
        return lap_service.get_best_drivers_lap()

    def show_result(self):
        try:
            last_laps = self._get_last_laps_duration()
            positions = self._get_positions(last_laps)

            for position in positions:
                print('{} {} {} {} {}'.format(
                    position.number,
                    position.driver.id,
                    position.driver.name,
                    position.finished_laps,
                    milliseconds_to_text(position.duration)
                ))
        except ServiceException as e:
            raise ManagerException(e)

    def show_best_drivers_lap(self):
        try:
            best_drivers_lap = self._get_best_drivers_lap()
            for lap in best_drivers_lap:
                print('{} {} {} {}'.format(
                    lap.driver.id,
                    lap.driver.name,
                    lap.number,
                    milliseconds_to_text(lap.duration)
                ))
        except ServiceException as e:
            raise ManagerException(e)

    def show_best_lap_of_race(self):
        try:
            lines = self._get_lines_file()
            laps = self._get_laps(lines)
            lap_service = LapService(laps)
            best_lap = lap_service.get_best_lap_of_race()
            print('{} {} {}'.format(
                best_lap.driver.id,
                best_lap.driver.name,
                milliseconds_to_text(best_lap.duration)
            ))
        except ServiceException as e:
            raise ManagerException(e)
