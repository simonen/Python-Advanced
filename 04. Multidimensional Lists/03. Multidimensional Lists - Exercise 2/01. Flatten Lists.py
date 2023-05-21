matrix = []
for i in input().split("|")[::-1]:
    matrix.extend(i.split())

print(*matrix)
