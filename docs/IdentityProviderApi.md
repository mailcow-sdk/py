# mailcow_sdk.IdentityProviderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_external_identity_provider_settings**](IdentityProviderApi.md#edit_external_identity_provider_settings) | **POST** /api/v1/edit/identity-provider | Edit external Identity Provider


# **edit_external_identity_provider_settings**
> edit_external_identity_provider_settings(edit_external_identity_provider_settings_request=edit_external_identity_provider_settings_request)

Edit external Identity Provider

Configure an external Identity Provider to use as user authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.edit_external_identity_provider_settings_request import EditExternalIdentityProviderSettingsRequest
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
    api_instance = mailcow_sdk.IdentityProviderApi(api_client)
    edit_external_identity_provider_settings_request = {"items":["identity-provider"],"attr":{"authsource":"keycloak","server_url":"https://auth.mailcow.tld","realm":"mailcow","client_id":"mailcow_client","client_secret":"Xy7GdPqvJ9m3R8sT2LkVZ5W1oNbCaYQf","redirect_url":"https://mail.mailcow.tld","redirect_url_extra":["https://extramail.mailcow.tld"],"version":"26.1.3","default_template":"Default","mappers":["small_mbox","medium_mbox"],"templates":["small","medium"],"ignore_ssl_error":true,"mailpassword_flow":true,"periodic_sync":true,"import_users":true,"sync_interval":30}} # EditExternalIdentityProviderSettingsRequest |  (optional)

    try:
        # Edit external Identity Provider
        api_instance.edit_external_identity_provider_settings(edit_external_identity_provider_settings_request=edit_external_identity_provider_settings_request)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->edit_external_identity_provider_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_external_identity_provider_settings_request** | [**EditExternalIdentityProviderSettingsRequest**](EditExternalIdentityProviderSettingsRequest.md)|  | [optional] 

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

