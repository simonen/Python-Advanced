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

miner = ''
coal_left = 0

for i in range(size):
    for j in range(size):
        if matrix[i][j] == "s":
            miner = [i, j]
        elif matrix[i][j] == "c":
            coal_left += 1

while commands:
    action = commands.pop(0)
    if action in commands_rows:
        miner[0] = commands_rows[action](miner[0])
    elif action in commands_cols:
        miner[1] = commands_cols[action](miner[1])
    if matrix[miner[0]][miner[1]] == "e":
        print('Game over!', tuple(miner))
        break
    if matrix[miner[0]][miner[1]] == "c":
        matrix[miner[0]][miner[1]] = "*"
        coal_left -= 1
    if coal_left == 0:
        print("You collected all coal!", tuple(miner))
        break
else:
    print(f"{coal_left} pieces of coal left. {tuple(miner)}")