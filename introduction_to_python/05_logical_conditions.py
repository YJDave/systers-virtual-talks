### LOGICAL CONDITIONS ###

"""
    Following are the special keywords used for logical
    conditioning in Python:
    - if        : Run if given condition is true
    - else      : Run if given condition is not true
    - while     : Run until the given condition is true
    - for       : Run for given no of times
"""
# NOTE: Indentation is very important here.

### IF ###

a = True
if a:
    print("A is True")
else:
    print("A is not True")

a = 0
if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")

# OR
if a != 0:
    if a > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")

### FOR ###
for i in [1, 2, 3,]:
    print("*", end="")

for i in range(0, 20):
    print(str(i) + " | ", end="")

l1 = ["Yashashvi", 234, [1,2], (6, 6), "Dave"]
for i in l1:
    print(i)

l2 = [13,1,3,2134,134,1,0,5,0,57,46,7]
for i in l2:
    if i == 0:
        print("Zero")

### WHILE ###
i = 1
while i < 10:
    print(i)
    i = i + 1

a = 6
while a > 0:
    print(a)
    a = a -1
