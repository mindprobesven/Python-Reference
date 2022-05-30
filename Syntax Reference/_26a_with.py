#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# with
#
# The with statement in Python is a quite useful tool for properly managing external resources in your programs. 
# It allows you to take advantage of existing context managers to automatically handle the setup and teardown 
# phases whenever you’re dealing with external resources or with operations that require those phases.
#
# "with" is a method to properly manages external resources, such as files, locks, and network connections.
# Managing resources properly is often a tricky problem. It requires both a setup phase and a teardown phase. 
# The latter phase requires you to perform some cleanup actions, such as closing a file, releasing a lock, or 
# closing a network connection.
# ----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # The try … finally Approach
    # --------------------------------------------------------------------
    # Safely open the file
    file = open("hello.txt", "w")

    try:
        file.write("Hello, World!")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    finally:
        # Make sure to close the file after using it
        file.close()

    # The with Statement Approach
    # --------------------------------------------------------------------
    # The Python with statement creates a runtime context that allows you 
    # to run a group of statements under the control of a context manager.
    # The with statement can make your code clearer, safer, and reusable. 
    # Many classes in the standard library support the with statement.
    #
    # General syntax
    # with expression as target_var:
    #     do_something(target_var)
    #
    # The context manager object results from evaluating the expression after
    # with. In other words, expression must return an object that implements 
    # the context management protocol. This protocol consists of two special methods:
    #
    # .__enter__() is called by the with statement to enter the runtime context.
    # .__exit__() is called when the execution leaves the with code block.
    #
    # The as specifier is optional. If you provide a target_var with as, then 
    # the return value of calling .__enter__() on the context manager object is 
    # bound to that variable.
    with open("hello.txt", mode="w") as file:
        file.write("Hello, World!")
    # When you run this with statement, open() returns an io.TextIOBase object. 
    # This object is also a context manager, so the with statement calls .__enter__() 
    # and assigns its return value to file. Then you can manipulate the file inside 
    # the with code block. When the block ends, .__exit__() automatically gets called 
    # and closes the file for you, even if an exception is raised inside the with block.