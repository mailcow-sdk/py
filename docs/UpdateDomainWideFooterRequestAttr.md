# UpdateDomainWideFooterRequestAttr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | **str** | Footer text in HTML format | [optional] 
**plain** | **str** | Footer text in PLAIN text format | [optional] 
**mbox_exclude** | **object** | Array of mailboxes to exclude from domain wide footer | [optional] 

## Example

```python
from mailcow_sdk.models.update_domain_wide_footer_request_attr import UpdateDomainWideFooterRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainWideFooterRequestAttr from a JSON string
update_domain_wide_footer_request_attr_instance = UpdateDomainWideFooterRequestAttr.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainWideFooterRequestAttr.to_json())

# convert the object into a dict
update_domain_wide_footer_request_attr_dict = update_domain_wide_footer_request_attr_instance.to_dict()
# create an instance of UpdateDomainWideFooterRequestAttr from a dict
update_domain_wide_footer_request_attr_from_dict = UpdateDomainWideFooterRequestAttr.from_dict(update_domain_wide_footer_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


