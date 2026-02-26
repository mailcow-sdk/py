# EditFail2BanRequestAttr

array containing the fail2ban settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backlist** | **str** | the backlisted ips or hostnames separated by comma | [optional] 
**ban_time** | **float** | the time an ip should be banned | [optional] 
**ban_time_increment** | **bool** | if the time of the ban should increase each time | [optional] 
**max_attempts** | **float** | the maximum numbe of wrong logins before a ip is banned | [optional] 
**max_ban_time** | **float** | the maximum time an ip should be banned | [optional] 
**netban_ipv4** | **float** | the networks mask to ban for ipv4 | [optional] 
**netban_ipv6** | **float** | the networks mask to ban for ipv6 | [optional] 
**retry_window** | **float** | the maximum time in which a ip as to login with false credentials to be banned | [optional] 
**whitelist** | **str** | whitelisted ips or hostnames sepereated by comma | [optional] 

## Example

```python
from mailcow_sdk.models.edit_fail2_ban_request_attr import EditFail2BanRequestAttr

# TODO update the JSON string below
json = "{}"
# create an instance of EditFail2BanRequestAttr from a JSON string
edit_fail2_ban_request_attr_instance = EditFail2BanRequestAttr.from_json(json)
# print the JSON string representation of the object
print(EditFail2BanRequestAttr.to_json())

# convert the object into a dict
edit_fail2_ban_request_attr_dict = edit_fail2_ban_request_attr_instance.to_dict()
# create an instance of EditFail2BanRequestAttr from a dict
edit_fail2_ban_request_attr_from_dict = EditFail2BanRequestAttr.from_dict(edit_fail2_ban_request_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


