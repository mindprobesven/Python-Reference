#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# JSON
# ----------------------------------------------------------------------------------------------------------------

import json

# some JSON
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
# The result is a Python dictionary
print(y["age"])

# convert From python to JSON
# a python dict
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)
print(y) # the result is a JSON

# example
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))
