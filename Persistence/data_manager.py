#!/usr/bin/python3
import os
from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        pass

class DataManager(IPersistenceManager):
    def __init__(self):
        self.countries = {}
        self.cities = {}
        self.amenities = {}
        self.reviews = {}

    def save(self, entity):
        entity_type = entity['type']
        if entity_type == 'country':
            self.save_country(entity)
        elif entity_type == 'city':
            self.save_city(entity)
        elif entity_type == 'amenity':
            self.save_amenity(entity)
        elif entity_type == 'place':
            self.save_place(entity)

    def get(self, entity_id, entity_type):
        if entity_type == 'country':
            return self.get_country(entity_id)
        elif entity_type == 'city':
            return self.get_city(entity_id)
        elif entity_type == 'amenity':
            return self.get_amenity(entity_id)
        elif entity_type == 'place':
            return self.get_place(entity_id)

    def update(self, entity):
        entity_type = entity['type']
        if entity_type == 'country':
            return self.update_country(entity['id'], entity)
        elif entity_type == 'city':
            return self.update_city(entity['id'], entity)
        elif entity_type == 'amenity':
            return self.update_amenity(entity['id'], entity)
        elif entity_type == 'place':
            return self.update_place(entity['id'], entity)

    def delete(self, entity_id, entity_type):
        if entity_type == 'country':
            return self.delete_country(entity_id)
        elif entity_type == 'city':
            return self.delete_city(entity_id)
        elif entity_type == 'amenity':
            return self.delete_amenity(entity_id)
        elif entity_type == 'place':
            return self.delete_place(entity_id)

    # Methods for managing countries
    def save_country(self, country_data):
        self.countries[country_data['country_code']] = country_data

    def get_all_countries(self):
        return list(self.countries.values())

    def get_country(self, country_code):
        return self.countries.get(country_code)

    def update_country(self, country_code, country_data):
        if country_code in self.countries:
            self.countries[country_code].update(country_data)
            return True
        return False  

    def delete_country(self, country_code):
        return self.countries.pop(country_code, None) is not None

    # Methods for managing cities
    def save_city(self, city_data):
        self.cities[city_data['city_id']] = city_data

    def get_all_cities(self):
        return list(self.cities.values())

    def get_city(self, city_id):
        return self.cities.get(city_id)

    def update_city(self, city_id, city_data):
        if city_id in self.cities:
            self.cities[city_id].update(city_data)
            return True
        return False

    def delete_city(self, city_id):
        return self.cities.pop(city_id, None) is not None
    
    # Amenities CRUD operations
    def save_amenity(self, amenity_data):
        if amenity_data['name'] in (amenity['name'] for amenity in self.amenities.values()):
            raise ValueError("Amenity with this name already exists")
        self.amenities[amenity_data['id']] = amenity_data

    def get_amenity(self, amenity_id):
        return self.amenities.get(amenity_id)

    def update_amenity(self, amenity_id, amenity_data):
        if amenity_id in self.amenities:
            self.amenities[amenity_id].update(amenity_data)
            return True
        return False

    def delete_amenity(self, amenity_id):
        if amenity_id in self.amenities:
            del self.amenities[amenity_id]
            return True
        return False
    
    # Place CRUD operations
    def save_place(self, place_data):
        self.places[place_data['id']] = place_data

    def get_all_places(self):
        return list(self.places.values())

    def get_place(self, place_id):
        return self.places.get(place_id)

    def update_place(self, place_id, place_data):
        if place_id in self.places:
            self.places[place_id].update(place_data)
            self.places[place_id]['updated_at'] = datetime.now().isoformat()
            return True
        return False

    def delete_place(self, place_id):
        if place_id in self.places:
            del self.places[place_id]
            return True
        return False

    # Validation methods for place
    def check_city_exists(self, city_id):
        return city_id in self.cities

    def check_amenity_exists(self, amenity_id):
        return amenity_id in self.amenities

    def validate_place_data(self, place_data):
        if not self.check_city_exists(place_data['city_id']):
            return False, 'Invalid city ID'
        if not all(self.check_amenity_exists(amenity_id) for amenity_id in place_data.get('amenity_ids', [])):
            return False, 'One or more invalid amenity IDs'
        if place_data['latitude'] < -90 or place_data['latitude'] > 90:
            return False, 'Invalid latitude'
        if place_data['longitude'] < -180 or place_data['longitude'] > 180:
            return False, 'Invalid longitude'
        if place_data['number_of_rooms'] < 0 or place_data['number_of_bathrooms'] < 0 or place_data['max_guests'] < 0:
            return False, 'Invalid room, bathroom, or guest count'
        if place_data['price_per_night'] < 0:
            return False, 'Invalid price per night'
        return True, 'Valid data'
    
    # Review CRUD operations
    def save_review(self, review_data):
        self.reviews[review_data['id']] = review_data

    def get_all_reviews(self):
        return list(self.reviews.values())

    def get_review(self, review_id):
        return self.reviews.get(review_id)

    def update_review(self, review_id, review_data):
        if review_id in self.reviews:
            self.reviews[review_id].update(review_data)
            self.reviews[review_id]['updated_at'] = datetime.now().isoformat()
            return True
        return False

    def delete_review(self, review_id):
        if review_id in self.reviews:
            del self.reviews[review_id]
            return True
        return False

    # Validation methods for reviews
    def check_user_exists(self, user_id):
        # Implement logic to check if the user exists
        pass

    def check_place_exists(self, place_id):
        return place_id in self.places

    def validate_review_data(self, review_data):
        if not self.check_user_exists(review_data['user_id']):
            return False, 'Invalid user ID'
        if not self.check_place_exists(review_data['place_id']):
            return False, 'Invalid place ID'
        if review_data['rating'] < 1 or review_data['rating'] > 5:
            return False, 'Rating must be between 1 and 5'
        place = self.get_place(review_data['place_id'])
        if place and place['host_id'] == review_data['user_id']:
            return False, 'Users cannot review their own place'
        return True, 'Valid data'

class FileStorage:
    def save(self, entity):
        with open(f"{entity['id']}_{entity['type']}.txt", 'w') as f:
            f.write(str(entity))

    def get(self, entity_id, entity_type):
        try:
            with open(f"{entity_id}_{entity_type}.txt", 'r') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def update(self, entity):
        with open(f"{entity['id']}_{entity['type']}.txt", 'w') as f:
            f.write(str(entity))

    def delete(self, entity_id, entity_type):
        try:
            os.remove(f"{entity_id}_{entity_type}.txt")
        except FileNotFoundError:
            pass