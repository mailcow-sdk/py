# mailcow_sdk.OutgoingTLSPolicyMapOverridesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tls_policy_map**](OutgoingTLSPolicyMapOverridesApi.md#create_tls_policy_map) | **POST** /api/v1/add/tls-policy-map | Create TLS Policy Map
[**delete_tls_policy_map**](OutgoingTLSPolicyMapOverridesApi.md#delete_tls_policy_map) | **POST** /api/v1/delete/tls-policy-map | Delete TLS Policy Map
[**get_tls_policy_map**](OutgoingTLSPolicyMapOverridesApi.md#get_tls_policy_map) | **GET** /api/v1/get/tls-policy-map/{id} | Get TLS Policy Map


# **create_tls_policy_map**
> CreateAlias200Response create_tls_policy_map(create_tls_policy_map_request=create_tls_policy_map_request)

Create TLS Policy Map

Using this endpoint you can create a TLS policy map override.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.create_tls_policy_map_request import CreateTLSPolicyMapRequest
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
    api_instance = mailcow_sdk.OutgoingTLSPolicyMapOverridesApi(api_client)
    create_tls_policy_map_request = mailcow_sdk.CreateTLSPolicyMapRequest() # CreateTLSPolicyMapRequest |  (optional)

    try:
        # Create TLS Policy Map
        api_response = api_instance.create_tls_policy_map(create_tls_policy_map_request=create_tls_policy_map_request)
        print("The response of OutgoingTLSPolicyMapOverridesApi->create_tls_policy_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutgoingTLSPolicyMapOverridesApi->create_tls_policy_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tls_policy_map_request** | [**CreateTLSPolicyMapRequest**](CreateTLSPolicyMapRequest.md)|  | [optional] 

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

# **delete_tls_policy_map**
> CreateAlias200Response delete_tls_policy_map(delete_tls_policy_map_request=delete_tls_policy_map_request)

Delete TLS Policy Map

Using this endpoint you can delete a TLS Policy Map, for this you have to know its ID. You can get the ID using the GET method.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.delete_tls_policy_map_request import DeleteTLSPolicyMapRequest
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
    api_instance = mailcow_sdk.OutgoingTLSPolicyMapOverridesApi(api_client)
    delete_tls_policy_map_request = mailcow_sdk.DeleteTLSPolicyMapRequest() # DeleteTLSPolicyMapRequest |  (optional)

    try:
        # Delete TLS Policy Map
        api_response = api_instance.delete_tls_policy_map(delete_tls_policy_map_request=delete_tls_policy_map_request)
        print("The response of OutgoingTLSPolicyMapOverridesApi->delete_tls_policy_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutgoingTLSPolicyMapOverridesApi->delete_tls_policy_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_tls_policy_map_request** | [**DeleteTLSPolicyMapRequest**](DeleteTLSPolicyMapRequest.md)|  | [optional] 

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

# **get_tls_policy_map**
> get_tls_policy_map(id, x_api_key=x_api_key)

Get TLS Policy Map

Using this endpoint you can get all TLS policy map override maps.

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
    api_instance = mailcow_sdk.OutgoingTLSPolicyMapOverridesApi(api_client)
    id = 'all' # str | id of entry you want to get
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get TLS Policy Map
        api_instance.get_tls_policy_map(id, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling OutgoingTLSPolicyMapOverridesApi->get_tls_policy_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of entry you want to get | 
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

