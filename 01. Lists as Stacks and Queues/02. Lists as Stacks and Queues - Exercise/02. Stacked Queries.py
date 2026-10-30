from collections import deque

stack = deque()
n = int(input())
for _ in range(n):
    command = input()
    if command[0] == "1":
        stack.append(command.split()[1])
    if not stack:
        continue
    if command[0] == "2":
        stack.pop()
    elif command[0] == "3":
        print(max(int(x) for x in stack))
    elif command[0] == "4":
        print(min(int(x) for x in stack))

res = [stack.pop() for _ in range(len(stack))]
print(", ".join(res))
