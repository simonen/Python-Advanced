rows, cols = [int(x) for x in input().split()]
matrix = [[j for j in map(int, input().split())] for i in range(rows)]

square = 3
max_sum = float('-inf')
max_submatrix = []

for i in range(rows - square + 1):
    for j in range(cols - square + 1):
        square_sum = 0
        submatrix = []
        for n in range(square):
            nth_row = matrix[i + n][j:j + square]
            submatrix.append(nth_row)
            square_sum += sum(nth_row)
        if square_sum > max_sum:
            max_sum = square_sum
            max_submatrix = submatrix

print(f"Sum = {max_sum}")
for i in max_submatrix:
    print(' '.join(map(str, i)))
