# Nature4cities-ColoureeAPI Manual
Version 1.0
The Api is located at https://apps.colouree.com/n4c/ and also https://app.colouree.com/n4c/

## Resources
The main resource of the API is  
```diff 
+api/kpi.json
```

It will respond with a json with this basic structure, depending on the request itself:

```diff
- text in red
+ text in green
! text in orange
# text in gray
```
```diff
{   
    kpi_name: "#requested-kpi",
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
    pilot_location: "alcala_de_henares",
    
}
```


## Endpoints

## Parameters

## Request Example

## Response Example
