# Smallest Permutation
"""Given a number, find the permutation with the smallest absolute value (no leading zeros).

-20 => -20
-32 => -23
0 => 0
10 => 10
29394 => 23499"""

def min_permutation(number):

    sorted_string_n = sorted(str(number))
    int_sorted_n = int("".join(sorted_string_n))
    sorted_string_n_no_zeros = str(int_sorted_n)
    number_of_zeros = str(number).count("0")

    if number_of_zeros:
        if str(int_sorted_n)[0] == "-":
            return int(f'{sorted_string_n_no_zeros[:2]}{number_of_zeros*"0"}{sorted_string_n_no_zeros[2:]}')
        else:
            return int(f'{sorted_string_n_no_zeros[:1]}{number_of_zeros*"0"}{sorted_string_n_no_zeros[1:]}')
    else:
        return int_sorted_n


print(min_permutation(-20))
print(min_permutation(29394))
print(min_permutation(-29394))
print(min_permutation(-32))
print(min_permutation(6092934))
