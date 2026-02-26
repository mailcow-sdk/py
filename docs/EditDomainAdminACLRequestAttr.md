# EditDomainAdminACLRequestAttr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**da_acl** | **object** | contains the list of acl names that are active for this user | [optional] 

## Example

```python
from mailcow_sdk.models.edit_domain_admin_acl_request_attr import EditDomainAdminACLRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of EditDomainAdminACLRequestAttr from a JSON string
edit_domain_admin_acl_request_attr_instance = EditDomainAdminACLRequestAttr.from_json(json)
# print the JSON string representation of the object
print(EditDomainAdminACLRequestAttr.to_json())

# convert the object into a dict
edit_domain_admin_acl_request_attr_dict = edit_domain_admin_acl_request_attr_instance.to_dict()
# create an instance of EditDomainAdminACLRequestAttr from a dict
edit_domain_admin_acl_request_attr_from_dict = EditDomainAdminACLRequestAttr.from_dict(edit_domain_admin_acl_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


