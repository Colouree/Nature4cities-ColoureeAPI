# Nature4cities-ColoureeAPI Manual
The Api is located at https://apps.colouree.com/n4c/api and also https://app.colouree.com/n4c/api. For the manual we will refer to apps.colouree as main address.

The scope of this API is to porvide calculations for a number of *Key Performance Indicators* (**KPI**) used to measure the implementation of Nature Based Solutions (**NBS**).


*Version 1.0*

*Curly braces in paths indicate a customizable parameter, in this case "path" function as a placehoolder /example/{path}/to/resource*
###### Contact: f.silvestri@colouree.com

## 1. Resources
The main resource of the API is  ```kpi.json```.

So, the complete url will be https://apps.colouree.com/n4c/api/kpi.json


## 2. Endpoints
The API has as many endpoints as the kpi it needs to calculate.

|**Kpi**|**Endpoint**|
|--|--|
|Urban Green Space Proportion|/kpi.json/ugsp|
|Accessibility of Green Spaces|/kpi.json/accessibility|
|Areal Sprawl|/kpi.json/areal_sprawl|
|Connectivity of Green Spaces|/kpi.json/connectivity|
|Shannon Index|/kpi.json/shannon_index|
|Betweenness|/kpi.json/betweenness|

 
## 3. Parameters
There are two types of parameters for this API: *path parameters* and *query parameters*.
### 3.1 Path Parameters
#### 3.1.1 Location
The only path parameter present in the API is the ```location``` parameter, used to specify one of the four pilot cities involved in the N4C Project (*Alcala de Henares, Szeged, Milan and Chankaya*) or if needed a custom location that will need additional contextual data, uploaded by the user through the SUAT.

**EXAMPLE:** ```https://apps.colouree.com/n4c/api/kpi.json/ugsp/{location}```

### 3.2 Query Parameters
#### 3.2.1 Assessment
**DEFAULT:** *'both'*
This parameter can be passed by the user to specify the type of calculation requested: *before* the implementation of the NBS, *after* the implementation of the NBS or *both* cases: therefore the parameter takes three possible string values:
*  ```after```
*  ```before```
*  ```both```
If the ```assessment``` parameter is not passed, it defaults to ```both```

**IMPORTANT:** if the value of the parameter is either ```after``` or ```both``` the project parameters is needed.


## 4. Request Example

## 5. Response Example

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
