import unittest
from flask import Flask
from API.user_api import user_blueprint

class TestUser(unittest.TestCase):
    def test_user(self):
        app = Flask(__name__)
        app.register_blueprint(user_blueprint)
        self.assertIn('user_blueprint', app.blueprints)

if __name__ == "__main__":
    unittest.main()
