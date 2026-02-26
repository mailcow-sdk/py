# mailcow_sdk.AddressRewritingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bcc_map**](AddressRewritingApi.md#create_bcc_map) | **POST** /api/v1/add/bcc | Create BCC Map
[**create_recipient_map**](AddressRewritingApi.md#create_recipient_map) | **POST** /api/v1/add/recipient_map | Create Recipient Map
[**delete_bcc_map**](AddressRewritingApi.md#delete_bcc_map) | **POST** /api/v1/delete/bcc | Delete BCC Map
[**delete_recipient_map**](AddressRewritingApi.md#delete_recipient_map) | **POST** /api/v1/delete/recipient_map | Delete Recipient Map
[**get_bcc_map**](AddressRewritingApi.md#get_bcc_map) | **GET** /api/v1/get/bcc/{id} | Get BCC Map
[**get_recipient_map**](AddressRewritingApi.md#get_recipient_map) | **GET** /api/v1/get/recipient_map/{id} | Get Recipient Map


# **create_bcc_map**
> CreateAlias200Response create_bcc_map(create_bcc_map_request=create_bcc_map_request)

Create BCC Map

Using this endpoint you can create a BCC map to forward all mails via a bcc for a given domain.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.create_bcc_map_request import CreateBCCMapRequest
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
    api_instance = mailcow_sdk.AddressRewritingApi(api_client)
    create_bcc_map_request = mailcow_sdk.CreateBCCMapRequest() # CreateBCCMapRequest |  (optional)

    try:
        # Create BCC Map
        api_response = api_instance.create_bcc_map(create_bcc_map_request=create_bcc_map_request)
        print("The response of AddressRewritingApi->create_bcc_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressRewritingApi->create_bcc_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bcc_map_request** | [**CreateBCCMapRequest**](CreateBCCMapRequest.md)|  | [optional] 

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

# **create_recipient_map**
> CreateAlias200Response create_recipient_map(create_recipient_map_request=create_recipient_map_request)

Create Recipient Map

Using this endpoint you can create a recipient map to forward all mails from one email address to another.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.create_recipient_map_request import CreateRecipientMapRequest
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
    api_instance = mailcow_sdk.AddressRewritingApi(api_client)
    create_recipient_map_request = mailcow_sdk.CreateRecipientMapRequest() # CreateRecipientMapRequest |  (optional)

    try:
        # Create Recipient Map
        api_response = api_instance.create_recipient_map(create_recipient_map_request=create_recipient_map_request)
        print("The response of AddressRewritingApi->create_recipient_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressRewritingApi->create_recipient_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_recipient_map_request** | [**CreateRecipientMapRequest**](CreateRecipientMapRequest.md)|  | [optional] 

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

# **delete_bcc_map**
> CreateAlias200Response delete_bcc_map(delete_bcc_map_request=delete_bcc_map_request)

Delete BCC Map

Using this endpoint you can delete a BCC map, for this you have to know its ID. You can get the ID using the GET method.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.delete_bcc_map_request import DeleteBCCMapRequest
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
    api_instance = mailcow_sdk.AddressRewritingApi(api_client)
    delete_bcc_map_request = mailcow_sdk.DeleteBCCMapRequest() # DeleteBCCMapRequest |  (optional)

    try:
        # Delete BCC Map
        api_response = api_instance.delete_bcc_map(delete_bcc_map_request=delete_bcc_map_request)
        print("The response of AddressRewritingApi->delete_bcc_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressRewritingApi->delete_bcc_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_bcc_map_request** | [**DeleteBCCMapRequest**](DeleteBCCMapRequest.md)|  | [optional] 

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

# **delete_recipient_map**
> CreateAlias200Response delete_recipient_map(delete_recipient_map_request=delete_recipient_map_request)

Delete Recipient Map

Using this endpoint you can delete a recipient map, for this you have to know its ID. You can get the ID using the GET method.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.delete_recipient_map_request import DeleteRecipientMapRequest
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
    api_instance = mailcow_sdk.AddressRewritingApi(api_client)
    delete_recipient_map_request = mailcow_sdk.DeleteRecipientMapRequest() # DeleteRecipientMapRequest |  (optional)

    try:
        # Delete Recipient Map
        api_response = api_instance.delete_recipient_map(delete_recipient_map_request=delete_recipient_map_request)
        print("The response of AddressRewritingApi->delete_recipient_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressRewritingApi->delete_recipient_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_recipient_map_request** | [**DeleteRecipientMapRequest**](DeleteRecipientMapRequest.md)|  | [optional] 

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

# **get_bcc_map**
> get_bcc_map(id, x_api_key=x_api_key)

Get BCC Map

Using this endpoint you can get all BCC maps.

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
    api_instance = mailcow_sdk.AddressRewritingApi(api_client)
    id = 'all' # str | id of entry you want to get
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get BCC Map
        api_instance.get_bcc_map(id, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling AddressRewritingApi->get_bcc_map: %s\n" % e)
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

# **get_recipient_map**
> get_recipient_map(id, x_api_key=x_api_key)

Get Recipient Map

Using this endpoint you can get all recipient maps.

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
    api_instance = mailcow_sdk.AddressRewritingApi(api_client)
    id = 'all' # str | id of entry you want to get
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get Recipient Map
        api_instance.get_recipient_map(id, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling AddressRewritingApi->get_recipient_map: %s\n" % e)
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

