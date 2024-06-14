from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, place_id="", user_id="", text="", comment="", *args, **kwargs):
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
        self.comment = comment
        super().__init__(*args, **kwargs)
