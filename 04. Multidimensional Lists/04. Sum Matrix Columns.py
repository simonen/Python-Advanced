rows, cols = [int(x) for x in input().split(", ")]

matrix = []
for i in range(rows):
    line = [x for x in map(int, input().split())]
    matrix.append(line)

# print(matrix)
inv_matrix = []

for x in range(len(matrix[0])):
    line = []
    for j in range(len(matrix)):
        line.append(matrix[j][x])
    inv_matrix.append(line)
    print(sum(line))
