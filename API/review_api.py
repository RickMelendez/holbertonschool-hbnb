from flask_restx import Resource, fields

from flask import request

from Models.review import Review
from Persistence.data_manager import DataManager
from flask_restx import Namespace

review_ns = Namespace('review', description='Review operations')
data_manager = DataManager()  # Initialize DataManager

review_model = review_ns.model('Review', {
    'id': fields.Integer(readOnly=True, description='The review unique identifier'),
    'place_id': fields.Integer(required=True, description='ID of the place reviewed'),
    'user_id': fields.Integer(required=True, description='ID of the user who made the review'),
    'rating': fields.Float(required=True, description='Rating of the review'),
    'comment': fields.String(description='Comment of the review')
})

@review_ns.route('/<int:place_id>')
@review_ns.doc(params={'place_id': 'ID of the place to create a review for'})
class ReviewResource(Resource):
    @review_ns.doc('create_review')
    @review_ns.expect(review_model)
    @review_ns.marshal_with(review_model, code=201)
    def post(self, place_id):
        """Create a new review for a place"""
        data = request.json
        if not all(key in data for key in ['user_id', 'rating', 'comment']):
            return {'error': 'Missing required fields'}, 400

        
