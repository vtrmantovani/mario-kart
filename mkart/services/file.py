from mkart.exceptions.service import ServiceException


class FileService:

    def __init__(self, file_name):
        self._check_file_exists(file_name)

    def _check_file_exists(self, file_name):
        try:
            self._file = open(file_name, "r")
        except FileNotFoundError:
            raise ServiceException('File not found')

    def get_lines(self):
        lines = self._file.readlines()

        if len(lines) == 0:
            raise ServiceException("File is empty")

        lines.pop(0)

        return lines
