import unittest
from flask import Flask
from API.user_api import user_blueprint

class TestUser(unittest.TestCase):
    def test_user_blueprint(self):
        self.assertIsNotNone(user_blueprint)

if __name__ == '__main__':
    unittest.main()
