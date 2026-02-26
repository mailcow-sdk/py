# UpdatePushoverSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | [**UpdatePushoverSettingsRequestAttr**](UpdatePushoverSettingsRequestAttr.md) |  | [optional] 
**items** | **object** | contains list of mailboxes you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.update_pushover_settings_request import UpdatePushoverSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePushoverSettingsRequest from a JSON string
update_pushover_settings_request_instance = UpdatePushoverSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePushoverSettingsRequest.to_json())

# convert the object into a dict
update_pushover_settings_request_dict = update_pushover_settings_request_instance.to_dict()
# create an instance of UpdatePushoverSettingsRequest from a dict
update_pushover_settings_request_from_dict = UpdatePushoverSettingsRequest.from_dict(update_pushover_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


