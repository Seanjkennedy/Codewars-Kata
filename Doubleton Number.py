#Doubleton number

"""We will call a natural number a "doubleton number" if it contains exactly two distinct digits. For example, 23, 35, 100, 12121 are doubleton numbers, and 123 and 9980 are not.

For a given natural number n (from 1 to 1 000 000), you need to find the next doubleton number. If n itself is a doubleton, return the next bigger than n.

Examples:
doubleton(120) == 121
doubleton(1234) == 1311
doubleton(10) == 12"""


def doubleton(num):

    for x in range(num, 1000000):
        num += 1
        answer = ([i for i in str(num)])
        dupe_answer =list(dict.fromkeys(answer))
        if len(dupe_answer) == 2:
            return num
        else:
            continue

print(doubleton(120), 121, 'Wrong result for 120. It should be 121')
print(doubleton(1234), 1311, 'Wrong result for 1234. It should be 1311')
print(doubleton(10), 12, 'Wrong result for 10. It should be 12')
print(doubleton(1), 10, 'Wrong result for 1. It should be 10')
print(doubleton(111), 112, 'Wrong result for 111. It should be 112')

def doubleton2(num):

    for x in range(num, 1000000):
        num += 1
        answer = ([i for i in str(num)])
        if len(set(answer)) == 2:
            return num
        else:
            continue

print(doubleton2(120), 121, 'Wrong result for 120. It should be 121')
print(doubleton2(1234), 1311, 'Wrong result for 1234. It should be 1311')
print(doubleton2(10), 12, 'Wrong result for 10. It should be 12')
print(doubleton2(1), 10, 'Wrong result for 1. It should be 10')
print(doubleton2(111), 112, 'Wrong result for 111. It should be 112')
