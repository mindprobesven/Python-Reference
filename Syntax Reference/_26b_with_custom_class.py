#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# with - Creating Custom Context Managers - Class based
#
# Context managers and the with statement aren’t limited to resource management. They allow you to provide and 
# reuse common setup and teardown code. In other words, with context managers, you can perform any pair of 
# operations that needs to be done before and after another operation or procedure, such as:
#
# Open and close
# Lock and release
# Change and reset
# Create and delete
# Enter and exit
# Start and stop
# Setup and teardown
# ----------------------------------------------------------------------------------------------------------------

from time import sleep, perf_counter

class HelloContextManager:
    # When the with statement executes, it calls .__enter__() on the context manager object to signal that you’re 
    # entering into a new runtime context. If you provide a target variable with the as specifier, then the return 
    # value of .__enter__() is assigned to that variable.
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"

    # When the flow of execution leaves the context, .__exit__() is called. If no exception occurs in the with code 
    # block, then the three last arguments to .__exit__() are set to None. Otherwise, they hold the type, value, 
    # and traceback associated with the exception at hand.
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        print(exc_type, exc_value, exc_tb, sep="\n")

class Timer:
    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0
        # Returns a lambda function that computes a time delta. In this case, .start holds the initial state or time 
        # measurement. .end is still set to 0.0 until __exit__ executes and updates the .end value.
        return lambda: self.end - self.start

    def __exit__(self, *args):
        # Once the with block ends, .__exit__() gets called. The method gets the time at the end of the block and 
        # updates the value of .end so that the lambda function can compute the time required to run the with code 
        # block.
        self.end = perf_counter()

class WritableFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file_object = open(self.file_path, mode="w")
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()

if __name__ == "__main__":
    # Example 1
    with HelloContextManager() as hello:
        # Note that hello holds the return value of .__enter__()
        print(hello)

    # Example 2
    with Timer() as timer:
         # Time-consuming code goes here...
        sleep(0.5)

    # timer holds an instance of the lambda function that computes the time delta, so you need to call timer() to 
    # get the final result.
    print(timer())

    # Example 3
    with WritableFile("hello.txt") as file:
        file.write("Hello World!")