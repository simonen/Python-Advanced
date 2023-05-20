rows, cols = [int(x) for x in input().split()]
matrix = [[j for j in input().split()] for i in range(rows)]
command = input()

while command != "END":
    command = command.split()
    action = command[0]
    coord = command[1:]
    valid = (
        action == "swap" and
        len(coord) == 4 and
        int(coord[0]) in range(len(matrix)) and int(coord[2]) in range(len(matrix)) and
        int(coord[1]) in range(len(matrix[0])) and int(coord[3]) in range(len(matrix[0]))
    )
    if valid:
        row1, col1, row2, col2 = list(map(int, coord))
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for i in matrix:
            print(' '.join(i))
    else:
        print("Invalid input!")

    command = input()
