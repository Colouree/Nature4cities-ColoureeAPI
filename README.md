# Nature4cities-ColoureeAPI Manual
The Api is located at https://apps.colouree.com/n4c/api and also https://app.colouree.com/n4c/api. For the manual we will refer to apps.colouree as main address.

The scope of this API is to porvide calculations for a number of *Key Performance Indicators* (**KPI**) used to measure the implementation of Nature Based Solutions (**NBS**).

*Curly braces in paths indicate a customizable parameter, in this case "path" function as a placehoolder /example/{path}/to/resource*
###### Contact: f.silvestri@colouree.com

## 1. Resources
The main resource of the API is  ```kpi.json```.
There is also a resource dedicated to access tokens at ```access_token.json```

Complete paths will be in the form of 

https://apps.colouree.com/n4c/api/kpi.json

and https://apps.colouree.com/n4c/api/access_token.json

## 2. Authentication
The API is accessible through token-based authentication: the Token is obtainable at https://apps.colouree.com/n4c, after the registration. The token needs to be passed for every request, as the value of the parameter ```token```

### 2.1 Endpoints for token management

since the service needs authentication to be accessed, the user can send a HTTP requests with a header of the form:
```
	GET /index.html HTTP/1.0
	Host: basic.example.com
	Authorization: Basic QwxhZGRpbjpvcGVuIHNlc2FtZQ==
 ```
 
|METHOD|ENDPOINT|RESPONSE
|--|--|--|
|GET|https://app.colouree.com/n4c/api/acces_token.json|list of active tokens|
|PUT|https://app.colouree.com/n4c/api/acces_token.json|creates a new token|
|DELETE|https://app.colouree.com/n4c/api/acces_token.json/{your-token}|deletes token|

## 3. Endpoints
The API has as many endpoints as the kpi it needs to calculate.

|**Kpi**|**Endpoint**|
The Method for all of these is POST.
|--|--|
|Urban Green Space Proportion|/kpi.json/ugsp|
|Accessibility of Green Spaces|/kpi.json/accessibility|
|Areal Sprawl|/kpi.json/areal_sprawl|
|Connectivity of Green Spaces|/kpi.json/connectivity|
|Shannon Index|/kpi.json/shannon_index|
|Betweenness|/kpi.json/betweenness|

 
## 4. Parameters
There are two types of parameters for this API: *path parameters* and *query parameters*.

### 4.1 Path Parameters

#### 4.1.1 Location
The only path parameter present in the API is the ```location``` parameter, used to specify one of the four pilot cities involved in the N4C Project (*Alcala de Henares, Szeged, Milan and Chankaya*) or if needed a custom location that will need additional contextual data, uploaded by the user through the SUA, and passed to the API in the ```context``` parameter (4.2.5)

**EXAMPLE:** ```https://apps.colouree.com/n4c/api/kpi.json/ugsp/{location}```

### 4.2 Query Parameters

#### 4.2.1 assessment (optional)
This parameter can be passed by the user to specify the type of calculation requested: *before* the implementation of the NBS, *after* the implementation of the NBS or *both* cases: therefore the parameter takes three possible string values:
*  ```after```
*  ```before```
*  ```both```

If the **assessment** parameter is not passed, it defaults to ```both```

**DEFAULTS TO:** *'both'*

**IMPORTANT:** if the value of the parameter is either ```after``` or ```both``` the project (4.2.2) parameter is required.

#### 4.2.2 Project (optional, depending on assessment type)
This parameter holds the geometric and attribute information about the NBS project to be assessed. Since the possibility to perform a calculation before the implementation of an NBS, this parameter isn't strictly required; it is instead required if if the ```before``` or ```both``` values are passed to ```assessment```

The data structure of the data passed to the **project** parameter must follow the [GeoJSON](https://geojson.org/) specification (RFC 7946). See the complete specification at https://tools.ietf.org/html/rfc7946

**EXAMPLE**
```javascript
{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [...]
  },
  "properties": {
    "name": "bench"
  }
}
```
***
The **geometry** key holds purely geometric information, represented in [EPSG:4326](https://spatialreference.org/ref/epsg/wgs-84/) projection as per the GeoJSON specification:

Latitude Bounds [-90.0000, 90.0000]
Longitude Bounds [-180.0000, 180.0000]

Geometries passed in any other projection will cause wrong or nonsensical results for the calculations.
***
The  **properties** key holds different attributes depending on the real world object they are describing:

The properties needed for a **building** are two:
|||
|--:|:--|
|**height**| number in (m)|
|**building**|'yes'|


**EXAMPLE:**
```javascript
"properties": {
    "building": "yes",
    "height": 33
  }
  ```
***
The property needed for a **green area** is just one:**landuse**. It can take different values, depending on the type of kpi. For every kpi except shi (Shannon Index), the value needed is *'green_area'*, while for the Shannon Index the possible values are 
 * 'trees'
 * 'shrubs'
 * 'grassland'
 * 'bare turf' (or 'grass')
 * 'built'
 
**EXAMPLE:**
```javascript
"properties": {
    "landuse": 'trees'
  }
  ```
#### 4.2.3 lon (required)
This is a simple numerical parameter to store the longitude of the center of the project (in EPSG:4326)

#### 4.2.4 lat (required)
This is a simple numerical parameter to store the latitude of the center of the project (in EPSG:4326)

#### 4.2.5 token (required)
This parameters stores the access token needed to access the API. The token is in the form of a Universal Unique Id (UUID)

#### 4.2.6 context(optional, depending on ```location``` 3.1.1)
This parameters holds the contextual information on which perform the calculation when a ```location``` different from the supported pilot cities is provided.
It has the same specifics of the **project** parameter.


## 5. Request Examples
Here are some request examples.

### 5.1 Tokens

**Token creation**
PUT https://apps.colouree.com/n4c/api/access_token.json

**Token list:**
GET https://apps.colouree.com/n4c/api/access_token.json

**Token deletion:**
DELETE https://apps.colouree.com/n4c/api/access_token.json/{your-token-here}

### 5.2 Kpi operations

**Kpi calculation before NBS implementation**
POST https://app.colouree.com/n4c/api/kpi.json/{kpi}/{pilot-location}/?lon=-3.4&lat=46.7?token={your-access-token}&assessment=before

**Note:** the ```project``` parameter does not need to be passed, since the ```assessment``` value is set to *before*

**Kpi calculation before and after NBS implementation**
POST https://app.colouree.com/n4c/api/kpi.json/{kpi}/{pilot-location}/?lon=-3.4&lat=46.7?token={your-access-token}&assessment=both&project={*GeoJSON data*}

**Kpi calculation not on a pilot location**
POST https://app.colouree.com/n4c/api/kpi.json/{kpi}/{*CUSTOM LOCATION*}/?lon=-3.4&lat=46.7?token={your-access-token}&assessment=both&project={*GeoJSON data*}&context={*GeoJSON data*}


## 6. Response Example

### 6.1 Response template

```javascript
{   
    kpi_name: "requested-kpi",
    result: {
          before: {GeoJSON},
          after: {GeoJSON}
    },
    context_geom: {
          before: {GeoJSON},
          after: {GeoJSON}
    },
    
    lat: 40.486748889356605,
    lon: -3.372669271997088,
    pilot_location: "pilot-city",
}
```
## 7. Standards
A brief list of the standards utilized by the API:

GeoJSON

EPSG:4326

