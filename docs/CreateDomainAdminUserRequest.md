# CreateDomainAdminUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **float** | 1 for a active user account 0 for a disabled user account | [optional] 
**domains** | **str** | the domains the user should be a admin of | [optional] 
**password** | **str** | domain admin user password | [optional] 
**password2** | **str** | domain admin user password | [optional] 
**username** | **str** | the username for the admin user | [optional] 

## Example

```python
from mailcow_sdk.models.create_domain_admin_user_request import CreateDomainAdminUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDomainAdminUserRequest from a JSON string
create_domain_admin_user_request_instance = CreateDomainAdminUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDomainAdminUserRequest.to_json())

# convert the object into a dict
create_domain_admin_user_request_dict = create_domain_admin_user_request_instance.to_dict()
# create an instance of CreateDomainAdminUserRequest from a dict
create_domain_admin_user_request_from_dict = CreateDomainAdminUserRequest.from_dict(create_domain_admin_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


