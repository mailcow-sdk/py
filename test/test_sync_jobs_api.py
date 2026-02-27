import unittest

from test.generated_api_test_case import GeneratedApiTestCase


class TestSyncJobsApi(GeneratedApiTestCase):
    API_MODULE = "sync_jobs_api"
    API_CLASS = "SyncJobsApi"


if __name__ == '__main__':
    unittest.main()