# mailcow_sdk.CrossOriginResourceSharingCORSApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_cross_origin_resource_sharing__cors_settings**](CrossOriginResourceSharingCORSApi.md#edit_cross_origin_resource_sharing__cors_settings) | **POST** /api/v1/edit/cors | Edit Cross-Origin Resource Sharing (CORS) settings


# **edit_cross_origin_resource_sharing__cors_settings**
> edit_cross_origin_resource_sharing__cors_settings(edit_cross_origin_resource_sharing_cors_settings_request=edit_cross_origin_resource_sharing_cors_settings_request)

Edit Cross-Origin Resource Sharing (CORS) settings

This endpoint allows you to manage Cross-Origin Resource Sharing (CORS) settings for the API. CORS is a security feature implemented by web browsers to prevent unauthorized cross-origin requests. By editing the CORS settings, you can specify which domains and which methods are permitted to access the API resources from outside the mailcow domain.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.edit_cross_origin_resource_sharing_cors_settings_request import EditCrossOriginResourceSharingCORSSettingsRequest
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
    api_instance = mailcow_sdk.CrossOriginResourceSharingCORSApi(api_client)
    edit_cross_origin_resource_sharing_cors_settings_request = mailcow_sdk.EditCrossOriginResourceSharingCORSSettingsRequest() # EditCrossOriginResourceSharingCORSSettingsRequest |  (optional)

    try:
        # Edit Cross-Origin Resource Sharing (CORS) settings
        api_instance.edit_cross_origin_resource_sharing__cors_settings(edit_cross_origin_resource_sharing_cors_settings_request=edit_cross_origin_resource_sharing_cors_settings_request)
    except Exception as e:
        print("Exception when calling CrossOriginResourceSharingCORSApi->edit_cross_origin_resource_sharing__cors_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_cross_origin_resource_sharing_cors_settings_request** | [**EditCrossOriginResourceSharingCORSSettingsRequest**](EditCrossOriginResourceSharingCORSSettingsRequest.md)|  | [optional] 

### Return type

void (empty response body)

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

