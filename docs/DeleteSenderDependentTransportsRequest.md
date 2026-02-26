# DeleteSenderDependentTransportsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of Sender-Dependent Transport you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_sender_dependent_transports_request import DeleteSenderDependentTransportsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSenderDependentTransportsRequest from a JSON string
delete_sender_dependent_transports_request_instance = DeleteSenderDependentTransportsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteSenderDependentTransportsRequest.to_json())

# convert the object into a dict
delete_sender_dependent_transports_request_dict = delete_sender_dependent_transports_request_instance.to_dict()
# create an instance of DeleteSenderDependentTransportsRequest from a dict
delete_sender_dependent_transports_request_from_dict = DeleteSenderDependentTransportsRequest.from_dict(delete_sender_dependent_transports_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


