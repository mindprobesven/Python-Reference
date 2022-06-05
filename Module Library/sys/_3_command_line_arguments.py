#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# sys - Command line arguments
#
# Command-line arguments are those which are passed during the calling of the program along with the calling 
# statement. To achieve this using the sys module, the sys module provides a variable called sys.argv. It’s main 
# purpose are:
#
# It is a list of command-line arguments.
# len(sys.argv) provides the number of command-line arguments.
# sys.argv[0] is the name of the current Python script.
#
# Run this example like this
# python3 _3_command_line_arguments.py 2 5
# ----------------------------------------------------------------------------------------------------------------

import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
  
# Arguments passed
print("\nName of Python script:", sys.argv[0])
  
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
      
# Addition of numbers
Sum = 0
  
for i in range(1, n):
    Sum += int(sys.argv[i])
      
print("\n\nResult:", Sum)