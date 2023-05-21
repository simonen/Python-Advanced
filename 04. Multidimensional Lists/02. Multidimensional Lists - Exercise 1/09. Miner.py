size = int(input())
commands = input().split()
matrix = [[j for j in input().split()] for i in range(size)]

commands_rows = {
    'up': lambda x: x - 1 if x - 1 in range(size) else x,
    'down': lambda x: x + 1 if x + 1 in range(size) else x,
}
commands_cols = {
    'left': lambda x: x - 1 if x - 1 in range(size) else x,
    'right': lambda x: x + 1 if x + 1 in range(size) else x
}

coal = sum(row.count('c') for row in matrix)
miner = next([x, y] for x in range(size) for y in range(size) if matrix[x][y] == "s")

while commands:
    action = commands.pop(0)
    if action in commands_rows:
        miner[0] = commands_rows[action](miner[0])
    elif action in commands_cols:
        miner[1] = commands_cols[action](miner[1])
    row, col = miner
    if matrix[row][col] == "e":
        print('Game over!', tuple(miner))
        break
    if matrix[row][col] == "c":
        matrix[row][col] = "*"
        coal -= 1
    if coal == 0:
        print("You collected all coal!", tuple(miner))
        break
else:
    print(f"{coal} pieces of coal left. {tuple(miner)}")
