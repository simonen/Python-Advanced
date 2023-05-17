string = input().split()

main_colors = ['red', 'yellow', 'blue']
secondary = {'orange': ('red', 'yellow'), 'purple': ('red', 'blue'), 'green': ('yellow', 'blue')}
paint = []
secs = []

while string:
    last = ''
    first = string.pop(0)
    if len(string) >= 1:
        last = string.pop()
    if first + last in main_colors:
        paint.append(first + last)
    elif last + first in main_colors:
        paint.append(last + first)
    elif first + last in secondary:
        secs.append(first + last)
        paint.append("")
    elif last + first in secondary:
        paint.append("")
        secs.append(last + first)
    else:
        if last[:-1] != '':
            string.insert(len(string) // 2, last[:-1])
        if first[:-1] != '':
            string.insert(len(string) // 2, first[:-1])

index = 0
for i in range(len(paint)):
    if paint[i] == "":
        if all(x in paint for x in secondary[secs[index]]):
            paint[i] = secs[index]
            index += 1

result = [x for x in paint if x != ""]
print(result)
