from datetime import datetime
from persistence.ipersistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {
            'User': {},
            'Place': {},
            'Review': {},
            'Amenity': {},
            'Country': {},
            'City': {}
        }

    def save(self, entity):
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            raise ValueError(f"Unsupported entity type: {entity_type}")

        entity.id = len(self.storage[entity_type])
        entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        self.storage[entity_type][entity.id] = entity

    def get(self, entity_id, entity_type):
        if entity_type not in self.storage:
            raise ValueError(f"Unsupported entity type: {entity_type}")

        return self.storage[entity_type].get(entity_id, None)

    def update(self, entity):
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            raise ValueError(f"Unsupported entity type: {entity_type}")

        if entity.id in self.storage[entity_type]:
            entity.updated_at = datetime.now()
            self.storage[entity_type][entity.id] = entity

    def delete(self, entity_id, entity_type):
        if entity_type not in self.storage:
            raise ValueError(f"Unsupported entity type: {entity_type}")

        if entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
