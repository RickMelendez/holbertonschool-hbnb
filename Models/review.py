from datetime import datetime

class Review:
    def __init__(self, id, user_id, place_id, text, rating):
        self.id = id
        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.rating = rating
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_summary(self):
        return f"Review by User {self.user_id} for Place {self.place_id}: {self.text}"

    def get_rating(self):
        return self.rating

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'text': self.text,
            'rating': self.rating,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
