#!/usr/bin/env python3

# ----------------------------------------------------------------------------------------------------------------
# Classes - Basics
# - Class constructor, class properties, instance properties, class methods
# ----------------------------------------------------------------------------------------------------------------

class Dog:
    # Class properties. Shared in all instances of the class. Similar to a global.
    class_id = 0

    # Class constructor
    def __init__(self, name, age):  # Class parameters
        # Incrementing a class property (class_id) when a class instance is created
        Dog.class_id += 1

        # Setting instance properties values
        self.name = name
        self.age = age

    # Class object methods
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

# Class properties can be accessed and modified without having to instantiate the class
# ------------------------------------------------------------------------------------------------------
print(Dog.class_id)                     # OUTPUT: 0
print("-----" * 10)

# Instantiating a class with parameters
# ------------------------------------------------------------------------------------------------------
LEIKA = Dog('Leika', 3)
print(f"Class ID: {LEIKA.class_id}")    # OUTPUT: Class ID: 1

SANDY = Dog('Sandy', 8)
print(f"Class ID: {SANDY.class_id}")    # OUTPUT: Class ID: 2

print("-----" * 10)

# Modifying class object properties
# ------------------------------------------------------------------------------------------------------
# Add
LEIKA.owner = "Sven"
print(LEIKA.owner)

# Change
LEIKA.name = "Mega Leika"
print(LEIKA.name)

# Delete property
del SANDY.age

#Delete class object
del SANDY

# Using get and set methods
# ------------------------------------------------------------------------------------------------------
print(LEIKA.get_name())                 # OUTPUT: Leika
LEIKA.set_name("Super Leika")
print(LEIKA.get_name())                 # OUTPUT: Super Leika

print("-----" * 10)

# List class object property keys and values
# ------------------------------------------------------------------------------------------------------
print(LEIKA.__dict__)

# The dir() function can list all the function names (or variable names)
# ----------------------------------------------------------------------------------------------------------------
print(dir(LEIKA))
