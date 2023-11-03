#!/usr/bin/python3
"""The entry point of the command interpreter"""


import cmd
import json
import uuid
from datetime import datetime
from models.base_model import BaseModel


MODEL_NAMES = {"BaseModel": BaseModel}
"""Model class"""


class HBNBCommand(cmd.Cmd):
    """Class definition"""
    prompt = "(hbnb) "
    store = {}

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True

    def do_create(self, arg):
        if len(arg) == 0:
            print("**class name missing**")
            return

        class_name = arg[0]
        class_ = MODEL_NAMES.get(class_name)

        if class_ is None:
            print("**class doesn\'t exist**")
            return

        instance = class_()
        instance.id = str(uuid.uuid4())
        instance.created_at = datetime.now()
        instance.updated_at = datetime.now()

        if class_name not in self.store:
            self.store[class_name] = {}

        self.store[class_name][instance.id] = instance.__dict__

        self.save_file("models.json", self.store)   

        print(instance.id)

    def do_show(self, arg):
        if len(arg) == 0:
            print("**class name missing**")
            return

        args = arg.split()
        class_name = args[0]
        class_ = MODEL_NAMES.get(class_name)

        if class_ is None:
            print("**class doesn\'t exist**")
            return

        if len(args) < 2:
            print("**instance id missing**")
            return

        instance_id = args[1]
        instance = self.store.get(class_name, {}).get(instance_id)

        if instance is None:
            print("**no instance found**")
            return

        print(json.dumps(instance, indent=2))

    def do_destroy(self, arg):
        if len(arg) == 0:
            print("**class name missing**")
            return

        args = arg.split()
        class_name = args[0]
        class_ = MODEL_NAMES.get(class_name)

        if class_ is None:
            print("**class doesn\'t exist**")
            return

        if len(arg) < 2:
            print("**instance id missing**")
            return

        instance_id = args[1]
        instance = self.store.get(class_name, {}).pop(instance_id, None)

        if instance is None:
            print("**no instance found**")
            return

        self.save_file("models.json", self.store)

    def do_all(self, arg):
        if len(arg) == 0:
            print("**class name missing**")
            return

        class_name = arg.split()[0]
        class_ = MODEL_NAMES.get(class_name)

        if class_ is None:
            print("**class doesn\'t exist**")
            return

        instances = self.store.get(class_name, {})

        if not instances:
            print("**no instances found**")
            return

        print(json.dumps(instances, indent=2))

    def do_update(self, arg):
        if len(arg) == 0:
            print("**class name missing**")
            return
        class_name = arg.split()[0]
        class_ = MODEL_NAMES.get(class_name)

        if class_ is None:
            print("**class doesn\'t exist**")
            return

        if len(arg) < 3:
            print("**instance id and attributes missing**")
            return

        instance_id = arg[1]
        attributes = arg[2:]

        instance = self.store.get(class_name, {}).get(instance_id)

        if instance is None:
            print("**no instance found**")
            return

        for attribute in attributes:
            key, value = attribute.split("=")
            instance[key] = value

    def emptyline(self):
        """Don't execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
