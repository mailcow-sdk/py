# mailcow_sdk.AliasesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alias**](AliasesApi.md#create_alias) | **POST** /api/v1/add/alias | Create alias
[**create_time_limited_alias**](AliasesApi.md#create_time_limited_alias) | **POST** /api/v1/add/time_limited_alias | Create time limited alias
[**delete_alias**](AliasesApi.md#delete_alias) | **POST** /api/v1/delete/alias | Delete alias
[**get_aliases**](AliasesApi.md#get_aliases) | **GET** /api/v1/get/alias/{id} | Get aliases
[**get_time_limited_aliases**](AliasesApi.md#get_time_limited_aliases) | **GET** /api/v1/get/time_limited_aliases/{mailbox} | Get time limited aliases
[**update_alias**](AliasesApi.md#update_alias) | **POST** /api/v1/edit/alias | Update alias


# **create_alias**
> CreateAlias200Response create_alias(create_alias_request=create_alias_request)

Create alias

You may create your own mailbox alias using this action. It takes a JSON object containing a domain informations.
Only one `goto*` option can be used, for ex. if you want learn as spam, then send just `goto_spam = 1` in request body.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.create_alias_request import CreateAliasRequest
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
    api_instance = mailcow_sdk.AliasesApi(api_client)
    create_alias_request = mailcow_sdk.CreateAliasRequest() # CreateAliasRequest |  (optional)

    try:
        # Create alias
        api_response = api_instance.create_alias(create_alias_request=create_alias_request)
        print("The response of AliasesApi->create_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasesApi->create_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_alias_request** | [**CreateAliasRequest**](CreateAliasRequest.md)|  | [optional] 

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

# **create_time_limited_alias**
> CreateAlias200Response create_time_limited_alias(create_time_limited_alias_request=create_time_limited_alias_request)

Create time limited alias

You may create a time limited alias using this action. It takes a JSON object containing a domain and mailbox informations. Mailcow will generate a random alias.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.create_time_limited_alias_request import CreateTimeLimitedAliasRequest
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
    api_instance = mailcow_sdk.AliasesApi(api_client)
    create_time_limited_alias_request = mailcow_sdk.CreateTimeLimitedAliasRequest() # CreateTimeLimitedAliasRequest |  (optional)

    try:
        # Create time limited alias
        api_response = api_instance.create_time_limited_alias(create_time_limited_alias_request=create_time_limited_alias_request)
        print("The response of AliasesApi->create_time_limited_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasesApi->create_time_limited_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_time_limited_alias_request** | [**CreateTimeLimitedAliasRequest**](CreateTimeLimitedAliasRequest.md)|  | [optional] 

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

# **delete_alias**
> CreateAlias200Response delete_alias(request_body=request_body)

Delete alias

You can delete one or more aliases.

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
    api_instance = mailcow_sdk.AliasesApi(api_client)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Delete alias
        api_response = api_instance.delete_alias(request_body=request_body)
        print("The response of AliasesApi->delete_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasesApi->delete_alias: %s\n" % e)
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

# **get_aliases**
> get_aliases(id, x_api_key=x_api_key)

Get aliases

You can list mailbox aliases existing in system.

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
    api_instance = mailcow_sdk.AliasesApi(api_client)
    id = 'all' # str | id of entry you want to get
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get aliases
        api_instance.get_aliases(id, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling AliasesApi->get_aliases: %s\n" % e)
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

# **get_time_limited_aliases**
> get_time_limited_aliases(mailbox, x_api_key=x_api_key)

Get time limited aliases

You can list time limited mailbox aliases existing in system.

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
    api_instance = mailcow_sdk.AliasesApi(api_client)
    mailbox = 'domain.tld' # str | mailbox you want to get aliasses from
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get time limited aliases
        api_instance.get_time_limited_aliases(mailbox, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling AliasesApi->get_time_limited_aliases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox** | **str**| mailbox you want to get aliasses from | 
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

# **update_alias**
> CreateAlias200Response update_alias(update_alias_request=update_alias_request)

Update alias

You can update one or more aliases per request. You can also send just attributes you want to change

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.update_alias_request import UpdateAliasRequest
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
    api_instance = mailcow_sdk.AliasesApi(api_client)
    update_alias_request = mailcow_sdk.UpdateAliasRequest() # UpdateAliasRequest |  (optional)

    try:
        # Update alias
        api_response = api_instance.update_alias(update_alias_request=update_alias_request)
        print("The response of AliasesApi->update_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasesApi->update_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_alias_request** | [**UpdateAliasRequest**](UpdateAliasRequest.md)|  | [optional] 

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

