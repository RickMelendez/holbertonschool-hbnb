from flask import Blueprint, request, jsonify
from Models.city import City
from Persistence.data_manager import DataManager

city_api = Blueprint('city_api', __name__)
data_manager = DataManager()  # Initialize DataManager

@city_api.route('/', methods=['POST'])
def create_city():
    data = request.json
    if not all(key in data for key in ['name', 'country_code']):
        return jsonify({'error': 'Missing required fields'}), 400

    city = City(name=data['name'], country_code=data['country_code'])
    data_manager.save(city)
    return jsonify({'message': 'City created successfully', 'city': city.to_dict()}), 201

@city_api.route('/', methods=['GET'])
def get_all_cities():
    cities = data_manager.get_all_cities()
    return jsonify({'cities': [city.to_dict() for city in cities]}), 200

@city_api.route('/<city_id>', methods=['GET'])
def get_city(city_id):
    city = data_manager.get(city_id, 'city')
    if not city:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city.to_dict()), 200

@city_api.route('/<city_id>', methods=['PUT'])
def update_city(city_id):
    city = data_manager.get(city_id, 'city')
    if not city:
        return jsonify({'error': 'City not found'}), 404

    data = request.json
    if 'name' in data:
        city.name = data['name']
    data_manager.update(city)
    return jsonify({'message': 'City updated successfully', 'city': city.to_dict()}), 200

@city_api.route('/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = data_manager.get(city_id, 'city')
    if not city:
        return jsonify({'error': 'City not found'}), 404

    data_manager.delete(city_id, 'city')
    return jsonify({'message': 'City deleted successfully'}), 204
