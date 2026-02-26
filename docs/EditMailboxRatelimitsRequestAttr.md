# EditMailboxRatelimitsRequestAttr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rl_frame** | **str** | contains the frame for the ratelimit h,s,m | [optional] 
**rl_value** | **float** | contains the rate for the ratelimit 10,20,50,1 | [optional] 

## Example

```python
from mailcow_sdk.models.edit_mailbox_ratelimits_request_attr import EditMailboxRatelimitsRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of EditMailboxRatelimitsRequestAttr from a JSON string
edit_mailbox_ratelimits_request_attr_instance = EditMailboxRatelimitsRequestAttr.from_json(json)
# print the JSON string representation of the object
print(EditMailboxRatelimitsRequestAttr.to_json())

# convert the object into a dict
edit_mailbox_ratelimits_request_attr_dict = edit_mailbox_ratelimits_request_attr_instance.to_dict()
# create an instance of EditMailboxRatelimitsRequestAttr from a dict
edit_mailbox_ratelimits_request_attr_from_dict = EditMailboxRatelimitsRequestAttr.from_dict(edit_mailbox_ratelimits_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


