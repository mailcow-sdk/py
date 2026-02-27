import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestQuarantineApi(GeneratedApiTestCase):
    API_MODULE = "quarantine_api"
    API_CLASS = "QuarantineApi"


if __name__ == '__main__':
    unittest.main()