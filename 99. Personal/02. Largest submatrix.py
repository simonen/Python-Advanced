def matrix_subdivide(matrix, subsize):
    new_matrix = []
    for i in range(size - subsize + 1):
        for j in range(size - subsize + 1):
            sub_matrix = []
            for k in range(subsize):
                sub_matrix.append(matrix[i + k][j:j + subsize])

            new_matrix.append(sub_matrix)

    return new_matrix


def biggest_submatrix(submatrices):
    biggest_sum = 0
    largest_matrix = []

    for sub_matrix in submatrices:
        matrix_sum = 0
        for row in sub_matrix:
            matrix_sum += sum(row)

        # print(matrix_sum, *z, sep='\n')
        if matrix_sum > biggest_sum:
            biggest_sum = matrix_sum
            largest_matrix = sub_matrix

    return largest_matrix


size = 6
sub_size = 5

matrix = [
    [1, 2, 15, 1, 3, 4],
    [5, 3, 0, 1, 2, 9],
    [2, 3, 1, 8, 6, 2],
    [0, 1, 4, 5, 8, 1],
    [7, 3, 1, 2, 6, 1],
    [0, 0, 1, 7, 2, 3],
]

print(*matrix, sep='\n')
print()


print(*biggest_submatrix(matrix_subdivide(matrix, sub_size)), sep='\n')