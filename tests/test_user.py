import unittest
from flask import Flask
from API.user_api import user_blueprint
from Persistence.data_manager import DataManager
from Models.user import User

class TestUserEndpoints(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = Flask(__name__)
        app.register_blueprint(user_blueprint)
        cls.app = app.test_client()
        cls.data_manager = DataManager('test_data.json')

    @classmethod
    def tearDownClass(cls):
        cls.data_manager.clear_data()

    def test_create_user(self):
        response = self.app.post('/api/v1/users', json={
            'email': 'test@example.com',
            'first_name': 'Rick',
            'last_name': 'Melendez'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        user = User(email='test@example.com', first_name='Rick', last_name='Melendez')
        self.data_manager.save(user)
        response = self.app.get(f'/api/v1/users/{user.id}')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        user = User(email='test@example.com', first_name='Rick', last_name='Melendez')
        self.data_manager.save(user)
        response = self.app.put(f'/api/v1/users/{user.id}', json={'first_name': 'Rick'})
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        user = User(email='test@example.com', first_name='Rick', last_name='Melendez')
        self.data_manager.save(user)
        response = self.app.delete(f'/api/v1/users/{user.id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
