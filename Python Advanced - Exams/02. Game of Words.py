string = list(input())
size = int(input())
matrix = [[j for j in list(input())] for i in range(size)]
number = int(input())

player_x, player_y = next([i, j] for i in range(size) for j in range(size) if matrix[i][j] == "P")

movement = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1),
}

for n in range(number):
    direction = input()
    p_x, p_y = movement[direction](player_x, player_y)

    if p_x not in range(size) or p_y not in range(size) and string:
        string.pop()
        continue

    hit = matrix[p_x][p_y]
    if hit.isalpha():
        string.append(hit)

    matrix[player_x][player_y] = '-'
    player_x, player_y = p_x, p_y
    matrix[player_x][player_y] = 'P'

print("".join(string))

for i in matrix:
    print(*i, sep='')
