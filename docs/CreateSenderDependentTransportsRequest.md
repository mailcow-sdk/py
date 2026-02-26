# CreateSenderDependentTransportsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | the hostname of the smtp server with port | [optional] 
**password** | **str** | the password for the smtp user | [optional] 
**username** | **str** | the username used to authenticate | [optional] 

## Example

```python
from mailcow_sdk.models.create_sender_dependent_transports_request import CreateSenderDependentTransportsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSenderDependentTransportsRequest from a JSON string
create_sender_dependent_transports_request_instance = CreateSenderDependentTransportsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSenderDependentTransportsRequest.to_json())

# convert the object into a dict
create_sender_dependent_transports_request_dict = create_sender_dependent_transports_request_instance.to_dict()
# create an instance of CreateSenderDependentTransportsRequest from a dict
create_sender_dependent_transports_request_from_dict = CreateSenderDependentTransportsRequest.from_dict(create_sender_dependent_transports_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


