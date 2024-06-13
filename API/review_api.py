from flask import Blueprint, request, jsonify
from models.review import Review
from data_manager import DataManager

review_api = Blueprint('review_api', __name__)
data_manager = DataManager()  # Initialize DataManager

@review_api.route('/<place_id>', methods=['POST'])
def create_review(place_id):
    data = request.json
    if not all(key in data for key in ['user_id', 'rating', 'comment']):
        return jsonify({'error': 'Missing required fields'}), 400

    review = Review(place_id=place_id, **data)
    data_manager.save(review)
    return jsonify({'message': 'Review created successfully', 'review': review.to_dict()}), 201

@review_api.route('/users/<user_id>', methods=['GET'])
def get_user_reviews(user_id):
    reviews = data_manager.get_reviews_by_user(user_id)
    return jsonify({'reviews': [review.to_dict() for review in reviews]}), 200

@review_api.route('/places/<place_id>', methods=['GET'])
def get_place_reviews(place_id):
    reviews = data_manager.get_reviews_by_place(place_id)
    return jsonify({'reviews': [review.to_dict() for review in reviews]}), 200

@review_api.route('/<review_id>', methods=['GET'])
def get_review(review_id):
    review = data_manager.get(review_id, 'review')
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review.to_dict()), 200

@review_api.route('/<review_id>', methods=['PUT'])
def update_review(review_id):
    review = data_manager.get(review_id, 'review')
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    data = request.json
    for key, value in data.items():
        setattr(review, key, value)
    data_manager.update(review)
    return jsonify({'message': 'Review updated successfully', 'review': review.to_dict()}), 200

@review_api.route('/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = data_manager.get(review_id, 'review')
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    data_manager.delete(review_id, 'review')
    return jsonify({'message': 'Review deleted successfully'}), 204
