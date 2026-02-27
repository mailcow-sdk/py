import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestLogsApi(GeneratedApiTestCase):
    API_MODULE = "logs_api"
    API_CLASS = "LogsApi"


if __name__ == '__main__':
    unittest.main()