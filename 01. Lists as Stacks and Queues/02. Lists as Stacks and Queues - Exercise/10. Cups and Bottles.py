from collections import deque


cups = deque(list(map(int, input())))
bottles = list(map(int, input()))
wasted = 0

while bottles and cups:
    bottle = bottles.pop()
    if bottle >= cups[0]:
        bottle -= cups[0]
        cups.popleft()
        wasted += bottle
    else:
        cups[0] -= bottle


if cups:
    print(f"Cups: {' '.join(map(str, cups))}")
else:
    print(f"Bottles: {' '.join(map(str, bottles))}")

print(f"Wasted litters of water: {wasted}")