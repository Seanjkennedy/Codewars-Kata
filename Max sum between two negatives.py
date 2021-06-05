#Max sum between two negatives

"""You have a list of integers. The task is to return the maximum sum of the elements located between
two negative elements, or -1, Nothing, or a similar empty value, if there is no such sum.
No negative element should be present in this sum.

Example:

[4, -1, 6, -2, 3, 5, -7, 7] -> 8
     ^      ^         ^
Not 14, because -2 is between -1 and -7, and not 6 but 8, because 8 is bigger."""


def max_sum_between_two_negatives(arr):
    max_sum_list = []
    max_sums = 0
    count = 0
    for i in arr:
        if i < 0:
            max_sum_list.append(max_sums)
            max_sums = 0
            count += 1
        elif i >= 0 and count != 0:
            max_sums += i
    return -1 if count < 2 else sorted(max_sum_list)[-1]


print(max_sum_between_two_negatives([-1, 6, -2, 3, 5, -7]))
