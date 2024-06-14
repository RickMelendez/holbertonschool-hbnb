import unittest
from Models.place import Place

class TestPlace(unittest.TestCase):
    def test_place(self):
        place = Place(city_id="city1", user_id="user1", name="name", description="desc", number_rooms=1, number_bathrooms=1, max_guest=1, price_by_night=100, latitude=12.34, longitude=56.78, address="123 Main St")
        self.assertEqual(place.address, "123 Main St")

if __name__ == '__main__':
    unittest.main()
