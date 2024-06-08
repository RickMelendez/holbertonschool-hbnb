import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City(1, "New York", 1)

    def test_get_city_name(self):
        self.assertEqual(self.city.get_city_name(), "New York")

if __name__ == "__main__":
    unittest.main()
