size = int(input())
racing_num = input()
matrix = [[j for j in input().split()] for i in range(size)]

matrix[0][0] = "C"
distance = 0
movement = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1)
}

car_x, car_y = [0, 0]

direction = input()
while direction != "End":
    p_x, p_y = movement[direction](car_x, car_y)
    position = matrix[p_x][p_y]

    if position == "T":
        matrix[p_x][p_y] = '.'
        t_end = next((i, j) for i in range(size) for j in range(size) if matrix[i][j] == "T")
        p_x, p_y = t_end
        distance += 20

    matrix[car_x][car_y] = '.'
    car_x, car_y = p_x, p_y
    matrix[car_x][car_y] = 'C'
    distance += 10

    if position == 'F':
        print(f"Racing car {racing_num} finished the stage!")
        break

    direction = input()

else:
    print(f"Racing car {racing_num} DNF.")

print(f"Distance covered {distance} km." )

for i in matrix:
    print("".join(i))
