# UpdateSyncJobRequestAttr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Is sync job active | [optional] 
**automap** | **bool** | Try to automap folders (\&quot;Sent items\&quot;, \&quot;Sent\&quot; &#x3D;&gt; \&quot;Sent\&quot; etc.) | [optional] 
**custom_params** | **str** | Custom parameters passed to imapsync command | [optional] 
**delete1** | **bool** | Delete from source when completed | [optional] 
**delete2** | **bool** | Delete messages on destination that are not on source | [optional] 
**delete2duplicates** | **bool** | Delete duplicates on destination | [optional] 
**enc1** | **str** | Encryption | [optional] 
**exclude** | **str** | Exclude objects (regex) | [optional] 
**host1** | **str** | Hostname | [optional] 
**maxage** | **float** | Maximum age of messages in days that will be polled from remote (0 &#x3D; ignore age) | [optional] 
**maxbytespersecond** | **float** | Max. bytes per second (0 &#x3D; unlimited) | [optional] 
**mins_interval** | **float** | Interval (min) | [optional] 
**password1** | **str** | Password | [optional] 
**port1** | **str** | Port | [optional] 
**skipcrossduplicates** | **bool** | Skip duplicate messages across folders (first come, first serve) | [optional] 
**subfolder2** | **str** | Sync into subfolder on destination (empty &#x3D; do not use subfolder) | [optional] 
**subscribeall** | **bool** | Subscribe all folders | [optional] 
**timeout1** | **float** | Timeout for connection to remote host | [optional] 
**timeout2** | **float** | Timeout for connection to local host | [optional] 
**user1** | **str** | Username | [optional] 

## Example

```python
from mailcow_sdk.models.update_sync_job_request_attr import UpdateSyncJobRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSyncJobRequestAttr from a JSON string
update_sync_job_request_attr_instance = UpdateSyncJobRequestAttr.from_json(json)
# print the JSON string representation of the object
print(UpdateSyncJobRequestAttr.to_json())

# convert the object into a dict
update_sync_job_request_attr_dict = update_sync_job_request_attr_instance.to_dict()
# create an instance of UpdateSyncJobRequestAttr from a dict
update_sync_job_request_attr_from_dict = UpdateSyncJobRequestAttr.from_dict(update_sync_job_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


