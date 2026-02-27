import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestQueueManagerApi(GeneratedApiTestCase):
    API_MODULE = "queue_manager_api"
    API_CLASS = "QueueManagerApi"


if __name__ == '__main__':
    unittest.main()