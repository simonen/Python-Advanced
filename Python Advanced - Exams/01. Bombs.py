effects = list(map(int, input().split(", ")))
casings = list(map(int, input().split(", ")))

crafted_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0,
}

bombs = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs',
}

while effects and casings:
    effect = effects.pop(0)
    casing = casings.pop()

    if effect + casing in bombs:
        crafted_bombs[bombs[effect + casing]] += 1
    else:
        casing -= 5
        casings.append(casing)
        effects.insert(0, effect)

    if all(v >= 3 for v in crafted_bombs.values()):
        print("Bene! You have successfully filled the bomb pouch!")
        break
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join(map(str, effects))}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join(map(str, casings))}")
else:
    print("Bomb Casings: empty")


for bomb, quant in sorted(crafted_bombs.items()):
    print(f"{bomb}: {quant}")