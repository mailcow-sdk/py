# mailcow_sdk.DomainAntispamPoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_domain_policy**](DomainAntispamPoliciesApi.md#create_domain_policy) | **POST** /api/v1/add/domain-policy | Create domain policy
[**delete_domain_policy**](DomainAntispamPoliciesApi.md#delete_domain_policy) | **POST** /api/v1/delete/domain-policy | Delete domain policy
[**list_blacklist_domain_policy**](DomainAntispamPoliciesApi.md#list_blacklist_domain_policy) | **GET** /api/v1/get/policy_bl_domain/{domain} | List blacklist domain policy
[**list_whitelist_domain_policy**](DomainAntispamPoliciesApi.md#list_whitelist_domain_policy) | **GET** /api/v1/get/policy_wl_domain/{domain} | List whitelist domain policy


# **create_domain_policy**
> CreateAlias200Response create_domain_policy(create_domain_policy_request=create_domain_policy_request)

Create domain policy

You may create your own domain policy using this action. It takes a JSON object containing a domain informations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.create_domain_policy_request import CreateDomainPolicyRequest
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
    api_instance = mailcow_sdk.DomainAntispamPoliciesApi(api_client)
    create_domain_policy_request = mailcow_sdk.CreateDomainPolicyRequest() # CreateDomainPolicyRequest |  (optional)

    try:
        # Create domain policy
        api_response = api_instance.create_domain_policy(create_domain_policy_request=create_domain_policy_request)
        print("The response of DomainAntispamPoliciesApi->create_domain_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAntispamPoliciesApi->create_domain_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_domain_policy_request** | [**CreateDomainPolicyRequest**](CreateDomainPolicyRequest.md)|  | [optional] 

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

# **delete_domain_policy**
> CreateAlias200Response delete_domain_policy(delete_domain_policy_request=delete_domain_policy_request)

Delete domain policy

You can delete one o more domain policies.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.delete_domain_policy_request import DeleteDomainPolicyRequest
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
    api_instance = mailcow_sdk.DomainAntispamPoliciesApi(api_client)
    delete_domain_policy_request = mailcow_sdk.DeleteDomainPolicyRequest() # DeleteDomainPolicyRequest |  (optional)

    try:
        # Delete domain policy
        api_response = api_instance.delete_domain_policy(delete_domain_policy_request=delete_domain_policy_request)
        print("The response of DomainAntispamPoliciesApi->delete_domain_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAntispamPoliciesApi->delete_domain_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_domain_policy_request** | [**DeleteDomainPolicyRequest**](DeleteDomainPolicyRequest.md)|  | [optional] 

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

# **list_blacklist_domain_policy**
> list_blacklist_domain_policy(domain, x_api_key=x_api_key)

List blacklist domain policy

You can list all blacklist policies per domain.

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
    api_instance = mailcow_sdk.DomainAntispamPoliciesApi(api_client)
    domain = 'domain_example' # str | name of domain
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # List blacklist domain policy
        api_instance.list_blacklist_domain_policy(domain, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling DomainAntispamPoliciesApi->list_blacklist_domain_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| name of domain | 
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

# **list_whitelist_domain_policy**
> list_whitelist_domain_policy(domain, x_api_key=x_api_key)

List whitelist domain policy

You can list all whitelist policies per domain.

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
    api_instance = mailcow_sdk.DomainAntispamPoliciesApi(api_client)
    domain = 'domain_example' # str | name of domain
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # List whitelist domain policy
        api_instance.list_whitelist_domain_policy(domain, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling DomainAntispamPoliciesApi->list_whitelist_domain_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| name of domain | 
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

