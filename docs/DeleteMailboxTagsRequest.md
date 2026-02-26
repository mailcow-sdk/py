# DeleteMailboxTagsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of mailboxes you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_mailbox_tags_request import DeleteMailboxTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMailboxTagsRequest from a JSON string
delete_mailbox_tags_request_instance = DeleteMailboxTagsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteMailboxTagsRequest.to_json())

# convert the object into a dict
delete_mailbox_tags_request_dict = delete_mailbox_tags_request_instance.to_dict()
# create an instance of DeleteMailboxTagsRequest from a dict
delete_mailbox_tags_request_from_dict = DeleteMailboxTagsRequest.from_dict(delete_mailbox_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


