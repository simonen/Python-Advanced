table = set()

for _ in range(int(input())):
    table.update(set(input().split()))

[print(el) for el in table]
