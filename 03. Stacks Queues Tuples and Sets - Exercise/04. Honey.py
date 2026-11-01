from collections import deque


funcs = {"+": lambda *args: sum(args),
         "-": lambda *args: abs(args[0] - args[1]),
         "*": lambda *args: args[0] * args[1],
         "/": lambda *args: args[0] / args[1] if args[1] > 0 else 0
        }

bees = deque(list(map(int, input().split())))
nectars = list(map(int, input().split()))
symbols = deque(input().split())
honey = 0

while bees and nectars:
    nectar = nectars.pop()
    if nectar >= bees[0]:
        bee = bees.popleft()
        curr_args = [bee, nectar]
        curr_operator = symbols.popleft()
        honey += funcs[curr_operator](*curr_args)
        curr_args = []

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectars:
    print(f"Nectar left: {', '.join(map(str, nectars))}")