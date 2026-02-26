# CreateOAuthClientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uri** | **str** | the uri where you should be redirected after oAuth | [optional] 

## Example

```python
from mailcow_sdk.models.create_o_auth_client_request import CreateOAuthClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOAuthClientRequest from a JSON string
create_o_auth_client_request_instance = CreateOAuthClientRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOAuthClientRequest.to_json())

# convert the object into a dict
create_o_auth_client_request_dict = create_o_auth_client_request_instance.to_dict()
# create an instance of CreateOAuthClientRequest from a dict
create_o_auth_client_request_from_dict = CreateOAuthClientRequest.from_dict(create_o_auth_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


