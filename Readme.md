# Welcome to Distributed Systems project 1
## Website

## API
### requests
#### get stations
this gives the info of all stations that are in the NMBS API

    /stations

#### get specific station info
returns all the info of a specific station. the `<name>` argument is the English name of a station. all station names can be obtained by the `/stations` url. 

	/stations/<name>

#### get directions 
returns directions to get from one station to another. It will return both the directions by train and by car.
It needs two arguments `<from>` and `<to>` that correspond to the name of the two stations.

	/direction/<from>/<to>
##### return value:
    {
        train: { 
				duration: `duration in seconds`,
				geojson: `linestring of directions`,
			   },
		car: { 
			   duration: `duration in seconds`,
			   geojson: `linestring of directions`,
			 },
	}
	