size = 7
p1, p2 = input().split(", ")
matrix = [[j for j in input().split()] for i in range(size)]

hit_func = {
    "D": lambda x, y: sum([int(matrix[0][y]), int(matrix[6][y]), int(matrix[x][0]), int(matrix[x][6])]) * 2,
    "T": lambda x, y: sum([int(matrix[0][y]), int(matrix[6][y]), int(matrix[x][0]), int(matrix[x][6])]) * 3,
    'B': lambda x, y: 501
}

player = [p1, p2]
player_score = [501, 501]
turn = [0, 0]

while True:
    turn[0] += 1
    tuple_elements = input().strip("()").split(",")
    row, col = map(int, tuple_elements)
    score = 0
    hit = ''

    if row in range(size) and col in range(size):
        hit = matrix[row][col]

    if hit in ['B', 'D', 'T']:
        score = hit_func[hit](row, col)
    elif hit.isdigit():
        score = int(hit)

    player_score[0] -= score

    if player_score[0] <= 0:
        print(f"{player[0]} won the game with {turn[0]} throws!")
        break

    turn[0], turn[1] = turn[1], turn[0]
    player[0], player[1] = player[1], player[0]
    player_score[0], player_score[1] = player_score[1], player_score[0]
