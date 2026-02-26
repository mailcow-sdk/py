# DeleteDomainAdminRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of usernames of the users you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_domain_admin_request import DeleteDomainAdminRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDomainAdminRequest from a JSON string
delete_domain_admin_request_instance = DeleteDomainAdminRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteDomainAdminRequest.to_json())

# convert the object into a dict
delete_domain_admin_request_dict = delete_domain_admin_request_instance.to_dict()
# create an instance of DeleteDomainAdminRequest from a dict
delete_domain_admin_request_from_dict = DeleteDomainAdminRequest.from_dict(delete_domain_admin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


