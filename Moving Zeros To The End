#Moving Zeros To The End

"""Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]"""

def move_zeros(array):
    count = 0
    for i in array:
        if i == 0:
            count +=1
        else:
            continue
    array2 = [i for i in array if i != 0]
    for i in range(count):
        array2.append(0)
    return array2
