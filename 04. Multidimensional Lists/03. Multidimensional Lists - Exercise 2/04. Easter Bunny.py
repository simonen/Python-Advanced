from math import inf


def is_valid(coords: tuple[int, int]) -> bool:
    r, c = coords
    return 0 <= r < size and 0 <= c < size

moves = {"up": lambda x, y: (x - 1, y),
         "down": lambda x, y: (x + 1, y),
         "left": lambda x, y: (x, y - 1),
         "right": lambda x, y: (x, y + 1),
         }

size = int(input())
matrix = [list(input().split()) for _ in range(size)]
b_coords = next((i, j) for i in range(size) for j in range(size) if matrix[i][j] == "B")
best_eggs = -inf
best_direction = None
best_coords = []

for m in moves:
    curr_coords = []
    collected_eggs = []
    b_x, b_y = b_coords
    for _ in range(size):
        b_x, b_y = moves[m](b_x, b_y)
        if not is_valid((b_x, b_y)) or matrix[b_x][b_y] == "X":
            break

        collected_eggs.append(int(matrix[b_x][b_y]))
        curr_coords.append([b_x, b_y])

    if not collected_eggs:
        continue

    curr_sum = sum(collected_eggs)
    if curr_sum > best_eggs:
        best_eggs = curr_sum
        best_direction = m
        best_coords = curr_coords

print(best_direction, *best_coords, best_eggs, sep='\n')
