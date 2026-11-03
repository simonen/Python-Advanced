from collections import deque


string = deque(input().split())
main = {"red", "yellow", "blue"}
secondary = {"purple": ("red", "blue"), "green": ("yellow", "blue"), "orange": ("red", "yellow")}
all_colors = set(secondary) | main
colors = []

while string:
    first = string.popleft()
    last = string.pop() if string else ''

    color_found = ''
    if first + last in all_colors:
        color_found = first + last
    elif last + first in all_colors:
        color_found = last + first

    if color_found:
        colors.append(color_found)
        continue

    if first[:-1]:
        string.insert(len(string) // 2, first[:-1])
    if last[:-1]:
        string.insert(len(string) // 2, last[:-1])

# res = [c for c in colors if c in main or all(m in colors for m in secondary[c])]
res = [c for c in colors if c in main or set(secondary[c]).issubset(colors)]

print(res)
