line1 = set(map(int, input().split()))
line2 = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()
    action = command[0]
    if action == "Check":
        print(line1.issubset(line2) or line2.issubset(line1))

    sequence = set(map(int, command[2:]))
    if action == 'Add':
        if command[1] == "First":
            line1.update(sequence)
        elif command[1] == "Second":
            line2.update(sequence)
    elif action == "Remove":
        if command[1] == "First":
            line1.difference_update(sequence)
        elif command[1] == "Second":
            line2.difference_update(sequence)

print(*sorted(line1), sep=", ")
print(*sorted(line2), sep=", ")
