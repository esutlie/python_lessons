"""
Places to store data
There are a few key ways to hold data that we use in python:
Variables, Lists, Arrays, and Dictionaries, among others.
"""

# Variables (variables should be made from letters, single words, or multiple words connected by underscores)
a = 5
banana = 'yummy'
chris_is_the_coolest = True

# Lists (lists are set to variables just like the other data types, but they can contain more than one piece of data)
fruits = ['apple', 'pear', 'strawberry', 'pineapple']
favorite_numbers = [4, 7, 12]
mixed_bag = [2.5, True, 'henlo', 5]  # Lists can contain different types of data

# Arrays (arrays are made from lists of lists, but they can only contain one data type)
# We make arrays using the numpy module. Modules are outside libraries of code that we pull in to use
import numpy as np

integer_array = np.array([[1, 2, 3], [4, 5, 6], [5, 3, 1]])
string_array = np.array([['chris', 'is', 'so'], ['cute', 'and', 'handsome']])
print(integer_array)
print(string_array)


# Dictionaries (like lists, but each item is attached to a label)
new_dictionary = {'label 1': 'chocolate', 'label 2': 12,
                  'label c': True, 'label 105': ['a', 'b', 'c']}
