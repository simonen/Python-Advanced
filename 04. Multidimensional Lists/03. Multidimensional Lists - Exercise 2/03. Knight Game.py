def is_valid(coords):
    if any(coord not in range(0, size) for coord in coords):
        return False
    return True

def moves(k_coords):
    k_x, k_y = k_coords
    possible_moves = set()
    dic = {"nw1": lambda x, y: (x - 2, y - 1),
        "nw2": lambda x, y: (x - 1, y - 2),
        "sw1": lambda x, y: (x + 1, y - 2),
        "sw2": lambda x, y: (x + 2, y - 1),
        "ne1": lambda x, y: (x - 2, y + 1),
        "ne2": lambda x, y: (x - 1, y + 2),
        "se1": lambda x, y: (x + 1, y + 2),
        "se2": lambda x, y: (x + 2, y + 1),
    }

    for m in dic:
        if is_valid(dic[m](k_x, k_y)):
            possible_moves.add(dic[m](k_x, k_y))

    return possible_moves

size = int(input())
matrix = [list(input()) for _ in range(size)]
knights = {(r, c): None for r in range(size) for c in range(size) if matrix[r][c] == 'K'}
removed = 0

while knights:
    knights_book = {}
    for k in knights:
        all_moves = moves(k)
        targets = all_moves.intersection(knights)
        knights_book[k] = len(targets)

    best_knight, attacks = max(knights_book.items(),key=lambda kv: kv[1])

    if attacks == 0:
        break

    del knights[best_knight]
    removed += 1


print(removed)
