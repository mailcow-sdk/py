# EditExternalIdentityProviderSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[object]** |  | [optional] [default to ["identity-provider"]]
**attr** | [**EditExternalIdentityProviderSettingsRequestAttr**](EditExternalIdentityProviderSettingsRequestAttr.md) |  | [optional] 

## Example

```python
from mailcow_sdk.models.edit_external_identity_provider_settings_request import EditExternalIdentityProviderSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditExternalIdentityProviderSettingsRequest from a JSON string
edit_external_identity_provider_settings_request_instance = EditExternalIdentityProviderSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(EditExternalIdentityProviderSettingsRequest.to_json())

# convert the object into a dict
edit_external_identity_provider_settings_request_dict = edit_external_identity_provider_settings_request_instance.to_dict()
# create an instance of EditExternalIdentityProviderSettingsRequest from a dict
edit_external_identity_provider_settings_request_from_dict = EditExternalIdentityProviderSettingsRequest.from_dict(edit_external_identity_provider_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


