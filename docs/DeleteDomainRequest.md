# DeleteDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | [optional] 

## Example

```python
from mailcow_sdk.models.delete_domain_request import DeleteDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDomainRequest from a JSON string
delete_domain_request_instance = DeleteDomainRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteDomainRequest.to_json())

# convert the object into a dict
delete_domain_request_dict = delete_domain_request_instance.to_dict()
# create an instance of DeleteDomainRequest from a dict
delete_domain_request_from_dict = DeleteDomainRequest.from_dict(delete_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


