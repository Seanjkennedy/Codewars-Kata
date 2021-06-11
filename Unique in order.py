def unique_in_order(iterable):
    new_string = []

    for count, i in enumerate(iterable):
        if count == 0:
            new_string.append(i)
            continue
        if i == iterable[count - 1]:
            continue
        else:
            new_string.append(i)
    return new_string

print(unique_in_order('AAAABBBCCDAABBB'))
