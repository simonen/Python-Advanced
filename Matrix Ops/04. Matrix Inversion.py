matrix = [
         [7, 1, 3, 3, 2, 1],
         [1, 3, 9, 8, 5, 6],
         [4, 6, 7, 9, 1, 0]
                          ]

rows, cols = len(matrix), len(matrix[0])
inverted = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

print(inverted)