from flask import Flask, request
from flask_restful import Resource, Api
import requests
import src.store as store


def getStations():
    print("started")
    url = 'https://api.irail.be/stations?format=json&lang=en'
    r = requests.get(url)
    data = r.json()
    store.store["stations"] = data
    return data

class Stations(Resource):
    def getStation(self, id):
        getStations()
        for i in store.store["stations"]['station']:
            print(i)
            if i['id'] == id:
                return i
        return {"error": "no such id corresponds to a station"}

    def get(self, id=None):
        if id:
            return self.getStation(id)
        else:
            return getStations()


