import unittest

from mkart.exceptions.manager import ManagerException


class TestManagerException(unittest.TestCase):

    def test_should_be_instance_from_exception(self):
        manager_exception = ManagerException()
        self.assertTrue(isinstance(manager_exception, Exception))
