#!/usr/bin/python3
"""The entry point of the command interpreter"""


import cmd

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

        instance = "{}.{}".format(argsp[0], argsp[1])

        if instance not in FileStorage.all():
            print("** no instance found **")
            return

        print(FileStorage.all()[instance])

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

        instance = "{}.{}".format(argsp[0], argsp[1])

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name"""

        if not arg:
            print("** class name missing **")
            return

        with open("data.json", "r") as file:
            data = json.load(file)

        if arg not in data:
            print("** class doesn't exist **")
            return

        instances = []
        for instance_id, instance_data in data[arg].items():
            instances.append(str(instance_data))

        print(instances)

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

        if len(argsp) < 2:
            print("** instance id missing **")
            return

        instance = f"{argsp[0]}.{argsp[1]}"

        if instance not in storage.all():
            print("** no instance found **")
            return

        if len(argsp) < 3:
            print("** attribute name missing **")
            return

        if len(argsp) < 4:
            print("** value missing **")
            return

        setattr(storage.all()[instance], argsp[2], argsp[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
