rows, cols = [int(x) for x in input().split(",")]
matrix = [[j for j in list(input())] for i in range(rows)]

mouse_x, mouse_y = next([i, j] for j in range(cols) for i in range(rows) if matrix[i][j] == 'M')
cheese = [matrix[i][j] for i in range(rows) for j in range(cols) if matrix[i][j] == 'C'].count('C')

movement = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1)
}

direction = input()

while direction != "danger":
    p_x, p_y = movement[direction](mouse_x, mouse_y)

    if p_x not in range(rows) or p_y not in range(cols):
        print("No more cheese for tonight!")
        break
    elif matrix[p_x][p_y] == '@':
        direction = input()
        continue
    elif matrix[p_x][p_y] == 'T':
        matrix[p_x][p_y] = 'M'
        matrix[mouse_x][mouse_y] = '*'
        print("Mouse is trapped!")
        break
    elif matrix[p_x][p_y] == 'C':
        cheese -= 1

    matrix[mouse_x][mouse_y] = '*'
    matrix[p_x][p_y] = 'M'
    mouse_x, mouse_y = p_x, p_y

    if cheese == 0:
        print("Happy mouse! All the cheese is eaten, good night!")
        break

    direction = input()
else:
    if cheese:
        print("Mouse will come back later!")

for i in matrix:
    print(*i, sep="")