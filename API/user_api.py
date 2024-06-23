from flask import Blueprint, Flask, request, jsonify
from flask_restx import Namespace, Resource, fields
from flask import request

from Models.user import User
from Persistence.data_manager import DataManager

user_blueprint = Blueprint('user', __name__)
user_ns = Namespace('user', description='User operations')
data_manager = DataManager()  # Initialize DataManager


# Endpoint to create a new user
@user_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not all(key in data for key in ['email', 'first_name', 'last_name']):
        return jsonify({'error': 'Missing required fields'}), 400

    email = data['email']
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format'}), 400

    # Check if email is already in use
    existing_user = data_manager.get_user_by_email(email)
    if existing_user:
        return jsonify({'error': 'Email already exists'}), 409

    user = User(email=email, first_name=data['first_name'], last_name=data['last_name'])
    data_manager.save(user)
    return jsonify({'message': 'User created successfully', 'user': user.to_dict()}), 201


# Endpoint to retrieve all users
@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    users = data_manager.get_all_users()
    return jsonify({'users': [user.to_dict() for user in users]}), 200


# Endpoint to retrieve a specific user
@user_blueprint.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200


# Endpoint to update a user
@user_blueprint.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = data_manager.get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    if not all(key in data for key in ['email', 'first_name', 'last_name']):
        return jsonify({'error': 'Missing required fields'}), 400

    email = data['email']
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format'}), 400

    # Check if email is already in use by another user
    existing_user = data_manager.get_user_by_email(email)
    if existing_user and existing_user.id != user_id:
        return jsonify({'error': 'Email already exists'}), 409

    user.email = email
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    data_manager.update(user)
    return jsonify({'message': 'User updated successfully', 'user': user.to_dict()}), 200


# Endpoint to delete a user
@user_blueprint.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = data_manager.get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data_manager.delete(user)
    return jsonify({'message': 'User deleted successfully'}), 204


def is_valid_email(email):
    # Basic email validation
    return '@' in email and '.' in email.split('@')[-1]


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(user_blueprint)
    app.run(debug=True)
user_model = user_ns.model('User', {
    'id': fields.Integer(readOnly=True, description='The user unique identifier'),
    'email': fields.String(required=True, description='User email address'),
    'first_name': fields.String(required=True, description='User first name'),
    'last_name': fields.String(required=True, description='User last name')
})

@user_ns.route('/users')
class UserList(Resource):
    @user_ns.doc('list_users')
    @user_ns.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        users = data_manager.get_all_users()
        return users

    @user_ns.doc('create_user')
    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        data = request.json
        email = data.get('email')
        if not email:
            return {'error': 'Email is required'}, 400

        if data_manager.get_user_by_email(email):
            return {'error': 'Email already exists'}, 409

        user = User(**data)
        data_manager.save(user)
        return user, 201

@user_ns.route('/users/<int:user_id>')
@user_ns.param('user_id', 'The user identifier')
class UserResource(Resource):
    @user_ns.doc('get_user')
    @user_ns.marshal_with(user_model)
    def get(self, user_id):
        """Get user by ID"""
        user = data_manager.get(user_id, 'user')
        if not user:
            return {'error': 'User not found'}, 404
        return user

    @user_ns.doc('update_user')
    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model)
    def put(self, user_id):
        """Update a user"""
        user = data_manager.get(user_id, 'user')
        if not user:
            return {'error': 'User not found'}, 404

        data = request.json
        email = data.get('email')
        if email and data_manager.get_user_by_email(email) and data_manager.get_user_by_email(email).id != user_id:
            return {'error': 'Email already exists'}, 409

        user.update(data)  # Ensure your User class has an update method
        data_manager.update(user)
        return user

    @user_ns.doc('delete_user')
    def delete(self, user_id):
        """Delete a user"""
        user = data_manager.get(user_id, 'user')
        if not user:
            return {'error': 'User not found'}, 404
