# mailcow_sdk.OAuthClientsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_o_auth_client**](OAuthClientsApi.md#create_o_auth_client) | **POST** /api/v1/add/oauth2-client | Create oAuth Client
[**delete_o_auth_client**](OAuthClientsApi.md#delete_o_auth_client) | **POST** /api/v1/delete/oauth2-client | Delete oAuth Client
[**get_o_auth_clients**](OAuthClientsApi.md#get_o_auth_clients) | **GET** /api/v1/get/oauth2-client/{id} | Get oAuth Clients


# **create_o_auth_client**
> CreateAlias200Response create_o_auth_client(create_o_auth_client_request=create_o_auth_client_request)

Create oAuth Client

Using this endpoint you can create a oAuth clients.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.create_o_auth_client_request import CreateOAuthClientRequest
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
    api_instance = mailcow_sdk.OAuthClientsApi(api_client)
    create_o_auth_client_request = mailcow_sdk.CreateOAuthClientRequest() # CreateOAuthClientRequest |  (optional)

    try:
        # Create oAuth Client
        api_response = api_instance.create_o_auth_client(create_o_auth_client_request=create_o_auth_client_request)
        print("The response of OAuthClientsApi->create_o_auth_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthClientsApi->create_o_auth_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_o_auth_client_request** | [**CreateOAuthClientRequest**](CreateOAuthClientRequest.md)|  | [optional] 

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

# **delete_o_auth_client**
> CreateAlias200Response delete_o_auth_client(delete_o_auth_client_request=delete_o_auth_client_request)

Delete oAuth Client

Using this endpoint you can delete a oAuth client, for this you have to know its ID. You can get the ID using the GET method.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.delete_o_auth_client_request import DeleteOAuthClientRequest
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
    api_instance = mailcow_sdk.OAuthClientsApi(api_client)
    delete_o_auth_client_request = mailcow_sdk.DeleteOAuthClientRequest() # DeleteOAuthClientRequest |  (optional)

    try:
        # Delete oAuth Client
        api_response = api_instance.delete_o_auth_client(delete_o_auth_client_request=delete_o_auth_client_request)
        print("The response of OAuthClientsApi->delete_o_auth_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthClientsApi->delete_o_auth_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_o_auth_client_request** | [**DeleteOAuthClientRequest**](DeleteOAuthClientRequest.md)|  | [optional] 

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

# **get_o_auth_clients**
> get_o_auth_clients(id, x_api_key=x_api_key)

Get oAuth Clients

Using this endpoint you can get all oAuth clients.

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
    api_instance = mailcow_sdk.OAuthClientsApi(api_client)
    id = 'all' # str | id of entry you want to get
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get oAuth Clients
        api_instance.get_o_auth_clients(id, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling OAuthClientsApi->get_o_auth_clients: %s\n" % e)
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

