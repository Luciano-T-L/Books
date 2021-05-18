"Just undestanding how to do tranposed matrix"

"""for i in range(4):
    print(i)
"""

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],]

"""for row in matrix:
    print(row[0])"""

transposed = []

for i in range(4):
    tranposed1 = []
    for row in matrix:
        tranposed1.append(row[i])
    transposed.append(tranposed1)

print(transposed)