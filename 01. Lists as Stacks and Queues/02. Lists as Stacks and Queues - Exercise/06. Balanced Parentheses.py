brackets = list(input())

opened = ['{', "(", "["]
closed = ['}', ")", ']']

stack = []
for i in range(len(brackets)):
    if brackets[i] in opened:
        stack.append(i)
    elif len(stack) > 0 and brackets[i] in closed and closed.index(brackets[i]) == opened.index(brackets[stack[-1]]):
        index = stack.pop()
        # print(brackets[index:i + 1])
    else:
        print("NO")
        break
else:
    print("YES")
