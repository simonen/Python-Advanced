evens = set()
odds = set()

def comma_sep(sets: set[int]) -> str:
    return ", ".join(map(str, sets))


for row in range(1, int(input()) + 1):
    name = input()
    ascii_sum = sum(ord(x) for x in name) // row
    if ascii_sum % 2 == 0:
        evens.add(ascii_sum)
    else:
        odds.add(ascii_sum)

if sum(evens) == sum(odds):
    print(comma_sep(odds.union(evens)))
elif sum(evens) < sum(odds):
    print(comma_sep(odds.difference(evens)))
else:
    print(comma_sep(odds.symmetric_difference(evens)))