import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city_creation(self):
        city = City(name="San Juan", country_id="1")
        self.assertEqual(city.name, "San Juan")
        self.assertEqual(city.country_id, "1")
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_city_save(self):
        city = City(name="San Juan", country_id="1")
        old_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
