# EditFail2BanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | [**EditFail2BanRequestAttr**](EditFail2BanRequestAttr.md) |  | [optional] 
**items** | **object** |  | [optional] 

## Example

```python
from mailcow_sdk.models.edit_fail2_ban_request import EditFail2BanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditFail2BanRequest from a JSON string
edit_fail2_ban_request_instance = EditFail2BanRequest.from_json(json)
# print the JSON string representation of the object
print(EditFail2BanRequest.to_json())

# convert the object into a dict
edit_fail2_ban_request_dict = edit_fail2_ban_request_instance.to_dict()
# create an instance of EditFail2BanRequest from a dict
edit_fail2_ban_request_from_dict = EditFail2BanRequest.from_dict(edit_fail2_ban_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


