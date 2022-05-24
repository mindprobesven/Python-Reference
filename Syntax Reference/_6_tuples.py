# ---------------------------------------------------------------------------------------------------------------
# Tuples
# A collection which is ordered and unchangeable. Allows duplicate members.
# ----------------------------------------------------------------------------------------------------------------

# Creating
x = (200, 50)           # Declaration
y = tuple((150, 30))    # Constructor
z = (100,)              # One item tuple needs a comma at the end

# Iterating
for i in x:
    print(i)

# This will fail because tubles are immutable
# tubleList[0] = 100

# Tuples can be joined
a = x + y
print(a)

# Deleting a tuple
del a
