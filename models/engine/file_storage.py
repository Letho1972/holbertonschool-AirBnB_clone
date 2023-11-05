#!/usr/bin/python3
"""Module file_storage"""

import json
import os


class FileStorage():
    """class that serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""

        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r") as file_path:
            objects = json.load(file_path)
            FileStorage.__objects = {}
            for key in objects:
                name = key.split(".")[0]
                if name in my_dict:
                    FileStorage.__objects[key] = my_dict[name](**objects[key])
