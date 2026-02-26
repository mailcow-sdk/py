# UpdateMailboxCustomAttributesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | [**UpdateMailboxCustomAttributesRequestAttr**](UpdateMailboxCustomAttributesRequestAttr.md) |  | [optional] 
**items** | **object** | contains list of mailboxes you want update | [optional] 

## Example

```python
from mailcow_sdk.models.update_mailbox_custom_attributes_request import UpdateMailboxCustomAttributesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMailboxCustomAttributesRequest from a JSON string
update_mailbox_custom_attributes_request_instance = UpdateMailboxCustomAttributesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMailboxCustomAttributesRequest.to_json())

# convert the object into a dict
update_mailbox_custom_attributes_request_dict = update_mailbox_custom_attributes_request_instance.to_dict()
# create an instance of UpdateMailboxCustomAttributesRequest from a dict
update_mailbox_custom_attributes_request_from_dict = UpdateMailboxCustomAttributesRequest.from_dict(update_mailbox_custom_attributes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


