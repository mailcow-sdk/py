# CreateResourcesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **float** | 1 for a active transport map 0 for a disabled transport map | [optional] 
**description** | **str** | a description of the resource | [optional] 
**domain** | **str** | the domain for which the resource should be | [optional] 
**kind** | **str** | the kind of recouse | [optional] 
**multiple_bookings** | **str** |  | [optional] 
**multiple_bookings_custom** | **float** | always empty | [optional] 
**multiple_bookings_select** | **str** |  | [optional] 

## Example

```python
from mailcow_sdk.models.create_resources_request import CreateResourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResourcesRequest from a JSON string
create_resources_request_instance = CreateResourcesRequest.from_json(json)
# print the JSON string representation of the object
print(CreateResourcesRequest.to_json())

# convert the object into a dict
create_resources_request_dict = create_resources_request_instance.to_dict()
# create an instance of CreateResourcesRequest from a dict
create_resources_request_from_dict = CreateResourcesRequest.from_dict(create_resources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


