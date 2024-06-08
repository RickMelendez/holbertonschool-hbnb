from flask import Flask
from api.user_api import user_api
from api.place_api import place_api
from api.review_api import review_api
from api.amenity_api import amenity_api
from api.country_api import country_api
from api.city_api import city_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_api, url_prefix='/api/users')
    app.register_blueprint(place_api, url_prefix='/api/places')
    app.register_blueprint(review_api, url_prefix='/api/reviews')
    app.register_blueprint(amenity_api, url_prefix='/api/amenities')
    app.register_blueprint(country_api, url_prefix='/api/countries')
    app.register_blueprint(city_api, url_prefix='/api/cities')
    return app
