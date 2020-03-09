# Nature4cities-ColoureeAPI Manual
Version 1.0
The Api is located at https://apps.colouree.com/n4c/ and also https://app.colouree.com/n4c/

## 1.0 Resources
The main resource of the API is  ```api/kpi.json```

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


## 2.0 Endpoints
The API has as many endpoints as the kpi it needs to calculate. S

## 3.0 Parameters

## 4.0 Request Example

## 5.0 Response Example
