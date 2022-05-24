# ---------------------------------------------------------------------------------------------------------------
# Dictionaries
# A collection which is unordered, changeable and indexed. No duplicate members.
# ----------------------------------------------------------------------------------------------------------------

# Creating
# ----------------------------------------------------------------------------------------------------------------
# Declaration
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict = dict(brand="Ford", model="Mustang", year=1964)       # Constructor
print(thisdict)

# Access
# ----------------------------------------------------------------------------------------------------------------
x = thisdict["model"]
x = thisdict.get("model")

# print all keys names
for x in thisdict:
    print(thisdict)

# print all values
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

# print both keys and values
for key, value in thisdict.items():
    print(key, value)

# Change
# ----------------------------------------------------------------------------------------------------------------
thisdict["year"] = 2019
print(thisdict)

# Add item
thisdict["owner"] = "Sven Kohn"
print(thisdict)

# length
print(len(thisdict))

# removing items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.pop("model")
print(thisdict)

del thisdict["year"]
print(thisdict)

# clearing
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.clear()
print(thisdict)

# Check
# ----------------------------------------------------------------------------------------------------------------
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Copy
# ----------------------------------------------------------------------------------------------------------------
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

mydict = thisdict.copy()

# or

mydict = dict(thisdict)
print(mydict)
