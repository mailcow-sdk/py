# DeleteMailboxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of mailboxes you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_mailbox_request import DeleteMailboxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMailboxRequest from a JSON string
delete_mailbox_request_instance = DeleteMailboxRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteMailboxRequest.to_json())

# convert the object into a dict
delete_mailbox_request_dict = delete_mailbox_request_instance.to_dict()
# create an instance of DeleteMailboxRequest from a dict
delete_mailbox_request_from_dict = DeleteMailboxRequest.from_dict(delete_mailbox_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


