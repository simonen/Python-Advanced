males = list(map(int, input().split()))
females = list(map(int, input().split()))

matches = 0

while males and females:
    male = males.pop()
    female = females.pop(0)

    if male <= 0:
        females.insert(0, female)
        continue

    if female <= 0:
        males.append(male)
        continue

    if male % 25 == 0:
        male = males.pop()
        females.insert(0, female)
        continue

    if female % 25 == 0:
        females.pop(0)
        males.append(male)
        continue

    if female == male:
        matches += 1
    elif male != female:
        male -= 2
        males.append(male)

print(f"Matches: {matches}")

if males:
    print("Males left:", ', '.join(map(str, males[::-1])))
else:
    print("Males left: none")

if females:
    print("Females left:", ', '.join(map(str, females)))
else:
    print("Females left: none")