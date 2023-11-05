#!/usr/bin/python3
"""Module file_storage"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():
    """class that serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                  "City": City, "Amenity": Amenity, "Place": Place,
                  "Review": Review,
                  }

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""

        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r") as file_path:
            objects = json.load(file_path)
            FileStorage.__objects = {}
            for key, value in objects.items():
                name, obj_id = key.split(".")
                my_dict = {"BaseModel": BaseModel, "FilsStorage": FileStorage}
                if name in my_dict:
                    obj = my_dict[name].from_dict(value)
                    FileStorage.__objects[key] = obj
