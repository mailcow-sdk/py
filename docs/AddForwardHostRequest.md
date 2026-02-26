# AddForwardHostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_spam** | **float** | 1 to enable spam filter, 0 to disable spam filter | [optional] 
**hostname** | **str** | contains the hostname you want to add | [optional] 

## Example

```python
from mailcow_sdk.models.add_forward_host_request import AddForwardHostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddForwardHostRequest from a JSON string
add_forward_host_request_instance = AddForwardHostRequest.from_json(json)
# print the JSON string representation of the object
print(AddForwardHostRequest.to_json())

# convert the object into a dict
add_forward_host_request_dict = add_forward_host_request_instance.to_dict()
# create an instance of AddForwardHostRequest from a dict
add_forward_host_request_from_dict = AddForwardHostRequest.from_dict(add_forward_host_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


