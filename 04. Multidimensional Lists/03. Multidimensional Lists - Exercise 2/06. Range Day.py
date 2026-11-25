def in_bounds(row: int, col: int, grid: list) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def move(direction: str, s: int, x: int, y: int, grid: list) -> tuple[int, int]:
    for _ in range(s):
        n_x, n_y = step(direction, x, y)
        invalid = ((not in_bounds(n_x, n_y, grid) or
                    (_ == s - 1 and matrix[n_x][n_y] == "x")))
        if invalid:
            break
        x, y = n_x, n_y
    return x, y


def shoot(direction: str, x: int, y: int, grid: list) -> tuple[int, int] | None:
    while True:
        x, y = step(direction, x, y)
        if not in_bounds(x, y, grid):
            return None
        if matrix[x][y] == "x":
            return x, y


def step(direction: str, x: int, y: int) -> tuple[int, int]:
    d_x, d_y = DELTAS[direction]
    return x + d_x, y + d_y


DELTAS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
size = 5

matrix = [list(input().split()) for _ in range(size)]

p_x, p_y = next((i, j) for i in range(size) for j in range(size) if matrix[i][j] == 'A')
targets = set((i, j) for i in range(size) for j in range(size) if matrix[i][j] == 'x')
initial_targets = len(targets)
hits = []

for _ in range(int(input())):
    action, direct, *rest = input().split()
    steps = int(rest[0]) if rest else 0
    if action == "shoot":
        target = shoot(direct, p_x, p_y, matrix)
        if target is not None:
            hits.append(target)
            t_x, t_y = target
            matrix[t_x][t_y] = "."
            targets.discard((t_x, t_y))
    elif action == "move":
        matrix[p_x][p_y] = '.'
        p_x, p_y = move(direct, steps, p_x, p_y, matrix)
        matrix[p_x][p_y] = 'A'

    if not targets:
        print(f"Training completed! All {initial_targets} targets hit.")
        break
else:
    print(f"Training not completed! {len(targets)} targets left.")

for r, c in hits:
    print(f"[{r}, {c}]")
