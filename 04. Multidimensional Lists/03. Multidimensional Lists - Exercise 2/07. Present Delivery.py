DELTAS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
def in_bounds(x, y, grid: list) -> bool:
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def move(direction: str, x: int, y: int) -> tuple[int, int]:
    d_x, d_y = DELTAS[direction]
    if not in_bounds(x + d_x, y + d_y, matrix):
        return x, y
    return x + d_x, y + d_y


def format_grid(grid: list) -> str:
    return "\n".join(' '.join(i) for i in grid)


def give_present(x: int, y: int) -> None:
    global presents
    presents -= 1
    matrix[x][y] = "-"
    nice_kids.discard((x, y))


presents = int(input())
size = int(input())
matrix = [list(input().split()) for _ in range(size)]

s_x, s_y = next((i, j) for i in range(size) for j in range(size) if matrix[i][j] == "S")
nice_kids = {(i, j) for i in range(size) for j in range(size) if matrix[i][j] == "V"}
initial_nice_kids = len(nice_kids)


while True:
    command = input()
    if command == "Christmas morning":
        break

    matrix[s_x][s_y] = "-"
    s_x, s_y = move(command, s_x, s_y)
    if matrix[s_x][s_y] == "V":
        give_present(s_x, s_y)
    elif matrix[s_x][s_y] == "C":
        for d in DELTAS:
            n_x, n_y = move(d, s_x, s_y)
            if matrix[n_x][n_y] in ("X", "V"):
                give_present(n_x, n_y)
                if presents == 0:
                    break

    matrix[s_x][s_y] = "S"
    if presents == 0:
        break

if presents == 0 and nice_kids:
    print("Santa ran out of presents!")

print(print_grid(matrix))

if nice_kids:
    print(f"No presents for {len(nice_kids)} nice kid/s.")
else:
    print(f"Good job, Santa! {initial_nice_kids} happy nice kid/s.")
