from flask_restx import Namespace, Resource, fields
from flask import request

from Models.user import User
from Persistence.data_manager import DataManager

user_ns = Namespace('user', description='User operations')
data_manager = DataManager()  # Initialize DataManager

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
        user = data_manager.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return user

    @user_ns.doc('update_user')
    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model)
    def put(self, user_id):
        """Update a user"""
        user = data_manager.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        data = request.json
        email = data.get('email')
        if email and data_manager.get_user_by_email(email) and data_manager.get_user_by_email(email).id != user_id:
            return {'error': 'Email already exists'}, 409

        user.update(data)
        data_manager.update(user)
        return user

    @user_ns.doc('delete_user')
    def delete(self, user_id):
        """Delete a user"""
        user = data_manager.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        data_manager.delete(user)
        return '', 204