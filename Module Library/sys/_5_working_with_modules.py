#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# sys - Working with modules
#
# ----------------------------------------------------------------------------------------------------------------

import sys

# sys.path returns the list of directories that the interpreter will search for the required module.
for path in sys.path:
    print(path)

print('-' * 75)

# sys.modules returns the names of the Python modules that the current shell has imported.
for module in sys.modules:
    print(module)

print('-' * 75)

# sys.builtin_module_names returns names of all modules that are compiled into this Python interpreter.
for module in sys.builtin_module_names:
    print(module)