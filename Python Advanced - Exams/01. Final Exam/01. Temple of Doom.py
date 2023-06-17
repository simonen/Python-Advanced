tools = list(map(int, input().split()))
substances = list(map(int, input().split()))
challenges = list(map(int, input().split()))

while tools and substances:
    tool = tools.pop(0)
    subst = substances.pop()

    product = tool * subst

    if product in challenges:
        challenges.pop(challenges.index(product))
    else:
        tool += 1
        subst -= 1
        tools.append(tool)
        if subst > 0:
            substances.append(subst)

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")
if substances:
    print(f"Substances: {', '.join(map(str, substances))}")
if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")