# DeleteDomainPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of domain policys you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_domain_policy_request import DeleteDomainPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDomainPolicyRequest from a JSON string
delete_domain_policy_request_instance = DeleteDomainPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteDomainPolicyRequest.to_json())

# convert the object into a dict
delete_domain_policy_request_dict = delete_domain_policy_request_instance.to_dict()
# create an instance of DeleteDomainPolicyRequest from a dict
delete_domain_policy_request_from_dict = DeleteDomainPolicyRequest.from_dict(delete_domain_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


