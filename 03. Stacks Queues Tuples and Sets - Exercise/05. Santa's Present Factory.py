from collections import deque


materials = list(map(int, input().split()))
magic_levels = deque(list(map(int, input().split())))

presents = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
zeroes = []
crafted = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while materials and magic_levels:
    if magic_levels[0] == 0:
        zeroes.append(magic_levels.popleft())
    if materials[-1] == 0:
        zeroes.append(materials.pop())
    if zeroes:
        zeroes = []
        continue

    magic = magic_levels.popleft()
    product = magic * materials[-1]

    if product < 0:
        materials.append(sum([materials.pop(), magic]))
    elif product not in presents:
        materials[-1] += 15
    else:
        material = materials.pop()
        toy = presents[product]
        crafted[toy] += 1


if (crafted["Doll"] > 0 and crafted["Wooden train"] > 0) or (crafted["Teddy bear"] > 0 and  crafted["Bicycle"] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

res = {k: v for k, v in crafted.items() if v > 0}
for item, amount in sorted(res.items()):
    print(f"{item}: {amount}")
