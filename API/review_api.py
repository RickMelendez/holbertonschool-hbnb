from flask import request
from flask_restx import Namespace, Resource, fields
from Persistence.data_manager import DataManager 
from Models.review import Review  

data_manager = DataManager()

review_ns = Namespace('review', description='Review operations')

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

        review = Review(
            place_id=place_id,
            user_id=data['user_id'],
            rating=data['rating'],
            comment=data.get('comment', '')
        )

        data_manager.save(review)

        return review, 201

    @review_ns.doc('update_review')
    @review_ns.expect(review_model)
    @review_ns.marshal_with(review_model)
    def put(self, place_id):
        """Update a review for a place"""
        data = request.json
        if not all(key in data for key in ['user_id', 'rating', 'comment']):
            return {'error': 'Missing required fields'}, 400

        review = Review(
            place_id=place_id,
            user_id=data['user_id'],
            rating=data['rating'],
            comment=data.get('comment', '')
        )

        data_manager.update(review)

        return review

@review_ns.route('/user/<int:user_id>')
@review_ns.param('user_id', 'The user identifier')
class UserReviewResource(Resource):
    @review_ns.doc('get_user_reviews')
    @review_ns.marshal_list_with(review_model)
    def get(self, user_id):
        """Get reviews by user ID"""
        reviews = data_manager.get_reviews_by_user(user_id)
        return reviews

@review_ns.route('/place/<int:place_id>')
@review_ns.param('place_id', 'The place identifier')
class PlaceReviewResource(Resource):
    @review_ns.doc('get_place_reviews')
    @review_ns.marshal_list_with(review_model)
    def get(self, place_id):
        """Get reviews by place ID"""
        reviews = data_manager.get_reviews_by_place(place_id)
        return reviews

@review_ns.route('/<int:review_id>')
@review_ns.param('review_id', 'The review identifier')
class SingleReviewResource(Resource):
    @review_ns.doc('get_review')
    @review_ns.marshal_with(review_model)
    def get(self, review_id):
        """Get review by ID"""
        review = data_manager.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return review

    @review_ns.doc('delete_review')
    def delete(self, review_id):
        """Delete a review"""
        success = data_manager.delete_review(review_id)
        if not success:
            return {'error': 'Review not found'}, 404
        return '', 204
