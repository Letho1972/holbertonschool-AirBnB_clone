#!/usr/bin/python3
"""The entry point of the command interpreter"""


import cmd
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class definition"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True
    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.split()[0]
            if not class_name in Base._subclasses:
                print("** class doesn't exist **")
            else:
                new_instance = Base._subclasses[class_name]()
                new_instance.save()
                print(new_instance.id)
  
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
        else:
            class_name, id = arg.split()
            if not class_name in Base._subclasses:
                print("** class doesn't exist **")
            elif not Base.exists(class_name, id):
                print("** no instance found **")
            else:
                instance = Base.find(class_name, id)
                print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        if not arg:
            print("** class name missing **")
        else:
            class_name, id = arg.split()
            if not class_name in Base._subclasses:
                print("** class doesn't exist **")
            elif not Base.exists(class_name, id):
                print("** no instance found **")
            else:
                Base.delete(class_name, id)
                print("** instance deleted **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        command = self.parseline(arg)[0]
        objs = models.storage.all()
        if command is None:
            print([str(objs[obj]) for obj in objs])
        elif command in self.allowed_classes:
            keys = objs.keys()
            print([str(objs[key]) for key in keys if key.startswith(command)])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name, id = args[0], args[1]
            if not class_name in Base._subclasses:
                print("** class doesn't exist **")
            elif not Base.exists(class_name, id):
                print("** no instance found **")
            else:
                instance = Base.find(class_name, id)
                if len(args) < 3:
                    print("** attribute name missing **")
                elif not hasattr(instance, args[2]):
                    print("** attribute doesn't exist **")
                elif len(args) > 3 and not args[3].startswith('"'):
                    print("** value missing **")
                else:
                    value = args[3].strip('"')
                    setattr(instance, args[2], type(getattr(instance, args[2]))
                            (value))
                    instance.save()
                    print("** instance updated **")

    def emptyline(self):
        """Don't execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
