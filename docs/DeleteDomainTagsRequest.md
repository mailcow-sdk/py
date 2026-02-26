# DeleteDomainTagsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of domains you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_domain_tags_request import DeleteDomainTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDomainTagsRequest from a JSON string
delete_domain_tags_request_instance = DeleteDomainTagsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteDomainTagsRequest.to_json())

# convert the object into a dict
delete_domain_tags_request_dict = delete_domain_tags_request_instance.to_dict()
# create an instance of DeleteDomainTagsRequest from a dict
delete_domain_tags_request_from_dict = DeleteDomainTagsRequest.from_dict(delete_domain_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


