# PRIMITIVE DATA TYPES
# str - string
# bool - boolean
# int - integer
# float

# COMPLEX DATA TYPES
# list
# dict

# CASTING
# str + int = runtime exception

# SCOPE
# white space in Python defines scope
#     block of code associated with a control structure

# CONTROL STRUCTURES
# --for loops--
# for {variable_name} in <collection>:
#     <action>

# --logical--
# if <bool>:
#   pass
# elif <bool>:
#   pass
# else <bool>:
#   pass

# --assignment--
# =

# --comparisons--
# == -> equals
# != -> not equals
# > -> greater than
# >= -> greater than equal
# < -> less than
# <= -> les than equal


"""
  PRACTICE: print each letter in a given string
"""
grande = 'Batmon'
print(grande)
count = 0
for sausage in grande:
    count += 1
    # count = count + 1
    if count == 5:
        print(sausage)

"""
  PRACTICE: create a function that takes an input,
  then prints each character of the input
"""


def print_characters(grandez):
    for sausage in grandez:
        print(sausage)


print_characters(grande)

"""
    PRACTICE: create a function that takes two inputs,
    then prints True/False whether or not the first input
    is contained within the second input
"""

# print(search_string('a', text_value))  # False
# print(search_string('so', text_value))  # True
# print(search_string('S', text_value))  # False

counts = [1, 2, 3, 4, 5, 6]
print(7 in counts)
