#!/usr/bin/env python3

# ----------------------------------------------------------------------------------------------------------------
# Singleton - The metaclass way
#
# In this example we create a singleton class using a metaclass. The metaclass allows us to intercept the creation
# of a class, modify the class and return the modified class.
#
# To create a singleton class, we will intercept the class creation and check if an instance of that class has
# already been created. If not, we create a new instance and return it. If yes, we return the existing class
# instance instead.
# ----------------------------------------------------------------------------------------------------------------

# What are Metaclasses?
#
# As soon as you use the keyword class, Python executes it and creates a class object automatically. Python also
# has a way to do it manually using the type function. It can create classes on the fly. type can take the 
# description of a class as parameters, and return a class.
#
# type(name, bases, attrs)
#
# name: name of the class
# bases: tuple of the parent class (for inheritance, can be empty)
# attrs: dictionary containing attributes names and values
#
# Example
# class MyClass():
#   pass
#
# Can be created like this
# MyClass = type('MyClass', (), {})     # returns a class object
#
# Metaclasses are the 'stuff' that creates classes. Function type is in fact a metaclass. type is the class (metaclass)
# Python uses to create all classes behind the scenes. Everything, and I mean everything, is an object in Python. That 
# includes integers, strings, functions and classes. All of them are objects. And all of them have been created from a 
# class.
#
# You see that by checking the __class__ attribute.
#
# age = 35
# age.__class__
# <type 'int'>
#
# class Bar(object): pass
# b = Bar()
# b.__class__
# <class '__main__.Bar'>
#
# The main purpose of a metaclass is to change the class automatically, when it's created.
#
# To create your own metaclass, first add the metaclass keyword argument in the list of base classes.
# class Foo(BaseClass(optional), metaclass=something):
#   pass
#
# Then we create a custom metaclass. This process is explained in the code below were we actually create the metaclass
# to create a singleton class.

# The metaclass
# `type` is actually a class like `str` and `int` so you can inherit from it
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        # Check if the class instance has been created already
        if cls not in cls._instances:
            # If not, create a new class instance and store it
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        # Return the new or existing class instance
        return cls._instances[cls]

class Person(metaclass=Singleton):
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    sven = Person(name='Sven')
    print(sven.name)        # Sven
    print(sven)             # <__main__.Person object at 0xffff92973640>

    # barbara is the same class instance as sven
    barbara = Person(name='Barbara')
    print(barbara.name)     # Sven
    print(barbara)          # <__main__.Person object at 0xffff92973640>