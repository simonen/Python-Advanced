expression = list(input())

stack = []
index = 0
for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        index = stack.pop()
        print("".join(expression[index:i + 1]))
