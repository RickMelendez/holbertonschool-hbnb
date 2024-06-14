import unittest
from Models.country import Country

class TestCountry(unittest.TestCase):
    def test_country_creation(self):
        country = Country(name="Puerto Rico")
        self.assertEqual(country.name, "Puerto Rico")
        self.assertIsNotNone(country.created_at)
        self.assertIsNotNone(country.updated_at)

    def test_country_save(self):
        country = Country(name="Puerto Rico")
        old_updated_at = country.updated_at
        country.save()
        self.assertNotEqual(country.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
