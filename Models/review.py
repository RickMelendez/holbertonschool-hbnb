from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, place_id="", user_id="", text="", comment="", **kwargs):
        super().__init__(**kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
        self.comment = comment

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'place_id': self.place_id,
            'user_id': self.user_id,
            'text': self.text,
            'comment': self.comment
        })
        return data
