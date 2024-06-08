import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review(1, 1, 1, "Great place!", 5.0)

    def test_get_summary(self):
        self.assertEqual(self.review.get_summary(), "Review by User 1 for Place 1: Great place!")

    def test_get_rating(self):
        self.assertEqual(self.review.get_rating(), 5.0)

if __name__ == "__main__":
    unittest.main()
