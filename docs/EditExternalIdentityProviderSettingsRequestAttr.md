# EditExternalIdentityProviderSettingsRequestAttr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authsource** | **str** | Specifies the type of the Identity Provider | [optional] 
**server_url** | **str** | The base URL of your Keycloak server. Required if &#x60;authsource&#x60; is keycloak. | [optional] 
**realm** | **str** | The Keycloak realm where the mailcow client is configured. Required if &#x60;authsource&#x60; is keycloak. | [optional] 
**client_id** | **str** | The Client ID assigned to mailcow Client in OIDC Provider. Required if &#x60;authsource&#x60; is keycloak or generic-oidc. | [optional] 
**client_secret** | **str** | The Client Secret assigned to mailcow Client in OIDC Provider. Required if &#x60;authsource&#x60; is keycloak or generic-oidc. | [optional] 
**redirect_url** | **str** | The redirect URL that OIDC Provider will use after authentication. Required if &#x60;authsource&#x60; is keycloak or generic-oidc. | [optional] 
**redirect_url_extra** | **List[object]** | Additional redirect URLs that OIDC Provider can use after authentication if valid. | [optional] 
**version** | **str** | Specifies the Keycloak version. Required if &#x60;authsource&#x60; is keycloak. | [optional] 
**default_template** | **str** | (Optional) If no matching Attribute Mapping exists for a User, the default template will be used for creating the mailbox, but not for updating the mailbox. | [optional] 
**mappers** | **List[object]** | (Optional) Attribute values used to match a mailbox template. Each element corresponds to the respective index in the templates array (i.e., the first element matches the first element of templates, the second matches the second, and so on). | [optional] 
**templates** | **List[object]** | (Optional) Defines the mailbox templates to be assigned. Each element corresponds to the respective index in the &#x60;mappers&#x60; array. | [optional] 
**ignore_ssl_error** | **bool** | If enabled, SSL certificate validation is bypassed | [optional] [default to False]
**mailpassword_flow** | **bool** | If enabled, mailcow will attempt to validate user credentials using the Keycloak Admin REST API instead of relying solely on the Authorization Code Flow. | [optional] [default to False]
**periodic_sync** | **bool** | If enabled, mailcow periodically performs a full sync of all users from Keycloak or LDAP. | [optional] [default to False]
**import_users** | **bool** | If enabled, new users are automatically imported from Keycloak or LDAP into mailcow. | [optional] [default to False]
**sync_interval** | **float** | Defines the time interval (in minutes) for periodic synchronization and user imports. | [optional] [default to 15]
**host** | **str** | The address of your LDAP server. You can provide a single hostname or a comma-separated list of hosts for fallback in case the primary server is unreachable. Required if &#x60;authsource&#x60; is ldap. | [optional] 
**port** | **str** | The port used to connect to the LDAP server. Required if &#x60;authsource&#x60; is ldap. | [optional] 
**use_ssl** | **bool** | enable LDAPS connection. If Port is set to 389 it will be overriden to 636. | [optional] [default to False]
**use_tls** | **bool** | enable TLS connection. TLS is recommended over SSL. SSL Ports cannot be used. | [optional] [default to False]
**basedn** | **str** | The Distinguished Name (DN) from which searches will be performed. Required if &#x60;authsource&#x60; is ldap. | [optional] 
**username_field** | **str** | The LDAP attribute used to identify users during authentication. Required if &#x60;authsource&#x60; is ldap. | [optional] [default to 'mail']
**filter** | **str** | An optional LDAP search filter to refine which users can authenticate. | [optional] 
**attribute_field** | **str** | Specifies an LDAP attribute that holds a specific value which can be mapped to a mailbox template using the Attribute Mapping section. Required if &#x60;authsource&#x60; is ldap. | [optional] 
**binddn** | **str** | The Distinguished Name (DN) of the LDAP user that will be used to authenticate and perform LDAP searches. This account should have sufficient permissions to read the required attributes. Required if &#x60;authsource&#x60; is ldap. | [optional] 
**bindpass** | **str** | The password for the Bind DN user. It is required for authentication when connecting to the LDAP server. Required if &#x60;authsource&#x60; is ldap. | [optional] 
**authorize_url** | **str** | The OIDC provider&#39;s authorization server URL. Required if &#x60;authsource&#x60; is generic-oidc. | [optional] 
**token_url** | **str** | The OIDC provider&#39;s token server URL. Required if &#x60;authsource&#x60; is generic-oidc. | [optional] 
**userinfo_url** | **str** | The OIDC provider&#39;s user info server URL. Required if &#x60;authsource&#x60; is generic-oidc. | [optional] 
**client_scopes** | **str** | Specifies the OIDC scopes requested during authentication. | [optional] [default to 'openid profile email mailcow_template']

## Example

```python
from mailcow_sdk.models.edit_external_identity_provider_settings_request_attr import EditExternalIdentityProviderSettingsRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of EditExternalIdentityProviderSettingsRequestAttr from a JSON string
edit_external_identity_provider_settings_request_attr_instance = EditExternalIdentityProviderSettingsRequestAttr.from_json(json)
# print the JSON string representation of the object
print(EditExternalIdentityProviderSettingsRequestAttr.to_json())

# convert the object into a dict
edit_external_identity_provider_settings_request_attr_dict = edit_external_identity_provider_settings_request_attr_instance.to_dict()
# create an instance of EditExternalIdentityProviderSettingsRequestAttr from a dict
edit_external_identity_provider_settings_request_attr_from_dict = EditExternalIdentityProviderSettingsRequestAttr.from_dict(edit_external_identity_provider_settings_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


