# hbnb_evolution/tests/test_datamanager.py

import unittest
import os
import json
from models.data_manager import DataManager
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.country import Country

class TestDataManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_manager = DataManager("test_data.json")
    
    @classmethod
    def tearDownClass(cls):
        # Clean up the test data file
        if os.path.exists("test_data.json"):
            os.remove("test_data.json")

    def setUp(self):
        self.data_manager.clear_data()  # Clear data before each test
    
    def test_save_and_load_user(self):
        user = User(email="test@example.com", password="123456", first_name="Rick", last_name="Melendez")
        self.data_manager.save(user)
        loaded_user = self.data_manager.load(User, user.id)
        self.assertEqual(user.email, loaded_user.email)
        self.assertEqual(user.first_name, loaded_user.first_name)
        self.assertEqual(user.last_name, loaded_user.last_name)

    def test_save_and_load_place(self):
        place = Place(name="Nice Place", description="A very nice place", address="787 Main St", city_id="1", latitude=37.7749, longitude=-122.4194, host_id="2", number_of_rooms=3, number_of_bathrooms=2, price_per_night=150, max_guests=4)
        self.data_manager.save(place)
        loaded_place = self.data_manager.load(Place, place.id)
        self.assertEqual(place.name, loaded_place.name)
        self.assertEqual(place.description, loaded_place.description)
        self.assertEqual(place.address, loaded_place.address)

    def test_save_and_load_review(self):
        review = Review(user_id="1", place_id="2", text="Great place!", rating=5)
        self.data_manager.save(review)
        loaded_review = self.data_manager.load(Review, review.id)
        self.assertEqual(review.text, loaded_review.text)
        self.assertEqual(review.rating, loaded_review.rating)

    def test_save_and_load_amenity(self):
        amenity = Amenity(name="WiFi")
        self.data_manager.save(amenity)
        loaded_amenity = self.data_manager.load(Amenity, amenity.id)
        self.assertEqual(amenity.name, loaded_amenity.name)

    def test_save_and_load_city(self):
        city = City(name="San Juan", country_id="1")
        self.data_manager.save(city)
        loaded_city = self.data_manager.load(City, city.id)
        self.assertEqual(city.name, loaded_city.name)
        self.assertEqual(city.country_id, loaded_city.country_id)

    def test_save_and_load_country(self):
        country = Country(name="Puerto Rico")
        self.data_manager.save(country)
        loaded_country = self.data_manager.load(Country, country.id)
        self.assertEqual(country.name, loaded_country.name)

    def test_clear_data(self):
        user = User(email="test@example.com", password="123456", first_name="Rick", last_name="Melendez")
        self.data_manager.save(user)
        self.data_manager.clear_data()
        loaded_user = self.data_manager.load(User, user.id)
        self.assertIsNone(loaded_user)

if __name__ == '__main__':
    unittest.main()
