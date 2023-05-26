size = int(input())
matrix = [[j if j == 'B' or j == 'X' else int(j) for j in input().split()] for i in range(size)]

bunny_x, bunny_y = next([i, j] for i in range(size) for j in range(size) if matrix[i][j] == "B")
book = {'up': [], 'down': [], 'left': [], 'right': []}
positions = {'up': [], 'down': [], 'left': [], 'right': []}

ups = bunny_x
downs = size - bunny_x - 1
lefts = bunny_y
rights = size - bunny_y - 1

for u in range(1, ups + 1):
    if matrix[bunny_x - u][bunny_y] == 'X':
        break
    book['up'].append(matrix[bunny_x - u][bunny_y])
    positions['up'].append([bunny_x - u, bunny_y])

for d in range(1, downs + 1):
    if matrix[bunny_x + d][bunny_y] == 'X':
        break
    book['down'].append(matrix[bunny_x + d][bunny_y])
    positions['down'].append([bunny_x + d, bunny_y])

for l in range(1, lefts + 1):
    if matrix[bunny_x][bunny_y - l] == 'X':
        break
    book['left'].append(matrix[bunny_x][bunny_y - l])
    positions['left'].append([bunny_x, bunny_y - l])

for r in range(1, rights + 1):
    if matrix[bunny_x][bunny_y + r] == 'X':
        break
    book['right'].append(matrix[bunny_x][bunny_y + r])
    positions['right'].append([bunny_x, bunny_y + r])

biggest = sorted(book.items(), key=lambda x: (-sum(x[1]), -len(x[1])))
direction = biggest[0][0]
eggs = sum(biggest[0][1])

print(direction, *positions[direction], eggs, sep='\n')
