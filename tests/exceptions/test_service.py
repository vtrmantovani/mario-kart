import unittest

from mkart.exceptions.service import ServiceException


class TestServiceException(unittest.TestCase):

    def test_should_be_instance_from_exception(self):
        service_exception = ServiceException()
        self.assertTrue(isinstance(service_exception, Exception))
