import uuid
from datetime import datetime

class BaseModel:
    """
    A base model class representing a generic model.
    """

    def __init__(self, created_at=None, updated_at=None, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            created_at (datetime): The creation date and time of the model.
            updated_at (datetime): The last update date and time of the model.
        """
        self.id = str(uuid.uuid4())
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
        
        # Set additional attributes from kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        """
        Updates the updated_at attribute with the current date and time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance to a dictionary format.
        
        Returns:
            dict: A dictionary representation of the instance.
        """
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string representation of the BaseModel instance.
        """
        return f'Your ID is {self.id}'
