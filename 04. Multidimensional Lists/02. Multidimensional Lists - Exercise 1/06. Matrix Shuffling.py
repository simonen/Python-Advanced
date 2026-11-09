rows, cols = map(int, input().split())
matrix = [[col for col in input().split()] for row in range(rows)]
is_valid = False

command = input().split()
while command[0] != "END":
    if len(command) == 5 and command[0] == "swap":
        try:
            row1, col1, row2, col2 = (int(command[x]) for x in range(1, 5))
            is_valid = (row1 in range(len(matrix)) and col1 in range(len(matrix[0])) and
                        row2 in range(len(matrix)) and col2 in range(len(matrix[0])))
        except ValueError:
            is_valid = False

    if is_valid:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in matrix:
            print(*row)
    else:
        print("Invalid input!")

    command = input().split()
