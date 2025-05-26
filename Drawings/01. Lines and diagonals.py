def crosses(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            if i == j or i == size // 2 or j == size // 2 or i + j == size - 1:
                print('+', end='')
            else:
                print(' ', end='')
        print()


# matrix = [[' '] * size for i in range(size)]

# for i in range(size):
#     for j in range(size):
#         if i == j or i == size // 2 or j == size // 2 or i + j == size - 1:
#             matrix[i][j] = '*'

# print(*matrix, sep='\n')
#
# for k in matrix:
#     print(*k, sep='')
while True:
    n = int(input("How big? "))
    crosses(n)
