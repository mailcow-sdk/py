# DeleteAppPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of app passwords you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_app_password_request import DeleteAppPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAppPasswordRequest from a JSON string
delete_app_password_request_instance = DeleteAppPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteAppPasswordRequest.to_json())

# convert the object into a dict
delete_app_password_request_dict = delete_app_password_request_instance.to_dict()
# create an instance of DeleteAppPasswordRequest from a dict
delete_app_password_request_from_dict = DeleteAppPasswordRequest.from_dict(delete_app_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


