from datetime import datetime

class Amenity:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_amenity_details(self):
        return f"Amenity: {self.name} - {self.description}"
