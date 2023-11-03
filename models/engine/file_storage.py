#!/usr/bin/python3
"""Module file_storage"""

import json
from models.base_model import BaseModel
import os


class FileStorage():
    """class that serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = type(obj).__name__
        my_id = obj.id
        instance_key = class_name + "." + my_id
        FileStorage.__objects[instance_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        my_obj_dict = {}
        for key in FileStorage.__objects:
            my_obj_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as file_path:
            json.dump(my_obj_dict, file_path)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""
        from models.base_model import BaseModel
        my_dict = {
            "BaseModel": BaseModel
            }
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file_path:
            objects = json.load(file_path)
            FileStorage.__objects = {}
            for key in objects:
                name = key.split(".")[0]
                FileStorage.__objects[key] = my_dict[name](**objects[key])
