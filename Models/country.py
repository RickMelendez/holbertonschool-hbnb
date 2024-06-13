from .base_model import BaseModel

class Country(BaseModel):
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name
        })
        return data
