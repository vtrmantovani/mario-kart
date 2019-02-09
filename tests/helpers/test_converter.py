import unittest

from mkart.exceptions.helper import HelperException
from mkart.helpers.converter import _create_driver, convert_text_to_lap
from mkart.models.driver import Driver
from mkart.models.lap import Lap


class TestHelperConverter(unittest.TestCase):

    def test_create_driver(self):
        driver = _create_driver(1, 'Joao')
        self.assertTrue(isinstance(driver, Driver))
        self.assertEquals(driver.id, 1)
        self.assertEquals(driver.name, 'Joao')

    def test_create_driver_with_id_empty(self):
        with self.assertRaises(HelperException) as error:
            _create_driver('', 'Joao')
        self.assertEqual(str(error.exception), 'Id is required')

    def test_create_driver_with_name_empty(self):
        with self.assertRaises(HelperException) as error:
            _create_driver(1, '')

        self.assertEqual(str(error.exception), 'Name is required')

    def test_convert_text_to_lap(self):
        line = '23:49:08.277      038 – F.MASSA                           1		1:02.852                        44,275'  # noqa
        lap = convert_text_to_lap(line)
        self.assertTrue(isinstance(lap, Lap))
        self.assertEquals(lap.number, '1')
        self.assertEquals(lap.average_speed, 44.275)
        self.assertEquals(lap.driver.id, '038')
        self.assertEquals(lap.driver.name, 'F.MASSA')
        self.assertEquals(lap.hour, 85789277)
        self.assertEquals(lap.duration, 62852)

    def test_convert_text_to_lap_without_pattern(self):
        with self.assertRaises(HelperException) as error:
            line = '1, 4 Joao'
            convert_text_to_lap(line)

        self.assertEqual(str(error.exception), 'Line 1, 4 Joao not match with pattern')  # noqa
