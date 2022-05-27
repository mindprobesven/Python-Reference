#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Modules
# ----------------------------------------------------------------------------------------------------------------

import platform
from _11a_functions import buildUserProfile as userInfo

user = userInfo('Sven', 'Kohn', occupation='Engineer', age=39)

for key, value in user.items():
    print(f"{key}: {value}")

# The dir() function can list all the function names (or variable names) in a module 
# ----------------------------------------------------------------------------------------------------------------
print(dir(platform))
