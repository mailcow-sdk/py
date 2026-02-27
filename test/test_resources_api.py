import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestResourcesApi(GeneratedApiTestCase):
    API_MODULE = "resources_api"
    API_CLASS = "ResourcesApi"


if __name__ == '__main__':
    unittest.main()