import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country(1, "USA")

    def test_get_country_name(self):
        self.assertEqual(self.country.get_country_name(), "USA")

if __name__ == "__main__":
    unittest.main()
