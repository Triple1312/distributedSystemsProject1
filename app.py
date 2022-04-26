from flask import Flask, render_template, url_for
from flask_restful import Api
from flask_cors import CORS
from src.stations import Stations
from src.directions import Direction

app = Flask(__name__)

api = Api(app)

CORS(app)

@app.route("/")
def index():
    return render_template("index.html")



api.add_resource(Stations, "/stations", "/stations/<id>")
api.add_resource(Direction, "/direction", "/direction/<name>", "/direction/<frm>/<to>")

if __name__ == '__main__':
    app.run(host="localhost", port=80)
    url_for('static', filename='/static/js/*.js')
    url_for('static', filename='/static/css/*.css')
