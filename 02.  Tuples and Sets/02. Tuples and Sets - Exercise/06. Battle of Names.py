odds = set()
evens = set()

for i in range(1, int(input()) + 1):
    ascii_sum = sum([ord(x) for x in input()]) // i
    if ascii_sum % 2 == 0:
        evens.add(ascii_sum)
    else:
        odds.add(ascii_sum)

if sum(evens) == sum(odds):
    print(", ".join(map(str, list(odds.union(evens)))))
elif sum(odds) > sum(evens):
    print(", ".join(map(str, list(odds.difference(evens)))))
else:
    print(", ".join(map(str, list(odds.symmetric_difference(evens)))))