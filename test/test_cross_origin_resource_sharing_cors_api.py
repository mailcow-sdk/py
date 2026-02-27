import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestCrossOriginResourceSharingCorsApi(GeneratedApiTestCase):
    API_MODULE = "cross_origin_resource_sharing_cors_api"
    API_CLASS = "CrossOriginResourceSharingCorsApi"


if __name__ == '__main__':
    unittest.main()