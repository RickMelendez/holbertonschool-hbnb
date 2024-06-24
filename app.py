#!/usr/bin/python3
from flask import Flask
from flask_restx import Api
from API.user_api import user_ns
from API.country_api import country_ns
from API.city_api import city_ns
from API.place_api import place_ns
from API.review_api import review_ns
from API.amenity_api import amenity_ns

app = Flask(__name__)
api = Api(app, version='1.0', title='Welcome To HBnB API', description='HBnB application')


api.add_namespace(user_ns)
api.add_namespace(country_ns)
api.add_namespace(city_ns)
api.add_namespace(place_ns)
api.add_namespace(review_ns)
api.add_namespace(amenity_ns)

if __name__ == '__main__':
    app.run(debug=True)
