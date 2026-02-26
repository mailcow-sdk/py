# mailcow_sdk.QuarantineApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_mails_in_quarantine**](QuarantineApi.md#delete_mails_in_quarantine) | **POST** /api/v1/delete/qitem | Delete mails in Quarantine
[**get_mails_in_quarantine**](QuarantineApi.md#get_mails_in_quarantine) | **GET** /api/v1/get/quarantine/all | Get mails in Quarantine


# **delete_mails_in_quarantine**
> CreateAlias200Response delete_mails_in_quarantine(delete_mails_in_quarantine_request=delete_mails_in_quarantine_request)

Delete mails in Quarantine

Using this endpoint you can delete a email from quarantine, for this you have to know its ID. You can get the ID using the GET method.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.delete_mails_in_quarantine_request import DeleteMailsInQuarantineRequest
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
    api_instance = mailcow_sdk.QuarantineApi(api_client)
    delete_mails_in_quarantine_request = mailcow_sdk.DeleteMailsInQuarantineRequest() # DeleteMailsInQuarantineRequest |  (optional)

    try:
        # Delete mails in Quarantine
        api_response = api_instance.delete_mails_in_quarantine(delete_mails_in_quarantine_request=delete_mails_in_quarantine_request)
        print("The response of QuarantineApi->delete_mails_in_quarantine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuarantineApi->delete_mails_in_quarantine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_mails_in_quarantine_request** | [**DeleteMailsInQuarantineRequest**](DeleteMailsInQuarantineRequest.md)|  | [optional] 

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

# **get_mails_in_quarantine**
> get_mails_in_quarantine()

Get mails in Quarantine

Get all mails that are currently in Quarantine.

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
    api_instance = mailcow_sdk.QuarantineApi(api_client)

    try:
        # Get mails in Quarantine
        api_instance.get_mails_in_quarantine()
    except Exception as e:
        print("Exception when calling QuarantineApi->get_mails_in_quarantine: %s\n" % e)
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

