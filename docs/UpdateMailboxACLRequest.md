# UpdateMailboxACLRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | [**UpdateMailboxACLRequestAttr**](UpdateMailboxACLRequestAttr.md) |  | [optional] 
**items** | **object** | contains list of mailboxes you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.update_mailbox_acl_request import UpdateMailboxACLRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMailboxACLRequest from a JSON string
update_mailbox_acl_request_instance = UpdateMailboxACLRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMailboxACLRequest.to_json())

# convert the object into a dict
update_mailbox_acl_request_dict = update_mailbox_acl_request_instance.to_dict()
# create an instance of UpdateMailboxACLRequest from a dict
update_mailbox_acl_request_from_dict = UpdateMailboxACLRequest.from_dict(update_mailbox_acl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


