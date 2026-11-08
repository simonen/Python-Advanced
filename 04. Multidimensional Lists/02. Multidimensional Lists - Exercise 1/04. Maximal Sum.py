def matrix_subdiv(matrix: list, size: int):
    """Yield all size×size (clamped) submatrices of matrix as lists of rows.
    Single-use generator: re-call to iterate again.
    """
    sub_rows, sub_cols = len(matrix), len(matrix[0])
    bucket_height = min(size, sub_rows)
    bucket_width = min(size, sub_cols)
    for row in range(sub_rows - bucket_height + 1):
        for col in range(sub_cols - bucket_width + 1):
            yield [matrix[row + s][col:col + bucket_width] for s in range(bucket_height)]


rows, cols = list(map(int, input().split()))
matrix = [[int(col) for col in input().split()[:cols]] for row in range(rows)]
size = 3

block = list(matrix_subdiv(matrix, size))
best_sum = max([sum(map(sum, b)) for b in block])
best_sub = max(block, key=lambda b: sum(map(sum, b)))

print(f"Sum = {best_sum}")

for b in best_sub:
    print(*b)
