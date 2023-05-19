row, col = [int(x) for x in input().split(", ")]

matrix = []
matrix_sum = 0
for i in range(row):
    line = [j for j in map(int, input().split(", "))]
    matrix.append(line)
    matrix_sum += sum(line)


print(matrix_sum)
print(matrix)