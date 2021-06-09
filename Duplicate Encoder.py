#Duplicate Encoder

"""The goal of this exercise is to convert a string to a new string where each character in the new string is "("
if that character appears only once in the original string, or ")" if that character appears more than once in the
original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
Notes

Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX",
the "XXX" is the expected result, not the input!"""


def duplicate_encode(word):
    return "".join(")" if word.lower().count(i) > 1 else "(" for i in word.lower())


def duplicate_encode(word):
    lower_case = word.lower()
    new_string = ""
    for count, letter in enumerate(lower_case):
        if lower_case.count(letter) > 1:
            new_string += ")"
        else:
            new_string += "("
    return new_string
