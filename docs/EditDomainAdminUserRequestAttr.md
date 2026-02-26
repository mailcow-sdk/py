# EditDomainAdminUserRequestAttr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | is the domain admin active or not | [optional] 
**username_new** | **str** | the username of the domain admin, change this to change the username | [optional] 
**domains** | **List[str]** | a list of all domains managed by this domain admin | [optional] 
**password** | **str** | the new domain admin user password | [optional] 
**password2** | **str** | the new domain admin user password for confirmation | [optional] 

## Example

```python
from mailcow_sdk.models.edit_domain_admin_user_request_attr import EditDomainAdminUserRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of EditDomainAdminUserRequestAttr from a JSON string
edit_domain_admin_user_request_attr_instance = EditDomainAdminUserRequestAttr.from_json(json)
# print the JSON string representation of the object
print(EditDomainAdminUserRequestAttr.to_json())

# convert the object into a dict
edit_domain_admin_user_request_attr_dict = edit_domain_admin_user_request_attr_instance.to_dict()
# create an instance of EditDomainAdminUserRequestAttr from a dict
edit_domain_admin_user_request_attr_from_dict = EditDomainAdminUserRequestAttr.from_dict(edit_domain_admin_user_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


