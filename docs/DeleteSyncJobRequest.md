# DeleteSyncJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of aliases you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_sync_job_request import DeleteSyncJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSyncJobRequest from a JSON string
delete_sync_job_request_instance = DeleteSyncJobRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteSyncJobRequest.to_json())

# convert the object into a dict
delete_sync_job_request_dict = delete_sync_job_request_instance.to_dict()
# create an instance of DeleteSyncJobRequest from a dict
delete_sync_job_request_from_dict = DeleteSyncJobRequest.from_dict(delete_sync_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


