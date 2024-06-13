import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(email="test@example.com", password="123456", first_name="Rick", last_name="Melendez")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "Rick")
        self.assertEqual(user.last_name, "Melendez")
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    def test_user_save(self):
        user = User(email="test@example.com", password="123456", first_name="Rick", last_name="Melendez")
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
