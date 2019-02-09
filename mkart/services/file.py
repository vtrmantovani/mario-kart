from mkart.exceptions.service import ServiceException


class FileService:

    def __init__(self, file):
        self._file = file

    def get_lines(self):
        try:
            file = open(self._file, "r")
            lines = file.readlines()

            if len(lines) == 0:
                raise ServiceException("File is empty")
            lines.pop(0)

            return lines

        except FileNotFoundError:
            raise ServiceException('File not found')
