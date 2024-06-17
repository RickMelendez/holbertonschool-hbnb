from flask import Flask, jsonify
from API.amenity_api import init_amenity_routes
from API.city_api import init_city_routes
from API.country_api import init_country_routes
from API.place_api import init_place_routes
from API.review_api import init_review_routes
from API.user_api import init_user_routes

def route_manager(app):
    # Initialize routes from different modules
    init_amenity_routes(app)
    init_city_routes(app)
    init_country_routes(app)
    init_place_routes(app)
    init_review_routes(app)
    init_user_routes(app)

    # Root route
    @app.route('/')
    def home():
        return "Welcome to the HBnB Evolution API!"

    # Endpoint to list all routes
    @app.route('/routes', methods=['GET'])
    def list_routes():
        routes = []
        for rule in app.url_map.iter_rules():
            routes.append({'endpoint': rule.endpoint, 'methods': ','.join(rule.methods), 'url': str(rule)})
        return jsonify(routes)
