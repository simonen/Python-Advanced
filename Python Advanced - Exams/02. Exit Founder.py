size = 6
players = input().split(", ")
matrix = [[j for j in input().split()] for i in range(size)]

resting = []

while True:
    coords = input()
    player = players[0]
    pos_x, pos_y = int(coords[1]), int(coords[4])
    if player in resting:
        resting.pop(resting.index(player))
    elif matrix[pos_x][pos_y] == 'E':
        print(f"{player} found the Exit and wins the game!")
        break
    elif matrix[pos_x][pos_y] == 'W':
        print(f"{player} hits a wall and needs to rest.")
        resting.append(player)
    elif matrix[pos_x][pos_y] == 'T':
        players.pop(players.index(player))
        print(f"{player} is out of the game! The winner is {players[0]}.")
        break

    players[0], players[1] = players[1], players[0]