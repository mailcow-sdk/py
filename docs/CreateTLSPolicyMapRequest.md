# CreateTLSPolicyMapRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | **str** | custom parameters you find out more about them [here](http://www.postfix.org/postconf.5.html#smtp_tls_policy_maps) | [optional] 
**active** | **float** | 1 for a active user account 0 for a disabled user account | [optional] 
**dest** | **str** | the target domain or email address | [optional] 
**policy** | **str** | the policy | [optional] 

## Example

```python
from mailcow_sdk.models.create_tls_policy_map_request import CreateTLSPolicyMapRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTLSPolicyMapRequest from a JSON string
create_tls_policy_map_request_instance = CreateTLSPolicyMapRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTLSPolicyMapRequest.to_json())

# convert the object into a dict
create_tls_policy_map_request_dict = create_tls_policy_map_request_instance.to_dict()
# create an instance of CreateTLSPolicyMapRequest from a dict
create_tls_policy_map_request_from_dict = CreateTLSPolicyMapRequest.from_dict(create_tls_policy_map_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


