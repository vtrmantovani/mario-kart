import unittest

from mkart.models.driver import Driver


class TestDriver(unittest.TestCase):

    def test_create_driver(self):
        driver = Driver(1, 'F.MASSA')
        self.assertEqual(type(driver), Driver)
        self.assertEqual(driver.id, 1)
        self.assertEqual(driver.name, 'F.MASSA')
