# DuplicateDKIMKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fron_domain** | **str** | the domain where the dkim key should be copied from | [optional] 
**to_domain** | **str** | the domain where the dkim key should be copied to | [optional] 

## Example

```python
from mailcow_sdk.models.duplicate_dkim_key_request import DuplicateDKIMKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateDKIMKeyRequest from a JSON string
duplicate_dkim_key_request_instance = DuplicateDKIMKeyRequest.from_json(json)
# print the JSON string representation of the object
print(DuplicateDKIMKeyRequest.to_json())

# convert the object into a dict
duplicate_dkim_key_request_dict = duplicate_dkim_key_request_instance.to_dict()
# create an instance of DuplicateDKIMKeyRequest from a dict
duplicate_dkim_key_request_from_dict = DuplicateDKIMKeyRequest.from_dict(duplicate_dkim_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


