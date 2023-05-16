chocolate = input().split(", ")
milk = input().split(", ")

milkshakes = 0
while chocolate and milk and milkshakes < 5:
    choco = chocolate.pop()
    milky = milk.pop(0)
    if int(choco) > 0:
        if int(milky) > 0:
            if int(choco) == int(milky):
                milkshakes += 1
            else:
                milk.append(milky)
                chocolate.append(str(int(choco) - 5))
        else:
            chocolate.append(choco)
    elif int(milky) > 0:
        milk.insert(0, milky)

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join(chocolate)}")
else:
    print(f"Chocolate: empty")
if milk:
    print(f"Milk: {', '.join(milk)}")
else:
    print(f"Milk: empty")
