from collections import deque


choco = list(map(int, input().split(", ")))
milk_cups = deque(list(map(int, input().split(", "))))
milkshakes = 0
invalid = []

while choco and milk_cups and milkshakes < 5:
    if choco[-1] <= 0:
        invalid.append(choco.pop())

    if milk_cups[0] <= 0:
        invalid.append(milk_cups.popleft())

    if invalid:
        invalid = []
        continue

    cup = milk_cups.popleft()
    if choco[-1] == cup:
        milkshakes += 1
        choco.pop()
        continue

    milk_cups.append(cup)
    choco[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(map(str, choco)) if choco else 'empty'}")
print(f"Milk: {', '.join(map(str, milk_cups)) if milk_cups else 'empty'}")
