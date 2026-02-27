import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestAppPasswordsApi(GeneratedApiTestCase):
    API_MODULE = "app_passwords_api"
    API_CLASS = "AppPasswordsApi"


if __name__ == '__main__':
    unittest.main()