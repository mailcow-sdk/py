# DeleteForwardHostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | contains the ip of the fowarding host you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_forward_host_request import DeleteForwardHostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteForwardHostRequest from a JSON string
delete_forward_host_request_instance = DeleteForwardHostRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteForwardHostRequest.to_json())

# convert the object into a dict
delete_forward_host_request_dict = delete_forward_host_request_instance.to_dict()
# create an instance of DeleteForwardHostRequest from a dict
delete_forward_host_request_from_dict = DeleteForwardHostRequest.from_dict(delete_forward_host_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


