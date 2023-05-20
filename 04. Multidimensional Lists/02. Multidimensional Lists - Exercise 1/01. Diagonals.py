matrix = [[j for j in input().split(", ")] for i in range(int(input()))]

primary = []
secondary = []

for i in range(len(matrix)):
    primary.append(matrix[i][i])
    secondary.append(matrix[i][-i - 1])


print(f"Primary diagonal: {', '.join(primary)}. Sum: {sum(map(int, primary))}")
print(f"Secondary diagonal: {', '.join(secondary)}. Sum: {sum(map(int, secondary))}")
