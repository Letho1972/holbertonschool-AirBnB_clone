#!/usr/bin/python3
"""The entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Class definition"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        print("")
        return True

    def do_emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
