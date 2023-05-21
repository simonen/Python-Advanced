string = input().split("|")

matrix = []
for i in string[::-1]:
    matrix.extend(i.split())

print(*matrix)
