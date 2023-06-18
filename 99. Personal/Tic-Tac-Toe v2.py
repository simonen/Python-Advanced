size = 3
matrix = [[i, i + 1, i + 2] for i in range(1, 10, 3)]

print(*matrix, sep='\n')
player1, player2 = [['Xopxe', 'X'], ['Mopxe', 'O']]
symbols = ['X', 'O']
turns = 9

while True:
    position = int(input(f"{player1[0]}, enter your position: "))
    row = (position - 1) // size
    col = (position - 1) % size

    if matrix[row][col] in symbols:
        print('Select a valid position!')
        continue

    matrix[row][col] = player1[1]
    turns -= 1

    for i in matrix:
        print(f"| {' | '.join(map(str, i))} |")

    if all(matrix[row][i] == player1[1] for i in range(size)) or \
            all(matrix[i][i] == player1[1] for i in range(size)) or \
            all(matrix[i][size - 1 - i] == player1[1] for i in range(size)) or \
            all(matrix[i][col] == player1[1] for i in range(size)):
        print(f"{player1[0]} wins!")
        break

    if turns == 0:
        print("Draw!")
        break

    player1, player2 = player2, player1
