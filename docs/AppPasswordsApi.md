# mailcow_sdk.AppPasswordsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_password**](AppPasswordsApi.md#create_app_password) | **POST** /api/v1/add/app-passwd | Create App Password
[**delete_app_password**](AppPasswordsApi.md#delete_app_password) | **POST** /api/v1/delete/app-passwd | Delete App Password
[**get_app_password**](AppPasswordsApi.md#get_app_password) | **GET** /api/v1/get/app-passwd/all/{mailbox} | Get App Password


# **create_app_password**
> CreateAlias200Response create_app_password(create_app_password_request=create_app_password_request)

Create App Password

Using this endpoint you can create a new app password for a specific mailbox.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.create_app_password_request import CreateAppPasswordRequest
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
    api_instance = mailcow_sdk.AppPasswordsApi(api_client)
    create_app_password_request = mailcow_sdk.CreateAppPasswordRequest() # CreateAppPasswordRequest |  (optional)

    try:
        # Create App Password
        api_response = api_instance.create_app_password(create_app_password_request=create_app_password_request)
        print("The response of AppPasswordsApi->create_app_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPasswordsApi->create_app_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_app_password_request** | [**CreateAppPasswordRequest**](CreateAppPasswordRequest.md)|  | [optional] 

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

# **delete_app_password**
> CreateAlias200Response delete_app_password(delete_app_password_request=delete_app_password_request)

Delete App Password

Using this endpoint you can delete a single app password.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.delete_app_password_request import DeleteAppPasswordRequest
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
    api_instance = mailcow_sdk.AppPasswordsApi(api_client)
    delete_app_password_request = mailcow_sdk.DeleteAppPasswordRequest() # DeleteAppPasswordRequest |  (optional)

    try:
        # Delete App Password
        api_response = api_instance.delete_app_password(delete_app_password_request=delete_app_password_request)
        print("The response of AppPasswordsApi->delete_app_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPasswordsApi->delete_app_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_app_password_request** | [**DeleteAppPasswordRequest**](DeleteAppPasswordRequest.md)|  | [optional] 

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

# **get_app_password**
> get_app_password(mailbox, x_api_key=x_api_key)

Get App Password

Using this endpoint you can get all app passwords from a specific mailbox.

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
    api_instance = mailcow_sdk.AppPasswordsApi(api_client)
    mailbox = 'hello@mailcow.email' # str | mailbox of entry you want to get
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get App Password
        api_instance.get_app_password(mailbox, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling AppPasswordsApi->get_app_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox** | **str**| mailbox of entry you want to get | 
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

