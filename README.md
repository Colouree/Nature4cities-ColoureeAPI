# Nature4cities-ColoureeAPI Manual
Version 1.0
The Api is located at https://apps.colouree.com/n4c/api and also https://app.colouree.com/n4c/api. For the manual we will refer to apps.colouree as main address.

## 1.0 Resources
The main resource of the API is  ```kpi.json```.

So, the complete url will be https://apps.colouree.com/n4c/api/kpi.json


## 2.0 Endpoints
The API has as many endpoints as the kpi it needs to calculate.
|**Kpi**|**Endpoint**||
|--|--|
|ugsp|/kpi.json/ugsp|
|ugsp|/kpi.json/accessibility|
|ugsp|/kpi.json/areal_sprawl|
|ugsp|/kpi.json/connectivity|
|ugsp|/kpi.json/shannon_index|
|ugsp|/kpi.json/betweenness|

 
## 3.0 Parameters
There are two types of parameters for this API: *path parameters* and *query parameters*.
### 3.1 Path Parameters
#### 3.1.1 Location
The only path parameter present in the API is the ```location``` parameter, used to specify one of the four pilot cities involved in the N4C Project or if needed a custom location that will need additional contextual data, uploaded by the user in the SUAT.

**EXAMPLE: ** ```https://apps.colouree.com/n4c/api/kpi.json/ugsp/{location}```


## 4.0 Request Example

## 5.0 Response Example

It will respond with a json with this basic structure, depending on the request itself:

```
{   
    kpi_name: "requested-kpi",
    result: {
          before: {[GEOJSON]},
          after: {[GEOJSON]}
    },
    context_geom: {
          before: {[GEOJSON]},
          after: {[GEOJSON]}
    },
    
    lat: 40.486748889356605,
    lon: -3.372669271997088,
    pilot_location: "pilot-city",
}
```
This will be discussed in depth in 5.0 Response Example
