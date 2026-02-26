# FlushQueueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | use flush to flush the mail queue | [optional] 

## Example

```python
from mailcow_sdk.models.flush_queue_request import FlushQueueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlushQueueRequest from a JSON string
flush_queue_request_instance = FlushQueueRequest.from_json(json)
# print the JSON string representation of the object
print(FlushQueueRequest.to_json())

# convert the object into a dict
flush_queue_request_dict = flush_queue_request_instance.to_dict()
# create an instance of FlushQueueRequest from a dict
flush_queue_request_from_dict = FlushQueueRequest.from_dict(flush_queue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


