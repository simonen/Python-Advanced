from collections import deque


def in_bounds(x: int, y: int):
    return 0 <= x < rows and 0 <= y < cols


def bunny_spread(x: int, y: int) -> set:
    res = set()
    for c in "UDLR":
        new_x, new_y = direction[c](x, y)
        if in_bounds(new_x, new_y):
            res.add((new_x, new_y))

    return res


direction = {"U": lambda x, y: (x - 1, y),
        "D": lambda x, y: (x + 1, y),
        "L": lambda x, y: (x, y - 1),
        "R": lambda x, y: (x, y + 1), }


rows, cols = map(int, input().split())
matrix = [list(input()) for _ in range(rows)]
commands = deque(input())
p_x, p_y = next((r, c) for r in range(rows) for c in range(cols) if matrix[r][c] == "P")
active_bunnies = {(row, col) for row in range(rows) for col in range(cols) if matrix[row][col] == "B"}
all_bunnies = active_bunnies.copy()
is_escape = False

while True:
    command = commands.popleft()
    matrix[p_x][p_y] = "."
    last_coords = (p_x, p_y)
    p_x, p_y = direction[command](p_x, p_y)

    if not in_bounds(p_x, p_y):
        is_escape = True
        p_x, p_y = None, None    # Sentinel: off-board, never matches a bunny coord.

    # Bunny propagation
    new_bunnies = set()
    for b_x, b_y in active_bunnies:
        new_bunnies.update(bunny_spread(b_x, b_y))

    active_bunnies = new_bunnies - all_bunnies # Keep only the last batch of bunnies
    all_bunnies.update(new_bunnies)

    for b_x, b_y in new_bunnies:
        matrix[b_x][b_y] = "B"

    is_dead = (p_x, p_y) in all_bunnies

    if is_escape or is_dead:
        break

    matrix[p_x][p_y] = "P"


for i in matrix:
    print("".join(i))

if is_dead:
    print(f"dead: {p_x} {p_y}")
elif is_escape:
    p_x, p_y = last_coords
    print(f"won: {p_x} {p_y}")
