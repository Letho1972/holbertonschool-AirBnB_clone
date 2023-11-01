#!/usr/bin/python3
"""
This is the base model that contains serial/deserial information
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """ Defines all common attributes/methods for other classes """
    def init(self, *args, **kwargs):
        """ Initializes the instances attributes """
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            k_dict = kwargs.copy()
            del k_dict["class"]
            for key in k_dict:
                if (key == "created_at" or key == "updated_at"):
                    k_dict[key] = datetime.strptime(k_dict[key], date_format)
            self.dict = k_dict
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def str(self):
        """ Prints object in friendly format"""
        return "[{}] ({}) {}".format(self.__class.name,
                                     self.id, self.dict)

    def save(self):
        """ Updates update_at """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """ Generate a new dict with an extra field class """
        new_dict = self.dict.copy()
        new_dict["class"] = self.__class.name
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
