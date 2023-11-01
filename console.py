#!/usr/bin/python3
"""The entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Class definition"""
    prompt = "(hbnb)"
    
    def quit(self):
        """exit the program"""
        return True
    
    def EOF(self):
        """exit the program"""
        return True
           
    
    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()