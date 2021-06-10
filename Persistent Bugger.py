#Persistent Bugger.

"""Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

persistence(39)  # returns 3, because 3*9=27, 2*7=14, 1*4=4
# and 4 has only one digit

persistence(999)  # returns 4, because 9*9*9=729, 7*2*9=126,
# 1*2*6=12, and finally 1*2=2

persistence(4)  # returns 0, because 4 is already a one-digit number"""


def persistence(n):
    x = str(n)
    count = 0
    while len(x) > 1:
        result = 1
        for i in x:
            result = int(result) * int(i)
            x = str(result)
        count += 1
    return count

def persistence(n):
    x = str(n)
    count = 0
    while len(x) > 1:
        x_string = ""
        for index, digit in enumerate(x):
            if index == 0:
                x_string += digit
            else:
                x_string += "*" + digit
        x = str(eval(x_string))
        count += 1
    return count



print(persistence(123))
print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(99999990199))

