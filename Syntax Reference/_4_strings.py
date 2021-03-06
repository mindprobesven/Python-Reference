# ---------------------------------------------------------------------------------------------------------------
# Strings
# ----------------------------------------------------------------------------------------------------------------

# Multiline strings
x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(x)

# string slicing
# From position 2 to 5 (not included)
x = "Hello, World!"
print(x[2:5])   # Output: llo

# negative indexing
# From position -5 to -2 (not included)
x = "Hello, World!"
print(x[-5:-2])   # Output: orl

# get length of string
x = "Hello, World!"
print(len(x))

# strip whitespaces
x = " Hello, World! "
print(x.strip())

# replace
x = "Hello, World!"
print(x.replace("H", "J"))

# split
x = "Hello, World!"
print(x.split(","))

# check
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x) # True

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) # False

# concatenation
a = "Hello"
b = "World"
c = a + b
print(c) # HelloWorld

# String formatting
# ----------------------------------------------------------------------------------------------------------------
quantity = 3
item_number = 567
price = 49.95

# Placeholders
order = "I want {} pieces of item {} for {} dollars"
print(order.format(quantity, item_number, price))

# Via index numbers
indexed_order = "I want to pay {2} dollars for {0} pieces of item {1}."
print(indexed_order.format(quantity, item_number, price))

# Via named indexes
my_order = "I have a {carname}, it is model {model}"
print(my_order.format(carname="Ford", model="Mustang"))

# Adding parameters to display a number with two decimals
price = 49
txt = "The price is {:.2F} dollars"
print(txt.format(price))

# escape character
# ----------------------------------------------------------------------------------------------------------------
x = "We are the so-called \"Vikings\" from the north."

""" 
\'  	Single Quote	
\\	    Backslash	
\n	    New Line	
\r	    Carriage Return	
\t	    Tab	
\b	    Backspace	
\f	    Form Feed	
\ooo	Octal value	
\x00    Hex value
"""

#??String methods
"""
capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	       Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans() 	Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()     	Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate() 	Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
"""
