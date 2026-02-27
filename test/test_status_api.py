import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestStatusApi(GeneratedApiTestCase):
    API_MODULE = "status_api"
    API_CLASS = "StatusApi"


if __name__ == '__main__':
    unittest.main()