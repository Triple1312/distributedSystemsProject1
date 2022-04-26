# Welcome to Distributed Systems project 1

## Running

Running the server is accomplished by running the [run.sh](run.sh) script.
If you havent already made and environment, you can do this by running [pyenv.sh](pyenv.sh)

## Website

The GUI of the website should be really intuitive. 
The entire background is a map that is movable and where the lines are drawn upon.
There is a bar on the left side with dropdown boxes and a submit button.
Submitting two station names will give the duration and draw the route on the map for both train and car.

the website could be opened by running the server and going to [localhost](http://localhost) or opening the [index.html](templates/index.html) file.

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

## Building

To run the backend server, the only thing you should do is make an python env and install the requirements.
The code for the website is already included in the tamplates folder and the static folder, 
with the source code in the client folder.

You can rebuild the source code using the command `npm i` followed by `npm run build`. 
To run these commands you should have nodejs and npm installed.
It will compile automatically to the /templates and /static folders