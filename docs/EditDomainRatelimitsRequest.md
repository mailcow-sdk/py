# EditDomainRatelimitsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | [**EditMailboxRatelimitsRequestAttr**](EditMailboxRatelimitsRequestAttr.md) |  | [optional] 
**items** | **object** | contains list of domains you want to edit the ratelimit of | [optional] 

## Example

```python
from mailcow_sdk.models.edit_domain_ratelimits_request import EditDomainRatelimitsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditDomainRatelimitsRequest from a JSON string
edit_domain_ratelimits_request_instance = EditDomainRatelimitsRequest.from_json(json)
# print the JSON string representation of the object
print(EditDomainRatelimitsRequest.to_json())

# convert the object into a dict
edit_domain_ratelimits_request_dict = edit_domain_ratelimits_request_instance.to_dict()
# create an instance of EditDomainRatelimitsRequest from a dict
edit_domain_ratelimits_request_from_dict = EditDomainRatelimitsRequest.from_dict(edit_domain_ratelimits_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


