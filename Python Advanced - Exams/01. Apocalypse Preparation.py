textiles = list(map(int, input().split()))
medicaments = list(map(int, input().split()))

items = {
    30: 'Patch',
    40: 'Bandage',
    100: 'MedKit'
}
aid = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}

while textiles and medicaments:
    text = textiles.pop(0)
    medi = medicaments.pop()
    if text + medi in items:
        aid[items[text + medi]] += 1
    elif text + medi > 100:
        remainder = text + medi - 100
        aid['MedKit'] += 1
        medicaments[-1] += remainder
    else:
        medicaments.append(medi + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for med, quant in sorted(aid.items(), key=lambda x: (-x[1], x[0])):
    if quant > 0:
        print(f"{med} - {quant}")

medicaments.reverse()
if medicaments:
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")