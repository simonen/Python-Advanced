from math import ceil

rows, cols = [int(x) for x in input().split()]
string = list(input())
symbols_needed = (rows * cols) / len(string)
string *= ceil(symbols_needed)
index = 0

for i in range(rows):
    if i % 2 == 0:
        print(''.join(string[index:index + cols]))
    else:
        print(''.join(string[index:index + cols][::-1]))

    index += cols
