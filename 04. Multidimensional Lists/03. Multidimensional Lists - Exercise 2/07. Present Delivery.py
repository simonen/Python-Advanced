presents = int(input())
size = int(input())
matrix = [[j for j in input().split()] for i in range(size)]

movement = {
    'up': lambda x, y: (x - 1, y) if x - 1 in range(size) else (x, y),
    'down': lambda x, y: (x + 1, y) if x + 1 in range(size) else (x, y),
    'left': lambda x, y: (x, y - 1) if y - 1 in range(size) else (x, y),
    'right': lambda x, y: (x, y + 1) if x + 1 in range(size) else (x, y),
}
player_x, player_y = next([i, j] for j in range(size) for i in range(size) if matrix[i][j] == 'S')
good_kids = sum([i.count('V') for i in matrix])
kids_left = good_kids

command = input()
while presents and command != "Christmas morning":
    matrix[player_x][player_y] = '-'
    player_x, player_y = movement[command](player_x, player_y)
    current_pos = matrix[player_x][player_y]
    visits = []
    if current_pos == "C":
        for direction in movement:
            p_x, p_y = movement[direction](player_x, player_y)
            if matrix[p_x][p_y] in "XV":
                visits.append(matrix[p_x][p_y])
            matrix[p_x][p_y] = '-'

    elif current_pos == "V":
        visits.append('V')

    kids_left -= visits.count('V')
    presents -= len(visits)
    matrix[player_x][player_y] = "S"

    if presents > 0:
        command = input()

if presents == 0 and kids_left > 0:
    print("Santa ran out of presents!")

for i in matrix:
    print(' '.join(i))

if kids_left == 0:
    print(f"Good job, Santa! {good_kids} happy nice kid/s.")
else:
    print(f"No presents for {kids_left} nice kid/s.")