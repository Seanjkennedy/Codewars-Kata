#Mumbling 7 KYU
"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

def accum(s):
    accum_string = ""
    s = s.lower()
    for count, i in enumerate(s,1):
        if count != len(s):
            temp = (i * count + "-")
            accum_string += temp.capitalize()
        else:
            temp = (i * count)
            accum_string += temp.capitalize()
    return accum_string
