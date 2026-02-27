import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestFordwardingHostsApi(GeneratedApiTestCase):
    API_MODULE = "fordwarding_hosts_api"
    API_CLASS = "FordwardingHostsApi"


if __name__ == '__main__':
    unittest.main()