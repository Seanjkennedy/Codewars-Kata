#Multiplication table
"""Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]"""
#print([[j for i in range(1,i+1)]i for i in range(1,size+1)])

def multiplication_table(size):
    table = []
    for x in range(1, size + 1):
        table.append([x * i for i in range(1, size + 1)])
    return table
