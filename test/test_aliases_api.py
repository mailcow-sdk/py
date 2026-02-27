import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestAliasesApi(GeneratedApiTestCase):
    API_MODULE = "aliases_api"
    API_CLASS = "AliasesApi"


if __name__ == '__main__':
    unittest.main()