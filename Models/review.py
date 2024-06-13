from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, user_id, place_id, text, rating, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.rating = rating

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'user_id': self.user_id,
            'place_id': self.place_id,
            'text': self.text,
            'rating': self.rating
        })
        return data
