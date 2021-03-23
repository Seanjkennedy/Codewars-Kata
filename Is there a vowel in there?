#Is there a vowel in there?

"""Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

If they are, change the array value to a string of that vowel.

Return the resulting array."""

def is_vow(inp):
    vowels = [ord("a"),ord("e"),ord("i"),ord("o"),ord("u")]
    new_list = []
    for i in inp:
        if i in vowels:
            new_list.append(chr(i))
        else:
            new_list.append(i)
    return new_list

def is_vow(inp):
    vowels = [ord("a"),ord("e"),ord("i"),ord("o"),ord("u")]
    return [chr(i) if i in vowels else i for i in inp]
