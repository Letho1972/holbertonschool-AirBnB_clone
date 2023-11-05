<h1 align="center"> AirBnB clone - The console </h1> <br>


* [Table of Contents](#-table-of-contents)
    * [Introduction](#introduction)
    * [Objective](#objective)
    * [Compilation](#compilation/Installation)
    * [Requirements](#requirements)
    * [The Console](#the-console)
    * [Storage](#storage)
    * [Examples and testing](#examples-and-testing)
    * [Peers](#peers)
    * [Sources](#sources)
    * [Authors](#authors)



## Introduction

This is the first step on the AirBnB clone project. We are creating the console that is a command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)


## Objective

The objective of this project is to create a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

        
## Compilation/Installation
All our files is interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
How to use the console:
- Run the script like this: `./console.py`
- It will show this prompt: `(hbnb)`
- Some commands that you can run are `help` and `quit`.


## Requirements

Python Scripts
- Allowed editors: vi, vim, emacs
- All our files has a end with a new line
- The first line of all our files is exactly #!/usr/bin/python3
- Our code use the pycodestyle (version 2.7.*)
- The length of our files will be tested using wc
- All our modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All our classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All our functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')


Python Unit Tests
- Allowed editors: vi, vim, emacs
- All our files should end with a new line
- All our test files should be inside a folder tests
- You have to use the unittest module
- All our test files should be python files (extension: .py)
- All our test files and folders should start by test_
- Our file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- We also tested file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All our modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All our classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All our functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
            

## The Console

The console is a command line interpreter that permits management of the backend of HolbertonBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the storage object defined above).

| **Commands** | **Syntax**                                                           |
| ------------ | -------------------------------------------------------------------- |
| create       | create < classname >                                                 |
| show         | show < classname > < id >                                            |
| destroy      | destroy < classname > < id >                                         |
| all          | all < classname >                                                    |
| update       | update < classname > < id > < attribute name > "< attribute value >" |

Using the console:

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit
```


## Storage

The above classes are handled by the abstracted storage engine defined in the [FileStorage](https://github.com/HolbyKate/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py) class.

Every time the backend is initialized, HolbertonBnB instantiates an instance of `FileStorage` called `storage`. The `storage` object is loaded/re-loaded from any class instances stored in the JSON file `file.json`. As class instances are created, updated, or deleted, the `storage` object is used to register corresponding changes in the `file.json`.



   
## Examples and testing

Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:


Testing BaseModel_attribute
```
class TestBaseModel_Attribut(unittest.TestCase):

    def test_no_args(self):
        # test if no arg instantiated
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_twoModel_uniqID(self):
        # test if 2 creation not the same ID
        basemodel1 = BaseModel()
        basemodel2 = BaseModel()
        self.assertNotEqual(basemodel1.id, basemodel2.id)

    def test_publicID(self):
        # test that ID is attribut string
        basemodel3 = BaseModel()
        self.assertEqual(type(basemodel3.id), str)
        # test ID can be modify
        basemodel3.id = "123123123"
        self.assertEqual("123123123", basemodel3.id)

    def test_publicCreated_at(self):
        # test that created_at is type datetime
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)
        # test created_at can be modify
        bm.created_at = '2022-02-22T10:02:02.02'
        self.assertEqual("2022-02-22T10:02:02.02", bm.created_at)

    def test_publicUpdate_at(self):
        # test that update_at is public and type datetime
        basemodel3 = BaseModel()
        self.assertIsInstance(basemodel3.updated_at, datetime)
        # test updated_at can be modify
        basemodel3.updated_at = '2022-02-22T10:02:02.02'
        self.assertEqual("2022-02-22T10:02:02.02", basemodel3.updated_at)
```



## Peers

Thank you to all the helper peers for your kindness and professionalism 🙏 


## Sources
 
 https://intranet.hbtn.io/concepts/900  
 https://en.wikipedia.org/wiki/Unix_shell
        
## Authors
#### Cathy Augustin
- Github: https://github.com/HolbyKate

#### Eric Maresq
- Github: https://github.com/Letho1972
