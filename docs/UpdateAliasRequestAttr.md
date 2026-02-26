# UpdateAliasRequestAttr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | is alias active or not | [optional] 
**address** | **str** | alias address, for catchall use \&quot;@domain.tld\&quot; | [optional] 
**goto** | **str** | destination address, comma separated | [optional] 
**goto_ham** | **bool** | learn as ham | [optional] 
**goto_null** | **bool** | silently ignore | [optional] 
**goto_spam** | **bool** | learn as spam | [optional] 
**private_comment** | **str** |  | [optional] 
**public_comment** | **str** |  | [optional] 
**sogo_visible** | **bool** | toggle visibility as selectable sender in SOGo | [optional] 

## Example

```python
from mailcow_sdk.models.update_alias_request_attr import UpdateAliasRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAliasRequestAttr from a JSON string
update_alias_request_attr_instance = UpdateAliasRequestAttr.from_json(json)
# print the JSON string representation of the object
print(UpdateAliasRequestAttr.to_json())

# convert the object into a dict
update_alias_request_attr_dict = update_alias_request_attr_instance.to_dict()
# create an instance of UpdateAliasRequestAttr from a dict
update_alias_request_attr_from_dict = UpdateAliasRequestAttr.from_dict(update_alias_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


