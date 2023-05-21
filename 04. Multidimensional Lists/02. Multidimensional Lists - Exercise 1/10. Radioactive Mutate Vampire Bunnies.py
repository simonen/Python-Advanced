def bunny_spread(row_f, col_f, rows_f, cols_f):
    coords = set()
    if row_f - 1 in range(rows_f):
        coords.add((row_f - 1, col_f))
    if row_f + 1 in range(rows_f):
        coords.add((row_f + 1, col_f))
    if col_f - 1 in range(cols_f):
        coords.add((row_f, col_f - 1))
    if col_f + 1 in range(cols_f):
        coords.add((row_f, col_f + 1))

    return coords


rows, cols = [int(x) for x in input().split()]
matrix = [[j for j in list(input())] for x in range(rows)]
commands = list(input())

commands_rows = {'U': lambda x: x - 1, 'D': lambda x: x + 1}
commands_cols = {'L': lambda x: x - 1, 'R': lambda x: x + 1}

bunnies = set()
row, col = next([x, y] for x in range(rows) for y in range(cols) if matrix[x][y] == 'P') # Locate player
is_winner = None

while commands:
    action = commands.pop(0)
    matrix[row][col] = '.'
    l_row = row
    l_col = col
    if action in commands_rows:
        row = commands_rows[action](row)
    elif action in commands_cols:
        col = commands_cols[action](col)

    if row not in range(rows):
        row = l_row
        is_winner = True
    elif col not in range(cols):
        col = l_col
        is_winner = True
    elif matrix[row][col] == 'B':
        is_winner = False
    else:
        matrix[row][col] = 'P'

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "B":
                bunnies = bunnies.union(bunny_spread(i, j, rows, cols))

    for a, b in bunnies:
        matrix[a][b] = "B"

    if matrix[row][col] == "B" and is_winner is None:
        is_winner = False
    # print(*matrix, sep="\n")
    # print()
    if is_winner is not None:
        break

for i in matrix:
    print("".join(i))
if not is_winner:
    print("dead:", row, col)
else:
    print('won:', row, col)
