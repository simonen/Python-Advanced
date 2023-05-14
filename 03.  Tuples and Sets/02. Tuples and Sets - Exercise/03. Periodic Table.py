table = set()

for _ in range(int(input())):
    table = table.union(set(input().split()))

[print(el) for el in table]
