from flask_restx import Namespace, Resource

country_ns = Namespace('countries', description='Country operations')


countries_data = [
    {"code": "PR", "name": "Puerto Rico"}
]

@country_ns.route('/')
class CountryList(Resource):
    def get(self):
        """List all countries"""
        return {'countries': countries_data}

@country_ns.route('/<string:country_code>')
class Country(Resource):
    def get(self, country_code):
        """Get details of a country"""
        country = next((c for c in countries_data if c["code"] == country_code), None)
        if country:
            return country
        else:
            return {'error': 'Country not found'}, 404
