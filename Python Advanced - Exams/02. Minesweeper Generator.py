size = int(input())
bomb_pos = [tuple(map(int, input().strip("()").split(", "))) for _ in range(int(input()))]
matrix = [['-' for j in range(size)] for i in range(size)]

movement = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1),
    'up_left': lambda x, y: (x - 1, y - 1),
    'up_right': lambda x, y: (x - 1, y + 1),
    'down_left': lambda x, y: (x + 1, y - 1),
    'down_right': lambda x, y: (x + 1, y + 1)
}

for i in range(size):
    for j in range(size):
        near_bombs = 0
        if (i, j) in bomb_pos:
            matrix[i][j] = '*'
        else:
            for direction in movement:
                p_x, p_y = movement[direction](i, j)
                if p_x in range(size) and p_y in range(size) and (p_x, p_y) in bomb_pos:
                    near_bombs += 1

            matrix[i][j] = str(near_bombs)

for i in matrix:
    print(*i, sep=' ')
