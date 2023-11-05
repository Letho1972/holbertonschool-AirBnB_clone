#!/usr/bin/python3
"""unittest for file_storage module"""


import os
import json
import unittest
import models
from os import path
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorageBasic(unittest.TestCase):
    """Test instantiation of the FileStorage class"""

    def test_file_storage_instance(self):
        # Test class FileStorage
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_file_storage_with_argument(self):
        # Test FileStorage with an argument
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_instance(self):
        # Test if storage is an instance of FileStorage
        self.assertIsInstance(models.storage, FileStorage)

    def test_file_path_string(self):
        # Test if file_path is a string (file.json)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_file_path_type(self):
        # Test if file_path is of type str
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_dict(self):
        # Test if __objects is a dictionary
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class TestFileStorageMethodAll(unittest.TestCase):
    """Test method all of the FileStorage class"""

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_all_output_type(self):
        # Test the output of all() is a dictionary
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_argument(self):
        # Test if trying to use all() with arguments raises TypeError
        with self.assertRaises(TypeError):
            models.storage.all(89)

    def test_all_with_objects(self):
        # Test if the dictionary is stored in __objects
        file_storage = FileStorage()
        base_model = BaseModel()
        objects = file_storage.all()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, objects)
        self.assertEqual(objects[key], base_model)

    def test_add_objects(self):
        # Test if adding objects in __objects with the key 'classname.id'
        file_storage = FileStorage()
        base_model = BaseModel()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertEqual(file_storage._FileStorage__objects[key], base_model)


class TestFileStorageMethodNew(unittest.TestCase):
    """Test method new of the FileStorage class"""

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_new(self):
        # Create 1 instance of Class and its subclasses
        base1 = BaseModel()
        usr1 = User()
        state1 = State()
        place1 = Place()
        city1 = City()
        amenity1 = Amenity()
        review1 = Review()

        # Add instances to storage
        models.storage.new(base1)
        models.storage.new(usr1)
        models.storage.new(state1)
        models.storage.new(place1)
        models.storage.new(city1)
        models.storage.new(amenity1)
        models.storage.new(review1)

        # Test for each key in storage and value
        self.assertIn("BaseModel." + base1.id, models.storage.all().keys())
        self.assertIn(base1, models.storage.all().values())
        self.assertIn("User." + usr1.id, models.storage.all().keys())
        self.assertIn(usr1, models.storage.all().values())
        self.assertIn("State." + state1.id, models.storage.all().keys())
        self.assertIn(state1, models.storage.all().values())
        self.assertIn("Place." + place1.id, models.storage.all().keys())
        self.assertIn(place1, models.storage.all().values())
        self.assertIn("City." + city1.id, models.storage.all().keys())
        self.assertIn(city1, models.storage.all().values())
        self.assertIn("Amenity." + amenity1.id, models.storage.all().keys())
        self.assertIn(amenity1, models.storage.all().values())
        self.assertIn("Review." + review1.id, models.storage.all().keys())
        self.assertIn(review1, models.storage.all().values())

    def test_new_with_args(self):
        # If using new with args should raise TypeError
        with self.assertRaises(TypeError):
            models.storage.new(User(), 45)

    def test_new_with_none(self):
        # If using new with None should raise AttributeError
        with self.assertRaises(AttributeError):
            models.storage.new(None)


class TestFileStorageMethodSave(unittest.TestCase):
    """Test method save of the FileStorage class"""

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save_with_arg(self):
        # Test if save with args should raise TypeError
        with self.assertRaises(TypeError):
            models.storage.save(456)


class TestFileStorageMethodReload(unittest.TestCase):
    """Test method reload of the FileStorage class"""

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_reload_with_arg(self):
        # Test reload with args should raise TypeError
        with self.assertRaises(TypeError):
            models.storage.reload("user123")

    def test_reload(self):
        # Test reload method
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
