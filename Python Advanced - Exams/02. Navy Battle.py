size = int(input())
matrix = [[j for j in list(input())] for i in range(size)]

movement = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1)
}

sub_x, sub_y = next([i, j] for i in range(size) for j in range(size) if matrix[i][j] == 'S')
hits = 0
cruisers = 3

command = input()

while True:
    matrix[sub_x][sub_y] = '-'
    p_x, p_y = movement[command](sub_x, sub_y)
    if matrix[p_x][p_y] == 'C':
        cruisers -= 1
    elif matrix[p_x][p_y] == '*':
        hits += 1

    sub_x, sub_y = p_x, p_y
    matrix[p_x][p_y] = 'S'

    if not cruisers:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

    if hits == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{p_x}, {p_y}]!")
        break

    command = input()

for i in matrix:
    print(*i, sep='')
