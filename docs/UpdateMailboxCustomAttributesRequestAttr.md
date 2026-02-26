# UpdateMailboxCustomAttributesRequestAttr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **object** | Array of attribute keys | [optional] 
**value** | **object** | Array of attribute values | [optional] 

## Example

```python
from mailcow_sdk.models.update_mailbox_custom_attributes_request_attr import UpdateMailboxCustomAttributesRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMailboxCustomAttributesRequestAttr from a JSON string
update_mailbox_custom_attributes_request_attr_instance = UpdateMailboxCustomAttributesRequestAttr.from_json(json)
# print the JSON string representation of the object
print(UpdateMailboxCustomAttributesRequestAttr.to_json())

# convert the object into a dict
update_mailbox_custom_attributes_request_attr_dict = update_mailbox_custom_attributes_request_attr_instance.to_dict()
# create an instance of UpdateMailboxCustomAttributesRequestAttr from a dict
update_mailbox_custom_attributes_request_attr_from_dict = UpdateMailboxCustomAttributesRequestAttr.from_dict(update_mailbox_custom_attributes_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


