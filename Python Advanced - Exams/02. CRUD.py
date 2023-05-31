size = 6
matrix = [[j for j in input().split()] for i in range(size)]

movement = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1)
}

commands = {
    'Create': lambda c, v: (v if c == '.' else c),
    'Update': lambda c, v: (v if c != '.' else c),
    'Delete': lambda c, v: ('.' if c != '.' else c),
}

position_tup = list(input())
pos_numbers = [int(x) for x in position_tup if x.isdigit()]
pos_x, pos_y = pos_numbers

command = input()
while command != 'Stop':
    command = command.split(", ")
    action, direction = command[0], command[1]
    p_x, p_y = movement[direction](pos_x, pos_y)
    value = command[2] if len(command) == 3 else None

    if action == 'Read':
        if matrix[p_x][p_y] != '.':
            print(matrix[p_x][p_y])
    else:
        matrix[p_x][p_y] = commands[action](matrix[p_x][p_y], value)

    pos_x, pos_y = p_x, p_y

    command = input()

for i in matrix:
    print(*i)
