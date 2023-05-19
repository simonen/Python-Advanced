rows, cols = [int(x) for x in input().split(", ")]

matrix = []
for i in range(rows):
    line = [x for x in map(int, input().split())]
    matrix.append(line)

# print(matrix)
inv_matrix = []

for j in range(len(matrix[0])):
    line = []
    for i in range(len(matrix)):
        line.append(matrix[i][j])
    inv_matrix.append(line)
    print(sum(line))

# chek = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
# print(chek)