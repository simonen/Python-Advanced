size = 6
matrix = [[j for j in input().split()] for i in range(size)]

col_sum = 0
prize_won = ''
prize = {
    range(100, 200): 'Football',
    range(200, 300): 'Teddy Bear',
    range(300, 10000000): 'Lego Construction Set'
}

for i in range(3):
    tuple_elements = input().strip("()").split(",")
    row, col = map(int, tuple_elements)
    if row not in range(size) or col not in range(size):
        continue
    if matrix[row][col] == "B":
        matrix[row][col] = 0
        for j in range(size):
            points = int(matrix[j][col])
            col_sum += points

for points, item in prize.items():
    if col_sum in points:
        prize_won = item
        print(f"Good job! You scored {col_sum} points, and you've won {item}.")
        break
else:
    print(f"Sorry! You need {100 - col_sum} points more to win a prize.")
