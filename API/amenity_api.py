from flask import Blueprint, request, jsonify
from models.amenity import Amenity
from data_manager import DataManager

amenity_api = Blueprint('amenity_api', __name__)
data_manager = DataManager()  # Initialize DataManager

@amenity_api.route('/', methods=['POST'])
def create_amenity():
    data = request.json
    if 'name' not in data:
        return jsonify({'error': 'Missing required field: name'}), 400

    amenity = Amenity(name=data['name'])
    data_manager.save(amenity)
    return jsonify({'message': 'Amenity created successfully', 'amenity': amenity.to_dict()}), 201

@amenity_api.route('/', methods=['GET'])
def get_all_amenities():
    amenities = data_manager.get_all_amenities()
    return jsonify({'amenities': [amenity.to_dict() for amenity in amenities]}), 200

@amenity_api.route('/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, 'amenity')
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    return jsonify(amenity.to_dict()), 200

@amenity_api.route('/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, 'amenity')
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404

    data = request.json
    if 'name' in data:
        amenity.name = data['name']
    data_manager.update(amenity)
    return jsonify({'message': 'Amenity updated successfully', 'amenity': amenity.to_dict()}), 200

@amenity_api.route('/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, 'amenity')
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404

    data_manager.delete(amenity_id, 'amenity')
    return jsonify({'message': 'Amenity deleted successfully'}), 204
