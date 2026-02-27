import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestRoutingApi(GeneratedApiTestCase):
    API_MODULE = "routing_api"
    API_CLASS = "RoutingApi"


if __name__ == '__main__':
    unittest.main()