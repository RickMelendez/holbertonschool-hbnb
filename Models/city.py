from datetime import datetime

class City:
    def __init__(self, id, name, country_id):
        self.id = id
        self.name = name
        self.country_id = country_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_city_name(self):
        return self.name
