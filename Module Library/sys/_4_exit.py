#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# sys - Exit
#
# sys.exit([arg]) can be used to exit the program. The optional argument arg can be an integer giving the exit or 
# another type of object. If it is an integer, zero is considered “successful termination”.
#
# Note: A string can also be passed to the sys.exit() method.
# ----------------------------------------------------------------------------------------------------------------

import sys
import time

count = 0

while True:
    print(f'Count = {count}')
    if count >= 3:
        print('Exiting program')
        sys.exit(0)
    count += 1
    time.sleep(1)