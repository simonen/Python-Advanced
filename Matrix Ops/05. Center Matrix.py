# matrix = [[8, 3, 2, 5, 6],
#           [6, 1, 7, 9, 7],
#           [9, 9, 3, 6, 2],
#           [6, 8, 1, 2, 3],
#           [0, 3, 4, 9, 0]]

def matrix_center(matrix: list, coord_x: int, coord_y: int, size: int) -> list:
    """Returns a sub-matrix of size n % 2 != 0 from a central point"""
    if size % 2 == 0:
        return "Size must be odd"
    rows, cols = len(matrix), len(matrix[0])
    start_row = max(0, coord_x - size // 2)
    start_col = max(0, coord_y - size // 2)
    end_row = min(rows - 1, coord_x + size // 2)
    end_col = min(cols - 1, coord_y + size // 2)
    bucket_width = min(size, end_col - start_col + 1)
    bucket_height = min(size, end_row - start_row + 1)

    return [matrix[start_row + s][start_col:start_col + bucket_width] for s in range(bucket_height)]
    # Return element indexes
    # return [(x, y) for x in range(start_row, end_row + 1) for y in range(start_col, end_col + 1)]


print(matrix_center(matrix,2, 2, 4))