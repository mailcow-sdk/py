# CreateTransportMapsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **float** | 1 for a active transport map 0 for a disabled transport map | [optional] 
**destination** | **str** |  | [optional] 
**nexthop** | **str** |  | [optional] 
**password** | **str** | the password for the smtp user | [optional] 
**username** | **str** | the username used to authenticate | [optional] 

## Example

```python
from mailcow_sdk.models.create_transport_maps_request import CreateTransportMapsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransportMapsRequest from a JSON string
create_transport_maps_request_instance = CreateTransportMapsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTransportMapsRequest.to_json())

# convert the object into a dict
create_transport_maps_request_dict = create_transport_maps_request_instance.to_dict()
# create an instance of CreateTransportMapsRequest from a dict
create_transport_maps_request_from_dict = CreateTransportMapsRequest.from_dict(create_transport_maps_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


