import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestRatelimitsApi(GeneratedApiTestCase):
    API_MODULE = "ratelimits_api"
    API_CLASS = "RatelimitsApi"


if __name__ == '__main__':
    unittest.main()