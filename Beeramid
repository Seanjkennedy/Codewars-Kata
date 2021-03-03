#Beeramid 5KYU
"""
Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate,
you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build,
 the largest three-dimensional beer can pyramid you can. And then probably drink those beers, because
 let's pretend it's Friday too.

A beer can pyramid will square the number of cans in each level -
1 can in the top level, 4 in the second, 9 in the next, 16, 25...

Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make,
given the parameters of:

1. your referral bonus, and
2. the price of a beer can

For example:
beeramid(1500, 2); // should === 12
beeramid(5000, 3); // should === 16"""
import math
def beeramid(bonus, price):
    beers_can_afford = math.floor(bonus / price)
    count = 1
    beers_bought = 0
    while beers_can_afford >= 0:
        beers_bought = count * count
        if beers_can_afford >= beers_bought:
            beers_can_afford -= beers_bought
            count += 1
        else:
            return count -1
    return count -1

print(beeramid(9, 2),  1)
print(beeramid(21, 1.5),  3)
print(beeramid(-1, 4), 0)
