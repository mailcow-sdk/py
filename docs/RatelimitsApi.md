# mailcow_sdk.RatelimitsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_domain_ratelimits**](RatelimitsApi.md#edit_domain_ratelimits) | **POST** /api/v1/edit/rl-domain/ | Edit domain ratelimits
[**edit_mailbox_ratelimits**](RatelimitsApi.md#edit_mailbox_ratelimits) | **POST** /api/v1/edit/rl-mbox/ | Edit mailbox ratelimits
[**get_domain_ratelimits**](RatelimitsApi.md#get_domain_ratelimits) | **GET** /api/v1/get/rl-domain/{domain} | Get domain ratelimits
[**get_mailbox_ratelimits**](RatelimitsApi.md#get_mailbox_ratelimits) | **GET** /api/v1/get/rl-mbox/{mailbox} | Get mailbox ratelimits


# **edit_domain_ratelimits**
> CreateAlias200Response edit_domain_ratelimits(edit_domain_ratelimits_request=edit_domain_ratelimits_request)

Edit domain ratelimits

Using this endpoint you can edit the ratelimits for a certain domains.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.edit_domain_ratelimits_request import EditDomainRatelimitsRequest
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
    api_instance = mailcow_sdk.RatelimitsApi(api_client)
    edit_domain_ratelimits_request = mailcow_sdk.EditDomainRatelimitsRequest() # EditDomainRatelimitsRequest |  (optional)

    try:
        # Edit domain ratelimits
        api_response = api_instance.edit_domain_ratelimits(edit_domain_ratelimits_request=edit_domain_ratelimits_request)
        print("The response of RatelimitsApi->edit_domain_ratelimits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatelimitsApi->edit_domain_ratelimits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_domain_ratelimits_request** | [**EditDomainRatelimitsRequest**](EditDomainRatelimitsRequest.md)|  | [optional] 

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

# **edit_mailbox_ratelimits**
> CreateAlias200Response edit_mailbox_ratelimits(edit_mailbox_ratelimits_request=edit_mailbox_ratelimits_request)

Edit mailbox ratelimits

Using this endpoint you can edit the ratelimits for a certain mailbox.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.edit_mailbox_ratelimits_request import EditMailboxRatelimitsRequest
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
    api_instance = mailcow_sdk.RatelimitsApi(api_client)
    edit_mailbox_ratelimits_request = mailcow_sdk.EditMailboxRatelimitsRequest() # EditMailboxRatelimitsRequest |  (optional)

    try:
        # Edit mailbox ratelimits
        api_response = api_instance.edit_mailbox_ratelimits(edit_mailbox_ratelimits_request=edit_mailbox_ratelimits_request)
        print("The response of RatelimitsApi->edit_mailbox_ratelimits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatelimitsApi->edit_mailbox_ratelimits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_mailbox_ratelimits_request** | [**EditMailboxRatelimitsRequest**](EditMailboxRatelimitsRequest.md)|  | [optional] 

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

# **get_domain_ratelimits**
> get_domain_ratelimits(domain, x_api_key=x_api_key)

Get domain ratelimits

Using this endpoint you can get the ratelimits for a certain domains. You can use all for all domain.

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
    api_instance = mailcow_sdk.RatelimitsApi(api_client)
    domain = 'domain_example' # str | name of domain or all
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get domain ratelimits
        api_instance.get_domain_ratelimits(domain, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling RatelimitsApi->get_domain_ratelimits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| name of domain or all | 
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

# **get_mailbox_ratelimits**
> get_mailbox_ratelimits(mailbox, x_api_key=x_api_key)

Get mailbox ratelimits

Using this endpoint you can get the ratelimits for a certain mailbox. You can use all for all mailboxes.

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
    api_instance = mailcow_sdk.RatelimitsApi(api_client)
    mailbox = 'mailbox_example' # str | name of mailbox or all
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get mailbox ratelimits
        api_instance.get_mailbox_ratelimits(mailbox, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling RatelimitsApi->get_mailbox_ratelimits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox** | **str**| name of mailbox or all | 
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

