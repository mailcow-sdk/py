import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestOAuthClientsApi(GeneratedApiTestCase):
    API_MODULE = "o_auth_clients_api"
    API_CLASS = "OAuthClientsApi"


if __name__ == '__main__':
    unittest.main()