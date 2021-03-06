# ---------------------------------------------------------------------------------------------------------------
# Lambda
# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have "one" expression
# ----------------------------------------------------------------------------------------------------------------
x = lambda a: a + 10
print(x(5)) # 15

# multiple arguments
x = lambda a, b: a * b
print(x(5, 10)) # 50

# Example
# ----------------------------------------------------------------------------------------------------------------
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)   # myfunc returns - lambda a: a * 2
mytripler = myfunc(3)   # myfunc returns - lambda a: a * 3

print(mydoubler(11)) # 22
print(mytripler(11)) # 33
