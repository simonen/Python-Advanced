clothes = input().split()

rack = 1
start_capacity = int(input())
curr_capacity = start_capacity

while clothes:
    if int(clothes[-1]) <= curr_capacity:
        curr_capacity -= int(clothes.pop())
    else:
        rack += 1
        curr_capacity = start_capacity

print(rack)