import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestSingleSignOnApi(GeneratedApiTestCase):
    API_MODULE = "single_sign_on_api"
    API_CLASS = "SingleSignOnApi"


if __name__ == '__main__':
    unittest.main()