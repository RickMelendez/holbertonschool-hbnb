from datetime import datetime

class Country:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_country_name(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
