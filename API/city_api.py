from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from Persistence.data_manager import DataManager

city_ns = Namespace('city', description='City operations')
data_manager = DataManager()

city_model = city_ns.model('City', {
    'name': fields.String(required=True, description='Name of the city'),
    'country_code': fields.String(required=True, description='Country code of the city')
})

@city_ns.route('/')
class CityListResource(Resource):
    @city_ns.doc('create_city')
    @city_ns.expect(city_model)
    @city_ns.marshal_with(city_model, code=201)
    def post(self):
        """Create a new city"""
        data = request.json
        if not all(key in data for key in ['name', 'country_code']):
            return {'error': 'Missing required fields'}, 400

        city = data_manager.save_city(data['name'], data['country_code'])
        return city, 201

    @city_ns.doc('get_all_cities')
    @city_ns.marshal_list_with(city_model)
    def get(self):
        """Get all cities"""
        cities = data_manager.get_all_cities()
        return cities

@city_ns.route('/<int:city_id>')
@city_ns.doc(params={'city_id': 'ID of the city'})
class CityResource(Resource):
    @city_ns.doc('get_city')
    @city_ns.marshal_with(city_model)
    def get(self, city_id):
        """Get a city by ID"""
        city = data_manager.get_city(city_id)
        if not city:
            return {'error': 'City not found'}, 404
        return city

    @city_ns.doc('update_city')
    @city_ns.expect(city_model)
    @city_ns.marshal_with(city_model)
    def put(self, city_id):
        """Update a city"""
        city = data_manager.get_city(city_id)
        if not city:
            return {'error': 'City not found'}, 404

        data = request.json
        if 'name' in data:
            city.name = data['name']
        if 'country_code' in data:
            city.country_code = data['country_code']
        data_manager.update_city(city)
        return city

    @city_ns.doc('delete_city')
    def delete(self, city_id):
        """Delete a city"""
        city = data_manager.get_city(city_id)
        if not city:
            return {'error': 'City not found'}, 404

        data_manager.delete_city(city_id)
        return '', 204
