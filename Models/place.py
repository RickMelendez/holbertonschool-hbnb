from datetime import datetime

class Place:
    def __init__(self, id, name, description, price, location, city_id, owner_id):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.location = location
        self.city_id = city_id
        self.owner_id = owner_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_details(self):
        return f"{self.name}: {self.description} at {self.location}"

    def calculate_price(self, nights):
        return self.price * nights

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'location': self.location,
            'city_id': self.city_id,
            'owner_id': self.owner_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

