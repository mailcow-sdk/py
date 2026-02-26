# CreateBCCMapRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **float** | 1 for a active user account 0 for a disabled user account | [optional] 
**bcc_dest** | **str** | the email address where all mails should be send to | [optional] 
**local_dest** | **str** | the domain which emails should be forwarded | [optional] 
**type** | **str** | the type of bcc map can be &#x60;sender&#x60; or &#x60;rcpt&#x60; | [optional] 

## Example

```python
from mailcow_sdk.models.create_bcc_map_request import CreateBCCMapRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBCCMapRequest from a JSON string
create_bcc_map_request_instance = CreateBCCMapRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBCCMapRequest.to_json())

# convert the object into a dict
create_bcc_map_request_dict = create_bcc_map_request_instance.to_dict()
# create an instance of CreateBCCMapRequest from a dict
create_bcc_map_request_from_dict = CreateBCCMapRequest.from_dict(create_bcc_map_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


