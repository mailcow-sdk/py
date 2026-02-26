# QuarantineNotificationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | [**QuarantineNotificationsRequestAttr**](QuarantineNotificationsRequestAttr.md) |  | [optional] 
**items** | **object** | contains list of mailboxes you want set qurantine notifications | [optional] 

## Example

```python
from mailcow_sdk.models.quarantine_notifications_request import QuarantineNotificationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuarantineNotificationsRequest from a JSON string
quarantine_notifications_request_instance = QuarantineNotificationsRequest.from_json(json)
# print the JSON string representation of the object
print(QuarantineNotificationsRequest.to_json())

# convert the object into a dict
quarantine_notifications_request_dict = quarantine_notifications_request_instance.to_dict()
# create an instance of QuarantineNotificationsRequest from a dict
quarantine_notifications_request_from_dict = QuarantineNotificationsRequest.from_dict(quarantine_notifications_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


