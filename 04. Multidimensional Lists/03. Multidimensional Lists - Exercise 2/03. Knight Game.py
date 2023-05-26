def moves(k_pos):
    k_row, k_col = k_pos
    possibles_moves = set()
    if k_row - 2 >= 0 and k_col - 1 >= 0:
        possibles_moves.add((k_row - 2, k_col - 1))
    if k_row - 1 >= 0 and k_col - 2 >= 0:
        possibles_moves.add((k_row - 1, k_col - 2))
    if k_row - 2 >= 0 and k_col + 1 < rows:
        possibles_moves.add((k_row - 2, k_col + 1))
    if k_row - 1 >= 0 and k_col + 2 < rows:
        possibles_moves.add((k_row - 1, k_col + 2))
    if k_row + 1 < rows and k_col - 2 >= 0:
        possibles_moves.add((k_row + 1, k_col - 2))
    if k_row + 2 < rows and k_col - 1 >= 0:
        possibles_moves.add((k_row + 2, k_col - 1))
    if k_row + 2 < rows and k_col + 1 < rows:
        possibles_moves.add((k_row + 2, k_col + 1))
    if k_row + 1 < rows and k_col + 2 < rows:
        possibles_moves.add((k_row + 1, k_col + 2))

    return possibles_moves


rows = int(input())
matrix = [[j for j in list(input())] for i in range(rows)]

knights = [(i, j) for i in range(rows) for j in range(rows) if matrix[i][j] == "K"]
removed = 0

while knights:
    knights_book = {}
    for k in knights:
        all_moves = moves(k)
        targets = all_moves.intersection(knights)
        knights_book[k] = len(targets)

    sorted_knights = sorted(knights_book.items(), key=lambda x: -x[1])

    if sorted_knights[0][1] == 0:
        break

    index = knights.index(sorted_knights[0][0])
    knights.pop(index)
    removed += 1

print(removed)