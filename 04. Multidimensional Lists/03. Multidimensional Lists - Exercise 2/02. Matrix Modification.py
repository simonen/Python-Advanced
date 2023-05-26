rows = int(input())
matrix = [[int(j) for j in input().split()] for i in range(rows)]

command = input()

while command != 'END':
    command = command.split()
    action, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])
    if row not in range(rows) or col not in range(len(matrix[0])):
        print("Invalid coordinates")
        command = input()
        continue

    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value

    command = input()

for i in matrix:
    print(" ".join(map(str, i)))
