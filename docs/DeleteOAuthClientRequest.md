# DeleteOAuthClientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of oAuth clients you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_o_auth_client_request import DeleteOAuthClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOAuthClientRequest from a JSON string
delete_o_auth_client_request_instance = DeleteOAuthClientRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteOAuthClientRequest.to_json())

# convert the object into a dict
delete_o_auth_client_request_dict = delete_o_auth_client_request_instance.to_dict()
# create an instance of DeleteOAuthClientRequest from a dict
delete_o_auth_client_request_from_dict = DeleteOAuthClientRequest.from_dict(delete_o_auth_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


