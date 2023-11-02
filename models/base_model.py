#!/usr/bin/python3
"""
This is the base model that contains serial/deserial information
"""
from datetime import datetime
import uuid


class BaseModel():
    """ Defines all common attributes/methods for other classes """
    def __init__(self):
        """ Initializes the instances attributes """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ Updates update_at """
        self.updated_at = datetime.now()
        return (self.updated_at)

    def __str__(self):
        """ Prints object in friendly format"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        """ Generate a new dict with an extra field class essai """
        new_dict = self.__dict__.copy()
        new_dict["class"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
