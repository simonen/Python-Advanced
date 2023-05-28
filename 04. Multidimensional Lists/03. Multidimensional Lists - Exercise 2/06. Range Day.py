size = 5
matrix = [[j for j in input().split()] for i in range(size)]

player_x, player_y = next([i, j] for j in range(5) for i in range(size) if matrix[i][j] == "A")
targets = sum(i.count('x') for i in matrix)
targets_left = targets
hits = []
movement = {'up': lambda x, y, s: (x - s, y) if s > 0 else (x - 1, y),
            'down': lambda x, y, s: (x + s, y) if s > 0 else (x + 1, y),
            'left': lambda x, y, s: (x, y - s) if s > 0 else (x, y - 1),
            'right': lambda x, y, s: (x, s + y) if s > 0 else (x, y + 1)}

commands = int(input())
for _ in range(commands):
    command = input().split()
    action = command[0]
    direction = command[1]
    p_x, p_y = player_x, player_y
    if action == "move":
        step = int(command[2])
        p_x, p_y = movement[direction](p_x, p_y, step)
        if p_x not in range(size) or p_y not in range(size) or matrix[p_x][p_y] != '.':
            p_x, p_y = player_x, player_y
        else:
            matrix[player_x][player_y] = "."
            player_x, player_y = p_x, p_y
            matrix[player_x][player_y] = "A"

    elif action == 'shoot':
        for _ in range(size):
            p_x, p_y = movement[direction](p_x, p_y, 0)
            if p_x not in range(0, size) or p_y not in range(0, size):
                break
            if matrix[p_x][p_y] == 'x':
                hits.append([p_x, p_y])
                targets_left -= 1
                matrix[p_x][p_y] = '.'
                break

    if targets_left == 0:
        print(f"Training completed! All {targets} targets hit.")
        break

else:
    print(f"Training not completed! {targets_left} targets left.")

print(*hits, sep='\n')
