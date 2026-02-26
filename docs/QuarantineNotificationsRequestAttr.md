# QuarantineNotificationsRequestAttr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quarantine_notification** | **str** | recurrence | [optional] 

## Example

```python
from mailcow_sdk.models.quarantine_notifications_request_attr import QuarantineNotificationsRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of QuarantineNotificationsRequestAttr from a JSON string
quarantine_notifications_request_attr_instance = QuarantineNotificationsRequestAttr.from_json(json)
# print the JSON string representation of the object
print(QuarantineNotificationsRequestAttr.to_json())

# convert the object into a dict
quarantine_notifications_request_attr_dict = quarantine_notifications_request_attr_instance.to_dict()
# create an instance of QuarantineNotificationsRequestAttr from a dict
quarantine_notifications_request_attr_from_dict = QuarantineNotificationsRequestAttr.from_dict(quarantine_notifications_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


