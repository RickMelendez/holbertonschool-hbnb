from flask import Flask, request, jsonify
from Models.user import User
from Models.place import Place
from Models.review import Review
from Models.city import City
from Models.country import Country
from Models.amenity import Amenity

users = []
places = []
reviews = []
cities = []
countries = []
amenities = []

def route_manager(app):
    @app.route('/')
    def home():
        return "Welcome to the HBnB Evolution API!"

    # User routes
    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        new_user = User(data['email'], data['password'], data.get('first_name', ''), data.get('last_name', ''))
        users.append(new_user)
        return jsonify({'id': new_user.id}), 201

    @app.route('/users/<user_id>', methods=['GET'])
    def get_user(user_id):
        user = next((u for u in users if u.id == user_id), None)
        if user:
            return jsonify({'id': user.id, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name}), 200
        return jsonify({'error': 'User not found'}), 404

    # Place routes
    @app.route('/places', methods=['POST'])
    def create_place():
        data = request.get_json()
        host = next((u for u in users if u.id == data['host_id']), None)
        if not host:
            return jsonify({'error': 'Host not found'}), 404
        new_place = Place(data['name'], data['description'], data['price'], data['max_guests'], host)
        places.append(new_place)
        return jsonify({'id': new_place.id}), 201

    @app.route('/places/<place_id>', methods=['GET'])
    def get_place(place_id):
        place = next((p for p in places if p.id == place_id), None)
        if place:
            return jsonify({'id': place.id, 'name': place.name, 'description': place.description, 'price': place.price, 'max_guests': place.max_guests, 'host': place.host.id}), 200
        return jsonify({'error': 'Place not found'}), 404

    # Review routes
    @app.route('/reviews', methods=['POST'])
    def create_review():
        data = request.get_json()
        user = next((u for u in users if u.id == data['user_id']), None)
        place = next((p for p in places if p.id == data['place_id']), None)
        if not user or not place:
            return jsonify({'error': 'User or Place not found'}), 404
        new_review = Review(user, place, data['text'])
        reviews.append(new_review)
        return jsonify({'id': new_review.id}), 201

    @app.route('/reviews/<review_id>', methods=['GET'])
    def get_review(review_id):
        review = next((r for r in reviews if r.id == review_id), None)
        if review:
            return jsonify({'id': review.id, 'user': review.user.id, 'place': review.place.id, 'text': review.text}), 200
        return jsonify({'error': 'Review not found'}), 404

    # City routes
    @app.route('/cities', methods=['POST'])
    def create_city():
        data = request.get_json()
        country = next((c for c in countries if c.id == data['country_id']), None)
        if not country:
            return jsonify({'error': 'Country not found'}), 404
        new_city = City(data['name'], country)
        cities.append(new_city)
        return jsonify({'id': new_city.id}), 201

    @app.route('/cities/<city_id>', methods=['GET'])
    def get_city(city_id):
        city = next((c for c in cities if c.id == city_id), None)
        if city:
            return jsonify({'id': city.id, 'name': city.name, 'country': city.country.id}), 200
        return jsonify({'error': 'City not found'}), 404

    # Country routes
    @app.route('/countries', methods=['POST'])
    def create_country():
        data = request.get_json()
        new_country = Country(data['name'])
        countries.append(new_country)
        return jsonify({'id': new_country.id}), 201

    @app.route('/countries/<country_id>', methods=['GET'])
    def get_country(country_id):
        country = next((c for c in countries if c.id == country_id), None)
        if country:
            return jsonify({'id': country.id, 'name': country.name}), 200
        return jsonify({'error': 'Country not found'}), 404

    # Amenity routes
    @app.route('/amenities', methods=['POST'])
    def create_amenity():
        data = request.get_json()
        new_amenity = Amenity(data['name'])
        amenities.append(new_amenity)
        return jsonify({'id': new_amenity.id}), 201

    @app.route('/amenities/<amenity_id>', methods=['GET'])
    def get_amenity(amenity_id):
        amenity = next((a for a in amenities if a.id == amenity_id), None)
        if amenity:
            return jsonify({'id': amenity.id, 'name': amenity.name}), 200
        return jsonify({'error': 'Amenity not found'}), 404
