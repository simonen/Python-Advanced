rows, cols = list(map(int, input().split()))

alpha = [chr(x) for x in range(97, 123)]
matrix = []

for i in range(rows):
    line = []
    for j in range(cols):
        palindrome = alpha[i]
        palindrome += alpha[i + j]
        palindrome += alpha[i]
        line.append(palindrome)

    matrix.append(line)

for k in matrix:
    print(*k, sep=' ')