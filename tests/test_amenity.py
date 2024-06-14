import unittest
import os
import sys

# Ensure the `models` package can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity(name="WiFi")

    def test_amenity_creation(self):
        self.assertEqual(self.amenity.name, "WiFi")
        self.assertIsNotNone(self.amenity.id)
        self.assertIsNotNone(self.amenity.created_at)
        self.assertIsNotNone(self.amenity.updated_at)

    def test_amenity_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "WiFi")
        self.assertEqual(amenity_dict['id'], self.amenity.id)

if __name__ == '__main__':
    unittest.main()
