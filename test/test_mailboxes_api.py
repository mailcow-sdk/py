import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestMailboxesApi(GeneratedApiTestCase):
    API_MODULE = "mailboxes_api"
    API_CLASS = "MailboxesApi"


if __name__ == '__main__':
    unittest.main()