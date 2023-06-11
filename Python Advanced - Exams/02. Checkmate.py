size = 8
matrix = [[j for j in input().split()] for i in range(size)]

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

queens = [[i, j] for i in range(size) for j in range(size) if matrix[i][j] == 'Q']
killer_queens = []

for queen in queens:
    for direction in movement:
        q_x, q_y = queen
        for _ in range(size):
            p_x, p_y = movement[direction](q_x, q_y)
            if p_x in range(size) and p_y in range(size):
                hit = matrix[p_x][p_y]
                if hit == 'Q':
                    break
                elif hit == 'K':
                    killer_queens.append(queen)
                    break
                q_x, q_y = p_x, p_y
            else:
                break

if killer_queens:
    print(*killer_queens, sep='\n')
else:
    print("The king is safe!")