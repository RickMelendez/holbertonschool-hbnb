import unittest
from Models.review import Review

class TestReview(unittest.TestCase):
    def test_review(self):
        review = Review(comment="Test Review")
        self.assertIsInstance(review, Review)

if __name__ == "__main__":
    unittest.main()
