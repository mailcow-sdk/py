# CreateSyncJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | **str** | your local mailcow mailbox | [optional] 
**host1** | **str** | the smtp server where mails should be synced from | [optional] 
**port1** | **str** | the smtp port of the target mail server | [optional] 
**user1** | **str** | the username of the mailbox | [optional] 
**password** | **str** | the password of the mailbox | [optional] 
**enc1** | **str** | the encryption method used to connect to the mailserver | [optional] 
**mins_internal** | **float** | the interval in which messages should be syned | [optional] 
**subfolder2** | **str** | sync into subfolder on destination (empty &#x3D; do not use subfolder) | [optional] 
**maxage** | **float** | only sync messages up to this age in days | [optional] 
**maxbytespersecond** | **float** | max speed transfer limit for the sync | [optional] 
**timeout1** | **float** | timeout for connection to remote host | [optional] 
**timeout2** | **float** | timeout for connection to local host | [optional] 
**exclude** | **str** | exclude objects (regex) | [optional] 
**custom_params** | **str** | custom parameters | [optional] 
**delete2duplicates** | **bool** | delete duplicates on destination (--delete2duplicates) | [optional] 
**delete1** | **bool** | delete from source when completed (--delete1) | [optional] 
**delete2** | **bool** | delete messages on destination that are not on source (--delete2) | [optional] 
**automap** | **bool** | try to automap folders (\&quot;Sent items\&quot;, \&quot;Sent\&quot; &#x3D;&gt; \&quot;Sent\&quot; etc.) (--automap) | [optional] 
**skipcrossduplicates** | **bool** | skip duplicate messages across folders (first come, first serve) (--skipcrossduplicates) | [optional] 
**subscribeall** | **bool** | subscribe all folders (--subscribeall) | [optional] 
**active** | **bool** | enables or disables the sync job | [optional] 

## Example

```python
from mailcow_sdk.models.create_sync_job_request import CreateSyncJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSyncJobRequest from a JSON string
create_sync_job_request_instance = CreateSyncJobRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSyncJobRequest.to_json())

# convert the object into a dict
create_sync_job_request_dict = create_sync_job_request_instance.to_dict()
# create an instance of CreateSyncJobRequest from a dict
create_sync_job_request_from_dict = CreateSyncJobRequest.from_dict(create_sync_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


