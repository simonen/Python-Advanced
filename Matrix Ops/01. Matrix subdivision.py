def matrix_subdiv(matrix: list, bucket_size: int) -> list:
    rows, cols = len(matrix), len(matrix[0])
    bucket_height = min(bucket_size, rows)
    bucket_width = min(bucket_size, cols)
    for row in range(rows - bucket_height + 1):
        for col in range(cols - bucket_width + 1):
            yield [matrix[row + s][col:col + bucket_width] for s in range(bucket_height)]


sub_size = 3
matrix = [
    ['1', 'R', 'T', 'Y', '1', '1'],
    ['1', 'W', '0', '2', '1', '1'],
    ['1', '3', '1', '4', '1', '1'],
    ['1', 'X', '6', 'Q', '1', '1'],
    ['1', 'A', 'B', 'C', '1', '1'],
    ['1', '1', '1', '1', '1', '1'],
]

block = list(matrix_subdiv(matrix, sub_size))

print(*matrix, sep='\n')
print()

for b in block:
    print(*b, sep='\n')
    print()
