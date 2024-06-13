from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.country import Country
from models.city import City

class DataManager:
    def __init__(self):
        self.users = {}
        self.places = {}
        self.reviews = {}
        self.amenities = {}
        self.countries = {}
        self.cities = {}

    def save(self, entity):
        if isinstance(entity, User):
            self.users[entity.id] = entity
        elif isinstance(entity, Place):
            self.places[entity.id] = entity
        elif isinstance(entity, Review):
            self.reviews[entity.id] = entity
        elif isinstance(entity, Amenity):
            self.amenities[entity.id] = entity
        elif isinstance(entity, Country):
            self.countries[entity.code] = entity
        elif isinstance(entity, City):
            self.cities[entity.id] = entity

    def get(self, entity_id, entity_type):
        if entity_type == 'user':
            return self.users.get(entity_id)
        elif entity_type == 'place':
            return self.places.get(entity_id)
        elif entity_type == 'review':
            return self.reviews.get(entity_id)
        elif entity_type == 'amenity':
            return self.amenities.get(entity_id)
        elif entity_type == 'city':
            return self.cities.get(entity_id)

    def update(self, entity):
        self.save(entity)

    def delete(self, entity_id, entity_type):
        if entity_type == 'user':
            self.users.pop(entity_id, None)
        elif entity_type == 'place':
            self.places.pop(entity_id, None)
        elif entity_type == 'review':
            self.reviews.pop(entity_id, None)
        elif entity_type == 'amenity':
            self.amenities.pop(entity_id, None)
        elif entity_type == 'city':
            self.cities.pop(entity_id, None)

    def get_user_by_email(self, email):
        for user in self.users.values():
            if user.email == email:
                return user
        return None

    def get_all_users(self):
        return list(self.users.values())

    def get_all_places(self):
        return list(self.places.values())

    def get_all_reviews(self):
        return list(self.reviews.values())

    def get_all_amenities(self):
        return list(self.amenities.values())

    def get_all_countries(self):
        return list(self.countries.values())

    def get_all_cities(self):
        return list(self.cities.values())

    def get_reviews_by_user(self, user_id):
        return [review for review in self.reviews.values() if review.user_id == user_id]

    def get_reviews_by_place(self, place_id):
        return [review for review in self.reviews.values() if review.place_id == place_id]

    def get_country_by_code(self, code):
        return self.countries.get(code)
