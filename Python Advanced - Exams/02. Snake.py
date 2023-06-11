size = int(input())
matrix = [[j for j in list(input())] for i in range(size)]
# print(*matrix, sep='\n')
movement = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1),
}

snake_x, snake_y = next([i, j] for i in range(size) for j in range(size) if matrix[i][j] == 'S')
burrows = [[i, j] for i in range(size) for j in range(size) if matrix[i][j] == 'B']

food = 0

while True:
    direction = input()
    matrix[snake_x][snake_y] = '.'
    p_x, p_y = movement[direction](snake_x, snake_y)
    if p_x not in range(size) or p_y not in range(size):
        print("Game over!")
        break

    if matrix[p_x][p_y] == "*":
        food += 1
    elif matrix[p_x][p_y] == 'B':
        matrix[p_x][p_y] = '.'
        burrows.pop(burrows.index([p_x, p_y]))
        p_x, p_y = burrows[0]

    matrix[p_x][p_y] = 'S'
    snake_x, snake_y = p_x, p_y

    if food >= 10:
        print("You won! You fed the snake.")
        break

    # print("----")
    # print(*matrix, sep='\n')

print(f"Food eaten: {food}")

for i in matrix:
    print(*i, sep='')