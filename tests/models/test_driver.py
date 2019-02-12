import unittest

from mkart.models.driver import Driver


class TestDriver(unittest.TestCase):

    def test_create_driver(self):
        driver = Driver(1, 'F.MASSA')
        self.assertEqual(type(driver), Driver)
        self.assertEqual(driver.id, 1)
        self.assertEqual(driver.name, 'F.MASSA')

    def test_create_driver_with_average_speed(self):
        driver = Driver(1, 'F.MASSA')
        driver.average_speed = 43.1913
        self.assertEqual(type(driver), Driver)
        self.assertEqual(driver.id, 1)
        self.assertEqual(driver.name, 'F.MASSA')
        self.assertEqual(driver.average_speed, 43.1913)
