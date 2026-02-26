# UpdatePushoverSettingsRequestAttr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **float** | Enables pushover 1 disable pushover 0 | [optional] 
**evaluate_x_prio** | **float** | Send the Push with High priority | [optional] 
**key** | **str** | Pushover key | [optional] 
**only_x_prio** | **float** | Only send push for prio mails | [optional] 
**sound** | **str** | Set notification sound | [optional] 
**senders** | **str** | Only send push for emails from these senders | [optional] 
**senders_regex** | **str** | Regex to match senders for which a push will be send | [optional] 
**text** | **str** | Custom push noficiation text | [optional] 
**title** | **str** | Push title | [optional] 
**token** | **str** | Pushover token | [optional] 

## Example

```python
from mailcow_sdk.models.update_pushover_settings_request_attr import UpdatePushoverSettingsRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePushoverSettingsRequestAttr from a JSON string
update_pushover_settings_request_attr_instance = UpdatePushoverSettingsRequestAttr.from_json(json)
# print the JSON string representation of the object
print(UpdatePushoverSettingsRequestAttr.to_json())

# convert the object into a dict
update_pushover_settings_request_attr_dict = update_pushover_settings_request_attr_instance.to_dict()
# create an instance of UpdatePushoverSettingsRequestAttr from a dict
update_pushover_settings_request_attr_from_dict = UpdatePushoverSettingsRequestAttr.from_dict(update_pushover_settings_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


