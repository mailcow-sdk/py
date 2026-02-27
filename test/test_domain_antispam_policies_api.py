import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestDomainAntispamPoliciesApi(GeneratedApiTestCase):
    API_MODULE = "domain_antispam_policies_api"
    API_CLASS = "DomainAntispamPoliciesApi"


if __name__ == '__main__':
    unittest.main()