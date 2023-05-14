longest_intersect = []
longest_len = 0

for _ in range(int(input())):
    range_a, range_b = input().split("-")
    first_range = list(range(int(range_a.split(",")[0]), int(int(range_a.split(",")[1])) + 1))
    second_range = list(range(int(range_b.split(",")[0]), int(int(range_b.split(",")[1])) + 1))
    current_intersect = set(first_range).intersection(set(second_range))
    length = len(current_intersect)
    if length > longest_len:
        longest_len = length
        longest_intersect = list(current_intersect)

print(f"Longest intersection is {longest_intersect} with length {longest_len}")
