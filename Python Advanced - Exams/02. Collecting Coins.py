size = int(input())
matrix = [[j for j in input().split()] for i in range(size)]

movement = {
    'up': lambda x, y: (x - 1, y) if x - 1 in range(size) else (size - 1, y),
    'down': lambda x, y: (x + 1, y) if x + 1 in range(size) else (0, y),
    'left': lambda x, y: (x, y - 1) if y - 1 in range(size) else (x, size - 1),
    'right': lambda x, y: (x, y + 1) if y + 1 in range(size) else (x, 0),
}

player_x, player_y = next([i, j] for i in range(size) for j in range(size) if matrix[i][j] == "P")
coins = 0
path = [[player_x, player_y]]
direction = input()

while True:
    matrix[player_x][player_y] = '.'
    player_x, player_y = movement[direction](player_x, player_y)
    path.append([player_x, player_y])
    hit = matrix[player_x][player_y]

    if hit == "X":
        print(f"Game over! You've collected {coins // 2} coins.")
        break

    elif hit.isdigit():
        coins += int(hit)

    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

    matrix[player_x][player_y] = "P"

    direction = input()

print('Your path:', *path, sep='\n')