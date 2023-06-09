size = 8
board = [[f"{chr(j)}{i}" for j in range(97, 105)] for i in range(size, 0, -1)]
matrix = [[j for j in input().split()] for i in range(size)]

black_x, black_y = next([i, j] for i in range(size) for j in range(size) if matrix[i][j] == 'b')
white_x, white_y = next([i, j] for i in range(size) for j in range(size) if matrix[i][j] == 'w')

movement = {
    'w': lambda x, y: (x - 1, y),
    'b': lambda x, y: (x + 1, y),
}

player = {'w': (white_x, white_y), 'b': (black_x, black_y)}
color = ['w', 'b']
pawn = ['White', 'Black']

while True:
    p_x, p_y = player[color[0]]
    if p_x - 1 in range(size) and p_y - 1 in range(size) and matrix[p_x - 1][p_y - 1] == 'b':
        print(f"Game over! White win, capture on {board[p_x - 1][p_y - 1]}.")
        break
    elif p_x - 1 in range(size) and p_y + 1 in range(size) and matrix[p_x - 1][p_y + 1] == 'b':
        print(f"Game over! White win, capture on {board[p_x - 1][p_y + 1]}.")
        break
    elif p_x + 1 in range(size) and p_y - 1 in range(size) and matrix[p_x + 1][p_y - 1] == 'w':
        print(f"Game over! Black win, capture on {board[p_x + 1][p_y - 1]}.")
        break
    elif p_x + 1 in range(size) and p_y + 1 in range(size) and matrix[p_x + 1][p_y + 1] == 'w':
        print(f"Game over! Black win, capture on {board[p_x + 1][p_y + 1]}.")
        break

    p_x, p_y = movement[color[0]](p_x, p_y)
    if p_x == 0 or p_x == 7:
        print(f"Game over! {pawn[0]} pawn is promoted to a queen at {board[p_x][p_y]}.")
        break

    player[color[0]] = (p_x, p_y)
    matrix[p_x][p_y] = color[0]

    color[0], color[1] = color[1], color[0]
    pawn[0], pawn[1] = pawn[1], pawn[0]