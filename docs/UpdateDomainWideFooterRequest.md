# UpdateDomainWideFooterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | [**UpdateDomainWideFooterRequestAttr**](UpdateDomainWideFooterRequestAttr.md) |  | [optional] 
**items** | **List[str]** | contains a list of domain names where you want to update the footer | [optional] 

## Example

```python
from mailcow_sdk.models.update_domain_wide_footer_request import UpdateDomainWideFooterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainWideFooterRequest from a JSON string
update_domain_wide_footer_request_instance = UpdateDomainWideFooterRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainWideFooterRequest.to_json())

# convert the object into a dict
update_domain_wide_footer_request_dict = update_domain_wide_footer_request_instance.to_dict()
# create an instance of UpdateDomainWideFooterRequest from a dict
update_domain_wide_footer_request_from_dict = UpdateDomainWideFooterRequest.from_dict(update_domain_wide_footer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


