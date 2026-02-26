# DeleteQueueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | use super_delete to delete the mail queue | [optional] 

## Example

```python
from mailcow_sdk.models.delete_queue_request import DeleteQueueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteQueueRequest from a JSON string
delete_queue_request_instance = DeleteQueueRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteQueueRequest.to_json())

# convert the object into a dict
delete_queue_request_dict = delete_queue_request_instance.to_dict()
# create an instance of DeleteQueueRequest from a dict
delete_queue_request_from_dict = DeleteQueueRequest.from_dict(delete_queue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


