size = int(input())
commands = input().split()
matrix = [[col for col in input().split()] for row in range(size)]
move = {"up": lambda x, y: (x - 1, y) if x > 0 else (x, y),
        "down": lambda x, y: (x + 1, y) if x < size - 1 else (x, y),
        "left": lambda x, y: (x, y - 1) if y > 0 else (x, y),
        "right": lambda x, y: (x, y + 1) if y < size - 1 else (x, y)}

coal = [col for row in range(size) for col in range(size) if matrix[row][col] == "c"]
miner_x, miner_y = next(((row, col) for row in range(size) for col in range(size) if matrix[row][col] == "s"))

while commands:
    command = commands.pop(0)
    matrix[miner_x][miner_y] = "*"
    miner_x, miner_y = move[command](miner_x, miner_y)
    if matrix[miner_x][miner_y] == "c":
        coal.pop()
    if not coal:
        print(f"You collected all coal! ({miner_x}, {miner_y})")
        break
    if matrix[miner_x][miner_y] == "e":
        print("Game over!", (miner_x, miner_y))
        break

    matrix[miner_x][miner_y] = "s"

else:
    print(f"{len(coal)} pieces of coal left. ({miner_x}, {miner_y})")
