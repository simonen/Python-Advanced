matrix = []

for i in range(int(input())):
    line = [x for x in map(int, input().split(", ")) if x % 2 == 0]
    matrix.append(line)

print(matrix)