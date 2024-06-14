from .base_model import BaseModel

class Place(BaseModel):
    def __init__(self, city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, *args, **kwargs):
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        super().__init__(*args, **kwargs)
