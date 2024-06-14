import unittest
from Models.city import City

class TestCity(unittest.TestCase):
    def test_city(self):
        city = City(name="Test City", country_id="123")
        self.assertIsInstance(city, City)

if __name__ == "__main__":
    unittest.main()
