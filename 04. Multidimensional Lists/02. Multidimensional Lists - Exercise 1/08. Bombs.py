size = int(input())
matrix = [[int(col) for col in input().split()] for x in range(size)]
blast_size = 3
coords = [c for c in input().split()]

def matrix_center(matrix: list, row: int, col: int, size: int):
    if size % 2 == 0:
        return "Size must be odd"
    rows, cols = len(matrix), len(matrix[0])
    start_row = max(0, row - size // 2)
    start_col = max(0, col - size // 2)
    end_row = min(rows - 1, row + size // 2)
    end_col = min(cols - 1, col + size // 2)
    return [(x, y) for x in range(start_row, end_row + 1) for y in range(start_col, end_col + 1)]

for coord in coords:
    b_row, b_col = map(int, coord.split(","))
    bomb = matrix[b_row][b_col]
    if bomb <= 0:
        continue

    for row, col in matrix_center(matrix, b_row, b_col, blast_size):
        if matrix[row][col] > 0:
            matrix[row][col] -= bomb


active = [y for x in matrix for y in x if y > 0]

print(f"Alive cells: {len(active)}")
print(f"Sum: {sum(active)}")
for row in matrix:
    print(*row)