#Sort and Star
"""You will be given a vector of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array."""

def two_sort(array):
    array.sort()
    new_string = ""
    for letter in array[0]:
        new_string += letter + "***"
    return new_string[:-3]

def two_sort(array):
    x = min(array)
    new_string = ""
    for letter in x:
        new_string += letter + "***"
    return new_string[:-3]

def two_sort(array):
    return "***".join([i for i in min(array)])[-3]
