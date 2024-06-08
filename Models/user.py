from datetime import datetime

class User:
    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def authenticate(self, password):
        return self.password == password

# Adding uniqueness constraint for email
    def __eq__(self, other):
        return self.email == other.email

    def __hash__(self):
        return hash(self.email)
