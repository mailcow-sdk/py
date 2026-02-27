import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestDkimApi(GeneratedApiTestCase):
    API_MODULE = "dkim_api"
    API_CLASS = "DkimApi"


if __name__ == '__main__':
    unittest.main()