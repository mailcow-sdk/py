# DeleteTLSPolicyMapRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of tls policy maps you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_tls_policy_map_request import DeleteTLSPolicyMapRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTLSPolicyMapRequest from a JSON string
delete_tls_policy_map_request_instance = DeleteTLSPolicyMapRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteTLSPolicyMapRequest.to_json())

# convert the object into a dict
delete_tls_policy_map_request_dict = delete_tls_policy_map_request_instance.to_dict()
# create an instance of DeleteTLSPolicyMapRequest from a dict
delete_tls_policy_map_request_from_dict = DeleteTLSPolicyMapRequest.from_dict(delete_tls_policy_map_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


