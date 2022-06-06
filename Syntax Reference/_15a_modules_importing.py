#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Modules - Importing
#
# - A module's defined global variables are encapsuled
# ----------------------------------------------------------------------------------------------------------------

# Importing a module
import fibo

# Imports names from a module directly into the importing module’s symbol table
from fibo import fib, fib2

# Imports all names that a module defines except those beginning with an underscore (_)
# A general the practice of importing * from a module or package is frowned upon
from fibo import *

# If the module name is followed by as, then the name following as is bound directly to the imported module.
import fibo as fib

# It can also be used when utilising from
from fibo import fib as fibonacci

if __name__ == "__main__":
    # Within a module, the module’s name (as a string) is available as the value of the global variable __name__
    print(fibo.__name__)