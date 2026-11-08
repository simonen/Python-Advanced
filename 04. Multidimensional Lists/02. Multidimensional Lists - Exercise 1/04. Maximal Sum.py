rows, cols = list(map(int, input().split()))
matrix = [[int(col) for col in input().split()[:cols]] for row in range(rows)]
size = 3
bucket_width = min(size, cols)
bucket_height = min(size, rows)
# largest_sum = size ** 2 * -20
largest_sum = sum(sum(matrix[i][:bucket_width]) for i in range(bucket_height)) # First 3x3 submatrix sum as initial best candidate
largest_sub = [matrix[i][:bucket_width] for i in range(bucket_height)]

for row in range(rows - bucket_height + 1): # always 1 if rows <= size
    for col in range(cols - bucket_width + 1):
        sub_sum = 0
        sub = []
        for s in range(bucket_height):
            curr_sub_row = matrix[row + s][col:col + bucket_width]
            sub.append(curr_sub_row)
            sub_sum += sum(curr_sub_row)

        if sub_sum > largest_sum:
            largest_sum = sub_sum
            largest_sub = sub


print(f"Sum = {largest_sum}")
for row in largest_sub:
    print(*row)
