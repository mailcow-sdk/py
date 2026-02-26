# UpdateAliasRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | [**UpdateAliasRequestAttr**](UpdateAliasRequestAttr.md) |  | [optional] 
**items** | **object** | contains list of aliases you want update | [optional] 

## Example

```python
from mailcow_sdk.models.update_alias_request import UpdateAliasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAliasRequest from a JSON string
update_alias_request_instance = UpdateAliasRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAliasRequest.to_json())

# convert the object into a dict
update_alias_request_dict = update_alias_request_instance.to_dict()
# create an instance of UpdateAliasRequest from a dict
update_alias_request_from_dict = UpdateAliasRequest.from_dict(update_alias_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


