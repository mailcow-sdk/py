# UpdateMailboxACLRequestAttr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_acl** | **object** | contains a list of active user acls | [optional] 

## Example

```python
from mailcow_sdk.models.update_mailbox_acl_request_attr import UpdateMailboxACLRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMailboxACLRequestAttr from a JSON string
update_mailbox_acl_request_attr_instance = UpdateMailboxACLRequestAttr.from_json(json)
# print the JSON string representation of the object
print(UpdateMailboxACLRequestAttr.to_json())

# convert the object into a dict
update_mailbox_acl_request_attr_dict = update_mailbox_acl_request_attr_instance.to_dict()
# create an instance of UpdateMailboxACLRequestAttr from a dict
update_mailbox_acl_request_attr_from_dict = UpdateMailboxACLRequestAttr.from_dict(update_mailbox_acl_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


