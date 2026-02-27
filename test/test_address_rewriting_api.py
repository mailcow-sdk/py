import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestAddressRewritingApi(GeneratedApiTestCase):
    API_MODULE = "address_rewriting_api"
    API_CLASS = "AddressRewritingApi"


if __name__ == '__main__':
    unittest.main()