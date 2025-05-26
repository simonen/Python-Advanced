def matrix_subdivide(matrix, subsize):
    new_matrix = []
    for i in range(size - subsize + 1):
        for j in range(size - subsize + 1):
            sub_matrix = []
            for k in range(subsize):
                sub_matrix.append(matrix[i + k][j:j + subsize])

            new_matrix.append(sub_matrix)

    return new_matrix


size = 6
sub_size = 5
matrix = [
    ['1', 'R', 'T', 'Y', '1', '1'],
    ['1', 'W', '0', '2', '1', '1'],
    ['1', '3', '1', '4', '1', '1'],
    ['1', 'X', '6', 'Q', '1', '1'],
    ['1', 'A', 'B', 'C', '1', '1'],
    ['1', '1', '1', '1', '1', '1'],
]

print(*matrix, sep='\n')
print()

for z in matrix_subdivide(matrix, sub_size):
    print(*z, sep='\n')
    print()