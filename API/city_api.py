from flask_restx import Resource, fields

from flask import Blueprint, request, jsonify

from Models.city import City
from Persistence.data_manager import DataManager
from flask_restx import Namespace

city_ns = Namespace('city', description='City operations')
city_api = Blueprint('city_api', __name__)
data_manager = DataManager()  # Initialize DataManager

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

        city = City(name=data['name'], country_code=data['country_code'])
        data_manager.save(city)
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
        city = data_manager.get(city_id, 'city')
        if not city:
            return {'error': 'City not found'}, 404
        return city

    @city_ns.doc('update_city')
    @city_ns.expect(city_model)
    @city_ns.marshal_with(city_model)
    def put(self, city_id):
        """Update a city"""
        city = data_manager.get(city_id, 'city')
        if not city:
            return {'error': 'City not found'}, 404

        data = request.json
        if 'name' in data:
            city.name = data['name']
        data_manager.update(city)
        return city

    @city_ns.doc('delete_city')
    def delete(self, city_id):
        """Delete a city"""
        city = data_manager.get(city_id, 'city')
        if not city:
            return {'error': 'City not found'}, 404

        data_manager.delete(city_id, 'city')
        return '', 204
