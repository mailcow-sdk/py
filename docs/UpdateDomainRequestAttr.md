# UpdateDomainRequestAttr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | is domain active or not | [optional] 
**aliases** | **float** | limit count of aliases associated with this domain | [optional] 
**backupmx** | **bool** | relay domain or not | [optional] 
**defquota** | **float** | predefined mailbox quota in &#x60;add mailbox&#x60; form | [optional] 
**description** | **str** | Description of domain | [optional] 
**gal** | **bool** | is domain global address list active or not, it enables shared contacts accross domain in SOGo webmail | [optional] 
**mailboxes** | **float** | limit count of mailboxes associated with this domain | [optional] 
**maxquota** | **float** | maximum quota per mailbox | [optional] 
**quota** | **float** | maximum quota for this domain (for all mailboxes in sum) | [optional] 
**relay_all_recipients** | **bool** | if not, them you have to create \&quot;dummy\&quot; mailbox for each address to relay | [optional] 
**relay_unknown_only** | **bool** | Relay non-existing mailboxes only. Existing mailboxes will be delivered locally. | [optional] 
**relayhost** | **float** | id of relayhost | [optional] 
**rl_frame** | **str** |  | [optional] 
**rl_value** | **float** | rate limit value | [optional] 
**tags** | **List[str]** | tags for this Domain | [optional] 

## Example

```python
from mailcow_sdk.models.update_domain_request_attr import UpdateDomainRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainRequestAttr from a JSON string
update_domain_request_attr_instance = UpdateDomainRequestAttr.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainRequestAttr.to_json())

# convert the object into a dict
update_domain_request_attr_dict = update_domain_request_attr_instance.to_dict()
# create an instance of UpdateDomainRequestAttr from a dict
update_domain_request_attr_from_dict = UpdateDomainRequestAttr.from_dict(update_domain_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


