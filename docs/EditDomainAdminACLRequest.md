# EditDomainAdminACLRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains the domain admin username you want to edit | [optional] 
**attr** | [**EditDomainAdminACLRequestAttr**](EditDomainAdminACLRequestAttr.md) |  | [optional] 

## Example

```python
from mailcow_sdk.models.edit_domain_admin_acl_request import EditDomainAdminACLRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditDomainAdminACLRequest from a JSON string
edit_domain_admin_acl_request_instance = EditDomainAdminACLRequest.from_json(json)
# print the JSON string representation of the object
print(EditDomainAdminACLRequest.to_json())

# convert the object into a dict
edit_domain_admin_acl_request_dict = edit_domain_admin_acl_request_instance.to_dict()
# create an instance of EditDomainAdminACLRequest from a dict
edit_domain_admin_acl_request_from_dict = EditDomainAdminACLRequest.from_dict(edit_domain_admin_acl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


