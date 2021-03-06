# ---------------------------------------------------------------------------------------------------------------
# If ... Else
# ----------------------------------------------------------------------------------------------------------------
a = 200
b = 33

if b > a:
    print("b > a")
elif a == b:
    print("a == b")
else:
    print("a > b")

# short hand

# one-line if statement
a = 50
b = 20
if a > b:
    print("a is greater than b")

# one line if else
a = 2
b = 330
print("A") if a > b else print("B")

#┬ámultiple statements in one line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# the pass statement
a = 33
b = 200
if b > a:
    pass
