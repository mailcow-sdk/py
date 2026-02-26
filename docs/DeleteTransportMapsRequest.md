# DeleteTransportMapsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **object** | contains list of transport maps you want to delete | [optional] 

## Example

```python
from mailcow_sdk.models.delete_transport_maps_request import DeleteTransportMapsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTransportMapsRequest from a JSON string
delete_transport_maps_request_instance = DeleteTransportMapsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteTransportMapsRequest.to_json())

# convert the object into a dict
delete_transport_maps_request_dict = delete_transport_maps_request_instance.to_dict()
# create an instance of DeleteTransportMapsRequest from a dict
delete_transport_maps_request_from_dict = DeleteTransportMapsRequest.from_dict(delete_transport_maps_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


