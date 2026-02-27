import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestOutgoingTlsPolicyMapOverridesApi(GeneratedApiTestCase):
    API_MODULE = "outgoing_tls_policy_map_overrides_api"
    API_CLASS = "OutgoingTlsPolicyMapOverridesApi"


if __name__ == '__main__':
    unittest.main()