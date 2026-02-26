# mailcow_sdk.DomainAdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_domain_admin_user**](DomainAdminApi.md#create_domain_admin_user) | **POST** /api/v1/add/domain-admin | Create Domain Admin user
[**delete_domain_admin**](DomainAdminApi.md#delete_domain_admin) | **POST** /api/v1/delete/domain-admin | Delete Domain Admin
[**edit_domain_admin_acl**](DomainAdminApi.md#edit_domain_admin_acl) | **POST** /api/v1/edit/da-acl | Edit Domain Admin ACL
[**edit_domain_admin_user**](DomainAdminApi.md#edit_domain_admin_user) | **POST** /api/v1/edit/domain-admin | Edit Domain Admin user
[**get_domain_admins**](DomainAdminApi.md#get_domain_admins) | **GET** /api/v1/get/domain-admin/all | Get Domain Admins


# **create_domain_admin_user**
> CreateAlias200Response create_domain_admin_user(create_domain_admin_user_request=create_domain_admin_user_request)

Create Domain Admin user

Using this endpoint you can create a new Domain Admin user. This user has full control over a domain, and can create new mailboxes and aliases.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.create_domain_admin_user_request import CreateDomainAdminUserRequest
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
    api_instance = mailcow_sdk.DomainAdminApi(api_client)
    create_domain_admin_user_request = mailcow_sdk.CreateDomainAdminUserRequest() # CreateDomainAdminUserRequest |  (optional)

    try:
        # Create Domain Admin user
        api_response = api_instance.create_domain_admin_user(create_domain_admin_user_request=create_domain_admin_user_request)
        print("The response of DomainAdminApi->create_domain_admin_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAdminApi->create_domain_admin_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_domain_admin_user_request** | [**CreateDomainAdminUserRequest**](CreateDomainAdminUserRequest.md)|  | [optional] 

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

# **delete_domain_admin**
> CreateAlias200Response delete_domain_admin(delete_domain_admin_request=delete_domain_admin_request)

Delete Domain Admin

Using this endpoint a existing Domain Admin user can be deleted.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.delete_domain_admin_request import DeleteDomainAdminRequest
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
    api_instance = mailcow_sdk.DomainAdminApi(api_client)
    delete_domain_admin_request = mailcow_sdk.DeleteDomainAdminRequest() # DeleteDomainAdminRequest |  (optional)

    try:
        # Delete Domain Admin
        api_response = api_instance.delete_domain_admin(delete_domain_admin_request=delete_domain_admin_request)
        print("The response of DomainAdminApi->delete_domain_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAdminApi->delete_domain_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_domain_admin_request** | [**DeleteDomainAdminRequest**](DeleteDomainAdminRequest.md)|  | [optional] 

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

# **edit_domain_admin_acl**
> CreateAlias200Response edit_domain_admin_acl(edit_domain_admin_acl_request=edit_domain_admin_acl_request)

Edit Domain Admin ACL

Using this endpoint you can edit the ACLs of a Domain Admin user. This user has full control over a domain, and can create new mailboxes and aliases.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.edit_domain_admin_acl_request import EditDomainAdminACLRequest
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
    api_instance = mailcow_sdk.DomainAdminApi(api_client)
    edit_domain_admin_acl_request = mailcow_sdk.EditDomainAdminACLRequest() # EditDomainAdminACLRequest |  (optional)

    try:
        # Edit Domain Admin ACL
        api_response = api_instance.edit_domain_admin_acl(edit_domain_admin_acl_request=edit_domain_admin_acl_request)
        print("The response of DomainAdminApi->edit_domain_admin_acl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAdminApi->edit_domain_admin_acl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_domain_admin_acl_request** | [**EditDomainAdminACLRequest**](EditDomainAdminACLRequest.md)|  | [optional] 

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

# **edit_domain_admin_user**
> CreateAlias200Response edit_domain_admin_user(edit_domain_admin_user_request=edit_domain_admin_user_request)

Edit Domain Admin user

Using this endpoint you can edit a existing Domain Admin user. This user has full control over a domain, and can create new mailboxes and aliases.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.edit_domain_admin_user_request import EditDomainAdminUserRequest
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
    api_instance = mailcow_sdk.DomainAdminApi(api_client)
    edit_domain_admin_user_request = mailcow_sdk.EditDomainAdminUserRequest() # EditDomainAdminUserRequest |  (optional)

    try:
        # Edit Domain Admin user
        api_response = api_instance.edit_domain_admin_user(edit_domain_admin_user_request=edit_domain_admin_user_request)
        print("The response of DomainAdminApi->edit_domain_admin_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAdminApi->edit_domain_admin_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_domain_admin_user_request** | [**EditDomainAdminUserRequest**](EditDomainAdminUserRequest.md)|  | [optional] 

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

# **get_domain_admins**
> get_domain_admins()

Get Domain Admins



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
    api_instance = mailcow_sdk.DomainAdminApi(api_client)

    try:
        # Get Domain Admins
        api_instance.get_domain_admins()
    except Exception as e:
        print("Exception when calling DomainAdminApi->get_domain_admins: %s\n" % e)
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

