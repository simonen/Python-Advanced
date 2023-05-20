rows, cols = [int(x) for x in input().split()]
matrix = [[j for j in input().split()] for i in range(rows)]

matched_cols = []

for i in range(rows - 1):
    for j in range(cols - 1):
        top_pair = matrix[i][j:j + 2]
        bottom_pair = matrix[i + 1][j:j + 2]
        if len(set(top_pair).union(set(bottom_pair))) == 1 :
            matched_cols.append([top_pair, bottom_pair])

print(len(matched_cols))