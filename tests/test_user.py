import unittest
from models.user.py import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "John", "Doe", "john.doe@example.com", "password123")

    def test_full_name(self):
        self.assertEqual(self.user.get_full_name(), "John Doe")

    def test_authenticate(self):
        self.assertTrue(self.user.authenticate("password123"))
        self.assertFalse(self.user.authenticate("wrongpassword"))

    def test_email_uniqueness(self):
        user2 = User(2, "Jane", "Doe", "john.doe@example.com", "password123")
        self.assertNotEqual(hash(self.user), hash(user2))

if __name__ == "__main__":
    unittest.main()
