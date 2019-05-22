### Data Structures ###

"""
    In built complex data structures:
    - list      : List or array of different variables
    - set       : Group of unique different variables
    - tuple     : Group of different variables
    - dict      : Group of different variables stored with key, value

    Methods:
    - list()    : create/convert to list type
    - set()     : create/convert to set type
    - dict()    : create/convert to dictionary type

"""

### List ###

# Examples
# Create list using `list()` function or []
l1 = list([1,2,3])
l2 = [1,2,3]
print(l1)
print(l2)
print(type(l1))
print(len(l1))

# You can create list of different variables
l3 = [1, "abc", "2", 22, [1, 1]]
print(l3)

# Each value has index in list, you can access value by index
print(l3[0])
print(l3[3])
print(l3[-1])

# Modify value in list using index
l3[0] = "11111"
print(l3)

# List operations
# Concatenate two list
print(l1 + l2)

# Append variable to list
print([1, 2, 3].append(4))

### Set ###
a = [1, 2, 3, 4]
s1 = set(a)
print(s1)
print(type(s1))
print(len(s1))

# Only unique values
a = [1, 1, 2, 2, 'a', 'a', 'aa']
s2 = set(a)
print(s2)

# NOTE: Set can not be modified once it is created unlike list

### Tuple ###
t1 = (1, 2, 3)
t2 = (1, 1, 'a', [1, 2,])
print(t2)
print(type(t2))
print(t2[0])

# NOTE: Tuple can not be modified once it is created like set unlike list

### Dictionaries ###

d1 = {
    "key1": "value1",
    "key2": "value2"
}
d1 = dict(
    key1="value1",
    key2="value2"
)
print(d1)
print(type(d1))

person = dict(
    name="Sara",
    age=35,
    favourite_movies=["Avengers", "Thor", "Captain America"],
    education=dict(
        undergraduate="Saint Mary School",
        graduate="San Jose State University",
    )
)

# You can access dictionary value by key
print(person['name'])
print(person['age'])
print(person['favourite_movies'])
print(person['education'])

print(person['favourite_movies'][0])

print(person['education']['undergraduate'])
print(person['education']['graduate'])

# Add new key: value to dictionary
person['current_job'] = "Python Developer"
person['current_company'] = "Google"

print(person)

# Add new favourite movie to dictionary
person['favourite_movies'].append("Iron Man")
print(person['favourite_movies'])

# Add new education to dictionary
person['education']['phd'] = 'New York University'
print(person['education'])
