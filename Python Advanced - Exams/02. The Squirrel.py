hazelnuts = 0
size = int(input())
commands = input().split(", ")

matrix = [[j for j in list(input())] for i in range(size)]
squirrel_x, squirrel_y = next([i, j] for j in range(size) for i in range(size) if matrix[i][j] == 's')
movement = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1)
}

is_exit = False

while commands:
    direction = commands.pop(0)
    s_x, s_y = movement[direction](squirrel_x, squirrel_y)

    if s_x not in range(size) or s_y not in range(size):
        print("The squirrel is out of the field.")
        is_exit = True
        break

    if matrix[s_x][s_y] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        is_exit = True
        break

    elif matrix[s_x][s_y] == 'h':
        hazelnuts += 1

    matrix[squirrel_x][squirrel_y] = '*'
    matrix[s_x][s_y] = 's'
    squirrel_x, squirrel_y = s_x, s_y

    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break

if hazelnuts < 3 and not is_exit:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
