# mailcow_sdk.LogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_acme_logs**](LogsApi.md#get_acme_logs) | **GET** /api/v1/get/logs/acme/{count} | Get ACME logs
[**get_api_logs**](LogsApi.md#get_api_logs) | **GET** /api/v1/get/logs/api/{count} | Get Api logs
[**get_autodiscover_logs**](LogsApi.md#get_autodiscover_logs) | **GET** /api/v1/get/logs/autodiscover/{count} | Get Autodiscover logs
[**get_dovecot_logs**](LogsApi.md#get_dovecot_logs) | **GET** /api/v1/get/logs/dovecot/{count} | Get Dovecot logs
[**get_netfilter_logs**](LogsApi.md#get_netfilter_logs) | **GET** /api/v1/get/logs/netfilter/{count} | Get Netfilter logs
[**get_postfix_logs**](LogsApi.md#get_postfix_logs) | **GET** /api/v1/get/logs/postfix/{count} | Get Postfix logs
[**get_ratelimit_logs**](LogsApi.md#get_ratelimit_logs) | **GET** /api/v1/get/logs/ratelimited/{count} | Get Ratelimit logs
[**get_rspamd_logs**](LogsApi.md#get_rspamd_logs) | **GET** /api/v1/get/logs/rspamd-history/{count} | Get Rspamd logs
[**get_sogo_logs**](LogsApi.md#get_sogo_logs) | **GET** /api/v1/get/logs/sogo/{count} | Get SOGo logs
[**get_watchdog_logs**](LogsApi.md#get_watchdog_logs) | **GET** /api/v1/get/logs/watchdog/{count} | Get Watchdog logs


# **get_acme_logs**
> get_acme_logs(count, x_api_key=x_api_key)

Get ACME logs

This Api endpoint lists all ACME logs from issued Lets Enctypts certificates.
Tip: You can limit how many logs you want to get by using `/<count>` at the end of the api url.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mailcow_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mailcow_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailcow_sdk.LogsApi(api_client)
    count = 3.4 # float | Number of logs to return
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get ACME logs
        api_instance.get_acme_logs(count, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling LogsApi->get_acme_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **float**| Number of logs to return | 
 **x_api_key** | **str**| e.g. api-key-string | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_logs**
> get_api_logs(count, x_api_key=x_api_key)

Get Api logs

This Api endpoint lists all Api logs.
Tip: You can limit how many logs you want to get by using `/<count>` at the end of the api url.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mailcow_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mailcow_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailcow_sdk.LogsApi(api_client)
    count = 3.4 # float | Number of logs to return
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get Api logs
        api_instance.get_api_logs(count, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling LogsApi->get_api_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **float**| Number of logs to return | 
 **x_api_key** | **str**| e.g. api-key-string | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_autodiscover_logs**
> get_autodiscover_logs(count, x_api_key=x_api_key)

Get Autodiscover logs

This Api endpoint lists all Autodiscover logs.
Tip: You can limit how many logs you want to get by using `/<count>` at the end of the api url.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mailcow_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mailcow_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailcow_sdk.LogsApi(api_client)
    count = 3.4 # float | Number of logs to return
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get Autodiscover logs
        api_instance.get_autodiscover_logs(count, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling LogsApi->get_autodiscover_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **float**| Number of logs to return | 
 **x_api_key** | **str**| e.g. api-key-string | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dovecot_logs**
> get_dovecot_logs(count, x_api_key=x_api_key)

Get Dovecot logs

This Api endpoint lists all Dovecot logs.
Tip: You can limit how many logs you want to get by using `/<count>` at the end of the api url.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mailcow_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mailcow_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailcow_sdk.LogsApi(api_client)
    count = 3.4 # float | Number of logs to return
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get Dovecot logs
        api_instance.get_dovecot_logs(count, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling LogsApi->get_dovecot_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **float**| Number of logs to return | 
 **x_api_key** | **str**| e.g. api-key-string | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netfilter_logs**
> get_netfilter_logs(count, x_api_key=x_api_key)

Get Netfilter logs

This Api endpoint lists all Netfilter logs.
Tip: You can limit how many logs you want to get by using `/<count>` at the end of the api url.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mailcow_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mailcow_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailcow_sdk.LogsApi(api_client)
    count = 3.4 # float | Number of logs to return
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get Netfilter logs
        api_instance.get_netfilter_logs(count, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling LogsApi->get_netfilter_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **float**| Number of logs to return | 
 **x_api_key** | **str**| e.g. api-key-string | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_postfix_logs**
> get_postfix_logs(count, x_api_key=x_api_key)

Get Postfix logs

This Api endpoint lists all Postfix logs.
Tip: You can limit how many logs you want to get by using `/<count>` at the end of the api url.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mailcow_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mailcow_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailcow_sdk.LogsApi(api_client)
    count = 3.4 # float | Number of logs to return
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get Postfix logs
        api_instance.get_postfix_logs(count, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling LogsApi->get_postfix_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **float**| Number of logs to return | 
 **x_api_key** | **str**| e.g. api-key-string | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ratelimit_logs**
> get_ratelimit_logs(count, x_api_key=x_api_key)

Get Ratelimit logs

This Api endpoint lists all Ratelimit logs.
Tip: You can limit how many logs you want to get by using `/<count>` at the end of the api url.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mailcow_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mailcow_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailcow_sdk.LogsApi(api_client)
    count = 3.4 # float | Number of logs to return
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get Ratelimit logs
        api_instance.get_ratelimit_logs(count, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling LogsApi->get_ratelimit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **float**| Number of logs to return | 
 **x_api_key** | **str**| e.g. api-key-string | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rspamd_logs**
> get_rspamd_logs(count, x_api_key=x_api_key)

Get Rspamd logs

This Api endpoint lists all Rspamd logs.
Tip: You can limit how many logs you want to get by using `/<count>` at the end of the api url.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mailcow_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mailcow_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailcow_sdk.LogsApi(api_client)
    count = 3.4 # float | Number of logs to return
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get Rspamd logs
        api_instance.get_rspamd_logs(count, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling LogsApi->get_rspamd_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **float**| Number of logs to return | 
 **x_api_key** | **str**| e.g. api-key-string | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sogo_logs**
> get_sogo_logs(count, x_api_key=x_api_key)

Get SOGo logs

This Api endpoint lists all SOGo logs.
Tip: You can limit how many logs you want to get by using `/<count>` at the end of the api url.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mailcow_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mailcow_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailcow_sdk.LogsApi(api_client)
    count = 3.4 # float | Number of logs to return
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get SOGo logs
        api_instance.get_sogo_logs(count, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling LogsApi->get_sogo_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **float**| Number of logs to return | 
 **x_api_key** | **str**| e.g. api-key-string | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_watchdog_logs**
> get_watchdog_logs(count, x_api_key=x_api_key)

Get Watchdog logs

This Api endpoint lists all Watchdog logs.
Tip: You can limit how many logs you want to get by using `/<count>` at the end of the api url.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mailcow_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mailcow_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailcow_sdk.LogsApi(api_client)
    count = 3.4 # float | Number of logs to return
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get Watchdog logs
        api_instance.get_watchdog_logs(count, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling LogsApi->get_watchdog_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **float**| Number of logs to return | 
 **x_api_key** | **str**| e.g. api-key-string | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

