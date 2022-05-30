#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# with - Creating Custom Context Managers - Function based
#
# If you decorate an appropriately coded generator function with @contextmanager, then you get a function-based 
# context manager that automatically provides both required methods, .__enter__() and .__exit__().
# ----------------------------------------------------------------------------------------------------------------

from contextlib import contextmanager

# writable_file() is a generator function that opens file for writing. Then it temporarily suspends its own execution 
# and yields the resource so with can bind it to its target variable. When the flow of execution leaves the with code 
# block, the function continues to execute and closes file correctly.
@contextmanager
def writable_file(file_path):
    file = open(file_path, mode="w")
    try:
        yield file
    finally:
        file.close()

if __name__ == "__main__":
    with writable_file("hello.txt") as file:
        file.write("Hello, World!")
