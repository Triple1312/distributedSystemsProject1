from flask_restful import Resource
import requests
import src.store as store
from .stations import getStations

class Direction(Resource):

    def error(self):
        return {"error": "you should add 2 stations to the end of this url"}

    def get(self, frm=None, to=None):
        if to:
            return {
                "train": self.getTrainDirections(frm, to),
                "car": self.getCarDirections(frm, to)
            }
        else:
            return self.error()

    def getCarDirections(self, frm, to):
        from_coords = self.stationCoordsAsList(frm)
        to_coords = self.stationCoordsAsList(to)
        print(from_coords[0], from_coords[1], to_coords[0], to_coords[1])
        url = 'https://api.mapbox.com/directions/v5/mapbox/driving/{},{};{},' \
              '{}?alternatives=false&geometries=geojson&overview=full&steps=false&access_token=pk' \
              '.eyJ1IjoicHBwYzEzMTIiLCJhIjoiY2wxNTk0dGR0MHl6NzNkczBxNzRxbTczNSJ9.qFzM1Q2oov0E6rFbDodAdQ'\
            .format(from_coords[0], from_coords[1], to_coords[0], to_coords[1])
        print(url)

        r = requests.get(url)
        data = r.json()["routes"][0]
        route = data["geometry"]["coordinates"]
        geojson = {
            'type': 'Feature',
            'properties': {},
            "geometry": {
                'type': 'LineString',
                'coordinates': route
            }
        }
        return {"duration": data["duration"], "geojson": geojson}

    def getTrainDirections(self, frm, to):
        url = "https://api.irail.be/connections?from={}&to={}&format=json&lang=en&results=2"\
            .format(frm, to)
        r = requests.get(url)
        data = r.json()
        duration = 0
        route = [self.stationCoordsAsList(frm)]
        try :
            duration = data["connection"][0]["duration"]
            vias = data["connection"][0]["vias"]["via"]
            for i in vias:
                route.append([i["stationinfo"]["locationX"], i["stationinfo"]["locationY"]])
        except:
            duration = 0
        route.append(self.stationCoordsAsList(to))
        geojson = {
            "type": 'Feature',
            "properties": {},
            "geometry": {
                'type': 'LineString',
                'coordinates': route,
            }
        }
        return {"duration": duration, "geojson": geojson}


    def stationCoordsAsList(self, station):
        if len(store.store["stations"]) == 0:
            getStations()
        for i in store.store["stations"]["station"]:
            if i["name"] == station:
                return [i["locationX"], i["locationY"]]
        return None
