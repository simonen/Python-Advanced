rows, cols = [int(x) for x in input().split(", ")]
matrix = [[j for j in map(int, input().split(", "))] for i in range(rows)]

# submatrix = []
max_submatrix = []
max_sum = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        subm = []
        top_pair = matrix[i][j:j + 2]
        subm.append(top_pair)
        bottom_pair = matrix[i + 1][j:j + 2]
        subm.append(bottom_pair)
        # submatrix.append(subm)
        if sum(top_pair) + sum(bottom_pair) > max_sum:
            max_sum = sum(top_pair) + sum(bottom_pair)
            max_submatrix = subm

for i in max_submatrix:
    print(*i)
print(max_sum)
