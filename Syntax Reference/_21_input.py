#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# User input
# ----------------------------------------------------------------------------------------------------------------

number = input('How old are you?: ')

age = int(number)

if age >= 18:
    print('You are an adult!')
else:
    print('You are underage. Go away kiddo!')
