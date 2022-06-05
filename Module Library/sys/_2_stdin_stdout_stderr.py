#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Module - sys
#
# The sys modules provide variables for better control over input or output. We can even redirect the input and 
# output to other devices. This can be done using three variables
# stdin
# stdout
# stderr
# ----------------------------------------------------------------------------------------------------------------

import sys

sys.stdout.write('Hello')
sys.stderr.write('Error')

# stdin: It can be used to get input from the command line directly. It is used for standard input. It internally 
# calls the input() method. It, also, automatically adds ‘\n’ after each sentence.
for line in sys.stdin: 
    if 'q' == line.rstrip(): 
        break
    print(f'Input : {line}')
  
print("Exit")