# mailcow_sdk.SingleSignOnApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issue_domain_admin_sso_token**](SingleSignOnApi.md#issue_domain_admin_sso_token) | **POST** /api/v1/add/sso/domain-admin | Issue Domain Admin SSO token


# **issue_domain_admin_sso_token**
> issue_domain_admin_sso_token(issue_domain_admin_sso_token_request=issue_domain_admin_sso_token_request)

Issue Domain Admin SSO token

Using this endpoint you can issue a token for Domain Admin user. This token can be used for autologin Domain Admin user by using query_string var sso_token={token}. Token expiration time is 30s

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.issue_domain_admin_sso_token_request import IssueDomainAdminSSOTokenRequest
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
    api_instance = mailcow_sdk.SingleSignOnApi(api_client)
    issue_domain_admin_sso_token_request = mailcow_sdk.IssueDomainAdminSSOTokenRequest() # IssueDomainAdminSSOTokenRequest |  (optional)

    try:
        # Issue Domain Admin SSO token
        api_instance.issue_domain_admin_sso_token(issue_domain_admin_sso_token_request=issue_domain_admin_sso_token_request)
    except Exception as e:
        print("Exception when calling SingleSignOnApi->issue_domain_admin_sso_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_domain_admin_sso_token_request** | [**IssueDomainAdminSSOTokenRequest**](IssueDomainAdminSSOTokenRequest.md)|  | [optional] 

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

