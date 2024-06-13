from .base_model import BaseModel

class City(BaseModel):
    def __init__(self, name, country_id, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.country_id = country_id

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name,
            'country_id': self.country_id
        })
        return data
