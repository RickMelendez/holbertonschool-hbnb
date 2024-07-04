from flask_restx import Namespace, Resource

country_ns = Namespace('countries', description='Country related operations')

@country_ns.route('/')
class CountryList(Resource):
    def get(self):
        return {'message': 'List of countries'}

    def post(self):
        return {'message': 'Add a new country'}
