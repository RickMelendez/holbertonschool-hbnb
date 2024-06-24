from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from Models.place import Place
from Persistence.data_manager import DataManager

place_ns = Namespace('place', description='Place operations')
data_manager = DataManager()  # Initialize DataManager

place_model = place_ns.model('Place', {
    'name': fields.String(required=True, description='Name of the place'),
    'description': fields.String(required=True, description='Description of the place'),
    'address': fields.String(required=True, description='Address of the place'),
    'city_id': fields.Integer(required=True, description='ID of the city where the place is located'),
    'latitude': fields.Float(required=True, description='Latitude coordinate of the place'),
    'longitude': fields.Float(required=True, description='Longitude coordinate of the place'),
    'host_id': fields.Integer(required=True, description='ID of the host of the place'),
    'number_of_rooms': fields.Integer(required=True, description='Number of rooms in the place'),
    'number_of_bathrooms': fields.Integer(required=True, description='Number of bathrooms in the place'),
    'price_per_night': fields.Float(required=True, description='Price per night of the place'),
    'max_guests': fields.Integer(required=True, description='Maximum number of guests the place can accommodate'),
    'amenity_ids': fields.List(fields.Integer, required=True, description='List of amenity IDs associated with the place')
})

@place_ns.route('/')
class PlaceListResource(Resource):
    @place_ns.doc('create_place')
    @place_ns.expect(place_model)
    @place_ns.marshal_with(place_model, code=201)
    def post(self):
        """Create a new place"""
        data = request.json
        if not all(key in data for key in ['name', 'description', 'address', 'city_id', 'latitude', 'longitude', 'host_id', 'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests', 'amenity_ids']):
            return {'error': 'Missing required fields'}, 400

        place = Place(**data)
        data_manager.save(place)
        return place, 201

    @place_ns.doc('get_all_places')
    @place_ns.marshal_list_with(place_model)
    def get(self):
        """Get all places"""
        places = data_manager.get_all_places()
        return places

@place_ns.route('/<int:place_id>')
@place_ns.doc(params={'place_id': 'ID of the place'})
class PlaceResource(Resource):
    @place_ns.doc('get_place')
    @place_ns.marshal_with(place_model)
    def get(self, place_id):
        """Get a place by ID"""
        place = data_manager.get(place_id, 'place')
        if not place:
            return {'error': 'Place not found'}, 404
        return place

    @place_ns.doc('update_place')
    @place_ns.expect(place_model)
    @place_ns.marshal_with(place_model)
    def put(self, place_id):
        """Update a place"""
        place = data_manager.get(place_id, 'place')
        if not place:
            return {'error': 'Place not found'}, 404

        data = request.json
        for key, value in data.items():
            setattr(place, key, value)
        data_manager.update(place)
        return place

    @place_ns.doc('delete_place')
    def delete(self, place_id):
        """Delete a place"""
        place = data_manager.get(place_id, 'place')
        if not place:
            return {'error': 'Place not found'}, 404

        data_manager.delete(place_id, 'place')
        return '', 204
