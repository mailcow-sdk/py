# CreateAlias200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log** | **List[object]** | contains request object | [optional] 
**msg** | **List[object]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from mailcow_sdk.models.create_alias200_response import CreateAlias200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlias200Response from a JSON string
create_alias200_response_instance = CreateAlias200Response.from_json(json)
# print the JSON string representation of the object
print(CreateAlias200Response.to_json())

# convert the object into a dict
create_alias200_response_dict = create_alias200_response_instance.to_dict()
# create an instance of CreateAlias200Response from a dict
create_alias200_response_from_dict = CreateAlias200Response.from_dict(create_alias200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


