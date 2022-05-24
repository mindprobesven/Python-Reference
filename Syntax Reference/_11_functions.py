# ---------------------------------------------------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------------------------------------------------

# default parameter
def my_function(country="Norway"):
    print(country)

# arbitrary number of arguments (*args)
def y(*kids):
    print(kids[2])

y("a", "b", "c", "d", "e")

# keyword arguments (kwargs)
# The order or arguments does not matter
def x(b, a, c):
    print(a, b, c)

x(a="a", b="b", c="c")

# Creates a dictionary for userInfo (**kwargs)
def buildUserProfile(first, last, **userInfo):
    userInfo['first'] = first
    userInfo['last'] = last
    return userInfo

user = buildUserProfile('Sven', 'Kohn', occupation='Engineer', age=39)

for key, value in user.items():
    print(f"{key}: {value}")

# Recursion
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

tri_recursion(4)
