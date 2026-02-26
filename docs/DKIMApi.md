# mailcow_sdk.DKIMApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dkim_key**](DKIMApi.md#delete_dkim_key) | **POST** /api/v1/delete/dkim | Delete DKIM Key
[**duplicate_dkim_key**](DKIMApi.md#duplicate_dkim_key) | **POST** /api/v1/add/dkim_duplicate | Duplicate DKIM Key
[**generate_dkim_key**](DKIMApi.md#generate_dkim_key) | **POST** /api/v1/add/dkim | Generate DKIM Key
[**get_dkim_key**](DKIMApi.md#get_dkim_key) | **GET** /api/v1/get/dkim/{domain} | Get DKIM Key


# **delete_dkim_key**
> CreateAlias200Response delete_dkim_key(request_body=request_body)

Delete DKIM Key

Using this endpoint a existing DKIM Key can be deleted

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
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
    api_instance = mailcow_sdk.DKIMApi(api_client)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Delete DKIM Key
        api_response = api_instance.delete_dkim_key(request_body=request_body)
        print("The response of DKIMApi->delete_dkim_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DKIMApi->delete_dkim_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**CreateAlias200Response**](CreateAlias200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_dkim_key**
> CreateAlias200Response duplicate_dkim_key(duplicate_dkim_key_request=duplicate_dkim_key_request)

Duplicate DKIM Key

Using this endpoint you can duplicate the DKIM Key of one domain.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.duplicate_dkim_key_request import DuplicateDKIMKeyRequest
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
    api_instance = mailcow_sdk.DKIMApi(api_client)
    duplicate_dkim_key_request = mailcow_sdk.DuplicateDKIMKeyRequest() # DuplicateDKIMKeyRequest |  (optional)

    try:
        # Duplicate DKIM Key
        api_response = api_instance.duplicate_dkim_key(duplicate_dkim_key_request=duplicate_dkim_key_request)
        print("The response of DKIMApi->duplicate_dkim_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DKIMApi->duplicate_dkim_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duplicate_dkim_key_request** | [**DuplicateDKIMKeyRequest**](DuplicateDKIMKeyRequest.md)|  | [optional] 

### Return type

[**CreateAlias200Response**](CreateAlias200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_dkim_key**
> CreateAlias200Response generate_dkim_key(generate_dkim_key_request=generate_dkim_key_request)

Generate DKIM Key

Using this endpoint you can generate new DKIM keys.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.generate_dkim_key_request import GenerateDKIMKeyRequest
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
    api_instance = mailcow_sdk.DKIMApi(api_client)
    generate_dkim_key_request = mailcow_sdk.GenerateDKIMKeyRequest() # GenerateDKIMKeyRequest |  (optional)

    try:
        # Generate DKIM Key
        api_response = api_instance.generate_dkim_key(generate_dkim_key_request=generate_dkim_key_request)
        print("The response of DKIMApi->generate_dkim_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DKIMApi->generate_dkim_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_dkim_key_request** | [**GenerateDKIMKeyRequest**](GenerateDKIMKeyRequest.md)|  | [optional] 

### Return type

[**CreateAlias200Response**](CreateAlias200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dkim_key**
> get_dkim_key(domain, x_api_key=x_api_key)

Get DKIM Key

Using this endpoint you can get the DKIM public key for a specific domain.

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
    api_instance = mailcow_sdk.DKIMApi(api_client)
    domain = 'domain_example' # str | name of domain
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get DKIM Key
        api_instance.get_dkim_key(domain, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling DKIMApi->get_dkim_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| name of domain | 
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

