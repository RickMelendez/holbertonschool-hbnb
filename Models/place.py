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
