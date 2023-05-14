m = set()
n = set()

# first_set = {int(input()) for _ in range(first)}
# second_set = {int(input()) for _ in range(second)}

first, second = list(map(int, input().split()))
for _ in range(first):
    m.add(int(input()))
for _ in range(second):
    n.add(int(input()))

[print(i) for i in m.intersection(n)]
# print(m.intersection(n))
# print('union:', m.union(n))
# print('intersection:', m.intersection(n))
# print('difference:', m.difference(n))
# print('symmetric difference:', m.symmetric_difference(n))

