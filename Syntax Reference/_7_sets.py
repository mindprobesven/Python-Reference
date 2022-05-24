# ---------------------------------------------------------------------------------------------------------------
# Sets
# A collection which is unordered and unindexed. No duplicate members.
# ----------------------------------------------------------------------------------------------------------------

# Creating
# ----------------------------------------------------------------------------------------------------------------
x = {"apple", "banana", "cherry"}       # Declaration
x = set(("apple", "banana", "cherry"))  # Constructor
x = frozenset(("apple", "banana", "cherry"))  # Frozenset is immutable
print(x)

# set eliminates duplicates
x = {1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6}
print(x)    # Output: {1, 2, 3, 4, 5, 6}

# Accessing
# ----------------------------------------------------------------------------------------------------------------
# Cannot access items by index
for i in x:
    print(i)

# Changing
# ----------------------------------------------------------------------------------------------------------------
# add one item
x = {"apple", "banana", "cherry"}
x.add("orange")
print(x)

# add multiple items
x = {"apple", "banana", "cherry"}
x.update(["orange", "mango", "grapes"])
print(x)

# remove item (If the items doe not exist, remove() will raise an error)
x = {"apple", "banana", "cherry"}
x.remove("banana")
print(x)

# discard item (If the items doe not exist, discard() will NOT raise an error)
x = {"apple", "banana", "cherry"}
x.discard("tomato")
print(x)

# remove the last item in the set. Sets are unordered so it is unknow what item gets removed.
x = {"apple", "banana", "cherry"}
x.pop()
print(x)

# empty a set
x = {"apple", "banana", "cherry"}
x.clear()
print(x)

# delete set completely
x = {"apple", "banana", "cherry"}
del x
# print(x) = error: x is not defined

# Checking
# ----------------------------------------------------------------------------------------------------------------
x = {"apple", "banana", "cherry"}
print("banana" in x)

# Union and intersection
# ----------------------------------------------------------------------------------------------------------------
# sets have operations such as union and intersection.
set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 3, 5, 6}
set1 |= set2
print(set1)

# union() returns a new set with all items from both sets
set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 3, 5, 6}
set3 = set1.union(set2)
print(set3)

# ----------------------------------------------------------------------------------------------------------------
# Sets have many methods, some are
# difference()
# intersection()
# issubset()
# symmetric_difference()
# etc.
