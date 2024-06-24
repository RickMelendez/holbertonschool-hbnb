from flask import request
from flask_restx import Namespace, Resource, fields
from datetime import datetime
import re
from Models.user import User
from Persistence.data_manager import DataManager

# Initialize Namespace and DataManager
user_ns = Namespace('users', description='User operations')
data_manager = DataManager()

# Define user model for serialization
user_model = user_ns.model('User', {
    'id': fields.Integer(readOnly=True, description='The user unique identifier'),
    'email': fields.String(required=True, description='User email address'),
    'first_name': fields.String(required=True, description='User first name'),
    'last_name': fields.String(required=True, description='User last name'),
    'created_at': fields.DateTime(readOnly=True, description='The user creation timestamp'),
    'updated_at': fields.DateTime(readOnly=True, description='The user update timestamp')
})

# Function to validate email format
def validate_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

# Function to validate user data
def validate_user_data(data):
    if 'email' not in data or not validate_email(data['email']):
        return False, 'Invalid or missing email'
    if 'first_name' not in data or not isinstance(data['first_name'], str) or not data['first_name'].strip():
        return False, 'Invalid or missing first name'
    if 'last_name' not in data or not isinstance(data['last_name'], str) or not data['last_name'].strip():
        return False, 'Invalid or missing last name'
    return True, None

# Define routes and resource classes

@user_ns.route('/')
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
        valid, message = validate_user_data(data)
        if not valid:
            return {'error': message}, 400

        if data_manager.get_user_by_email(data['email']):
            return {'error': 'Email already exists'}, 409

        data['created_at'] = datetime.utcnow()
        data['updated_at'] = datetime.utcnow()
        user = User(**data)
        data_manager.save(user)
        return user, 201

@user_ns.route('/<int:user_id>')
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
        valid, message = validate_user_data(data)
        if not valid:
            return {'error': message}, 400

        email = data.get('email')
        existing_user = data_manager.get_user_by_email(email)
        if email and existing_user and existing_user.id != user_id:
            return {'error': 'Email already exists'}, 409

        data['updated_at'] = datetime.utcnow()
        user.update(data)
        data_manager.update(user)
        return user

    @user_ns.doc('delete_user')
    def delete(self, user_id):
        """Delete a user"""
        user = data_manager.get(user_id, 'user')
        if not user:
            return {'error': 'User not found'}, 404

        data_manager.delete(user)
        return '', 204
