matrix = [[j for j in input().split()] for i in range(int(input()))]
char = input()

for i, j in enumerate(matrix):
    if char in ''.join(j):
        print((i, ''.join(j).index(char)))
        break
else:
    print(f"{char} does not occur in the matrix")