import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_place_creation(self):
        place = Place(name="Nice Place", description="A very nice place", address="123 Main St", city_id="1", latitude=37.7749, longitude=-122.4194, host_id="2", number_of_rooms=3, number_of_bathrooms=2, price_per_night=150, max_guests=4)
        self.assertEqual(place.name, "Nice Place")
        self.assertEqual(place.description, "A very nice place")
        self.assertEqual(place.address, "787 Main St")
        self.assertEqual(place.city_id, "1")
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.host_id, "2")
        self.assertEqual(place.number_of_rooms, 3)
        self.assertEqual(place.number_of_bathrooms, 2)
        self.assertEqual(place.price_per_night, 150)
        self.assertEqual(place.max_guests, 4)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)

    def test_place_save(self):
        place = Place(name="Nice Place", description="A very nice place", address="787 Main St", city_id="1", latitude=37.7749, longitude=-122.4194, host_id="2", number_of_rooms=3, number_of_bathrooms=2, price_per_night=150, max_guests=4)
        old_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(place.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
