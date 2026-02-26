# DeleteResourcesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of Resources you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_resources_request import DeleteResourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteResourcesRequest from a JSON string
delete_resources_request_instance = DeleteResourcesRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteResourcesRequest.to_json())

# convert the object into a dict
delete_resources_request_dict = delete_resources_request_instance.to_dict()
# create an instance of DeleteResourcesRequest from a dict
delete_resources_request_from_dict = DeleteResourcesRequest.from_dict(delete_resources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


