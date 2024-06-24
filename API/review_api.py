from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace
from Persistence.data_manager import DataManager  # Assuming DataManager import path is correct
from Models.review import Review  # Assuming Review import path is correct

app = Flask(__name__)

# Initialize DataManager
data_manager = DataManager()

# Initialize Namespace
review_ns = Namespace('review', description='Review operations')

# Model for Review
review_model = review_ns.model('Review', {
    'id': fields.Integer(readOnly=True, description='The review unique identifier'),
    'place_id': fields.Integer(required=True, description='ID of the place reviewed'),
    'user_id': fields.Integer(required=True, description='ID of the user who made the review'),
    'rating': fields.Float(required=True, description='Rating of the review'),
    'comment': fields.String(description='Comment of the review')
})

# Resource for managing reviews
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

        # Create the review object
        review = Review(
            place_id=place_id,
            user_id=data['user_id'],
            rating=data['rating'],
            comment=data.get('comment', '')
        )

        # Save the review using the DataManager
        data_manager.save(review)

        # Return the created review with HTTP status code 201
        return review, 201

# Register the review namespace with the Flask application
api = Api(app, version='1.0', title='Review API', description='API for managing reviews')
api.add_namespace(review_ns)

if __name__ == '__main__':
    app.run(debug=True)
