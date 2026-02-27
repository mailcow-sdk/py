import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestDomainAdminApi(GeneratedApiTestCase):
    API_MODULE = "domain_admin_api"
    API_CLASS = "DomainAdminApi"


if __name__ == '__main__':
    unittest.main()