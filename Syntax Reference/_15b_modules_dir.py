#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Modules - dir() function
#
# The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings.
# ----------------------------------------------------------------------------------------------------------------

import fibo, sys, builtins

a = [1, 2, 3]
b = 'Sven'

# Without arguments, dir() lists the names you have defined currently. It lists all types of names: variables, modules, 
# functions, etc.
print(dir())

# Find out which names a module defines
print(dir(fibo))

# dir() does not list the names of built-in functions and variables. If you want a list of those, they are defined in 
# the standard module builtins
print(dir(builtins))