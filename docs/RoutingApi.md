# mailcow_sdk.RoutingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sender_dependent_transports**](RoutingApi.md#create_sender_dependent_transports) | **POST** /api/v1/add/relayhost | Create Sender-Dependent Transports
[**create_transport_maps**](RoutingApi.md#create_transport_maps) | **POST** /api/v1/add/transport | Create Transport Maps
[**delete_sender_dependent_transports**](RoutingApi.md#delete_sender_dependent_transports) | **POST** /api/v1/delete/relayhost | Delete Sender-Dependent Transports
[**delete_transport_maps**](RoutingApi.md#delete_transport_maps) | **POST** /api/v1/delete/transport | Delete Transport Maps
[**get_sender_dependent_transports**](RoutingApi.md#get_sender_dependent_transports) | **GET** /api/v1/get/relayhost/{id} | Get Sender-Dependent Transports
[**get_transport_maps**](RoutingApi.md#get_transport_maps) | **GET** /api/v1/get/transport/{id} | Get Transport Maps


# **create_sender_dependent_transports**
> CreateAlias200Response create_sender_dependent_transports(create_sender_dependent_transports_request=create_sender_dependent_transports_request)

Create Sender-Dependent Transports

Using this endpoint you can create Sender-Dependent Transports.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.create_sender_dependent_transports_request import CreateSenderDependentTransportsRequest
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
    api_instance = mailcow_sdk.RoutingApi(api_client)
    create_sender_dependent_transports_request = mailcow_sdk.CreateSenderDependentTransportsRequest() # CreateSenderDependentTransportsRequest |  (optional)

    try:
        # Create Sender-Dependent Transports
        api_response = api_instance.create_sender_dependent_transports(create_sender_dependent_transports_request=create_sender_dependent_transports_request)
        print("The response of RoutingApi->create_sender_dependent_transports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->create_sender_dependent_transports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sender_dependent_transports_request** | [**CreateSenderDependentTransportsRequest**](CreateSenderDependentTransportsRequest.md)|  | [optional] 

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

# **create_transport_maps**
> CreateAlias200Response create_transport_maps(create_transport_maps_request=create_transport_maps_request)

Create Transport Maps

Using this endpoint you can create Sender-Dependent Transports.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.create_transport_maps_request import CreateTransportMapsRequest
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
    api_instance = mailcow_sdk.RoutingApi(api_client)
    create_transport_maps_request = mailcow_sdk.CreateTransportMapsRequest() # CreateTransportMapsRequest |  (optional)

    try:
        # Create Transport Maps
        api_response = api_instance.create_transport_maps(create_transport_maps_request=create_transport_maps_request)
        print("The response of RoutingApi->create_transport_maps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->create_transport_maps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_transport_maps_request** | [**CreateTransportMapsRequest**](CreateTransportMapsRequest.md)|  | [optional] 

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

# **delete_sender_dependent_transports**
> CreateAlias200Response delete_sender_dependent_transports(delete_sender_dependent_transports_request=delete_sender_dependent_transports_request)

Delete Sender-Dependent Transports

Using this endpoint you can delete a Sender-Dependent Transport, for this you have to know its ID. You can get the ID using the GET method.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.delete_sender_dependent_transports_request import DeleteSenderDependentTransportsRequest
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
    api_instance = mailcow_sdk.RoutingApi(api_client)
    delete_sender_dependent_transports_request = mailcow_sdk.DeleteSenderDependentTransportsRequest() # DeleteSenderDependentTransportsRequest |  (optional)

    try:
        # Delete Sender-Dependent Transports
        api_response = api_instance.delete_sender_dependent_transports(delete_sender_dependent_transports_request=delete_sender_dependent_transports_request)
        print("The response of RoutingApi->delete_sender_dependent_transports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->delete_sender_dependent_transports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_sender_dependent_transports_request** | [**DeleteSenderDependentTransportsRequest**](DeleteSenderDependentTransportsRequest.md)|  | [optional] 

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

# **delete_transport_maps**
> CreateAlias200Response delete_transport_maps(delete_transport_maps_request=delete_transport_maps_request)

Delete Transport Maps

Using this endpoint you can delete a Transport Maps, for this you have to know its ID. You can get the ID using the GET method.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.delete_transport_maps_request import DeleteTransportMapsRequest
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
    api_instance = mailcow_sdk.RoutingApi(api_client)
    delete_transport_maps_request = mailcow_sdk.DeleteTransportMapsRequest() # DeleteTransportMapsRequest |  (optional)

    try:
        # Delete Transport Maps
        api_response = api_instance.delete_transport_maps(delete_transport_maps_request=delete_transport_maps_request)
        print("The response of RoutingApi->delete_transport_maps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->delete_transport_maps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_transport_maps_request** | [**DeleteTransportMapsRequest**](DeleteTransportMapsRequest.md)|  | [optional] 

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

# **get_sender_dependent_transports**
> get_sender_dependent_transports(id, x_api_key=x_api_key)

Get Sender-Dependent Transports

Using this endpoint you can get all Sender-Dependent Transports.

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
    api_instance = mailcow_sdk.RoutingApi(api_client)
    id = 'all' # str | id of entry you want to get
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get Sender-Dependent Transports
        api_instance.get_sender_dependent_transports(id, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling RoutingApi->get_sender_dependent_transports: %s\n" % e)
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

# **get_transport_maps**
> get_transport_maps(id, x_api_key=x_api_key)

Get Transport Maps

Using this endpoint you can get all Transport Maps.

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
    api_instance = mailcow_sdk.RoutingApi(api_client)
    id = 'all' # str | id of entry you want to get
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get Transport Maps
        api_instance.get_transport_maps(id, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling RoutingApi->get_transport_maps: %s\n" % e)
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

