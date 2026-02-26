# mailcow_sdk.Fail2BanApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_fail2_ban**](Fail2BanApi.md#edit_fail2_ban) | **POST** /api/v1/edit/fail2ban | Edit Fail2Ban
[**get_fail2_ban_config**](Fail2BanApi.md#get_fail2_ban_config) | **GET** /api/v1/get/fail2ban | Get Fail2Ban Config


# **edit_fail2_ban**
> CreateAlias200Response edit_fail2_ban(edit_fail2_ban_request=edit_fail2_ban_request)

Edit Fail2Ban

Using this endpoint you can edit the Fail2Ban config and black or whitelist new ips.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.edit_fail2_ban_request import EditFail2BanRequest
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
    api_instance = mailcow_sdk.Fail2BanApi(api_client)
    edit_fail2_ban_request = mailcow_sdk.EditFail2BanRequest() # EditFail2BanRequest |  (optional)

    try:
        # Edit Fail2Ban
        api_response = api_instance.edit_fail2_ban(edit_fail2_ban_request=edit_fail2_ban_request)
        print("The response of Fail2BanApi->edit_fail2_ban:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Fail2BanApi->edit_fail2_ban: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_fail2_ban_request** | [**EditFail2BanRequest**](EditFail2BanRequest.md)|  | [optional] 

### Return type

[**CreateAlias200Response**](CreateAlias200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fail2_ban_config**
> get_fail2_ban_config()

Get Fail2Ban Config

Gets the current Fail2Ban configuration.

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
    api_instance = mailcow_sdk.Fail2BanApi(api_client)

    try:
        # Get Fail2Ban Config
        api_instance.get_fail2_ban_config()
    except Exception as e:
        print("Exception when calling Fail2BanApi->get_fail2_ban_config: %s\n" % e)
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

