import unittest

from mkart.exceptions.helper import HelperException


class TestServiceException(unittest.TestCase):

    def test_should_be_instance_from_exception(self):
        helper_exception = HelperException()
        self.assertTrue(isinstance(helper_exception, Exception))
