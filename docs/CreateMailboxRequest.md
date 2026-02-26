# CreateMailboxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | is mailbox active or not | [optional] 
**domain** | **str** | domain name | [optional] 
**local_part** | **str** | left part of email address | [optional] 
**name** | **str** | Full name of the mailbox user | [optional] 
**authsource** | **str** | Specifies the authentication source for the mailbox. | [optional] [default to 'mailcow']
**password2** | **str** | mailbox password for confirmation | [optional] 
**password** | **str** | mailbox password when using &#x60;mailcow&#x60; as the authentication source. | [optional] 
**quota** | **float** | mailbox quota | [optional] 
**force_pw_update** | **bool** | forces the user to update its password on first login | [optional] 
**tls_enforce_in** | **bool** | force inbound email tls encryption | [optional] 
**tls_enforce_out** | **bool** | force oubound tmail tls encryption | [optional] 

## Example

```python
from mailcow_sdk.models.create_mailbox_request import CreateMailboxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMailboxRequest from a JSON string
create_mailbox_request_instance = CreateMailboxRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMailboxRequest.to_json())

# convert the object into a dict
create_mailbox_request_dict = create_mailbox_request_instance.to_dict()
# create an instance of CreateMailboxRequest from a dict
create_mailbox_request_from_dict = CreateMailboxRequest.from_dict(create_mailbox_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


