import importlib
import inspect
import unittest
from unittest.mock import patch

from mailcow_sdk.api_client import ApiClient
from mailcow_sdk.configuration import Configuration
from mailcow_sdk.exceptions import ApiException


class GeneratedApiTestCase(unittest.TestCase):
    API_MODULE = None
    API_CLASS = None

    def setUp(self):
        cfg = Configuration(host="https://mailcow.example.test")
        cfg.api_key["ApiKeyAuth"] = "test-api-key"
        self.api_client = ApiClient(cfg)
        api_cls = self._api_class()
        self.api = api_cls(self.api_client)

    @classmethod
    def _api_class(cls):
        module = importlib.import_module(f"mailcow_sdk.api.{cls.API_MODULE}")
        return getattr(module, cls.API_CLASS)

    def _required_serializer_kwargs(self, method):
        kwargs = {}
        for name, parameter in inspect.signature(method).parameters.items():
            if name == "self":
                continue
            if parameter.default is not inspect._empty:
                continue
            if name == "_host_index":
                kwargs[name] = 0
            elif name in {"_request_auth", "_content_type", "_headers"}:
                kwargs[name] = None
            else:
                kwargs[name] = self._sample_value(name)
        return kwargs

    def _sample_value(self, name):
        if "mailbox" in name:
            return "user@example.test"
        if "domain" in name:
            return "example.test"
        if name == "count":
            return 10
        if name in {"id", "username"}:
            return "value/with space"
        if name.endswith("_request"):
            return None
        return "sample"

    def test_request_serializers_build_method_url_headers_body(self):
        serializer_names = [n for n in dir(self.api) if n.endswith("_serialize")]
        self.assertGreater(len(serializer_names), 0)

        for serializer_name in serializer_names:
            serializer = getattr(self.api, serializer_name)
            kwargs = self._required_serializer_kwargs(serializer)
            with self.subTest(serializer=serializer_name):
                method, url, headers, body, post_params = serializer(**kwargs)
                self.assertIn(method, {"GET", "POST"})
                self.assertIn("/api/v1/", url)
                self.assertNotIn("{", url)
                self.assertEqual(headers.get("X-API-Key"), "test-api-key")
                if body is not None:
                    self.assertTrue(isinstance(body, (dict, list, str, int, float, bool)))

    def test_first_operation_propagates_api_exception_with_status(self):
        operations = [
            n for n in dir(self.api)
            if not n.startswith("_")
            and not n.endswith("_with_http_info")
            and not n.endswith("_without_preload_content")
            and callable(getattr(self.api, n))
        ]
        self.assertGreater(len(operations), 0)
        op_name = sorted(operations)[0]
        op = getattr(self.api, op_name)

        kwargs = {}
        for name, parameter in inspect.signature(op).parameters.items():
            if name == "self":
                continue
            if parameter.default is inspect._empty:
                kwargs[name] = self._sample_value(name)

        with patch.object(self.api_client, "call_api", side_effect=ApiException(status=401, reason="Unauthorized", body='{"type":"danger"}')):  # noqa: E501
            with self.assertRaises(ApiException) as exc:
                op(**kwargs)
            self.assertEqual(exc.exception.status, 401)

