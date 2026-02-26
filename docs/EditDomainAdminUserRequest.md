# EditDomainAdminUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | [**EditDomainAdminUserRequestAttr**](EditDomainAdminUserRequestAttr.md) |  | [optional] 
**items** | **object** | contains the domain admin username you want to edit | [optional] 

## Example

```python
from mailcow_sdk.models.edit_domain_admin_user_request import EditDomainAdminUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditDomainAdminUserRequest from a JSON string
edit_domain_admin_user_request_instance = EditDomainAdminUserRequest.from_json(json)
# print the JSON string representation of the object
print(EditDomainAdminUserRequest.to_json())

# convert the object into a dict
edit_domain_admin_user_request_dict = edit_domain_admin_user_request_instance.to_dict()
# create an instance of EditDomainAdminUserRequest from a dict
edit_domain_admin_user_request_from_dict = EditDomainAdminUserRequest.from_dict(edit_domain_admin_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


