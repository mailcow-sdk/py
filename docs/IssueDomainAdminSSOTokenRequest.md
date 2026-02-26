# IssueDomainAdminSSOTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **object** | the username for the admin user | [optional] 

## Example

```python
from mailcow_sdk.models.issue_domain_admin_sso_token_request import IssueDomainAdminSSOTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssueDomainAdminSSOTokenRequest from a JSON string
issue_domain_admin_sso_token_request_instance = IssueDomainAdminSSOTokenRequest.from_json(json)
# print the JSON string representation of the object
print(IssueDomainAdminSSOTokenRequest.to_json())

# convert the object into a dict
issue_domain_admin_sso_token_request_dict = issue_domain_admin_sso_token_request_instance.to_dict()
# create an instance of IssueDomainAdminSSOTokenRequest from a dict
issue_domain_admin_sso_token_request_from_dict = IssueDomainAdminSSOTokenRequest.from_dict(issue_domain_admin_sso_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


