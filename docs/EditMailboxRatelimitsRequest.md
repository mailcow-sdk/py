# EditMailboxRatelimitsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | [**EditMailboxRatelimitsRequestAttr**](EditMailboxRatelimitsRequestAttr.md) |  | [optional] 
**items** | **object** | contains list of mailboxes you want to edit the ratelimit of | [optional] 

## Example

```python
from mailcow_sdk.models.edit_mailbox_ratelimits_request import EditMailboxRatelimitsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditMailboxRatelimitsRequest from a JSON string
edit_mailbox_ratelimits_request_instance = EditMailboxRatelimitsRequest.from_json(json)
# print the JSON string representation of the object
print(EditMailboxRatelimitsRequest.to_json())

# convert the object into a dict
edit_mailbox_ratelimits_request_dict = edit_mailbox_ratelimits_request_instance.to_dict()
# create an instance of EditMailboxRatelimitsRequest from a dict
edit_mailbox_ratelimits_request_from_dict = EditMailboxRatelimitsRequest.from_dict(edit_mailbox_ratelimits_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


