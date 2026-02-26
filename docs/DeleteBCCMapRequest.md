# DeleteBCCMapRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of bcc maps you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_bcc_map_request import DeleteBCCMapRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBCCMapRequest from a JSON string
delete_bcc_map_request_instance = DeleteBCCMapRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteBCCMapRequest.to_json())

# convert the object into a dict
delete_bcc_map_request_dict = delete_bcc_map_request_instance.to_dict()
# create an instance of DeleteBCCMapRequest from a dict
delete_bcc_map_request_from_dict = DeleteBCCMapRequest.from_dict(delete_bcc_map_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


