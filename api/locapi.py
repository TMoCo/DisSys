from flask import Flask, jsonify, request
from flask_restful import Resource

from api import api, app, db
from api.data import models as m
from api.calc import distance as d

# Queries the database of countries and returns a list of the countries
class CountryNames(Resource):
    def get(self):
        query = m.Location.query.all()
        countries = []
        for i in range(len(query)):
            countries.append(query[i].country)
        return jsonify({"locations": countries})

# Queries the database returning code of language spoken in requested country
class LanguageCode(Resource):
    def get(self):
        country = request.args.get('country')
        query = m.Location.query.filter_by(country=country)
        return jsonify({"code":query[0].langCode})

# Queries the database returning the capital of the requested country
class CountryCapital(Resource):
    def get(self):
        country = request.args.get('country')
        query = m.Location.query.filter_by(country=country)
        return jsonify({"capital":query[0].capital})

# acceptes two capitals as arguments and calculates the distance between them
class Distance(Resource):
    def get(self):
        # get args from get request
        start = request.args.get('start')
        end = request.args.get('end')
        # query database for args
        query1 = m.Location.query.filter_by(capital=start)
        query2 = m.Location.query.filter_by(capital=end)
        # coordinates of start point
        lat1 = float(query1[0].latitude)
        lon1 = float(query1[0].longitude)
        # coordinates of end point
        lat2 = float(query2[0].latitude)
        lon2 = float(query2[0].longitude)

        return jsonify({"distance":d.distance(lat1,lat2,lon1,lon2)})


api.add_resource(CountryNames, '/getCountries')
api.add_resource(Distance, '/getDistance')
api.add_resource(LanguageCode, '/getCode')
api.add_resource(CountryCapital, '/getCapital')
