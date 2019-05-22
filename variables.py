### VARIABLES ###

"""
    In Python, you don't need to worry about defining the variable type.
    And you can also modify the variable value at any time.
    - int       : numeric values
    - str       : list of characters or strings
    - bool      : boolean values - False or True

    - list
    - set
    - dict

    In built functions to create/modify variables
    - int()     : create/convert to integer type
    - str()     : create/convert to sting type
    - bool()    : create/convert to bool type
    - type()    : returns type of variable

    - list()
    - set()
    - dict()
"""

# String variables
attendee_name = ""
speaker_name = "Yashashvi Dave"
talk_name = "Introduction to Python Programming"
organizer_name = "Lenka"

# Store numeric values, string values, boolean values to variables
no_of_attendees = 20
is_anita_attending = False

# This is called string concatenation. It allows to concatenate or join multiple
# strings, variables in one statement
print("Welcome " + attendee_name + " to " + "GHC Virtual Talk - "
      + talk_name)
print("Speaker: " + speaker_name)
print("Organizer: " + organizer_name)

# Convert variables to string using `str` function
print("Total no of attendees are: " + str(no_of_attendees))
print("Is Anita attending the event: " + str(is_anita_attending))

# `type` function returns the type of variable
print(type(no_of_attendees))
print(type(str(no_of_attendees)))
print(type(is_anita_attending))

# Convert to integer variables using `int`
print(int('-12'))
print(int('12'))
print(type(int('12')))
# ERROR
# print(int('12a'))

# Convert to boolean variables using `bool`
print("Any non-zero value returns True and zero returns False")
print(bool(12))
print(bool(-12))
print(bool(0))

print("Any non empty string returns True and empty string returns False")
print(bool('Any non empty string'))
print(bool(''))
