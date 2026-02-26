# GenerateDKIMKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dkim_selector** | **str** | the DKIM selector default dkim | [optional] 
**domains** | **str** | a list of domains for which a dkim key should be generated | [optional] 
**key_size** | **float** | the key size (1024, 2048, 3072 or 4096) | [optional] 

## Example

```python
from mailcow_sdk.models.generate_dkim_key_request import GenerateDKIMKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateDKIMKeyRequest from a JSON string
generate_dkim_key_request_instance = GenerateDKIMKeyRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateDKIMKeyRequest.to_json())

# convert the object into a dict
generate_dkim_key_request_dict = generate_dkim_key_request_instance.to_dict()
# create an instance of GenerateDKIMKeyRequest from a dict
generate_dkim_key_request_from_dict = GenerateDKIMKeyRequest.from_dict(generate_dkim_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


