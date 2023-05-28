rows, cols = [int(x) for x in input().split()]
matrix = [[j for j in input().split()] for i in range(rows)]

movement = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1)
}
touched = 0
moves = 0
blind_x, blind_y = next([i, j] for j in range(cols) for i in range(rows) if matrix[i][j] == 'B')

command = input()
while command != "Finish":

    p_x, p_y = movement[command](blind_x, blind_y)
    if p_x not in range(0, rows) or p_y not in range(0, cols) or matrix[p_x][p_y] == 'O':
        command = input()
        continue
    moves += 1
    if matrix[p_x][p_y] == "P":
        touched += 1

    matrix[blind_x][blind_y] = "-"
    blind_x, blind_y = p_x, p_y
    matrix[blind_x][blind_y] = "B"

    if touched == 3:
        break

    command = input()

print("Game over!")
print(f"Touched opponents: {touched} Moves made: {moves}")
