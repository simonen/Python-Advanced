matrix = [[int(j) for j in map(int, input().split())] for i in range(int(input()))]

# print(matrix)

primary_diag = [matrix[i][i] for i in range(len(matrix))]

print(sum(primary_diag))