# DeleteMailsInQuarantineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of emails you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_mails_in_quarantine_request import DeleteMailsInQuarantineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMailsInQuarantineRequest from a JSON string
delete_mails_in_quarantine_request_instance = DeleteMailsInQuarantineRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteMailsInQuarantineRequest.to_json())

# convert the object into a dict
delete_mails_in_quarantine_request_dict = delete_mails_in_quarantine_request_instance.to_dict()
# create an instance of DeleteMailsInQuarantineRequest from a dict
delete_mails_in_quarantine_request_from_dict = DeleteMailsInQuarantineRequest.from_dict(delete_mails_in_quarantine_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


