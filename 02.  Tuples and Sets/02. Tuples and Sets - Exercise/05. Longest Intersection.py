longest = []

for i in range(int(input())):
    ranges = input().split("-")
    start_n, end_n = ranges[0].split(",")
    start_n2, end_n2 = ranges[1].split(",")
    range1 = range(int(start_n), int(end_n) + 1)
    range2 = range(int(start_n2), int(end_n2) + 1)
    if len((set(range1).intersection(set(range2)))) > len(longest):
        longest = list(set(range1).intersection(set(range2)))

print(f"Longest intersection is {longest} with length {len(longest)}")