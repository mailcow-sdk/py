# CreateAppPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | is alias active or not | [optional] 
**username** | **str** | mailbox for which the app password should be created | [optional] 
**app_name** | **str** | name of your app password | [optional] 
**app_passwd** | **str** | your app password | [optional] 
**app_passwd2** | **str** | your app password | [optional] 

## Example

```python
from mailcow_sdk.models.create_app_password_request import CreateAppPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppPasswordRequest from a JSON string
create_app_password_request_instance = CreateAppPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAppPasswordRequest.to_json())

# convert the object into a dict
create_app_password_request_dict = create_app_password_request_instance.to_dict()
# create an instance of CreateAppPasswordRequest from a dict
create_app_password_request_from_dict = CreateAppPasswordRequest.from_dict(create_app_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


