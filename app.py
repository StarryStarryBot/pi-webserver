import os
from flask import Flask, render_template, request, redirect, session, send_from_directory, jsonify
from data.DataHandler import StarData
import json

app = Flask(__name__)

#global database var
StarDatabase = StarData()

@app.route("/<path:path>")
def home():
    return send_from_directory('static', path)

@app.route("/getStarInfo", methods=['GET']) #?name=Polaris
def getStar():
    name = request.args.get('name')
    global StarDatabase
    star = StarDatabase.find_star(attribute = "hd", value = "12929")

    sky_coordinates = star.get_sky_coordinates()
    coords = f"{sky_coordinates.az.degree:,.3}, {sky_coordinates.alt.degree:,.3}"

    print(coords)

    return json.dumps(coords) #send json

@app.route("/getNearbyStars", methods=['GET']) #?name=Polaris
def getNearbyStars():
    global StarDatabase
    nearby_stars = StarDatabase.find_closest_stars(2, 30)

    return json.dumps(nearby_stars) #send json

if __name__ == '__main__' : 
    app.run(debug=True, port=8888)
    