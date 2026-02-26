# mailcow_sdk.FordwardingHostsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_forward_host**](FordwardingHostsApi.md#add_forward_host) | **POST** /api/v1/add/fwdhost | Add Forward Host
[**delete_forward_host**](FordwardingHostsApi.md#delete_forward_host) | **POST** /api/v1/delete/fwdhost | Delete Forward Host
[**get_forwarding_hosts**](FordwardingHostsApi.md#get_forwarding_hosts) | **GET** /api/v1/get/fwdhost/all | Get Forwarding Hosts


# **add_forward_host**
> CreateAlias200Response add_forward_host(add_forward_host_request=add_forward_host_request)

Add Forward Host

Add a new Forwarding host to mailcow. You can chose to enable or disable spam filtering of incoming emails by specifing `filter_spam` 0 = inactive, 1 = active.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.add_forward_host_request import AddForwardHostRequest
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
    api_instance = mailcow_sdk.FordwardingHostsApi(api_client)
    add_forward_host_request = mailcow_sdk.AddForwardHostRequest() # AddForwardHostRequest |  (optional)

    try:
        # Add Forward Host
        api_response = api_instance.add_forward_host(add_forward_host_request=add_forward_host_request)
        print("The response of FordwardingHostsApi->add_forward_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FordwardingHostsApi->add_forward_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_forward_host_request** | [**AddForwardHostRequest**](AddForwardHostRequest.md)|  | [optional] 

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

# **delete_forward_host**
> CreateAlias200Response delete_forward_host(delete_forward_host_request=delete_forward_host_request)

Delete Forward Host

Using this endpoint you can delete a forwarding host, in order to do so you need to know the IP of the host.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.delete_forward_host_request import DeleteForwardHostRequest
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
    api_instance = mailcow_sdk.FordwardingHostsApi(api_client)
    delete_forward_host_request = mailcow_sdk.DeleteForwardHostRequest() # DeleteForwardHostRequest |  (optional)

    try:
        # Delete Forward Host
        api_response = api_instance.delete_forward_host(delete_forward_host_request=delete_forward_host_request)
        print("The response of FordwardingHostsApi->delete_forward_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FordwardingHostsApi->delete_forward_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_forward_host_request** | [**DeleteForwardHostRequest**](DeleteForwardHostRequest.md)|  | [optional] 

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

# **get_forwarding_hosts**
> get_forwarding_hosts()

Get Forwarding Hosts

You can list all Forwarding Hosts in your mailcow.

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
    api_instance = mailcow_sdk.FordwardingHostsApi(api_client)

    try:
        # Get Forwarding Hosts
        api_instance.get_forwarding_hosts()
    except Exception as e:
        print("Exception when calling FordwardingHostsApi->get_forwarding_hosts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

