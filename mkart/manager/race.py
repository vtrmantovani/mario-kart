from mkart.exceptions.manager import ManagerException
from mkart.exceptions.service import ServiceException
from mkart.helpers.converter import convert_text_to_lap
from mkart.services.file import FileService
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

    def _get_positions(self, laps):
        position_service = PositionService(laps)
        return position_service.get_positions()

    def show_result(self):
        try:
            lines = self._get_lines_file()
            laps = self._get_laps(lines)
            positions = self._get_positions(laps)

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
