import unittest
from model.user import User
from model.place import Place
from model.review import Review
from model.amenity import Amenity
from model.country import Country
from model.city import City
from persistence.data_manager import DataManager

class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.data_manager = DataManager()

    def test_save_and_get_user(self):
        user = User(id=None, first_name="John", last_name="Doe", email="john.doe@example.com", password="password")
        self.data_manager.save(user)
        retrieved_user = self.data_manager.get(user.id, 'User')
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, "john.doe@example.com")

    def test_update_user(self):
        user = User(id=None, first_name="Jane", last_name="Doe", email="jane.doe@example.com", password="password")
        self.data_manager.save(user)
        user.first_name = "Janet"
        self.data_manager.update(user)
        updated_user = self.data_manager.get(user.id, 'User')
        self.assertEqual(updated_user.first_name, "Janet")

    def test_delete_user(self):
        user = User(id=None, first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="password")
        self.data_manager.save(user)
        self.data_manager.delete(user.id, 'User')
        deleted_user = self.data_manager.get(user.id, 'User')
        self.assertIsNone(deleted_user)

    # Additional tests for Place, Review, Amenity, Country, City can be added similarly

if __name__ == '__main__':
    unittest.main()
