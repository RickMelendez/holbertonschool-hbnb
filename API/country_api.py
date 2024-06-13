from flask import Blueprint, jsonify
from data_manager import DataManager

country_api = Blueprint('country_api', __name__)
data_manager = DataManager()  # Initialize DataManager

@country_api.route('/', methods=['GET'])
def get_all_countries():
    countries = data_manager.get_all_countries()
    return jsonify({'countries': [country.to_dict() for country in countries]}), 200

@country_api.route('/<country_code>', methods=['GET'])
def get_country(country_code):
    country = data_manager.get_country_by_code(country_code)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country.to_dict()), 200
