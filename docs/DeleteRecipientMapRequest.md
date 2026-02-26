# DeleteRecipientMapRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of recipient maps you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_recipient_map_request import DeleteRecipientMapRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRecipientMapRequest from a JSON string
delete_recipient_map_request_instance = DeleteRecipientMapRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteRecipientMapRequest.to_json())

# convert the object into a dict
delete_recipient_map_request_dict = delete_recipient_map_request_instance.to_dict()
# create an instance of DeleteRecipientMapRequest from a dict
delete_recipient_map_request_from_dict = DeleteRecipientMapRequest.from_dict(delete_recipient_map_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


