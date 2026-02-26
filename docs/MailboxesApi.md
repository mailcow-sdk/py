# mailcow_sdk.MailboxesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mailbox**](MailboxesApi.md#create_mailbox) | **POST** /api/v1/add/mailbox | Create mailbox
[**delete_mailbox**](MailboxesApi.md#delete_mailbox) | **POST** /api/v1/delete/mailbox | Delete mailbox
[**delete_mailbox_tags**](MailboxesApi.md#delete_mailbox_tags) | **POST** /api/v1/delete/mailbox/tag/{mailbox} | Delete mailbox tags
[**edit_mailbox_spam_filter_score**](MailboxesApi.md#edit_mailbox_spam_filter_score) | **POST** /api/v1/edit/spam-score/ | Edit mailbox spam filter score
[**get_mailbox_or_global_spam_filter_score**](MailboxesApi.md#get_mailbox_or_global_spam_filter_score) | **GET** /api/v1/get/spam-score/{mailbox} | Get mailbox or global spam filter score
[**get_mailboxes**](MailboxesApi.md#get_mailboxes) | **GET** /api/v1/get/mailbox/{id} | Get mailboxes
[**get_mailboxes_of_a_domain**](MailboxesApi.md#get_mailboxes_of_a_domain) | **GET** /api/v1/get/mailbox/all/{domain} | Get mailboxes of a domain
[**quarantine_notifications**](MailboxesApi.md#quarantine_notifications) | **POST** /api/v1/edit/quarantine_notification | Quarantine Notifications
[**update_mailbox**](MailboxesApi.md#update_mailbox) | **POST** /api/v1/edit/mailbox | Update mailbox
[**update_mailbox_acl**](MailboxesApi.md#update_mailbox_acl) | **POST** /api/v1/edit/user-acl | Update mailbox ACL
[**update_mailbox_custom_attributes**](MailboxesApi.md#update_mailbox_custom_attributes) | **POST** /api/v1/edit/mailbox/custom-attribute | Update mailbox custom attributes
[**update_pushover_settings**](MailboxesApi.md#update_pushover_settings) | **POST** /api/v1/edit/pushover | Update Pushover settings


# **create_mailbox**
> CreateAlias200Response create_mailbox(create_mailbox_request=create_mailbox_request)

Create mailbox

You may create your own mailbox using this action. It takes a JSON object containing a domain informations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.create_mailbox_request import CreateMailboxRequest
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
    api_instance = mailcow_sdk.MailboxesApi(api_client)
    create_mailbox_request = mailcow_sdk.CreateMailboxRequest() # CreateMailboxRequest |  (optional)

    try:
        # Create mailbox
        api_response = api_instance.create_mailbox(create_mailbox_request=create_mailbox_request)
        print("The response of MailboxesApi->create_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->create_mailbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_mailbox_request** | [**CreateMailboxRequest**](CreateMailboxRequest.md)|  | [optional] 

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

# **delete_mailbox**
> CreateAlias200Response delete_mailbox(delete_mailbox_request=delete_mailbox_request)

Delete mailbox

You can delete one or more mailboxes.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.delete_mailbox_request import DeleteMailboxRequest
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
    api_instance = mailcow_sdk.MailboxesApi(api_client)
    delete_mailbox_request = mailcow_sdk.DeleteMailboxRequest() # DeleteMailboxRequest |  (optional)

    try:
        # Delete mailbox
        api_response = api_instance.delete_mailbox(delete_mailbox_request=delete_mailbox_request)
        print("The response of MailboxesApi->delete_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->delete_mailbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_mailbox_request** | [**DeleteMailboxRequest**](DeleteMailboxRequest.md)|  | [optional] 

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

# **delete_mailbox_tags**
> CreateAlias200Response delete_mailbox_tags(mailbox, delete_mailbox_tags_request=delete_mailbox_tags_request)

Delete mailbox tags

You can delete one or more mailbox tags.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.delete_mailbox_tags_request import DeleteMailboxTagsRequest
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
    api_instance = mailcow_sdk.MailboxesApi(api_client)
    mailbox = 'info@domain.tld' # str | name of mailbox
    delete_mailbox_tags_request = mailcow_sdk.DeleteMailboxTagsRequest() # DeleteMailboxTagsRequest |  (optional)

    try:
        # Delete mailbox tags
        api_response = api_instance.delete_mailbox_tags(mailbox, delete_mailbox_tags_request=delete_mailbox_tags_request)
        print("The response of MailboxesApi->delete_mailbox_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->delete_mailbox_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox** | **str**| name of mailbox | 
 **delete_mailbox_tags_request** | [**DeleteMailboxTagsRequest**](DeleteMailboxTagsRequest.md)|  | [optional] 

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

# **edit_mailbox_spam_filter_score**
> CreateAlias200Response edit_mailbox_spam_filter_score(body=body)

Edit mailbox spam filter score

Using this endpoint you can edit the spam filter score for a certain mailbox.

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
    api_instance = mailcow_sdk.MailboxesApi(api_client)
    body = None # object |  (optional)

    try:
        # Edit mailbox spam filter score
        api_response = api_instance.edit_mailbox_spam_filter_score(body=body)
        print("The response of MailboxesApi->edit_mailbox_spam_filter_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->edit_mailbox_spam_filter_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | [optional] 

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

# **get_mailbox_or_global_spam_filter_score**
> get_mailbox_or_global_spam_filter_score(mailbox, x_api_key=x_api_key)

Get mailbox or global spam filter score

Using this endpoint you can get the global spam filter score or the spam filter score of a certain mailbox.

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
    api_instance = mailcow_sdk.MailboxesApi(api_client)
    mailbox = 'mailbox_example' # str | name of mailbox or empty for current user - admin user will retrieve the global spam filter score
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get mailbox or global spam filter score
        api_instance.get_mailbox_or_global_spam_filter_score(mailbox, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling MailboxesApi->get_mailbox_or_global_spam_filter_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox** | **str**| name of mailbox or empty for current user - admin user will retrieve the global spam filter score | 
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

# **get_mailboxes**
> get_mailboxes(id, tags=tags, x_api_key=x_api_key)

Get mailboxes

You can list all mailboxes existing in system.

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
    api_instance = mailcow_sdk.MailboxesApi(api_client)
    id = 'all' # str | id of entry you want to get
    tags = 'tag1,tag2' # str | comma seperated list of tags to filter by (optional)
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get mailboxes
        api_instance.get_mailboxes(id, tags=tags, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling MailboxesApi->get_mailboxes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of entry you want to get | 
 **tags** | **str**| comma seperated list of tags to filter by | [optional] 
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

# **get_mailboxes_of_a_domain**
> get_mailboxes_of_a_domain(domain, x_api_key=x_api_key)

Get mailboxes of a domain

You can list all mailboxes existing in system for a specific domain.

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
    api_instance = mailcow_sdk.MailboxesApi(api_client)
    domain = 'domain_example' # str | name of domain
    x_api_key = 'api-key-string' # str | e.g. api-key-string (optional)

    try:
        # Get mailboxes of a domain
        api_instance.get_mailboxes_of_a_domain(domain, x_api_key=x_api_key)
    except Exception as e:
        print("Exception when calling MailboxesApi->get_mailboxes_of_a_domain: %s\n" % e)
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

# **quarantine_notifications**
> quarantine_notifications(quarantine_notifications_request=quarantine_notifications_request)

Quarantine Notifications

You can update one or more mailboxes per request.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.quarantine_notifications_request import QuarantineNotificationsRequest
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
    api_instance = mailcow_sdk.MailboxesApi(api_client)
    quarantine_notifications_request = mailcow_sdk.QuarantineNotificationsRequest() # QuarantineNotificationsRequest |  (optional)

    try:
        # Quarantine Notifications
        api_instance.quarantine_notifications(quarantine_notifications_request=quarantine_notifications_request)
    except Exception as e:
        print("Exception when calling MailboxesApi->quarantine_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quarantine_notifications_request** | [**QuarantineNotificationsRequest**](QuarantineNotificationsRequest.md)|  | [optional] 

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

# **update_mailbox**
> CreateAlias200Response update_mailbox(update_mailbox_request=update_mailbox_request)

Update mailbox

You can update one or more mailboxes per request. You can also send just attributes you want to change

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.update_mailbox_request import UpdateMailboxRequest
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
    api_instance = mailcow_sdk.MailboxesApi(api_client)
    update_mailbox_request = mailcow_sdk.UpdateMailboxRequest() # UpdateMailboxRequest |  (optional)

    try:
        # Update mailbox
        api_response = api_instance.update_mailbox(update_mailbox_request=update_mailbox_request)
        print("The response of MailboxesApi->update_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->update_mailbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_mailbox_request** | [**UpdateMailboxRequest**](UpdateMailboxRequest.md)|  | [optional] 

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

# **update_mailbox_acl**
> CreateAlias200Response update_mailbox_acl(update_mailbox_acl_request=update_mailbox_acl_request)

Update mailbox ACL

Using this endpoints its possible to update the ACL's for mailboxes

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.update_mailbox_acl_request import UpdateMailboxACLRequest
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
    api_instance = mailcow_sdk.MailboxesApi(api_client)
    update_mailbox_acl_request = mailcow_sdk.UpdateMailboxACLRequest() # UpdateMailboxACLRequest |  (optional)

    try:
        # Update mailbox ACL
        api_response = api_instance.update_mailbox_acl(update_mailbox_acl_request=update_mailbox_acl_request)
        print("The response of MailboxesApi->update_mailbox_acl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->update_mailbox_acl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_mailbox_acl_request** | [**UpdateMailboxACLRequest**](UpdateMailboxACLRequest.md)|  | [optional] 

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

# **update_mailbox_custom_attributes**
> CreateAlias200Response update_mailbox_custom_attributes(update_mailbox_custom_attributes_request=update_mailbox_custom_attributes_request)

Update mailbox custom attributes

You can update custom attributes of one or more mailboxes per request.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.update_mailbox_custom_attributes_request import UpdateMailboxCustomAttributesRequest
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
    api_instance = mailcow_sdk.MailboxesApi(api_client)
    update_mailbox_custom_attributes_request = mailcow_sdk.UpdateMailboxCustomAttributesRequest() # UpdateMailboxCustomAttributesRequest |  (optional)

    try:
        # Update mailbox custom attributes
        api_response = api_instance.update_mailbox_custom_attributes(update_mailbox_custom_attributes_request=update_mailbox_custom_attributes_request)
        print("The response of MailboxesApi->update_mailbox_custom_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->update_mailbox_custom_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_mailbox_custom_attributes_request** | [**UpdateMailboxCustomAttributesRequest**](UpdateMailboxCustomAttributesRequest.md)|  | [optional] 

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

# **update_pushover_settings**
> CreateAlias200Response update_pushover_settings(update_pushover_settings_request=update_pushover_settings_request)

Update Pushover settings

Using this endpoint it is possible to update the pushover settings for mailboxes

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import mailcow_sdk
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response
from mailcow_sdk.models.update_pushover_settings_request import UpdatePushoverSettingsRequest
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
    api_instance = mailcow_sdk.MailboxesApi(api_client)
    update_pushover_settings_request = mailcow_sdk.UpdatePushoverSettingsRequest() # UpdatePushoverSettingsRequest |  (optional)

    try:
        # Update Pushover settings
        api_response = api_instance.update_pushover_settings(update_pushover_settings_request=update_pushover_settings_request)
        print("The response of MailboxesApi->update_pushover_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->update_pushover_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_pushover_settings_request** | [**UpdatePushoverSettingsRequest**](UpdatePushoverSettingsRequest.md)|  | [optional] 

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

