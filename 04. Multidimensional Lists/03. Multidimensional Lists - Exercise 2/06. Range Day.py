def in_bounds(row: int, col: int, grid: list) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def move(direction: str, s: int, x: int, y: int, grid: list) -> tuple:
    temp_x, temp_y = x, y
    for _ in range(s):
        temp_x, temp_y = x, y
        x, y = directions[direction](x, y)
        if not in_bounds(x, y, grid):
            return temp_x, temp_y

    if matrix[x][y] == "x":
        return temp_x, temp_y
    return x, y


def shoot(direction: str, s: int, x: int, y: int, grid: list) -> list[int] | None:
    for _ in range(s):
        x, y = directions[direction](x, y)
        if not in_bounds(x, y, grid):
            break
        if matrix[x][y] == "x":
            return [x, y]
    return None


size = 5
matrix = [list(input().split()) for _ in range(size)]

p_x, p_y = next((i, j) for i in range(size) for j in range(size) if matrix[i][j] == 'A')
targets = set((i, j) for i in range(size) for j in range(size) if matrix[i][j] == 'x')
hits = []

directions = {"up": lambda x, y: (x - 1, y),
              "down": lambda x, y: (x + 1, y),
              "left": lambda x, y: (x, y - 1),
              "right": lambda x, y: (x, y + 1), }

for _ in range(int(input())):
    c = input().split()
    action, direct = c[0], c[1]
    if action == "shoot":
        target = shoot(direct, size, p_x, p_y, matrix)
        if target is not None:
            hits.append(target)
            t_x, t_y = target
            matrix[t_x][t_y] = "."
            targets -= {(t_x, t_y)}
    elif action == "move":
        steps = int(c[2])
        matrix[p_x][p_y] = '.'
        p_x, p_y = move(direct, steps, p_x, p_y, matrix)
        matrix[p_x][p_y] = 'A'

    if not targets:
        print(f"Training completed! All {len(hits)} targets hit.")
        break
else:
    print(f"Training not completed! {len(targets)} targets left.")

for h in hits:
    print(h)
