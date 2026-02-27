import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestIdentityProviderApi(GeneratedApiTestCase):
    API_MODULE = "identity_provider_api"
    API_CLASS = "IdentityProviderApi"


if __name__ == '__main__':
    unittest.main()