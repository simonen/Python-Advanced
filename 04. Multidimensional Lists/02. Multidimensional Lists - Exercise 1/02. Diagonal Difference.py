matrix = [[j for j in map(int, input().split())] for i in range(int(input()))]

primary = [matrix[i][i] for i in range(len(matrix))]
secondary = [matrix[i][-i - 1] for i in range(len(matrix))]
difference = abs(sum(primary) - sum(secondary))

print(difference)