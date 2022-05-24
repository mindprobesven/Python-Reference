#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# RegEx
# A great guide is at https://w3schools.com/python/python_regex.asp
# ----------------------------------------------------------------------------------------------------------------

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
print(x.span())
