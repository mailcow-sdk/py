import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestDomainsApi(GeneratedApiTestCase):
    API_MODULE = "domains_api"
    API_CLASS = "DomainsApi"


if __name__ == '__main__':
    unittest.main()