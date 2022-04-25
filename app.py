from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.stations import Stations
from src.directions import Direction

app = Flask(__name__)

api = Api(app)

CORS(app)

api.add_resource(Stations, "/stations", "/stations/<id>")
api.add_resource(Direction, "/direction", "/direction/<name>", "/direction/<frm>/<to>")

if __name__ == '__main__':
    app.run(host="localhost", port=5000)
