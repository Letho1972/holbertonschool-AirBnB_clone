<h1 align="center"> AirBnB clone - The console </h1> <br>
<p align="center">
  <img src=""/>
  <p align="center">


* [Table of Contents](#-table-of-contents)
    * [Introduction](#introduction)
    * [Objective](#objective)
    * [Compilation](#compilation/Installation)
    * [Requirements](#requirements)
    * [The Console](#the-console)
    * [Storage](#storage)
    * [Project instructions](#project-instructions)
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
            

## The console



## Storage


## Project instructions


* [Task 0](https://github.com/HolbyKate/holbertonschool-Simple_Shell-Testing/blob/master/Shell/Task%200.png)
* [Task 1](https://github.com/HolbyKate/holbertonschool-Simple_Shell-Testing/blob/master/Shell/Task%201.png)
* [Task 2](https://github.com/HolbyKate/holbertonschool-Simple_Shell-Testing/blob/master/Shell/Task%202.png)
* [Task 3](https://github.com/HolbyKate/holbertonschool-Simple_Shell-Testing/blob/master/Shell/Task%203.png)
* [Task 4](https://github.com/HolbyKate/holbertonschool-Simple_Shell-Testing/blob/master/Shell/Task%204.png)
* [Task 5](https://github.com/HolbyKate/holbertonschool-Simple_Shell-Testing/blob/master/Shell/Task%205.png)
* [Task 6](https://github.com/HolbyKate/holbertonschool-Simple_Shell-Testing/blob/master/Shell/Task%206.png)

   
## Examples and testing

```shell
$ ./hsh
($) /bin/ls
hsh main.c shell.c
($)
($) exit
$
```

```shell
$ echo "/bin/ls" | ./hsh
hsh main.c shell.c test_ls_2
$
$ cat test_ls_2
/bin/ls
/bin/ls
$
$ cat test_ls_2 | ./hsh
hsh main.c shell.c test_ls_2
hsh main.c shell.c test_ls_2
$
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
