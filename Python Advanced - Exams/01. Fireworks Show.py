effects = list(map(int, input().split(", ")))
explosion = list(map(int, input().split(", ")))

fireworks = {'Palm': 0, 'Willow': 0, 'Crossette': 0}

while effects and explosion:
    firework = effects.pop(0)

    if firework <= 0:
        continue

    power = explosion.pop()

    if power <= 0:
        effects.insert(0, firework)
        continue

    boom = firework + power

    if boom % 3 == 0 and boom % 5 != 0:
        fireworks['Palm'] += 1
    elif boom % 5 == 0 and boom % 3 != 0:
        fireworks['Willow'] += 1
    elif boom % 15 == 0:
        fireworks['Crossette'] += 1
    else:
        firework -= 1
        effects.append(firework)
        explosion.append(power)

    if all(v >= 3 for k, v in fireworks.items()):
        print("Congrats! You made the perfect firework show!")
        break
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print("Firework Effects left:", ", ".join(map(str, effects)))

if explosion:
    print('Explosive Power left:', ", ".join(map(str, explosion)))

for firework, quant in fireworks.items():
    print(f"{firework} Fireworks: {quant}")