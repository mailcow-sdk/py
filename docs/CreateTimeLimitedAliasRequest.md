# CreateTimeLimitedAliasRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | the mailbox an alias should be created for | [optional] 
**domain** | **str** | the domain | [optional] 

## Example

```python
from mailcow_sdk.models.create_time_limited_alias_request import CreateTimeLimitedAliasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTimeLimitedAliasRequest from a JSON string
create_time_limited_alias_request_instance = CreateTimeLimitedAliasRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTimeLimitedAliasRequest.to_json())

# convert the object into a dict
create_time_limited_alias_request_dict = create_time_limited_alias_request_instance.to_dict()
# create an instance of CreateTimeLimitedAliasRequest from a dict
create_time_limited_alias_request_from_dict = CreateTimeLimitedAliasRequest.from_dict(create_time_limited_alias_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


