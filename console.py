#!/usr/bin/python3
"""The entry point of the command interpreter"""


import cmd
import json

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Class definition"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True

    def emptyline(self):
        """Don't execute anything"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it"""
        if not arg:
            print("** class name missing **")
            return
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")
            except Exception as e:
                print(f"Error creating instance: {e}")

    def do_show(self, arg):
        """Prints string representationof an instance based on classname"""
        if not arg:
            print("** class name missing **")
            return

        argsp = arg.split()

        if argsp[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(argsp) < 2:
            print("** instance id missing **")
            return

        instance = f"{argsp[0]}.{argsp[1]}"
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        if instance in objects:
            print(objects[instance])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on classname and id"""
        if not arg:
            print("** class name missing **")
            return
        argsp = arg.split()
        if argsp[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(argsp) < 2:
            print("** instance id missing **")
            return
        
        instance = f"{argsp[0]}.{argsp[1]}"
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        if instance in objects:
            del objects[instance]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name"""

        storage = FileStorage()
        storage.reload()
        objects = storage.all()

        if not arg:
            print([str(obj) for obj in objects.values()])
        elif arg in globals():
            print([str(obj) for obj in objects.values()
                   if isinstance(obj, globals()[arg])])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on classname and id"""
        if not arg:
            print("** class name missing **")
            return
        argsp = arg.split()
        if argsp[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(argsp) < 2:
            print("** instance id missing **")
            return
        
        instance = f"{argsp[0]}.{argsp[1]}"
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        if instance in objects:
            if len(argsp) < 3:
                print("** attribute name missing **")
                return
            if len(argsp) < 4:
                print("** value missing **")
                return
            setattr(objects[instance], argsp[2], argsp[3])
            storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
