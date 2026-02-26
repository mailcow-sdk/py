# CreateDomainPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | domain name to which policy is associated to | [optional] 
**object_from** | **str** | exact address or use wildcard to match whole domain | [optional] 
**object_list** | **str** |  | [optional] 

## Example

```python
from mailcow_sdk.models.create_domain_policy_request import CreateDomainPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDomainPolicyRequest from a JSON string
create_domain_policy_request_instance = CreateDomainPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDomainPolicyRequest.to_json())

# convert the object into a dict
create_domain_policy_request_dict = create_domain_policy_request_instance.to_dict()
# create an instance of CreateDomainPolicyRequest from a dict
create_domain_policy_request_from_dict = CreateDomainPolicyRequest.from_dict(create_domain_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


