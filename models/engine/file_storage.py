#!/usr/bin/python3
"""Module file_storage"""

import json
from models.base_model import BaseModel


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
        self.__objects
        
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        
    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""
        