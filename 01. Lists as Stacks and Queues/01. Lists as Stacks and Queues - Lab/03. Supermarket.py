from collections import deque

queue = deque()
command = input()

while command != "End":
    if command == "Paid":
        for i in range(len(queue)):
            served = queue.pop()
            print(served)
    else:
        queue.appendleft(command)
    command = input()

print(f"{len(queue)} people remaining.")
