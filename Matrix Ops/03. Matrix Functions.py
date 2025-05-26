# Create an n x m matrix, elements separated by space
rows, cols = [int(x) for x in input().split()]
matrix = [[j for j in input().split()] for i in range(rows)]

# Print the matrix

print(*matrix, sep='\n')

# Move to the same row by n-steps in the opposite direction when leaving a matrix

movement = {
    'up': lambda x, y: ((x - 1) % rows, y),
    'down': lambda x, y: ((x + 1) % rows, y),
    'left': lambda x, y: (x, (y - 1) % cols),
    'right': lambda x, y: (x, (1 + y) % cols)
}

# Normal movement by 1 step, no boundary checking

movement = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1)
}

# Normal movement by 1 step, including diagonals, no boundary checking,

movement = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1),
    'up_left': lambda x, y: (x - 1, y - 1),
    'up_right': lambda x, y: (x - 1, y + 1),
    'down_left': lambda x, y: (x + 1, y - 1),
    'down_right': lambda x, y: (x + 1, y + 1)
}

# Move to the opposite end of a matrix when leaving it.

movement = {
    'up': lambda x, y: (x - 1, y) if x - 1 in range(size) else (size - 1, y),
    'down': lambda x, y: (x + 1, y) if x + 1 in range(size) else (0, y),
    'left': lambda x, y: (x, y - 1) if y - 1 in range(size) else (x, size - 1),
    'right': lambda x, y: (x, y + 1) if y + 1 in range(size) else (x, 0),
}


# Unpack a tuple from a string input ex. (1, 2)
tuple_elements = input().strip("()").split(", ")

