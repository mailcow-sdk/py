# UpdateMailboxRequestAttr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | is mailbox active or not | [optional] 
**force_pw_update** | **bool** | force user to change password on next login | [optional] 
**name** | **str** | Full name of the mailbox user | [optional] 
**authsource** | **str** | Specifies the authentication source for the mailbox. | [optional] 
**password2** | **str** | new mailbox password for confirmation | [optional] 
**password** | **str** | new mailbox password when using &#x60;mailcow&#x60; as the authentication source. | [optional] 
**quota** | **float** | mailbox quota | [optional] 
**sender_acl** | **object** | list of allowed send from addresses | [optional] 
**sogo_access** | **bool** | is access to SOGo webmail active or not | [optional] 

## Example

```python
from mailcow_sdk.models.update_mailbox_request_attr import UpdateMailboxRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMailboxRequestAttr from a JSON string
update_mailbox_request_attr_instance = UpdateMailboxRequestAttr.from_json(json)
# print the JSON string representation of the object
print(UpdateMailboxRequestAttr.to_json())

# convert the object into a dict
update_mailbox_request_attr_dict = update_mailbox_request_attr_instance.to_dict()
# create an instance of UpdateMailboxRequestAttr from a dict
update_mailbox_request_attr_from_dict = UpdateMailboxRequestAttr.from_dict(update_mailbox_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


