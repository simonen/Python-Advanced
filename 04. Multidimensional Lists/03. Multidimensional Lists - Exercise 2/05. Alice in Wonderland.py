def in_bounds(r: int, c: int, grid: list) -> bool:
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

moves = {"up": lambda x, y: (x - 1, y),
         "down": lambda x, y: (x + 1, y),
         "left": lambda x, y: (x, y - 1),
         "right": lambda x, y: (x, y + 1),
         }

size = int(input())
matrix = [list(input().split()) for _ in range(size)]
a_x, a_y = [(i, j) for i in range(size) for j in range(size) if matrix[i][j] == "A"]
bags = 0

while True:
    command = input()
    matrix[a_x][a_y] = "*"
    a_x, a_y = moves[command](a_x, a_y)

    is_exit = not in_bounds(a_x, a_y, matrix)
    if not is_exit:
        if matrix[a_x][a_y].isdigit():
            bags += int(matrix[a_x][a_y])
        elif matrix[a_x][a_y] == "R":
            is_exit = True

        matrix[a_x][a_y] = "*"

    if is_exit:
        print("Alice didn't make it to the tea party.")
        break

    if bags >= 10:
        print("She did it! She went to the party.")
        break

    matrix[a_x][a_y] = "A"

for i in matrix:
    print(*i)