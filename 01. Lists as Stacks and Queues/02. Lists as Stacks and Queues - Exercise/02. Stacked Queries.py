stack =[]
for i in range(int(input())):
    query = input()
    if '1' in query:
        number = int(query.split()[1])
        stack.append(number)
    elif query == '2' and len(stack) > 0:
        stack.pop()
    elif query == "3" and len(stack) > 0:
        print(max(stack))
    elif query == "4" and len(stack) > 0:
        print(min(stack))

stack = list(map(str, stack))
stack2 = []
for _ in range(len(stack)):
    stack2.append(stack.pop())

print(", ".join(stack2))
