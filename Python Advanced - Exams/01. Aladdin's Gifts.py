materials = list(map(int, input().split()))
magic = list(map(int, input().split()))

items = {
    range(100, 200): 'Gemstone',
    range(200, 300): 'Porcelain Sculpture',
    range(300, 400): 'Gold',
    range(400, 500): 'Diamond Jewellery',
}

crafted = {'Gemstone': 0,
           'Porcelain Sculpture': 0,
           'Gold': 0,
           'Diamond Jewellery': 0
           }

while materials and magic:
    mat = materials.pop()
    energy = magic.pop(0)
    product = mat + energy
    if product < 100:
        if product % 2 == 0:
            product = 2 * mat + 3 * energy
        else:
            product *= 2
    elif product > 499:
        product //= 2
    for k, item in items.items():
        if product in k:
            crafted[item] += 1
            break

if (crafted['Gemstone'] > 0 and crafted['Porcelain Sculpture'] > 0) or \
        (crafted['Gold'] > 0 and crafted['Diamond Jewellery'] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print('Materials left:', ', '.join(map(str, materials)))
if magic:
    print('Magic left:', ', '.join(map(str, magic)))

for item, quant in sorted(crafted.items()):
    if quant > 0:
        print(f"{item}: {quant}")