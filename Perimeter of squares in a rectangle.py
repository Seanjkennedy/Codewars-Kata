#Perimeter of squares in a rectangle

"""The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:

alternative text

Hint:
See Fibonacci sequence

Ref:
http://oeis.org/A000045

The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.

perimeter(5)  should return 80
perimeter(7)  should return 216"""

#print("0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55")

def perimeter(n):

    fib = [0,1,1]
    count = 2
    for i in list(range(0,n-1)):
        temp = fib[count] + fib[count-1]
        fib.append(temp)
        count +=1

    return sum(fib) * 4

print(perimeter(5))
print(perimeter(100))
