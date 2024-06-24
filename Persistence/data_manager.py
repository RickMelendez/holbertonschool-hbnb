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

from Models.user import User

class DataManager:
    def __init__(self):
        self.users = {}
        self.countries = {}
        self.cities = {}
        self.amenities = {}
        self.places = {}
        self.reviews = {}

    def save(self, entity):
        entity_type = entity['type']
        if entity_type == 'user':
            self.save_user(entity)
        elif entity_type == 'country':
            self.save_country(entity)
        elif entity_type == 'city':
            self.save_city(entity)
        elif entity_type == 'amenity':
            self.save_amenity(entity)
        elif entity_type == 'place':
            self.save_place(entity)
        elif entity_type == 'review':
            self.save_review(entity)

    def get(self, entity_id, entity_type):
        if entity_type == 'user':
            return self.get_user(entity_id)
        elif entity_type == 'country':
            return self.get_country(entity_id)
        elif entity_type == 'city':
            return self.get_city(entity_id)
        elif entity_type == 'amenity':
            return self.get_amenity(entity_id)
        elif entity_type == 'place':
            return self.get_place(entity_id)
        elif entity_type == 'review':
            return self.get_review(entity_id)

    def update(self, entity):
        entity_type = entity['type']
        if entity_type == 'user':
            return self.update_user(entity['id'], entity)
        elif entity_type == 'country':
            return self.update_country(entity['country_code'], entity)
        elif entity_type == 'city':
            return self.update_city(entity['city_id'], entity)
        elif entity_type == 'amenity':
            return self.update_amenity(entity['id'], entity)
        elif entity_type == 'place':
            return self.update_place(entity['id'], entity)
        elif entity_type == 'review':
            return self.update_review(entity['id'], entity)

    def delete(self, entity_id, entity_type):
        if entity_type == 'user':
            return self.delete_user(entity_id)
        elif entity_type == 'country':
            return self.delete_country(entity_id)
        elif entity_type == 'city':
            return self.delete_city(entity_id)
        elif entity_type == 'amenity':
            return self.delete_amenity(entity_id)
        elif entity_type == 'place':
            return self.delete_place(entity_id)
        elif entity_type == 'review':
            return self.delete_review(entity_id)

    # User management methods
    def save_user(self, user_data):
        self.users[user_data['id']] = user_data

    def get_all_users(self):
        return list(self.users.values())

    def get_user(self, user_id):
        return self.users.get(user_id)

    def get_user_by_email(self, email):
        for user in self.users.values():
            if user['email'] == email:
                return user
        return None

    def update_user(self, user_id, user_data):
        if user_id in self.users:
            self.users[user_id].update(user_data)
            return True
        return False

    def delete_user(self, user_id):
        return self.users.pop(user_id, None) is not None
