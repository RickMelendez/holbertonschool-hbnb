from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from Persistence.data_manager import DataManager
from Models.amenity import Amenity

amenity_ns = Namespace('amenity', description='Amenity operations')
data_manager = DataManager()  # Initialize DataManager

amenity_model = amenity_ns.model('Amenity', {
    'id': fields.Integer(readOnly=True, description='The amenity unique identifier'),
    'name': fields.String(required=True, description='Amenity name')
})

@amenity_ns.route('/')
class AmenityList(Resource):
    @amenity_ns.doc('list_amenities')
    @amenity_ns.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        amenities = data_manager.get_all_amenities()
        return amenities

    @amenity_ns.doc('create_amenity')
    @amenity_ns.expect(amenity_model)
    @amenity_ns.marshal_with(amenity_model, code=201)
    def post(self):
        """Create a new amenity"""
        data = request.json
        if 'name' not in data:
            return {'error': 'Missing required field: name'}, 400

        amenity = Amenity(name=data['name'])
        data_manager.save(amenity)
        return amenity, 201

@amenity_ns.route('/<int:amenity_id>')
@amenity_ns.param('amenity_id', 'The amenity identifier')
class AmenityResource(Resource):
    @amenity_ns.doc('get_amenity')
    @amenity_ns.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Get amenity by ID"""
        amenity = data_manager.get(amenity_id, 'amenity')
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        return amenity

    @amenity_ns.doc('update_amenity')
    @amenity_ns.expect(amenity_model)
    @amenity_ns.marshal_with(amenity_model)
    def put(self, amenity_id):
        """Update an amenity"""
        amenity = data_manager.get(amenity_id, 'amenity')
        if not amenity:
            return {'error': 'Amenity not found'}, 404

        data = request.json
        if 'name' in data:
            amenity.name = data['name']
        data_manager.update(amenity)
        return amenity

    @amenity_ns.doc('delete_amenity')
    def delete(self, amenity_id):
        """Delete an amenity"""
        amenity = data_manager.get(amenity_id, 'amenity')
        if not amenity:
            return {'error': 'Amenity not found'}, 404

        data_manager.delete(amenity_id, 'amenity')
        return '', 204
