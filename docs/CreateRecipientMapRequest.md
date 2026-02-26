# CreateRecipientMapRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **float** | 1 for a active user account 0 for a disabled user account | [optional] 
**recipient_map_new** | **str** | the email address that should receive the forwarded emails | [optional] 
**recipient_map_old** | **str** | the email address which emails should be forwarded | [optional] 

## Example

```python
from mailcow_sdk.models.create_recipient_map_request import CreateRecipientMapRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRecipientMapRequest from a JSON string
create_recipient_map_request_instance = CreateRecipientMapRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRecipientMapRequest.to_json())

# convert the object into a dict
create_recipient_map_request_dict = create_recipient_map_request_instance.to_dict()
# create an instance of CreateRecipientMapRequest from a dict
create_recipient_map_request_from_dict = CreateRecipientMapRequest.from_dict(create_recipient_map_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


