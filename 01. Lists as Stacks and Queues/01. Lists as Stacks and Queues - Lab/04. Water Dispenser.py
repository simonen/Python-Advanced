from collections import deque
queue = deque()

water = int(input())
command = input()

while command != "Start":
    queue.appendleft(command)
    command = input()

command = input()
liters = 0
while command != 'End':
    command = command.split()
    if command[0] == "refill":
        liters = int(command[1])
        water += liters
        command = input()
        continue
    liters = int(command[0])
    name = queue.pop()
    if liters <= water:
        water -= liters
        print(f"{name} got water")
    else:
        print(f"{name} must wait")

    command = input()

print(f"{water} liters left")
