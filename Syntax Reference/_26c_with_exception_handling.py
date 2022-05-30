#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# with - Creating Custom Context Managers - Exception handling
#
# In this example, we encapsulate exception handling in a context manager.
# ----------------------------------------------------------------------------------------------------------------

class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        # exc_type is the exception class, IndexError.
        # exc_value is the exception instance.
        # exc_tb is the traceback object.
        print(exc_type, exc_value, exc_tb, sep="\n")

        if isinstance(exc_value, IndexError):
            # Handle IndexError here...
            print(f"An exception occurred in your with block: {exc_type}")
            print(f"Exception message: {exc_value}")

            # Returning a truthy value makes it possible to swallow the exception and continue the normal execution 
            # after the with code block. However, if you want to be more explicit, then you can return False from 
            # outside the if block.
            return True

if __name__ == "__main__":
    with HelloContextManager() as hello:
        print(hello)
        # This will raise an IndexError because the returned string is not that long
        print(hello[100])

    print("Continue normally from here...")