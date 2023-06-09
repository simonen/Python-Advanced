size = 6
matrix = [[j for j in input().split()] for i in range(size)]

rover_x, rover_y = next([i, j] for i in range(size) for j in range(size) if matrix[i][j] == 'E')
directions = input().split(", ")

movement = {
    'up': lambda x, y: (x - 1, y) if x - 1 in range(size) else (size - 1, y),
    'down': lambda x, y: (x + 1, y) if x + 1 in range(size) else (0, y),
    'left': lambda x, y: (x, y - 1) if y - 1 in range(size) else (x, size - 1),
    'right': lambda x, y: (x, y + 1) if y + 1 in range(size) else (x, 0),
}

deposits = {
    'C': 'Concrete',
    'W': 'Water',
    'M': 'Metal',
}
discovered = []
for direction in directions:
    rover_x, rover_y = movement[direction](rover_x, rover_y)
    position = matrix[rover_x][rover_y]

    if position == 'R':
        print(f'Rover got broken at ({rover_x}, {rover_y})')
        break
    elif position in deposits:
        print(f"{deposits[position]} deposit found at ({rover_x}, {rover_y})")
        if deposits[position] not in discovered:
            discovered.append(deposits[position])

if len(discovered) == 3:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')