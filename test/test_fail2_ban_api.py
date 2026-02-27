import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestFail2BanApi(GeneratedApiTestCase):
    API_MODULE = "fail2_ban_api"
    API_CLASS = "Fail2BanApi"


if __name__ == '__main__':
    unittest.main()