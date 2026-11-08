rows, cols = list(map(int, input().split()))

alpha = [chr(x) for x in range(97, 123)]
matrix = []

for row in range(rows):
    line = []
    for col in range(cols):
        palindrome = alpha[row]
        palindrome += alpha[row + col]
        palindrome += alpha[row]
        line.append(palindrome)

    matrix.append(line)

for k in matrix:
    print(*k, sep=' ')