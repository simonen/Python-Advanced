size = int(input())
matrix = [[j for j in input().split()] for i in range(size)]

bags = 0
alice_x, alice_y = next([i, j] for j in range(size) for i in range(size) if matrix[i][j] == "A")
matrix[alice_x][alice_y] = '*'
commands_rows = {'up': lambda x: x - 1, 'down': lambda x: x + 1}
commands_cols = {'left': lambda x: x - 1, 'right': lambda x: x + 1}

command = input()

while bags < 10:

    if command in commands_rows:
        alice_x = commands_rows[command](alice_x)
    elif command in commands_cols:
        alice_y = commands_cols[command](alice_y)

    is_exit = (
        (alice_x not in range(0, size)) or
        (alice_y not in range(0, size))
    )
    if not is_exit:
        if matrix[alice_x][alice_y].isdigit():
            bags += int(matrix[alice_x][alice_y])
        elif matrix[alice_x][alice_y] == 'R':
            is_exit = True

        matrix[alice_x][alice_y] = '*'

    if is_exit:
        print("Alice didn't make it to the tea party.")
        break

    if bags >= 10:
        print('She did it! She went to the party.')
        break

    command = input()

for i in matrix:
    print(*i)
