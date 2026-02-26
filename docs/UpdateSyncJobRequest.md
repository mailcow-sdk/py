# UpdateSyncJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | [**UpdateSyncJobRequestAttr**](UpdateSyncJobRequestAttr.md) |  | [optional] 
**items** | **object** | contains list of aliases you want update | [optional] 

## Example

```python
from mailcow_sdk.models.update_sync_job_request import UpdateSyncJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSyncJobRequest from a JSON string
update_sync_job_request_instance = UpdateSyncJobRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSyncJobRequest.to_json())

# convert the object into a dict
update_sync_job_request_dict = update_sync_job_request_instance.to_dict()
# create an instance of UpdateSyncJobRequest from a dict
update_sync_job_request_from_dict = UpdateSyncJobRequest.from_dict(update_sync_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


