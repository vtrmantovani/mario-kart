import os
import unittest

from mkart.exceptions.service import ServiceException
from mkart.services.file import FileService


class TestServiceFile(unittest.TestCase):

    def setUp(self):
        self.fixtures_path = os.path.join(os.path.dirname(__file__), '../fixtures')  # noqa

    def test_get_lines(self):
        file = FileService(self.fixtures_path + '/file_with_laps.log')
        result = file.get_lines()
        self.assertEquals(len(result), 2)
        self.assertEquals(result[0], '23:49:08.277      038 – MARIO                           1\t\t1:02.852                        44,275\n')  # noqa

    def test_get_lines_with_file_not_found(self):
        with self.assertRaises(ServiceException) as error:
            file = FileService(self.fixtures_path + '/file_not_found.log')
            file.get_lines()

        self.assertEqual(str(error.exception), 'File not found')

    def test_get_lines_with_file_empty(self):
        file = FileService(self.fixtures_path + '/file_empty.log')
        with self.assertRaises(ServiceException) as error:
            file.get_lines()

        self.assertEqual(str(error.exception), 'File is empty')
