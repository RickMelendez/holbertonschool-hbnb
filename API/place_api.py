from flask import Blueprint, request, jsonify
from Models.place import Place
from Persistence.data_manager import DataManager

place_api = Blueprint('place_api', __name__)
data_manager = DataManager()  # Initialize DataManager

@place_api.route('/', methods=['POST'])
def create_place():
    data = request.json
    required_fields = ['name', 'description', 'address', 'city_id', 'latitude', 'longitude', 'host_id', 'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests', 'amenity_ids']
    if not all(key in data for key in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    place = Place(**data)
    data_manager.save(place)
    return jsonify({'message': 'Place created successfully', 'place': place.to_dict()}), 201

@place_api.route('/', methods=['GET'])
def get_all_places():
    places = data_manager.get_all_places()
    return jsonify({'places': [place.to_dict() for place in places]}), 200

@place_api.route('/<place_id>', methods=['GET'])
def get_place(place_id):
    place = data_manager.get(place_id, 'place')
    if not place:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify(place.to_dict()), 200

@place_api.route('/<place_id>', methods=['PUT'])
def update_place(place_id):
    place = data_manager.get(place_id, 'place')
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    data = request.json
    for key, value in data.items():
        setattr(place, key, value)
    data_manager.update(place)
    return jsonify({'message': 'Place updated successfully', 'place': place.to_dict()}), 200

@place_api.route('/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = data_manager.get(place_id, 'place')
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    data_manager.delete(place_id, 'place')
    return jsonify({'message': 'Place deleted successfully'}), 204

