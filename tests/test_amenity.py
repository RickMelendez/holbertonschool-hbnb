import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity(1, "WiFi", "High-speed wireless internet")

    def test_get_amenity_details(self):
        self.assertEqual(self.amenity.get_amenity_details(), "Amenity: WiFi - High-speed wireless internet")

if __name__ == "__main__":
    unittest.main()
