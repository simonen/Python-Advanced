rows, cols = list(map(int, input().split(", ")))
matrix = [[j for j in input().split()] for i in range(rows)]

movement = {
    'up': lambda x, y: ((x - 1) % rows, y),
    'down': lambda x, y: ((x + 1) % rows, y),
    'left': lambda x, y: (x, (y - 1) % cols),
    'right': lambda x, y: (x, (1 + y) % cols)
}

items = [matrix[i][j] for i in range(rows) for j in range(cols) if matrix[i][j] not in ['.', 'Y']]
decorations = 0
gifts = 0
cookies = 0
is_christmas = False
santa_x, santa_y = next([i, j] for i in range(rows) for j in range(cols) if matrix[i][j] == 'Y')
command = input()

while command != 'End':
    command = command.split("-")
    direction = command[0]
    step = int(command[1])
    for i in range(step):
        matrix[santa_x][santa_y] = "x"
        santa_x, santa_y = movement[direction](santa_x, santa_y)

        if matrix[santa_x][santa_y] == "D":
            decorations += 1
        elif matrix[santa_x][santa_y] == "G":
            gifts += 1
        elif matrix[santa_x][santa_y] == "C":
            cookies += 1

        matrix[santa_x][santa_y] = "Y"
        if cookies + decorations + gifts == len(items):
            print("Merry Christmas!")
            is_christmas = True
            break
        # print([santa_x, santa_y], *matrix, sep='\n')
    if is_christmas:
        break

    command = input()

print(f"You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

for i in matrix:
    print(*i, sep=' ')
