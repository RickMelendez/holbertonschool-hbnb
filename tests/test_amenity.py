import sys
import os
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity_creation(self):
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)

    def test_amenity_save(self):
        amenity = Amenity(name="WiFi")
        old_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
